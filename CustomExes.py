#This class defines all the custom Exceptions for this project.



#called by :getname.GetManualInput()
class NameNotFoundException(Exception):
	def __init__(self,a=""):	
		a="Name not found kindly enter name in 'Enter_Your_name_here.ss' file in the 'Name' folder "
		Exception.__init__(self,a)

#called by :getname.GetName()
class InvalidInputException(Exception):
	def __init__(self,a=""):	
		a="input error: only 'y' or 'n' is accepted "
		Exception.__init__(self,a)

#called by :extract.readFile()
class FileNotFoundError(Exception):
	def __init__(self,a=""):	
		a="No file to extract. \n Kindly paste the schedule email as '.txt' format in 'Paste_Here' folder  "
		Exception.__init__(self,a)
