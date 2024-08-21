@echo off
echo Installing Python packages...

:: Ensure pip is up-to-date using the py launcher
py -m pip install --upgrade pip

:: Install the specified Python packages using the py launcher
py -m pip install times
py -m pip install colorama
py -m pip install random-number

echo Installation complete.
pause
