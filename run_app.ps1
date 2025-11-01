# Cancer Diagnosis Statistical Analysis - PowerShell Launcher
# Run this script to start the Streamlit application

Write-Host "🏥 Cancer Diagnosis Statistical Analysis" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# Get the script directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# Check if virtual environment exists
$VenvPath = Join-Path (Split-Path $ScriptDir -Parent) ".venv"
$PythonExe = Join-Path $VenvPath "Scripts\python.exe"

if (Test-Path $PythonExe) {
    Write-Host "✅ Virtual environment found" -ForegroundColor Green
    Write-Host "📊 Starting application..." -ForegroundColor Yellow
    Write-Host ""
    
    # Start Streamlit
    & $PythonExe -m streamlit run app.py
} else {
    Write-Host "❌ Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please ensure the .venv directory exists in the parent folder" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "To set up the environment:" -ForegroundColor Cyan
    Write-Host "1. pip install -r requirements.txt" -ForegroundColor White
    Write-Host "2. Run this script again" -ForegroundColor White
}

Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")