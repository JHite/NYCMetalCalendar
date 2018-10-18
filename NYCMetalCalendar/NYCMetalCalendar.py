import requests
from bs4 import BeautifulSoup

#####               Variables Begin                   ######
monthsOfYear =  ['Jan', 
              'Feb', 
              'Mar', 
              'April', 
              'May',  
              'June', 
              'July',
              'Aug',
              'Sept',
              'Oct',
              'Nov',
              'Dec']

iCalHeading = "BEGIN:VCALENDAR \n VERSION:2.0 \n PRODID:-//DDay.iCal//NONSGML ddaysoftware.com//EN"

iCalEventBegin = "BEGIN:VEVENT"
iCalEventEnd ="END:VEVENT"
icalCreated = "CREATED:"
icalDescription = "DESCRIPTION:" 
icalDescriptionLink = " \nAdditional Information can be found at: "
icaldtEnd= "DTEND:" 

icaldtStamp = "DTSTAMP:" 
icaldtStart = "DTSTART:" 
icalLocation = "LOCATION:" 
icalSequence = "SEQUENCE:0" 
icalSummary = "SUMMARY:" 
icalUid = "UID:" 
icalUrl = "URL:"

icalFooter = "END:VCALENDAR"
###                     Variables End                  ###

page = requests.get("http://nycmetalscene.com/")
soup = BeautifulSoup(page.text, 'html.parser')


icalCount  = 0

for p in soup.find_all('p'):
    for month in monthsOfYear: 
        if month in p.text:
            icalCount +=1
            print(p.text)

print (icalCount)
#if p.text has a month and a link, scrape the text into ical format.

