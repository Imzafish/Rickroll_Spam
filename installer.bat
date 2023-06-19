@echo off
title Installing rickroll...
echo Checking internet connection

ping google.com -n 1 >nul 2>&1

if errorlevel 1 (
    echo Internet connection not available
    pause
    exit /b 1
)

REM Check if Python is installed
set /p="Checking for python..." <nul
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    goto PYTHON_CHECKED
) else (
    goto PYTHON_INSTALL
)
:PYTHON_CHECKED
echo "Python is installed."
goto PYTHON_SKIP

:PYTHON_INSTALL
echo.
choice /C YN /M "Do you want to download and install python?"
if errorlevel 2 goto PYTHON_CANCEL
if errorlevel 1 goto PYTHON_INSTALL_2

:PYTHON_INSTALL_2
REM Download Python installer
if not exist "./tmp" mkdir "./tmp"
echo Downloading Python installer...
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe' -OutFile 'tmp/python.exe'"
REM Install Python
echo Installing Python...
tmp/python.exe /quiet /norestart

:PYTHON_CANCEL
echo Please install python and try again.
pause
exit /b 1

:PYTHON_SKIP

REM Check if pip is installed
set /p="Checking for pip..." <nul
python -m pip >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    goto PIP_CHECKED
) else (
    goto PIP_INSTALL
)
:PIP_CHECKED
echo "Pip is installed."
goto PIP_SKIP

:PIP_INSTALL
echo.
choice /C YN /M "Do you want to download and install pip?"
if errorlevel 2 goto PIP_CANCEL
if errorlevel 1 goto PIP_INSTALL_2

:PIP_INSTALL_2
REM Download get-pip.py
echo Downloading get-pip.py...
powershell -Command "Invoke-WebRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -OutFile 'tmp/get-pip.py'"
REM Install pip
echo Installing pip...
python tmp/get-pip.py

:PIP_CANCEL
echo Please install pip and try again.
pause
exit /b 1

:PIP_SKIP

REM Upgrading pip setuptools and wheel
echo Updating pip setuptools and wheel
python -m pip install --upgrade pip setuptools wheel

echo Installing requirements...
pip install -r requirements.txt

echo Everything is complete. You may now rickroll away.
pause >nul
exit /b 0