#!/usr/bin/python3

import sys

import bs4
import requests


def main():
    # get page content
    url = sys.argv[1]
    try:
        r = requests.get(url)
        if r.ok:
            page_soup = bs4.BeautifulSoup(r.content, 'lxml')
        r.close()
    except Exception as e:
        print "Could not download", e
        sys.exit(1)

    # find all episodes list items
    episode_chunk = page_soup.find(id='play_title-page__content--more-episodes')
    episode_items = \
            episode_chunk.findAll('li',
                    attrs={'class':
                           'play_vertical-list__item ' + \
                           'play_js-vertical-list-item'})

    episodes = {}
    for ep in episode_items:
        print ep.p.contents[0].strip()
        print "https:" + str(ep.img['src'])
        print "http://svtplay.se" + str(ep.a['href'])
        print "---"


if __name__ == "__main__":
    main()
