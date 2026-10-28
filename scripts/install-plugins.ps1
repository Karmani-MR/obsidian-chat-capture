# Optional helper (Windows PowerShell): downloads Dataview, Templater, Calendar and Obsidian Git
# into the starter vault so they load the first time you open it.
#
# Usage:   powershell -ExecutionPolicy Bypass -File .\install-plugins.ps1
#          powershell -ExecutionPolicy Bypass -File .\install-plugins.ps1 -Vault "C:\path\to\vault"
param(
  [string]$Vault = (Join-Path $PSScriptRoot "..\vault-template")
)
$ErrorActionPreference = "Stop"

if (-not (Test-Path (Join-Path $Vault ".obsidian"))) {
  Write-Error "Could not find $Vault\.obsidian - pass the vault folder with -Vault."
}

$plugins = @(
  @{ id = "dataview";           repo = "blacksmithgu/obsidian-dataview" },
  @{ id = "templater-obsidian"; repo = "SilentVoid13/Templater" },
  @{ id = "calendar";           repo = "liamcain/obsidian-calendar-plugin" },
  @{ id = "obsidian-git";       repo = "Vinzent03/obsidian-git" }
)

foreach ($p in $plugins) {
  $dest = Join-Path $Vault ".obsidian\plugins\$($p.id)"
  New-Item -ItemType Directory -Force -Path $dest | Out-Null

  $manifest = Invoke-RestMethod "https://raw.githubusercontent.com/$($p.repo)/HEAD/manifest.json"
  $version = $manifest.version
  Write-Host "Installing $($p.id) $version ..."
  $base = "https://github.com/$($p.repo)/releases/download/$version"

  Invoke-WebRequest "$base/main.js"       -OutFile (Join-Path $dest "main.js")
  Invoke-WebRequest "$base/manifest.json" -OutFile (Join-Path $dest "manifest.json")
  try { Invoke-WebRequest "$base/styles.css" -OutFile (Join-Path $dest "styles.css") } catch { }
}

Write-Host ""
Write-Host "Done. Open the vault in Obsidian and choose 'Trust author and enable plugins'."
Write-Host "Then enable Templater > 'Trigger Templater on new file creation' (see README Quick start step 5)."
