REM a főkönyvtárban állva futtasd pl.: .pyt/.pyenv_start.bat

REM git clone https://github.com/DIOTGIT/MIR_webclient.git MIR_webclient
REM cd MIR_webclient

python -m venv .venv
call .venv\Scripts\activate

python.exe -m pip install --upgrade pip
pip install -r .pyt\requirements.txt

rem pip freeze > requirements.txt