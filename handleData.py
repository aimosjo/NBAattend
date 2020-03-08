from bs4 import BeautifulSoup
import requests
import tldextract
import os
import pandas as pd

def urlToDomain(url, month):
	# create tldextract objects to get the domain, subdomain and suffix from the url
	ext = tldextract.extract(url)

	# use the tldextract objects to rejoin domain + subdomain + suffix for URLs
	website = '.'.join(ext[0:3])

	# add month in front of the website title
	website = website + "-" + month

	return(website)

def urlToHTML(url, month):
	# call url2domain and use function to name the html file appropriately
	# [LATER] add time stamp function to this s.t. the saved html file will not be overwritten
	webname = urlToDomain(url, month) + ".html"

	# use requests library to scrape the HTML text from the website
	r = requests.get(url)

	# get current directory so this can be passed to next function
	# which will use it to find the saved html file
	current_dir = os.getcwd()

	# save the scraped html text to file for use later
	Html_file= open(webname,"w")
	Html_file.write(r.text)
	Html_file.close()

	# After HTML file is written to current directory, return this path s.t. the next function
	# can find it and operate on it
	return(current_dir + "/" + webname)

# def tableData(url):
# 	page = requests.get(url)
# 	soup = BeautifulSoup(page.text, 'html.parser')
# 	table = soup.find_all('table')[0].get_text("| ")
# 	# table should be returned with | character as delimiter
# 	return table;

# def saveTable(url, month):
# 	page = requests.get(url)
# 	soup = BeautifulSoup(page.text, 'html.parser')
# 	table = soup.find_all('table')[0].get_text("| ")
# 	f = open(month + ".txt", "w+")
# 	for i in range(len(table)):

def filterHTML(htmlstring):
	#parse the HTML code using BeautifulSoup, so we can filter the HTML by cssid and tags
	soup = BeautifulSoup(open(htmlstring), 'html.parser')

	# store the result of the soup's filtered contents in a string
	filteredSoup = soup.find_all('table')[0].get_text('|')
	dat = filteredSoup.split('|')

	# create variable lines which will hold the string of values, without \n and , inside the values
	lines = ""

	# start this from 1, since at place 0 is the title
	# April Schedule Table
	for x in range(1, len(dat)):
		box_val = dat[x]

		# check to see if this is an empty string; if it isn't
		# empty, proceed
		if box_val == 'Playoffs':
			break
		if box_val not in ['\n', ' ', 'Notes', 'Box Score', '\xa0', 'OT', '2OT', '3OT', '4OT', 'at London, England']:
			update_val = ""
			for y in range(0,len(box_val)):
				if box_val[y] != ',':
					update_val += box_val[y]

			lines += update_val + "|"

	str_split = lines[0:-1].split('|')
	
	# first 7 entries are column titles
	col = []
	for x in range(0,7):
		col.append(str_split[x])

	# find the number of rows remaining in the dataset
	num_rows =int((len(str_split) - 7)/7 - 1)

	lst = [[]]
	# create new list to hold each game's details

	for x in range(1,num_rows):
		# first entry in str_split is columns, so start
		# indexing at 7, 14, 21, ..., 7*num_rows
		lst.append([])
		lst[x].append(str_split[7*x])
		lst[x].append(str_split[7*x+1])
		lst[x].append(str_split[7*x+2])
		lst[x].append(str_split[7*x+3])
		lst[x].append(str_split[7*x+4])
		lst[x].append(str_split[7*x+5])
		lst[x].append(str_split[7*x+6])
		# print(lst[x])	

	df = pd.DataFrame(lst[1:], columns = col)
	return df
	
