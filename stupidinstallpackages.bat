@echo off
REM This batch file will install the required Python packages

echo Installing required Python packages...

REM Install requests
py -m pip install requests

REM Install colorama
py -m pip install colorama

REM Display message after installation
echo All packages have been installed.

REM Pause to keep the window open
pause
