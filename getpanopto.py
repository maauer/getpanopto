#!/usr/bin/python3
import xml.etree.ElementTree as ET
import os

os.system("""wget "PANOPTO_FEED_URL_GOES_HERE" -O feed.rss""")
root = ET.parse('feed.rss').getroot()
items = root[0].findall('item')

for item in items:
    title = item.find('title').text
    url = item.find('enclosure').get('url')
    print(title)
    print(url)
    command = f"""wget "{url}" -O "{title}.mp4" """
    os.system(command)
