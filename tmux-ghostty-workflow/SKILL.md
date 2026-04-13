---
name: tmux-ghostty-workflow
description: Set up and use a practical Ghostty + tmux workflow with clear naming, fresh home-directory tabs, simple tmux entry, session switching, and save/restore shortcuts. Use when the user wants to configure Ghostty/tmux, understand the difference between tabs, sessions, windows, and panes, create reusable terminal workspaces, or sync this workflow across machines.
---

# Tmux Ghostty Workflow

Use this skill to keep Ghostty simple and let tmux handle named workspaces.

## Overview

Apply a low-confusion workflow:
- Ghostty `Cmd + T` opens a fresh normal terminal tab in `~`
- tmux is entered explicitly with short commands
- tmux session names are visible and readable
- save/restore is available with simple commands

Prefer this model unless the user explicitly wants Ghostty to auto-attach into tmux on launch.

## Target workflow

Use these conventions:
- **Ghostty tabs** are just terminal tabs
- **tmux sessions** are workspaces, for example `main`, `harness`, `blog`
- **tmux windows** are sub-areas inside one workspace
- **tmux panes** are splits inside one window

Keep the user's mental model simple:
1. `Cmd + T` gives a clean terminal in `~`
2. `ta` enters the main tmux workspace
3. `tn <name>` enters or creates a named workspace
4. `ts` saves tmux state
5. `tr` restores tmux state
6. `tl` lists all tmux sessions

## Required config shape

### Ghostty

Keep Ghostty opening plain tabs from the home directory. Do not make every new tab auto-attach to the same tmux session.

Expected `~/.config/ghostty/config` lines:

```ini
working-directory = home
```

Do not keep a default line like this unless the user explicitly wants it:

```ini
command = /opt/homebrew/bin/tmux new-session -A -s main
```

That pattern makes new Ghostty tabs look like cloned views of the same tmux client, which is confusing for many users.

### zsh helpers

Add these helpers in `~/.zshrc`:

```bash
alias ta='if [ -n "$TMUX" ]; then tmux switch-client -t main 2>/dev/null || tmux new-session -d -s main -c "$HOME" && tmux switch-client -t main; else tmux attach -t main || tmux new -s main -c "$HOME"; fi'

tn() { if [ -z "$1" ]; then echo "usage: tn <session> [dir]"; return 1; fi; local dir="${2:-$HOME}"; if [ -n "$TMUX" ]; then tmux has-session -t "$1" 2>/dev/null || tmux new-session -d -s "$1" -c "$dir"; tmux switch-client -t "$1"; else tmux has-session -t "$1" 2>/dev/null && tmux attach -t "$1" || tmux new-session -s "$1" -c "$dir"; fi }

alias tl='tmux ls'
alias ts='tmux run-shell ~/.tmux/plugins/tmux-resurrect/scripts/save.sh'
alias tr='tmux run-shell ~/.tmux/plugins/tmux-resurrect/scripts/restore.sh'
```

Behavior:
- `ta` enters `main`
- `tn harness ~/harness` creates or enters `harness`
- `tl` shows sessions
- `ts` saves
- `tr` restores

### tmux naming and switching

Keep readable titles and add simple session switching in `~/.tmux.conf`:

```tmux
bind c new-window -c "#{pane_current_path}"
bind C new-window -c "$HOME" -n home

bind-key A command-prompt -p "session name" "new-session -A -s '%%' -c '$HOME'"
bind-key W choose-tree -Zw -s -O name
bind-key S choose-tree -Zs -O name
bind-key N switch-client -n
bind-key P switch-client -p

set -g set-titles on
set -g set-titles-string '#S:#W'
set -g automatic-rename on
set -g automatic-rename-format '#{pane_current_command}'
```

Behavior:
- `Prefix + c` creates a tmux window in the current path
- `Prefix + C` creates a tmux window from `~`
- `Prefix + A` prompts for a session name and switches or creates it
- `Prefix + S` shows sessions
- `Prefix + W` shows session and window tree
- `Prefix + N` / `Prefix + P` switches next or previous session
- tab titles display like `main:zsh`, `harness:nvim`

## Save and restore

Use TPM plus these plugins:
- `tmux-plugins/tpm`
- `tmux-plugins/tmux-resurrect`
- `tmux-plugins/tmux-continuum`

Recommended lines in `~/.tmux.conf`:

```tmux
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @resurrect-capture-pane-contents 'on'
set -g @continuum-restore 'on'
run-shell ~/.tmux/plugins/tpm/tpm
```

Use these commands for users who want the simplest possible explanation:
- Save now: `ts`
- Restore now: `tr`

Only explain tmux's built-in key form if helpful:
- `Prefix + Ctrl-s` save
- `Prefix + Ctrl-r` restore

## Explain the model clearly

When teaching the user, say it plainly:
- Ghostty is the outer shell
- tmux is the workspace manager inside it
- `Cmd + T` creates a new Ghostty tab, not a tmux session
- `Prefix + c` creates a tmux window
- `Prefix + |` and `Prefix + -` create real tmux splits
- Avoid relying on Ghostty split shortcuts when the goal is tmux panes

## Minimal cheat sheet to give the user

Use this exact compact explanation when the user asks how to use it:

```text
Cmd + T           新开一个普通终端 tab，起始目录 ~
ta                进入 main 工作区
tn 名字           进入或创建命名工作区
tl                查看所有 tmux 工作区
ts                保存当前 tmux 状态
tr                恢复 tmux 状态
Ctrl-a c          tmux 新窗口
Ctrl-a Shift+C    tmux 新 home 窗口
Ctrl-a |          左右分屏
Ctrl-a -          上下分屏
Ctrl-a S          选择 session
Ctrl-a W          选择 session/window
Ctrl-a N / P      下一个 / 上一个 session
```

## Guardrails

Follow these rules:
- Do not default Ghostty to auto-attach one shared tmux session unless the user asks for that behavior
- Do not recommend `tmux attach` from inside tmux, use `switch-client` there
- Do not blur Ghostty tabs, tmux sessions, tmux windows, and tmux panes
- Prefer fewer commands and clearer names over clever automation
- When the user is confused, first simplify the workflow, then teach it
