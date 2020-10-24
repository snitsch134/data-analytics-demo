#Samuel Nitsch 10/22/2020
#Debugged by Jack Sheehan (The webscraping goat)
#Web scraper for months in 2019
#Requirements
#
#BeautifulSoup4
#requests
#lxml
#matplotlib

#   Uses a function called getMonthData
#   scrapes each month in 2019 of dallas temp.
#   uses all averages and plots them in a graph using matplotlib

import urllib.request
from urllib.request import Request, urlopen
import matplotlib.pyplot as plt
import requests
import itertools
import bs4

#Takes the url of the month you scrape and the days in the given month
def getMonthData(url,num):
    avgTemp = 0
    totalTemp = 0
    totalHigh = 0
    totalLow = 0
    avgHigh = 0
    avgLow = 0
    avgPercip =0
    totalPercip = 0
    source = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(source).read()

    scraper = bs4.BeautifulSoup(webpage,"lxml")

    print(scraper.title.string)

    #Finds all the tables on the website
    table_main = scraper.find_all("section")

    #Finds all tags with <tr> but only  for the second table  (the one we want)
    table_sets = table_main[1].find_all("tr")

    #for the table in table_sets, we find all <td> tags that have our info
    for table in table_sets:
        data = table.find_all("td")
        #If its not null, then we add to the total until all values have been added
        if data:
            totalString = data[1].string
            maxString = data[2].string
            minString = data[3].string
            rainString = data[4].string
            totalTemp += int(totalString[0:totalString.index('°')])
            totalHigh += int(maxString[0:maxString.index('°')])
            totalLow += int (minString[0:minString.index('°')])
            totalPercip += float(rainString[0:rainString.index('m')])

    #Calculate averages
    avgHigh = round(totalHigh/num)
    avgTemp = round(totalTemp/num)
    avgLow = round(totalLow/num)
    avgPercip = round(totalPercip/num)

    #returns averages
    return [avgTemp,avgHigh,avgLow,avgPercip]

#Getting the averages for every month in dallas for 2019

jan = getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/january-1/',31)
feb = getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/february-2/',28)
mar = getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/march-3/',31)
apr = getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/april-4/',30)
may = getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/may-5/',31)
jun = getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/june-6/',30)
jul = getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/july-7/',31)
aug = getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/august-8/',31)
sept =  getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/september-9/',30)
octo =  getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/october-10/',31)
nov =  getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/november-11/',30)
dec =  getMonthData('https://en.climate-data.org/north-america/united-states-of-america/texas/dallas-292/t/december-12/',31)

#Plot the three lines (Average temp, average High, average low)
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],[jan[0],feb[0],mar[0],apr[0],may[0],jun[0],jul[0],aug[0],sept[0],octo[0],nov[0],dec[0]], label = "Avg. Temp.")
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],[jan[1],feb[1],mar[1],apr[1],may[1],jun[1],jul[1],aug[1],sept[1],octo[1],nov[1],dec[1]], label = "Avg. High")
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],[jan[2],feb[2],mar[2],apr[2],may[2],jun[2],jul[2],aug[2],sept[2],octo[2],nov[2],dec[2]],label ="Avg. Low")
#Set axis labels
plt.ylabel('Temperatures')
plt.xlabel('Month by Number')
#Show Legend
plt.legend()
#Show chart
plt.show()
