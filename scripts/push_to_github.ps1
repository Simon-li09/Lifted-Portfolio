param(
  [string] $remoteUrl = "https://github.com/simonebuka852-art/Portfolio-of-lifted.git",
  [string] $branch = "main",
  [switch] $Force
)

# Move to project root (parent of scripts folder) so git commands operate on repository root
Set-Location -Path (Split-Path -Path $PSScriptRoot -Parent)

# Ensure git is installed
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  Write-Error "git is not installed or not available in PATH. Please install git and re-run this script."
  exit 1
}

if (-not (Test-Path -Path .git)) {
  git init
  git add .
  git commit -m "Initial commit — Portfolio-of-lifted"
} else {
  git add .
  git commit -m "Update from script: $(Get-Date -Format o)" -q --allow-empty
}

# Check for DB file and warn the user before pushing
if (Test-Path -Path "db.sqlite3") {
  Write-Warning "db.sqlite3 file exists in the repository root. This file often contains dev data and should usually NOT be pushed to a public repo."
  try {
    $tracked = git ls-files --error-unmatch db.sqlite3 2>$null
    if ($LASTEXITCODE -eq 0) { Write-Warning "db.sqlite3 is already tracked in git." }
  } catch { }
  if (-not $Force) {
    $an = Read-Host "Remove db.sqlite3 from the repo and .gitignore it before pushing? (y/N)"
    if ($an -eq 'y' -or $an -eq 'Y') {
      git rm --cached db.sqlite3 -q
      Add-Content -Path .gitignore -Value "db.sqlite3" -Encoding UTF8
      git add .gitignore
      git commit -m "Remove db.sqlite3 from tracking and add to .gitignore" -q --allow-empty
    }
  }
}

# If not forced, show git status and confirm with the user before pushing
if (-not $Force) {
  try {
    git status --porcelain -uall | Out-String | Write-Output
  } catch { }
  $answer = Read-Host "Proceed with pushing to $remoteUrl on branch $branch? (y/N)"
  if ($answer -ne 'y' -and $answer -ne 'Y') {
    Write-Output "Aborted by user."
    exit 0
  }
}

# Ensure branch
git branch -M $branch

# Set remote (replace if exists)
if (git remote | Select-String -Pattern "origin") {
  git remote set-url origin $remoteUrl
} else {
  git remote add origin $remoteUrl
}

Write-Output "Pushing to $remoteUrl (branch: $branch) ..."
try {
  git push -u origin $branch
  Write-Output "Push completed."
} catch {
  Write-Error "Failed to push. Please check your credentials and that you have access to the remote repository."
  exit 1
}
