::disable TaskMrg and CMD

SET AND=If

::check if the disable value exists. If not it disable it
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System 
if EXIST reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System %AND% if EXIST reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\System goto say
goto setup
::if %ERRORLEVEL% == 0 goto say  


:say
echo "exists"

:setup