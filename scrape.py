import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".titleline")
subtext = soup.select(".subtext")

def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k:k['votes'], reverse=True)

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
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))