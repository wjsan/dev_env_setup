@echo off

cd %~dp0

echo Installing Chocolatey...
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"

echo Refreshing Environment Variables...
call refreshenv

echo Installing Python...
call choco install python -y
echo Python Installed!

echo Refreshing Environment Variables...
call refreshenv

echo Installing Dev Tools...
call python install.py

pause