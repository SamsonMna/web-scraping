#! python3
import webbrowser, sys, pyperclip # Pyperclip is used for clipboard commands
webbrowser.open("https://website.com/")# Using google maps for reference
# mapIt.py - launches a map in the browser using the address from the terminal or clipboard
if len(sys.argv) > 1:
    # Get address from the Terminal
    address = ' ' .join(sys.argv[1:])
else:
# Get address from clipboard
    address = pyperclip.paste()
webbrowser.open("https://www.maps.google.com/place" + address)


# Downloading files from the web with requests module
import requests
res = requests.get("https://website.com/query")
type(res) # Asks what sort of a variable the res above returns.
res.status_code == requests.codes.ok #Checks whether the requests https call was made successfully
res.raise_for_status() # Checking for errors in the request

len(res.text/number/digits/integers/) # Checks the length of the of file in characters; be it digits, integers, text etc.
# Another way to check for error is:
try:
    raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))
    
# Saving files to the SSD
playFile = open("File", 'wb') #'wb' for writing in binary or use 'w' for just write.
for chunk in res.iter_content(1000):
    playFile.write(chunk)
playFile.close()



# HTML. creating a BeautifulSoup object from HTML
import requests, bs4
res = requests.get('https://nostarch.com')# Reference website
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarhSoup)

#Tag values have attrs attribute that shows all the HTML attributes of the tags as a dictionary
import bs4
exampleFile = open('example.html')
#Working within the file
exampleSoup = bs4.BeautifulSoup(exampleFile.read)
elems exampleSoup.select('#author')
type(elems) # element type datatype
len(elems)

type(elems[0]) # the datatype of the element index 0
elems[0].getText() # get author's name at index 0
str(elems[0]) # What HTML tags have been used in the making of this element
elems[0].attrs # What is the relationship between the element and the HTML tag that holds it.

pElems = exampleSoup('p') #pulling the <p> element using BeautifulSoup object
str(pElems[0])


#Getting data from an element's attributes
import bs4
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
str(spanElem)
spanElem.get('id')
spanElem.get('get_nonexistent_addr') == None
spanElem.attrs




