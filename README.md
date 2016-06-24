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


# convert_df - function to convert RPT to pandas DataFrame. 


	Based on convert()  

	Differences: 
		Script does not run from __main__ 
		it is meant to be imported from other python scripts. 
		requires pandas 
		
		Iteration over the rpt file is done inside a try/except using file.readline() 
			to prevent an invalid character from crashing the script. 
			If an invalid character if found, the script prints the row number where 
			it can be located on the rpt file. 
		
		
		
		sample code:
		```
			from rpt2pd import convert_df
			df = convert_df("/home/filename.rpt")
		```
	
	