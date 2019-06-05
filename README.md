# multitable

A crude python script translating multiple cif crystal structure files into a multi-page MS Word (docx) formatted crystallographic table.
This is especially useful for manuscripts containing many structures.

Usage:
1. copy script (or compiled exe file if you don't have Python) to a scratch folder
2. copy all relevant cif files to same folder
3. rename cif files with leading numbers to adjust sort order (optional)
4. run script (or compiled exe file): a file called "multitable.docx" will be created

Notes:
- 3 structures fit into one table, new pages/tables will be appended until no more structures are left
- Formatting is very crude, details should be fixed in Word (changing font size, cell spacing, etc.)
- Subscript and italics in the actual table entries now works (experimental, be careful)
- For some reason, sometimes special characters are shown as squares. Select all text and set the font again to fix.

Warning:
No responsibility taken for errors! There is no sanity check, entries might be missing (e.g. if they are not stored in the cif file or contain unexpected characters).