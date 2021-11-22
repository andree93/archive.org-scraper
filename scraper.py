import argparse
import os
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Webpage link in the format \"https://archive.org/details/ABC\"",)
parser.add_argument("--filename", help="File name (where all links will be saved)",)
args = parser.parse_args()


if args.url is None: #the argument "url" is optional, if the user hasn't typed on command line, the argument is None and the user must enter the URL
    print("With this script you can save all direct links to archive.org website audio and video streams\nAll playable links with the internal HTML5 player will be extracted and saved in a TXT file (one per line)\nYou must enter the webpage link in the format \"https://archive.org/details/ABC\"")
    URL = input("Please enter archive.org URL page: ")
else:
    URL = args.url


while not URL.startswith("https://archive.org/details/"):
    print("URL format error! Please try again: ")
    URL = input("Please enter archive.org URL page: ")

print("Please wait...")

page = requests.get(URL)
if page.status_code == 200:
    link_txt = ""
    soup_obj = BeautifulSoup(page.content, "html.parser")
    links = soup_obj.find_all(itemprop="associatedMedia")
    print("Found "+str(len(links))+" link")
    for link in links:
        link_txt += link['href']+"\n"
    if args.filename is None: #same as url argument, if the user hasn't typed on command line
        file_name = input("Please enter file name (where all links will be saved): ")
    else:
        file_name = args.filename
    percorso = os.path.join(os.getcwd(), file_name + ".txt") # Build the path. The File will be saved in the working directory
    with open(percorso, "w", encoding='utf-8') as file:
        file.write(link_txt)
        print("File saved as: "+percorso)
else:
    print("Request error! HTTP Error code: "+ str(page.status_code))
    print("Exiting...")

