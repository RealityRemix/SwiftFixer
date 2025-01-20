@echo off

:: Colors
set "green=[1;32m"
set "red=[1;31m"
set "reset_color=[0m"

set "name=Bloxstrap"
set "baseDir=%localappdata%\%name%\Versions"

if not exist "%baseDir%" (
    echo %red%Directory does not exist: %baseDir%%reset_color%
    exit /b 1
)

set "path2="

for /d %%d in ("%baseDir%\*") do (
    if exist "%%d\RobloxPlayerBeta.exe" (
        set "path2=%%d\RobloxPlayerBeta.exe"
        goto :found
    )
)

if not defined path2 (
    echo %red%RobloxPlayerBeta.exe not found in any subdirectory of %baseDir%.%reset_color%
    echo Launch Roblox through %name% and try again.
    pause >nul
    exit /b 2
)

:found

set "path1=%localappdata%\%name%\%name%.exe"

if not exist "%path1%" (
    echo %red%%name%.exe not found at the specified path.%reset_color%
    echo Install the latest %name% and try again.
    pause >nul
    exit /b 1
)

reg add "HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /v "%path1%" /t REG_SZ /d "~ DISABLEDXMAXIMIZEDWINDOWEDMODE" /f
reg add "HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /v "%path2%" /t REG_SZ /d "~ DISABLEDXMAXIMIZEDWINDOWEDMODE" /f

cls
echo %green%Black screen fixed, try injecting Synapse Z.%reset_color%
echo Press any key to exit...
pause >nul
exit /b 0
