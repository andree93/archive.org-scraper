import os
import requests
from bs4 import BeautifulSoup


print("Con questo programma potrai salvare i link diretti agli episodi di vari shows presenti su archive.org\nSaranno estratti gli url diretti ai file riproducibili con il player HTML5 integrato nel sito\nTi basterà inserire l'URL alla pagina nel formato \"https://archive.org/details/ABC\"")
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
    file_name = input("Nome del file dove salvare i link: ")
    percorso = os.path.join(os.getcwd(), file_name + ".txt")
    with open(percorso, "w", encoding='utf-8') as file:
        file.write(link_txt)
        print("File salvato in: "+percorso)
        
else:
    print("Request error! HTTP Error code: "+ str(page.status_code))
    print("Exiting...")




