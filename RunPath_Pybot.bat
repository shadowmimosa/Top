:Start
echo  pybot Run Start ... 
@echo off
set  "Path1=%cd%"
cd ..
set  "Path2=%cd%"
if exist   "%Path2%\Public\JoyrunOnline_var.py"   (  
	set  "Path3=%Path2%\Public\JoyrunOnline_var.py" 
	) else (
	set  "Path3=%Path1%\Public\JoyrunOnline_var.py" 
	)
cd   %Path1%
choice /T 180  /C  123  /M  "Run file [Multiple]/[Single]/[Cancel]; Multiple Enter [1]; Single Enter [2]; Cancel Enter [3] " /D   1
@echo off
if errorlevel 3 goto End 
if errorlevel 2 goto Inputfile 
if errorlevel 1 goto Multiple

:Multiple
choice /T 120  /C  123  /M  "Run Env [Test]/[Online]/[Cancel]; Test Enter [1]; Online Enter [2]; Cancel Enter [3] " /D  1 
@echo off
if errorlevel 3 goto End 
if errorlevel 2 goto Online 
if errorlevel 1 goto Test 

:singlecmd
choice /T 120  /C  123  /M  "Run Env [Test]/[Online]/[Cancel]; Test Enter [1]; Online Enter [2]; Cancel Enter [3] " /D  1 
@echo off
if errorlevel 3 goto End 
if errorlevel 2 goto Online1 
if errorlevel 1 goto Test1 
 
:Test 
pybot --include Test   --variable  JoyrunEvn:Test     %Path1%
goto End 
 
:Online 
pybot --include   Online   --variable  JoyrunEvn:Online   -V  %Path3%  %Path1% 
goto End 

:Test1 
pybot --include Test   --variable  JoyrunEvn:Test     %input%  
goto End 
 
:Online1 
set /p OnlineVar=Please input your JoyrunOnline_var.py path:
echo Your input:%OnlineVar%
pause
pybot --include   Online   --variable  JoyrunEvn:Online   -V  %OnlineVar%  %input% 
goto End 

:Inputfile
@echo off
set /p input=Please input yourfile path:
echo Your input:%input%
pause
goto  singlecmd
 
:End 
echo good bye