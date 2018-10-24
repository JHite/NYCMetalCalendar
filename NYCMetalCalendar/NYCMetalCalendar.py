import requests
import dateparser
import os
from unidecode import unidecode
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

#iCalFileLocationWin32 = "C:\Users\jhite\source\repos\NYCMetalCalendar\ical\nycmetalscene.ical"
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
todaysDateData = {"date" : dateparser.parse('today')}
###                     Variables End                  ###

#TODO:
#create a function to convert normal date entries into zulu time
#add time to Created, dtEnd, dtStamp,dtStart
#strip location from link and add to location field
#figure out file location differences between OSs

def wrapEvent(showData, File):
    f = open(File, "w+")
    f.write(iCalEventBegin.encode("ASCII"))
    f.write((icalCreated + printShowDataDateZulu(todaysDateData)).encode("ASCII"))
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
    print((iCalCreated + printShowDataDateZulu(todaysDateData)).encode("ASCII"))
    print((iCalDescription + showData["text"] + iCalDescriptionLink + showData["link"]).encode("ASCII"))
    print((iCaldtEnd + printShowDataDateZulu(showData)).encode("ASCII"))
    print((iCaldtStamp + printShowDataDateZulu(showData)).encode("ASCII"))
    print((iCaldtStart + printShowDataDateZulu(showData)).encode("ASCII"))
    print((iCalLocation + showData["loc"]).encode("ASCII"))
    print(iCalSequence.encode("ASCII")) 
    print((iCalSummary + showData["text"]).encode("ASCII"))
    print((iCalUid + showData["link"]).encode("ASCII"))
    print((iCalUrl + showData["link"]).encode("ASCII"))
    print(iCalEventEnd.encode("ASCII"))

def printShowDataDateZulu(date):
    if date["date"].month  < 10:
        return str(date["date"].year) + "0" + str(date["date"].month) + str(date["date"].day) + "T000000Z"
    return str(date["date"].year) + str(date["date"].month) + str(date["date"].day) + "T000000Z"

def main():
    page = requests.get("http://nycmetalscene.com/")
    soup = BeautifulSoup(page.text, 'html.parser')


    icalCount  = 0

    for p in soup.find_all('p'):
        for month in monthsOfYear: 
            if month in p.text:
                icalCount +=1
                eventDate = p.text.split(':')
                eventLoc = p.text.split(" at ")
                #convert p.text into a dictionary containing event details to wrap.
                #eventDate[0] contains the day i.e Fri Oct 19th 2018 TODO: convert to zulu
                showData["date"] = dateparser.parse(eventDate[0])
                showData["link"] = p.a['href']
                showData["text"] = p.a.string
                showData["loc"] = eventLoc[len(eventLoc) -1]
                if len(eventLoc[len(eventLoc) -1]) > 50:
                    showData["loc"] = "Check event details"
            
                wrapEventConsole(showData)
           
            

    #print (icalCount)
def test():
    page = requests.get("http://nycmetalscene.com/")
    newPage = page.text.replace("Thurs.","Thu.")
    newSoup = BeautifulSoup(newPage, "html.parser")
    for p in newSoup.find_all('p'):
        for month in monthsOfYear: 
            eventDate = p.text.split(':')
            eventLoc = p.text.split(" at ")
            if month in p.text:
                if dateparser.parse(eventDate[0]):
                
                    #convert p.text into a dictionary containing event details to wrap.
                    #eventDate[0] contains the day i.e Fri Oct 19th 2018 TODO: convert to zulu
                    showData["date"] = dateparser.parse(eventDate[0])
                    showData["link"] = " "
                    #showData["text"] = unidecode(p.a.string)
                    showData["text"] = unidecode(p.text)
                    showData["loc"] = unidecode(eventLoc[len(eventLoc) -1])
                    if len(eventLoc[len(eventLoc) -1]) > 50:
                        showData["loc"] = "Check event details"
                    if p.a:
                        if p.a['href']:
                            showData["link"] = p.a['href']
                        
            
                    wrapEventConsole(showData)
test()


