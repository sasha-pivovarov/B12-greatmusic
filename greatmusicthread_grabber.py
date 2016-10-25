import requests
import re
import json

#Modify this to grab whatever. The regex can probably be improved too, but I didn't care enough.
page_urls = ['http://www.bay12forums.com/smf/index.php?topic=82547.' + str(x) for x in range(0,4306, 15)]

def grab_youtube_links(url):
    source = str(requests.get(url).content)
    return re.findall('a href="(http://www.youtu.*?)"', source)

link_list = []

for url in page_urls:
    link_list.extend(grab_youtube_links(url))
    
print(len(set(link_list)))

with open('yt_links_from_b12.json', 'w') as file:
    json.dump(set(link_list), file)
