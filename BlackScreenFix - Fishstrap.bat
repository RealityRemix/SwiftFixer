@echo off

:: colors
set "green=[1;32m"
set "red=[1;31m"
set "reset_color=[0m"

set "name=Fishstrap"
set "baseDir=%localappdata%\%name%"

set "path1=%baseDir%\%name%.exe"
set "path2=%baseDir%\Roblox\Player\RobloxPlayerBeta.exe"

if not exist "%path1%" (
    echo %red%%name%.exe not found at the specified path.
	echo Install the latest %name% and try again.%reset_color%
	echo Press any key to exit...
	pause >nul
    exit /b 1
)

reg add "HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /v "%path1%" /t REG_SZ /d "~ DISABLEDXMAXIMIZEDWINDOWEDMODE" /f
reg add "HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /v "%path2%" /t REG_SZ /d "~ DISABLEDXMAXIMIZEDWINDOWEDMODE" /f

cls
echo %red%Black screen fixed, try using Swift.%reset_color%
echo Press any key to exit...
pause >nul
exit /b 0
