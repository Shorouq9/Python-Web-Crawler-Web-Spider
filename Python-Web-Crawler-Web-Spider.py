import requests
from bs4 import BeautifulSoup
 
url = 'https://www.w3schools.com/' #You can choose any public website that you want
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

#open a file in writing mode to store all of the webpages names
webpages_file = open("webpages.txt", "w")
for link in soup.find_all('a'):
   urls = link.get('href')
   webpages_file.write(urls)
   webpages_file.write("\n")
#colse the file
webpages_file.close()

#open the file to print all of the webpages and then close it
webpages_file = open("webpages.txt", "r")
for line in webpages_file:
    print(line)
webpages_file.close()

#Ask the user to enter a webpage name
value = input("Please enter a wbpage name: \n")

#open the file in reading mode to read all of the webpages names
webpages_file = open("webpages.txt", "r")
flag = 0
index = 0

#searching for the webpage given name in the file
for line in webpages_file:
   index = index + 1
   if value in line:
       flag = 1
       break
      
#if the webpage is not found print 404
if flag ==0:
    print("404")

#if the webpage is found print 200
else:
    print("200")
#close the file
webpages_file.close()


