#!/usr/bin/env python3
"""Validate a local reverse-engineering scope manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


ALLOWED_ACTIONS = {
    "static-analysis",
    "local-debugging",
    "runtime-instrumentation",
    "crash-reproduction",
    "test-only-patching",
    "patch-validation",
}
ALLOWED_BASES = {"owned", "explicit-authorization"}
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def fail(message: str) -> None:
    raise ValueError(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_string(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{field} must be a non-empty string")
    return value.strip()


def validate_target(target: object, index: int, check_files: bool) -> str:
    if not isinstance(target, dict):
        fail(f"targets[{index}] must be an object")

    kind = require_string(target.get("kind"), f"targets[{index}].kind")
    if kind == "binary":
        raw_path = require_string(target.get("path"), f"targets[{index}].path")
        path = Path(raw_path)
        if not path.is_absolute():
            fail(f"targets[{index}].path must be absolute")

        expected_hash = target.get("sha256")
        if expected_hash is not None:
            expected_hash = require_string(expected_hash, f"targets[{index}].sha256")
            if not SHA256_RE.fullmatch(expected_hash):
                fail(f"targets[{index}].sha256 must contain 64 hexadecimal characters")

        if check_files:
            if not path.is_file():
                fail(f"targets[{index}].path is not a readable file: {path}")
            if expected_hash and sha256_file(path) != expected_hash.lower():
                fail(f"targets[{index}].sha256 does not match {path}")
        return f"binary:{path}"

    if kind == "mobile-app":
        bundle_id = require_string(target.get("bundle_id"), f"targets[{index}].bundle_id")
        alias = require_string(target.get("device_alias"), f"targets[{index}].device_alias")
        transport = require_string(
            target.get("device_transport"), f"targets[{index}].device_transport"
        )
        if transport not in {"usb", "local"}:
            fail(f"targets[{index}].device_transport must be 'usb' or 'local'")
        if target.get("owned_by_user") is not True:
            fail(f"targets[{index}].owned_by_user must be true")

        device_hash = target.get("device_id_hash")
        if device_hash is not None and not SHA256_RE.fullmatch(
            require_string(device_hash, f"targets[{index}].device_id_hash")
        ):
            fail(f"targets[{index}].device_id_hash must contain 64 hexadecimal characters")
        return f"mobile-app:{bundle_id}@{alias}"

    fail(f"targets[{index}].kind must be 'binary' or 'mobile-app'")


def validate(manifest: object, check_files: bool) -> list[str]:
    if not isinstance(manifest, dict):
        fail("manifest root must be an object")
    if manifest.get("schema_version") != 1:
        fail("schema_version must be 1")

    authorization = manifest.get("authorization")
    if not isinstance(authorization, dict):
        fail("authorization must be an object")
    basis = require_string(authorization.get("basis"), "authorization.basis")
    if basis not in ALLOWED_BASES:
        fail("authorization.basis must be 'owned' or 'explicit-authorization'")
    if authorization.get("attested_by_user") is not True:
        fail("authorization.attested_by_user must be true")

    actions = manifest.get("allowed_actions")
    if not isinstance(actions, list) or not actions:
        fail("allowed_actions must be a non-empty array")
    if not all(isinstance(action, str) and action for action in actions):
        fail("allowed_actions entries must be non-empty strings")
    unknown_actions = sorted(set(actions) - ALLOWED_ACTIONS)
    if unknown_actions:
        fail(f"unsupported allowed_actions: {', '.join(unknown_actions)}")
    if manifest.get("network_access") is not False:
        fail("network_access must be false")
    if manifest.get("external_targets") is not False:
        fail("external_targets must be false")

    targets = manifest.get("targets")
    if not isinstance(targets, list) or not targets:
        fail("targets must be a non-empty array")
    return [validate_target(target, index, check_files) for index, target in enumerate(targets)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument(
        "--check-files",
        action="store_true",
        help="require binary paths to exist and verify supplied SHA-256 values",
    )
    args = parser.parse_args()

    try:
        with args.manifest.open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        targets = validate(manifest, args.check_files)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1

    actions = ", ".join(manifest["allowed_actions"])
    print("VALID: authorized local scope")
    print(f"Targets: {', '.join(targets)}")
    print(f"Allowed actions: {actions}")
    print("Network: disabled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
