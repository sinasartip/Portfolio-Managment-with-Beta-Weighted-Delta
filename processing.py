import os

def processFile(szPath,szFile):
	"""Will take the file path and name as input
		Each new line is omitted and and the file is seperated by 
		the tabs on each line.
		The final parse will be placed in lstInput"""
	os.chdir(szPath)
	lstFile = szFile.split(".")
	
	f0 = open(szFile, "r")
	lstInput=[]
	for oLine in f0:
		try:
			lstLine =  oLine.replace("\n","").replace(",","").split("\t")
		except Exception as e:
			print(e)
			pass

		lstInput.append(lstLine)
	f0.close()
	#write a file  with clean to represent the comma delimated file.
	fW = open(lstFile[0] + "Clean.csv","w")
	for oLine in lstInput:
		szWriteLine = ",".join(oLine)
		fW.write(szWriteLine + "\n")
	fW.close()

