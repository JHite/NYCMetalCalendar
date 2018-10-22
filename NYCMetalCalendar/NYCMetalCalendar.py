import requests
import dateparser
import os
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

icalFileLocationWin32 = "C:\Users\jhite\source\repos\NYCMetalCalendar\ical\nycmetalscene.ical"
icalFileLocationMacOS = "\Users\jhite\Programming\ical\nycmetalscene\"

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

showData = {}
###                     Variables End                  ###

#TODO:
#create a function to convert normal date entries into zulu time
#create a eventWrap function
def wrapEvent(showData, File):
    f = open(File, "w+")
    f.write(iCalEventBegin.encode("ASCII"))
	f.write(icalCreated + )
	iCalDescription + $clEvent.description + $iCalDescriptionLink + $clEvent.eventUrl| Out-File -encoding ASCII -append $dest
	$iCaldtEnd + (Convert-MilliToZulu $clEvent.endDateTime) | Out-File -encoding ASCII -append $dest
	$iCaldtStamp + (Convert-MilliToZulu $now)| Out-File -encoding ASCII -append $dest
	$iCaldtStart + (Convert-MilliToZulu $clEvent.startDateTime) | Out-File -encoding ASCII -append $dest
	$iCalLocation  + $clEvent.otherLocation| Out-File -encoding ASCII -append $dest
	$iCalSequence | Out-File -encoding ASCII -append $dest
	$iCalSummary + $clEvent.eventName| Out-File -encoding ASCII -append $dest
	$iCalUid + $clEvent.eventId + "@collegiatelink.net"| Out-File -encoding ASCII -append $dest
	$iCalUrl + $clEvent.eventUrl | Out-File -encoding ASCII -append $dest
	$iCalEventEnd | Out-File -encoding ASCII -append $dest
}

page = requests.get("http://nycmetalscene.com/")
soup = BeautifulSoup(page.text, 'html.parser')


icalCount  = 0

for p in soup.find_all('p'):
    for month in monthsOfYear: 
        if month in p.text:
            icalCount +=1
            eventDate = p.text.split(':')
            #convert p.text into a dictionary containing event details to wrap.
            #eventDate[0] contains the day i.e Fri Oct 19th 2018 TODO: convert to zulu
            showData["date"] = dateparser.parse(eventDate[0])
            showData["link"] = p.a['href']
            showData["text"] = p.a.string
           
            

print (icalCount)




