from bs4 import BeautifulSoup
import requests
import json

url ="https://kapeli.com/cheat_sheets/Font_Awesome.docset/Contents/Resources/Documents/index"

result = requests.get(url)
resultObj = BeautifulSoup(result.text, "html.parser")
listOfNames = []
listOfCodes = []
listOfIds = []
listOfFontAwesomeIcons = []

open("FontAwesomeIconsDetail.txt", "w").close()
resultFile = open("FontAwesomeIconsDetail.txt", "+a")
allIconClass = resultObj.find_all("td", class_="command")
allIconNamesAndCode = resultObj.find_all("div", class_="td_notes")
for eachIconClass in allIconClass:
    iconClassVal = eachIconClass.find("code").text
    listOfIds.append(iconClassVal)

for x in range(0, len(allIconNamesAndCode) , 3):
    listOfNames.append(allIconNamesAndCode[x].text)
    listOfCodes.append(allIconNamesAndCode[x + 1].text)

for y in range(0, 3):
    listOfNames.pop(0)
    listOfCodes.pop(0)

for x in range(0, len(listOfIds)):
    currentIconDetails = {
        "Name": listOfNames[x].replace("\n", ""),
        "Class": listOfIds[x],
        "Uni-Code": listOfCodes[x].replace("\n", "")
    }

    listOfFontAwesomeIcons.append(currentIconDetails)

jsonOutput = json.dumps(listOfFontAwesomeIcons, indent=2)
resultFile.write(jsonOutput)