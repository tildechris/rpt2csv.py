# rpt2csv.py - Another RPT to CSV Converter

This is a simple python script to convert a RPT file to a properly escaped CSV file.
	
## Usage

Command line:
	
	python rp2csv.py inputFile outputFile

Python script:

```python
import rpt2csv

with open("path\to\input.rpt") as inputFile:
	with open("path\to\output.rpt",'wb') as outputFile:
		rpt2csv.convert(inputFile,outputFile)
```
