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
    except:
        print("Could not download")
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
        # episode name
        ep_hdr_class = {'class': 'play_vertical-list__header'}
        print(ep.find('h2', attrs=ep_hdr_class).a.contents[0])

        print(ep.find('time').contents[0])              # episode length
        print(ep.p.contents[0].strip())                 # published
        print("https:" + str(ep.img['src']))            # thumbnail
        print("http://svtplay.se" + str(ep.a['href']))  # episode page
        print("---")


if __name__ == "__main__":
    main()
