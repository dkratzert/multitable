cd ..
venv_py\Scripts\pyinstaller.exe --clean ^
                                --add-data="gui;gui" ^
                                -p "D:\Programme\Windows Kits\10\Redist\ucrt\DLLs\x64" ^
                                --add-data="templates;templates" ^
                                -y ^
                                -n Multitable_gui ^
                                -F ^
                                multi_gui.py
rem exit

