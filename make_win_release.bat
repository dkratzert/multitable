
REM execute me from the main directory

REM before: python3 -m venv venv

CALL venv\Scripts\activate.bat

pip install pip -U

pip install -r requirements.txt

pyinstaller Multitable_gui.spec --clean -y

pyinstaller Multitable_cmd.spec --clean -y
