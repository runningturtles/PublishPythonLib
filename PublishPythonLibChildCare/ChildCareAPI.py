# Class ChildCareAPI provides the interfaces to
# import, query and filter data

from . import ChildCare as ChildCare_Class
import re
import os

class ChildCareAPI:
	# Initializing ChildCareAPI with empty data
	def __init__(self):
		self.datasets = []

	# Reading data sets from a file.
	# If the file doesn't exist, throw out an error message,
	# otherwise generate a list of data sets
	def read_data(self, filename):

		# Checking if file exists
		if not os.path.isfile(filename):
			raise Exception("File doesn't exist.")

		# Opening file and reading the contents line by line
		fh = open(filename, 'r')
		count = 0
		while True:
			count += 1 
			# Get next line from file,
			# if line is empty, end of file is reached
			line = fh.readline()
			if not line:
				break
			# If the content is a year, then two data sets will be 
			# added into the list 
			if (re.match(r"\d{4}", line.strip())):				
				# Initializing the variables
				cc1 = ChildCare_Class.ChildCare()
				cc2 = ChildCare_Class.ChildCare()
				cc1.set_category("Tageseinrichtung")
				cc2.set_category("Tagespflege")
				year = line.strip()
				num_kids1 = []
				num_kids2 = []
				num_lunches1 = ""
				num_lunches2 = ""
				# Skipping the line about the total number of the kids.
				# Because this information can be calculated by available data.
				line = fh.readline()
				line = fh.readline()
				# The next three lines are about the number of children
				# categorized by ages; the fourth line is about the number of
				# children taken lunches.
				for i in range(4):
					sp = []
					count += 1
					line = fh.readline()
					line = line.replace(".", "")
					sp = line.split(";")
					if (i < 3):
						num_kids1.append(sp[1].strip())
						num_kids2.append(sp[2].strip())
					else:
						num_lunches1 = sp[1].strip()
						num_lunches2 = sp[2].strip()
				# Setting values and appending the two data sets to the list
				cc1.set_num_kids(num_kids1)
				cc2.set_num_kids(num_kids2)
				cc1.set_num_lunches(num_lunches1)
				cc2.set_num_lunches(num_lunches2)
				cc1.set_year(year)
				cc2.set_year(year)
				self.datasets.append(cc1)        
				self.datasets.append(cc2)
		# Closing the file
		fh.close()

		if (len(self.datasets) == 0):
			raise Exception("File doesn't contain any valid data.")			
		return 0
       
    # Filtering the data sets by year     
	def filter_by_year(self, year):
		cc = ChildCare_Class.ChildCare()
		res = []
		for cc in self.datasets:
			if (str(cc.get_year()) == year):
				res.append(cc)
		if (len(res) == 0):
			raise Exception("No valid data found.")
		return res

	def filter_by_category(self, category):
		cc = ChildCare_Class.ChildCare()
		res = []
		for cc in self.datasets:
			if (cc.get_category() == category):
				res.append(cc)
		if (len(res) == 0):
			raise Exception("No valid data found.")
		return res
