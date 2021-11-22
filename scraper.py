import os
import requests
from bs4 import BeautifulSoup

print("With this script you can save all direct links to archive.org website audio and video streams\nAll playable links with the internal HTML5 player will be extracted and saved in a TXT file (one per line)\nYou must enter the webpage link in the format \"https://archive.org/details/ABC\"")
URL = input("Please enter archive.org URL page: ")

if not URL.startswith("https://archive.org/details/"):
    print("URL format error! Please try again: ")
    URL = input("Please enter archive.org URL page: ")

page = requests.get(URL)
if page.status_code == 200:
    link_txt = ""
    soup_obj = BeautifulSoup(page.content, "html.parser")
    links = soup_obj.find_all(itemprop="associatedMedia")
    print("Trovati "+str(len(links))+" link")
    for link in links:
        link_txt += link['href']+"\n"
    file_name = input("Please enter file name (where all links will be saved): ")
    percorso = os.path.join(os.getcwd(), file_name + ".txt")
    with open(percorso, "w", encoding='utf-8') as file:
        file.write(link_txt)
        print("File salvato in: "+percorso)
else:
    print("Request error! HTTP Error code: "+ str(page.status_code))
    print("Exiting...")

