# script used to scrape attendance data from website
# www.basketball-reference.com/leagues/NBA_YEAR_games-MONTH.html
# where YEAR represents the most recent year in the season
# (e.g. for the 2017-2018 season, URL will use 2018)
# and MONTH represents the months between october to june,
# saves these separate html files to calling folder

# note - this dataset contains playoff games

# imported tools being used
import handleData

# last year of desired NBA season
year = "2019"

# months of the year
months = ["october", "november", "december", "january", "february", "march", "april", \
		"may", "june"]

# this is the base URL that we'll add year and months to
# in order to access the data
base = "http://www.basketball-reference.com/leagues/NBA_"

# loop through the relevant months, and pass to our
# scraping function to save the data tables from each month
for month in months:
	url = base + year + "_games-" + month + ".html"
	handleData.urlToHTML(url, month);






