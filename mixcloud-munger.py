#!/usr/bin/env python

#
# mixcloud-munger -- reformat Mixxx CSV track list for pasting into Mixcloud
#
# Mixcloud.com expects some bizarre format for data pasted into its
# tracklist upload box. This script converts from a sane comma
# separated value (CSV) file (e.g. produced by Mixxx's "Export
# Playlist" history functionality) into the bizarre format expected by
# Mixcloud (i.e. "Artist"Title").
#
# It may not handle embedded " characters correctly.
#
#
# ./mixcloud-munger.py mixxx_track_list.csv > output.txt
#
# ./mixcloud-munger.py mixxx_track_list.csv | pbpaste # (On OS X.)
#
#
# Author: follower@rancidbacon.com
#

import csv
import sys

if __name__ == "__main__":
    mixxx_csv_track_list_filename = sys.argv[1]

    fieldnames = ['Artist', 'Title']

    track_list_csv = csv.DictReader(open(mixxx_csv_track_list_filename))

    # Oh, yeah, this bit is obsolete, 'cos it's not actually CSV.
    #writer = csv.DictWriter(sys.stdout,
    #                        fieldnames=fieldnames,
    #                        delimiter='\t',
    #                        quoting=csv.QUOTE_ALL,
    #                        extrasaction='ignore')

    # writer.writeheader()

    for track in track_list_csv:
        #writer.writerow(track)
        sys.stdout.write('"%s"%s"\r\n' %
                         (track[fieldnames[0]], track[fieldnames[1]]) )

