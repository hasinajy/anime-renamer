@echo off
setlocal enabledelayedexpansion

REM Check if a directory path is provided as an argument
if "%~1"=="" (
    echo Error: Please provide a directory path as an argument.
    pause
    exit /b 1
)

REM Set the target directory from the argument
set "target_dir=%~1"

REM Check if the directory exists, if not, create it
if not exist "%target_dir%" (
    echo Creating directory: %target_dir%
    mkdir "%target_dir%"
)

REM Define the base name of the files
set "base_name=Watch Boku no Hero Academia A new delimiter Episode"

REM Define the number of episodes to generate
set "episodes=5"

REM Loop to create the files
for /l %%i in (1,1,%episodes%) do (
    set "filename=%target_dir%\!base_name! %%i English Subbed.mp4"
    echo Creating file: !filename!
    type nul > "!filename!"
)

echo All files have been created successfully in: %target_dir%
pause