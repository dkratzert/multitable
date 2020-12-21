
REM execute me from the main directory

python3 -m venv venv

CALL venv\Scripts\activate.bat

venv\Scripts\python -m pip install -U pip

pip install -r requirements.txt

pyinstaller Multitable_gui.spec --clean -y

pyinstaller Multitable_cmd.spec --clean -y
