# Convert SSA results to DSS
This project converts SSA results tables into DSS files. The resulting DSS file will inherit the basename of the table file but with a ".dss" extension code.

## 🧑🏽‍💻 Author
### Ned Santiago  📞+63 (917) 890 5173  ✉️ [nedsantiago@tutanota.com](mailto:nedsantiago@tutanota.com)

## 🎯 Purpose
This github project was made for the reference of Hydrologists. This was especially made for coworkers needing to move data from Autodesk Storm and Sanitary Analysis (SSA) to Hydrologic Engineering Center's River Analysis System (HEC-RAS).

## ⚡Usage
### For exporting flooding flow rate data
1) While results are displayed in SSA, export data to a table file: In SSA, Output > Time Series Table by Variable
2) Select the appropriate data, then press ok. Right-click on the table and export as table.
3) Provide the name for the table

<video width="640" height="480" controls>
  <source src="docs/exporting-flooding-flowrate.mp4" type="video/mp4">
</video>

4) Run the executable file
5) Select the table file
6) It's done! The resulting file should be in the same folder as the executable.

<video width="640" height="480" controls>
  <source src="docs/converting-todss.mp4" type="video/mp4">
</video>

## 📖 Documentation
### How to create the executable
This package uses PyInstaller to create an executable version of the convert_table_to_dss.py script. First, install PyInstaller
```
py -m pip install pyinstaller
```
Second, locate the PyInstaller script. Using PyInstaller requires using the package itself (and not as a module). Thus, to compile the code:
```
pyinstaller ./convert_table_to_dss.py
```
The executable is located in the dist folder as
```
convert_table_to_dss.exe
```