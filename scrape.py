import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".titleline")
subtext = soup.select(".subtext")

def create_custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get("sitestr")
        vote = subtext[i].select(".score")
        if len(vote):
            # Converting our points value from strings to integer values
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({"title":title, "votes":points})
    return hn

pprint.pprint(create_custom_hn(links, subtext))