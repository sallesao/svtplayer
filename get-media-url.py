#!/usr/bin/python3

import sys
#sys.path.append('svtplay-dl/lib')

from svtplay_dl.service.svtplay import Svtplay
from svtplay_dl import Options


# get svtplay video streams
svtplay = Svtplay(Options(), sys.argv[1])  # supply url from commande line
streams = svtplay.get()

# iterate over acquired stream and use the one with highest quality
bitrate = 0
url = None
for stream in streams:
    if stream.url[:7] == "http://":
        if stream.bitrate >= bitrate:
            bitrate = stream.bitrate
            url = stream.url

print(url)
