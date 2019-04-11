from Notifier import Notifier 
import bs4 as bs
import urllib.request
import time
import math
over = 0
over1 = 0
url = "https://www.cricbuzz.com/live-cricket-scores/22460/rajasthan-vs-chennai-25th-match-indian-premier-league-2019"
n = Notifier()
while True:
    sp =urllib.request.urlopen(url).read()
    soup=bs.BeautifulSoup(sp,'lxml')
    hd = soup.find('h1',{"class":"cb-nav-hdr cb-font-18 line-ht24"})
    header = hd.text.split(",", 1)
    link="cb-font-20 text-bold"
    span = soup.find_all('span', {"class" : link})
    try:
        print(span[0].text)
        s = span[0].text
        s = s[s.find("(")+1:s.find(")")]
        over1 = over
        over = s.split(" ",1)[0]
    except Exception as e:
        print('Exception occured')
        time.sleep(5)
        continue
    if(math.ceil(float(over))-(float(over)) == 0 and over!=over1):
        n.show_toast("Match Info-"+str(header[0]),span[0].text,6)
    time.sleep(10)