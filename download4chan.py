# python3
# download4chan.py - To download images from 4chan from a specific thread, listed below

import requests, os, bs4

url = 'http://boards.4channel.org/v/thread/484142341' # base site url
os.makedirs('PP', exist_ok=True) #where the images will be stored
  
#TODO - download page
print('Downloading')
res = requests.get(url)
res.raise_for_status()
print(res.status_code)

soup = bs4.BeautifulSoup(res.text, "lxml")
    
#TODO - Find url of images
for i in range(1,160): # will need to change the range manually
        
        imageElem = soup.find_all(attrs={"class": "fileThumb"})     
        imageUrl = 'http:' + imageElem[i].get('href')                     
        
#TODO - D/L images

        print('Downloading ... %s'  % imageUrl)
        res = requests.get(imageUrl)
        res.raise_for_status()

#TODO - Save file to HDD

        imageFile = open(os.path.join('PP', os.path.basename(imageUrl)), 'wb')
        for pow in res.iter_content(10000):
               imageFile.write(pow)
        imageFile.close()
        print(imageUrl)

print('Done.')
