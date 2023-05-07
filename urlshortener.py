import pyshorteners

url=input()

def urlshortener(url):
    short=pyshorteners.Shortener()
    print(short.tinyurl.short(url))

urlshortener(url)