# Web Scraper Creation Task
# Must install BeautifulSoup libraries and run on Python2.7

from bs4 import BeautifulSoup
import requests
import urllib2
from urllib2 import urlopen
import csv

if __name__ == "__main__":

	# Contains all urls from pages of years 2010 - 2015 
	# If there were many more urls to scrape this should probably be done programmatically
	urls = ["http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2010&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2010&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2010&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2010&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2010&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2010&p=.htm",

			"http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2011&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2011&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2011&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2011&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2011&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2011&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=7&view=releasedate&view2=domestic&yr=2011&p=.htm", 
			
			"http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2012&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2012&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2012&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2012&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2012&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2012&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=7&view=releasedate&view2=domestic&yr=2012&p=.htm", 
			
			"http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2013&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2013&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2013&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2013&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2013&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2013&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=7&view=releasedate&view2=domestic&yr=2013&p=.htm", 

			"http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2014&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2014&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2014&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2014&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2014&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2014&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=7&view=releasedate&view2=domestic&yr=2014&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=8&view=releasedate&view2=domestic&yr=2014&p=.htm", 

			"http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2015&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2015&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2015&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2015&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2015&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2015&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=7&view=releasedate&view2=domestic&yr=2015&p=.htm", 
			"http://www.boxofficemojo.com/yearly/chart/?page=8&view=releasedate&view2=domestic&yr=2015&p=.htm"]


	output = open("movies.csv", "w")
	writer = csv.writer(output)
	writer.writerow(['Rank', 'Movie Title', 'Studio', 'Total Gross', 'Total Theatres',  \
		'Opening Gross', 'Opening Theatres', 'Opening Date', 'Closing Date'])

	count = 0
	for url in urls:
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')

		a = soup.find_all('tr')

		# The table row indices are the same for each year.  This only differs on the last page for a year
		# when there aren't 100 movies on the page, hence the if statement checking if the movie name begins with 'Summary of'
		# In this case, we break out of the inner loop and move on to the next year
		for i in range(9, 109):
			try:
				s = a[i]
				if str(s.find_all('font')[0].string).strip()[:10] == 'Summary of': # for last pages in a year
					break

				rank = str(s.find_all('font')[0].string).strip()                                    # Rank
				title = s.find_all('font')[1].find_all('a')[0].string.encode('utf-8').strip()       # Movie Title
				studio = str(s.find_all('font')[2].find_all('a')[0].string).strip()                 # Studio
				total_gross = str(s.find_all('font')[3].find_all('b')[0].string).strip()            # Total gross
				total_theatres = str(s.find_all('font')[4].string).strip()                          # Total theatres
				opening_gross = str(s.find_all('font')[5].string).strip()                           # Opening gross 
				opening_theatres = str(s.find_all('font')[6].string).strip()                        # Opening theatres
				opening_date = str(s.find_all('font')[7].string).strip()                            # Opening Date
				closing_date = str(s.find_all('font')[8].string).strip()                            # Closing Date

				writer.writerow([rank, title, studio, total_gross, total_theatres, opening_gross, opening_theatres, opening_date, closing_date])

			# An exception is only thrown once for all 3906 movies.  It gets thrown for "Waiting for <i>'Superman'</i>"
			# due to the italics tag.  This had to be handled individually by first extracting the content from the <i></i> tags
			# and then getting the remaining string content that wasn't italicized and concatenating the two together.  
			except Exception as e:
				rank = str(s.find_all('font')[0].string).strip()                                    # Rank

				italicized = str(s.find_all('font')[1].find_all('a')[0].i.string)                   # Has to extract content from
				s.find_all('font')[1].find_all('a')[0].i.decompose()                                # italicized tag and join it with 
				non_italicized = str(s.find_all('font')[1].find_all('a')[0].string)                 # the rest of the title
				title = non_italicized + italicized

				studio = str(s.find_all('font')[2].find_all('a')[0].string).strip()                 # Studio
				total_gross = str(s.find_all('font')[3].find_all('b')[0].string).strip()            # Total gross
				total_theatres = str(s.find_all('font')[4].string).strip()                          # Total theatres
				opening_gross = str(s.find_all('font')[5].string).strip()                           # Opening gross 
				opening_theatres = str(s.find_all('font')[6].string).strip()                        # Opening theatres
				opening_date = str(s.find_all('font')[7].string).strip()                            # Opening Date
				closing_date = str(s.find_all('font')[8].string).strip()                            # Closing Date

				writer.writerow([rank, title, studio, total_gross, total_theatres, opening_gross, opening_theatres, opening_date, closing_date])

	output.close()
		



