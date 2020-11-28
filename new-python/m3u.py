#!/usr/bin/env python

import os
import sys
import glob
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from pathlib import Path

#
# MP3 playlist generator
#
# Generate an mp3 playlist file (.m3u), sorted by album track number.
#
# DEPENDENCIES
#
#   - Mutagen (http://code.google.com/p/mutagen/)
#
# NOTE: To install `mutagen`, run:
#
#   $ cd /path/to/mutagen/download/dir && python setup.py install
#
# USAGE
#
# You can pass directories two ways this script - as arguments or
# via standard input.
#
#   $ m3u.py /AphexTwin/Drukqs
#
# or multiple directories:
#
#   $ find /dir/Music -type d -links 2 | m3u.py -
#
# Author: Jon LaBelle <jon@tech0.com>
# Date: Sun Jul 28 2013 06:27:42 GMT-0500 (CDT)
#

def create_m3u(dir="."):
    mp3s = []
    cwd = os.path.dirname(os.path.realpath(__file__))
    print("Listing all mp3s in %s" % cwd)
    glob_pattern = "*.[mM][pP]3"
    for file in Path(cwd).rglob(glob_pattern):
        try:
            meta_info = {
                'filename': file,
				'artist': EasyID3(file)['artist'][0],
				'title': EasyID3(file)['title'][0],
                'length': int(MP3(file).info.length),
                'tracknumber': EasyID3(file)['tracknumber'][0].split('/')[0],
            }
            print(file)
            mp3s.append(meta_info)
        except:
            continue
    return mp3s


def main(argv=None):
    mp3s = []
    mp3s = create_m3u(dir)

    print("Writing playlist playlist.m3u8")

    # write the playlist
    playlist = "playlist.m3u8"
    of = open(playlist, 'w', encoding='utf-8')
    of.write("#EXTM3U\n")
    # sorted by track number
    for mp3 in mp3s:
        of.write("#EXTINF:%s,%s - %s\n" % (mp3['length'], mp3['artist'], mp3['title']))
        of.write(str(mp3['filename']) + "\n")
    of.close()
    print("Playlist written successfully!\n")
    return 0

main()