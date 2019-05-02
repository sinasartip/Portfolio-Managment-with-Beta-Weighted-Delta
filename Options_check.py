import os,sys
import processing as proc 
import numpy as np





#THIS IS THE MAIN PROGRAM 

#Set up options file
 
#File_f.File_find(sys.argv[1],sys.argv[2],sys.argv[3])

#WIll define where each file is stored (txt) _ this is the Use interface
	if len(sys.argv) == 4:
		file_path = str(sys.argv[2])
		file_name = str(sys.argv[1])
		if str(sys.argv[3]) == 'Y':
			pass
		else:
			file_s_path = input("If the screener is in the current dir, leave empty else give directory\n")
			if file_s_path == '':
				file_s_path = os.getcwd()
				file_s_name = input("If the name is screener.txt leave empty, else place file name .txt\n")
			if file_s_name == '':
				file_s_name = "screener.txt"
			else:
				os.chdir(file_s_path)
				file_s_name = input("If the name is screener.txt leave empty, else place file name .txt\n")



	elif len(sys.argv) == 3:
		file_path = str(sys.argv[2])
		file_name = str(sys.argv[1])
		file_s_name = 'screener.txt'
		file_s_path = os.getcwd()
	elif len(sys.argv)== 2:
		file_name = str(sys.argv[1])
		file_path = os.getcwd()
		file_s_name = 'screener.txt'
		file_s_path = os.getcwd()
	else:
		file_path = os.getcwd()
		file_name = 'options.txt'
		file_s_name = 'screener.txt'
		file_s_path = os.getcwd()
		print("options.txt in the current directory was used by default.")

#WIll compare the two lists. 
proc.processFile(file_path,file_name)





