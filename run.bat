@echo off

REM Install pip if it's not already installed
where pip >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pip...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    del get-pip.py
)

REM Install dependencies from requirements.txt
echo Installing dependencies...
pip install -r requirements.txt

REM Open the "main.py" file
echo Opening main.py...
start "" /B pythonw.exe ./src/main.py
