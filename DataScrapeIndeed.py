import urllib
from bs4 import BeautifulSoup
import pandas as pd

source = urllib.request.urlopen('http://www.indeed.com/jobs?q=data+scientist&l=').read()
#print(source)

soup = BeautifulSoup(source,'html.parser')


urls = []
    
for l in soup.find_all(name = 'span', attrs= {'class': 'pn'}): 
    ''' This loop iterates over page numbers.'''
    for link in soup.find_all(name = 'a', attrs= {'class': 'jobtitle'}):
        ''' This loop iterates over Data science jobs and gets the urls.'''
        part_url = link.get('href')
        url = "https://www.indeed.com/" + part_url
        urls.append(url)
        #print(len(urls))

''' Creating dataframe for the job urls.'''
data = [urls]
df = pd.DataFrame(data, index = ['Job Links']).transpose()
print(df)