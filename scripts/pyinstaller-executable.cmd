cd ..
venv\Scripts\pyinstaller.exe --clean ^
                                --add-data="gui;gui" ^
                                rem --add-data="icons;icons" ^
                                rem --hidden-import PyQt5.sip ^
                                rem -n StructureFinder ^
                                -y ^
                                rem -i "icons/strf.ico" ^
                                --windowed ^
                                multi_gui.py
exit

