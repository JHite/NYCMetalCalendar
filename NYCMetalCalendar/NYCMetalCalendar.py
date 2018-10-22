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

iCalFileLocationWin32 = "C:\Users\jhite\source\repos\NYCMetalCalendar\ical\nycmetalscene.ical"
#iCalFileLocationMacOS = "\Users\jhite\Programming\ical\nycmetalscene\"

iCalHeading = "BEGIN:VCALENDAR \n VERSION:2.0 \n PRODID:-//DDay.iCal//NONSGML ddaysoftware.com//EN"

iCalEventBegin = "BEGIN:VEVENT"
iCalEventEnd = "END:VEVENT"
iCalCreated = "CREATED:"
iCalDescription = "DESCRIPTION:" 
iCalDescriptionLink = " \nAdditional Information can be found at: "
iCaldtEnd= "DTEND:" 

iCaldtStamp = "DTSTAMP:" 
iCaldtStart = "DTSTART:" 
iCalLocation = "LOCATION:" 
iCalSequence = "SEQUENCE:0" 
iCalSummary = "SUMMARY:" 
iCalUid = "UID:" 
iCalUrl = "URL:"

iCalFooter = "END:VCALENDAR"

showData = {}
###                     Variables End                  ###

#TODO:
#create a function to convert normal date entries into zulu time
#add time to Created, dtEnd, dtStamp,dtStart
#strip location from link and add to location field
#figure out file location differences between OSs

def wrapEvent(showData, File):
    f = open(File, "w+")
    f.write(iCalEventBegin.encode("ASCII"))
    f.write(icalCreated.encode("ASCII"))
    f.write((iCalDescription + showData["text"] + iCalDescriptionLink + showData["link"]).encode("ASCII"))
    f.write(iCaldtEnd.encode("ASCII"))
    f.write(icaldtStamp.encode("ASCII"))
    f.write(iCaldtStart.encode("ASCII"))
    f.write(icalLocation.encode("ASCII"))
    f.write(iCalSequence.encode("ASCII")) 
    f.write((iCalSummary + showData["text"]).encode("ASCII"))
    f.write((iCalUid + showData["link"]).encode("ASCII"))
    f.write((iCalUrl + showData["link"]).encode("ASCII"))
    f.write(iCalEventEnd.encode("ASCII"))

def wrapEventConsole(showData):
    print(iCalEventBegin.encode("ASCII"))
    print(iCalCreated.encode("ASCII"))
    print((iCalDescription + showData["text"] + iCalDescriptionLink + showData["link"]).encode("ASCII"))
    print(iCaldtEnd.encode("ASCII"))
    print(iCaldtStamp.encode("ASCII"))
    print(iCaldtStart.encode("ASCII"))
    print(iCalLocation.encode("ASCII"))
    print(iCalSequence.encode("ASCII")) 
    print((iCalSummary + showData["text"]).encode("ASCII"))
    print((iCalUid + showData["link"]).encode("ASCII"))
    print((iCalUrl + showData["link"]).encode("ASCII"))
    print(iCalEventEnd.encode("ASCII"))


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




