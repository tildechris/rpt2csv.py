import sys
import csv

def convert(inputFile,outputFile):
	"""
	Convert a RPT file to a properly escaped CSV file
	
	RPT files are usually sourced from old versions of Microsoft SQL Server Management Studio
	RPT files are fixed width with column names on the first line, a second line with dashes and spaces,
	and then on one row per record.

	The column widths are calculated from the longest field in a column, so the format varies 
	depending on the results.  Thankfully, we can reliably infer column widths by looking at the indexes
	of spaces on the second line.

	Here we chop each record at the index of the space on the second line and strip the result.

	Note, if the source data has significant whitespace, the striping will remove this, but likely significant
	whitespace was destroyed by the RPT field padding anyway.
	"""
	
	writer = csv.writer(outputFile)
	fieldIndexes = []
	headers = ""

	for idx, val in enumerate(inputFile):
		if(idx == 0):
			headers = val
		elif(idx == 1):
			fieldIndexes = list(getFieldIndexes(val," "))
			row = list(getFields(headers,fieldIndexes))
			writer.writerow(row)
		else:
			row = list(getFields(val,fieldIndexes))
			writer.writerow(row)

def getFieldIndexes(input, sep):
	lastIndex = 0
	for idx, c in enumerate(input):
		if(c == sep):
			yield (lastIndex,idx)
			lastIndex = idx+1
	yield lastIndex, len(input)

def getFields(input, indexes):
	for index in indexes:
		yield input[index[0]:index[1]].strip()

if __name__ == '__main__':
	if(len(sys.argv) == 3):
		with open(sys.argv[1]) as inputFile:
			with open(sys.argv[2],'wb') as outputFile:
				convert(inputFile,outputFile)
	else:
		print("Usage: rpt2csv.py inputFile outputFile")
    