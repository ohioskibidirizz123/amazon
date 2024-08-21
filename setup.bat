@echo off
echo Installing Python packages...

:: Ensure pip is up-to-date
python -m pip install --upgrade pip

:: Install the specified Python packages
pip install times
pip install colorama
pip install random-number

echo Installation complete.
pause
