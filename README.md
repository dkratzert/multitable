# multitable

A python script translating multiple cif crystal structure files into a multi-page MS Word (docx) formatted crystallographic table.
This is especially useful for manuscripts containing many structures.

Usage:
1. copy script (or compiled exe file if you don't have Python) to a scratch folder
2. copy all relevant cif files to same folder
3. rename cif files with leading numbers to adjust sort order (optional)
4. run script (or compiled exe file): a file called "multitable.docx" will be created

Download Windows exe:
* Commandline: https://dkratzert.de/files/multitable/multitable.exe
* Graphical Version: https://dkratzert.de/files/multitable/multitable_gui.exe

Notes:
- 3 structures fit into one table, new pages/tables will be appended until no more structures are left
- Formatting is very crude, details should be fixed in Word (changing font size, cell spacing, etc.)
- Sometimes special characters are shown as squares. Select all text and set the font again to fix.

Missing or invalid cif entries create question marks in the table.


The original Idea of this project was realized by Nils Trapp. Major modifications and an
additional graphical user interface were made by Daniel Kratzert.
