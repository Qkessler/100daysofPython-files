import feedparser

file = "WSJcomUSBusiness.xml"

feed = feedparser.parse(file)


for entry in feed.entries:
    print(f'{entry.title}')
