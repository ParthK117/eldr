import os
import zipfile
import sys
import urllib.request
import webbrowser

version = ""
newversion = ""


url = 'https://tungstencore.com/cdn/version.txt'
urllib.request.urlretrieve(url, "version.txt")

with open('version.txt') as f:
    for x in f:
        newversion = x.split("#")
try:
    with open('settings.dat') as f:
        for x in f:
            if "version" in x:
                version = x.split("=")
                break
except:        
    print("No version file found, fresh installing")
    assume = "version=0.0.1"
    version = assume.split("=")

print(newversion[1])
print("New version is " + str(newversion[0]))
print("Current version is " + str(version[1]))

if not newversion[0].strip("\n") == version[1].strip("\n"):
    try:
        os.system("taskkill /f /im  Emuloader.exe")
    except:
        print("That's okay...")
    print("That's okay...")
    url2 = newversion[1]
    print("Downloading update from Github...")
    urllib.request.urlretrieve(url2, "update.zip")
    print("Unzipping...")
    # Create a ZipFile Object and load sample.zip in it
    with zipfile.ZipFile('update.zip', 'r') as zipObj:
   # Get a list of all archived file names from the zip
       listOfFileNames = zipObj.namelist()
   # Iterate over the file names
       for fileName in listOfFileNames:
       # Check filename endswith csv
            if not "eldr.exe" in fileName:
           # Extract a single file from zip
                zipObj.extract(fileName)
            else:
                zipObj.extract(fileName, "neweldr")
    print("Success! Cleaning up...")    
    os.remove("update.zip")
    print("Launching Emuloader.exe")
    os.startfile("Emuloader.exe")
    webbrowser.open('https://tungstencore.com/emuloader', new=2)
os.remove("version.txt")