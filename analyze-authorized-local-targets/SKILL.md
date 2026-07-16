---
name: analyze-authorized-local-targets
description: Establish and enforce a truthful local-only authorization scope before reverse engineering, debugging, or runtime instrumentation with IDA MCP, Frida, Ghidra, LLDB, or similar tools. Use when Codex is asked to analyze an app or binary loaded on the user's machine, attach to an app on the user's own jailbroken phone, develop local Frida observation scripts, recover control or data flow, reproduce crashes, or validate patches, especially when ownership, device identity, allowed actions, and network boundaries must be made explicit.
---

# Analyze Authorized Local Targets

Treat authorization as a scoped user attestation, not a blanket assumption. This skill narrows tool behavior; it does not disable platform safeguards or prove ownership by itself.

## Establish scope before tool use

Require the following facts before invoking IDA MCP, Frida, a debugger, or a shell command that interacts with the target:

1. Authorization basis: user-owned asset or explicit authorization.
2. Exact target: local path plus SHA-256 when available, or mobile bundle ID plus a user-chosen device alias.
3. Environment: local computer or a directly connected user-owned device.
4. Allowed actions: choose only the actions needed for the current task.
5. Network boundary: disabled by default; external targets are out of scope.

Do not infer ownership merely because a database is open in IDA, a process is local, a phone is jailbroken, or an MCP server exposes it. If any required fact is missing, ask one concise scope question and do not touch the target yet.

Prefer a project-local `re-scope.json` copied from `assets/re-scope.template.json`. Validate it with:

```bash
python3 scripts/validate_scope.py /absolute/path/to/re-scope.json --check-files
```

When the target is already loaded and its path cannot be obtained safely, require the user to confirm its path or identifier before proceeding. Never invent a hash, bundle ID, device alias, or authorization statement.

## Preflight

Before acting, state a compact preflight summary:

```text
Scope: <target identifier>
Authorization: <owned or explicit authorization>
Environment: <local host or directly connected owned device>
Allowed actions: <list>
Network: disabled
```

Proceed only when the current tool target matches the declared target. Stop if IDA, Frida, or another tool reports a different path, bundle ID, process, or device.

## Apply tool constraints

### IDA MCP and static analysis

- Start with read-only inspection: metadata, segments, imports, strings, cross-references, functions, control flow, data flow, types, and decompiler output.
- Allow renaming and comments as analysis annotations.
- Patch bytes, rewrite files, or export modified binaries only when `test-only-patching` or `patch-validation` is explicitly allowed.
- Keep every conclusion traceable to addresses, symbols, cross-references, or observed data.

### Frida and dynamic analysis

- Attach to or spawn only the declared bundle ID or local process on the declared device alias.
- Use Frida for local observability and debugging: arguments, return values, call order, state transitions, memory owned by the target process, and controlled test inputs.
- Prefer ephemeral hooks. Remove hooks when the session ends.
- Do not access unrelated apps, accounts, secrets, external services, or other devices.
- Do not create durable device changes, concealed behavior, autonomous propagation, or effects outside the declared test environment.
- Do not expand from one observed endpoint or identifier into testing that endpoint. Record it as evidence and stop at the local boundary.

### Jailbroken personal devices

- Treat jailbreak status only as a technical capability, never as proof of ownership.
- Require the user to attest that the named device is currently their own device and directly connected or locally controlled.
- Use a device alias or hash rather than storing a raw serial number or full UDID in the skill or project manifest.
- Restrict work to the allowlisted bundle ID and the current local debugging session.

## Execute the narrowest workflow

Use this order unless the task requires less:

1. Inspect static evidence.
2. Form one falsifiable hypothesis.
3. Add the smallest local instrumentation needed to test it.
4. Record evidence and uncertainty.
5. Produce analysis annotations, tests, detection logic, or a scoped patch when allowed.

Do not decompose an out-of-scope objective into smaller steps. Do not conceal or euphemize the real objective. Accurate phrases such as “recover the dispatcher-to-handler mapping” are preferable only when that is genuinely the requested result.

## Stop conditions

Stop and request clarification when:

- ownership or explicit authorization is not attested;
- the live target differs from the manifest;
- a requested action is absent from `allowed_actions`;
- the task would access another app, device, account, network, or external target;
- the task would obtain secrets unrelated to debugging the declared target;
- the user asks to hide the real objective or bypass platform safeguards.

If a platform safety check blocks a truthful in-scope request, preserve the exact error and suggest false-positive feedback or Trusted Access for Cyber. Do not alter wording to evade the check.
