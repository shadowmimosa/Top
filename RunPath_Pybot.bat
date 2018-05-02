echo  pybot Run Start ... 
set  "Path1=%cd%"
cd ..
set  "Path2=%cd%"
if exist   "%Path2%\Public\JoyrunOnline_var.py"   (  
	set  "Path3=%Path2%\Public\JoyrunOnline_var.py" 
	) else (
	set  "Path3=%Path1%\Public\JoyrunOnline_var.py" 
	)
cd   %Path1%
choice /T 30  /C  123  /M  "Run Env [Test]/[Online]/[Cancel]; Test Enter [1]; Online Enter [2]; Cancel Enter [3] " /D  1 
if errorlevel 3 goto End 
if errorlevel 2 goto Online 
if errorlevel 1 goto Test 
 
:Test 
pybot --include Test   --variable  JoyrunEvn:Test     %Path1%
goto End 
 
:Online 
pybot --include   Online   --variable  JoyrunEvn:Online   -V  %Path3%  %Path1% 
goto End 
 
:End 
echo good bye 