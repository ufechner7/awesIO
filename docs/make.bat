@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=.
set BUILDDIR=_build

REM Put it first so that "make" without argument is like "make help".
if "%1" == "" goto help
if "%1" == "help" goto help
if "%1" == "schemas" goto schemas
if "%1" == "html" goto html
if "%1" == "clean" goto clean
if "%1" == "serve" goto serve
if "%1" == "switcher" goto switcher
if "%1" == "deploy" goto deploy

goto default

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:schemas
echo Generating schema HTML documentation...
python schema_export.py --placeholders
goto end

:html
echo Generating schema HTML documentation...
python schema_export.py --placeholders
echo Building HTML documentation...
%SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:clean
echo Cleaning build directory...
if exist %BUILDDIR% rmdir /s /q %BUILDDIR%
if exist _static\*_schema.html del /q _static\*_schema.html
goto end

:serve
call :html
echo Starting local server at http://localhost:8000
python -m http.server -d %BUILDDIR%\html 8000
goto end

:switcher
echo Generating version switcher JSON...
python generate_switcher_json.py
goto end

:deploy
call :clean
call :schemas
call :switcher
%SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:default
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:end
popd
