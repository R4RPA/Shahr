@echo off
setlocal EnableDelayedExpansion

::--- helper -------------------------------------------------
::   1st arg = folder path where script is located
::   2nd arg = script name
:RunPy
  pushd "%~1"
  echo(
  echo ==== Running %~2 in %CD% ====
  rem run script in new window, wait for it to complete, then exit
  start "py:%~2" /wait cmd /c "python %~2"
  popd
  goto :eof
::------------------------------------------------------------

call :RunPy "C:\Path\to\project"  my_code1.py
call :RunPy "C:\Path\to\project"  my_code2.py
call :RunPy "C:\Path\to\project"  my_code3.py

echo(
echo All scripts finished.
pause
