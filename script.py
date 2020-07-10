import requests
from bs4 import BeautifulSoup
import urllib.request #download from source attribute links
import csv

#Where to Scrape?
url = "http://www.reddit.com/r/BabyYoda"
#Response Object=> Server's response => Web Content&etc.
response = requests.get(url)

#Noodle is an Instance to instantiate WebScraper
noodle = BeautifulSoup(response.content, 'html.parser')

#PRINTS Entire HTML File(run in terminal "python script.py" then comment out)
# print(noodle.prettify())

#Extracting "img" tag or Image tags 
#that have specific attributes(dictionary)
#with an Alternate name and images Posted
images = noodle.find_all("img",attrs={'alt':"Post image"})

number = 0 #counter variable
# writes the dataset to file
filename = "baby_yoda.csv"
headers = "yoda pics\n"
# opens file, and writes headers
f = open(filename, "w")
f.write(headers)

#Iterating through each image tag in HTML
for image in images:
    image_src = image["src"]#Indexing  to get source element
    print(image_src)#Shows location in files
    (pic,_) = urllib.request.urlretrieve(image_src, str(number))#Retrieving image and then naming it
    number+=1 #counting file images
    f.write(image_src)
f.close()  # Close the file

