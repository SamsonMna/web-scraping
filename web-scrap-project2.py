#! python3
# Downloadxkcd.py # Downloads every single XKCD comic
import requests, os, bs4
url = 'https://xkcd.com' # starting url
os.mkdirs('xkcd', exist ok=True) # store comics in ./xkcd directory
while not url.endswith('#'):
    # Download the page
    print("Downloading page %s..." $ url)
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text)
    
    # Find the URL of the comic image
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("Could not find comic image")
    else:
        comicUrl = comicElem[0].get('src')
        # Download the image
        print("Downloading image %s..." % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        
        #save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basement(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Get the prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')

    
