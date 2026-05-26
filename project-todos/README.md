# Project todos

Synced snapshots from GitHub organization issues, produced by `scripts/excalibur-command.ps1`.

## Refresh

```powershell
powershell.exe -ExecutionPolicy Bypass -File ./scripts/excalibur-command.ps1 -DryRun -Verbose
```

Remove `-DryRun` to write `*.md` files in this folder.

## Status

```powershell
./scripts/todo-manager.ps1 status
```
