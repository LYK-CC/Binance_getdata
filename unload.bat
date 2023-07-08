@echo off&cd /d "%~dp0"
rem 设置WinRAR软件的路径
title %#% +%$%%$%/%_% %z%
set "rarpath=C:\Program Files\WinRAR\WinRAR.exe"
if not exist "%rarpath%" (echo;WinRAR指定的路径不正确或没有安装软件&pause&exit)
for /f "delims=" %%a in ('dir /a-d /s /b *.zip') do (
    echo;"%%a"
    "%rarpath%" e -y "%%a" "%%~dpa\"
    del "%%a"
)
echo;%#% +%$%%$%/%_% %z%
pause
exit