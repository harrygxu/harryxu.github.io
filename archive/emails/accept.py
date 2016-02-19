#!/bin/python

import sys
import codecs

msg ="""Hi {name},

Your talk \"{title}\" has been accepted for SoCal PLS Fall 2015 at Pomona College on Saturday, December 5th, 2015. We'll post a schedule shortly, but if you have any scheduling needs, please let us know as soon as you can. We apologize for the late notice, and hope you can still make it.

Thanks and see you on Saturday,
Michael, Chris, John, Crista, and Sorin""" # you probably want to change this message :)

# this is a TSV parsing script... total hack
subs = [[f.strip() for f in l.split('\t')] for l in codecs.open(sys.argv[1], "r", "utf8").readlines()[1:]]

# change these to accomodate your file
title = 1
abstract = 2
coauthors = 4
author = 3
email = 6

for sub in subs:
    out = codecs.open(sub[email], "w", "utf8")

    out.write(str(msg.format(name = sub[author], title = sub[title])))
    out.close()

    print u"""
<div class="talk">
  <div class="title">{title}</div>
  <div class="authors">{name} (with {coauthors})</div>
  <div class="abstract">{abstract}</div>
</div>
""".format(name = sub[author],
           coauthors = sub[coauthors],
           title = sub[title],
           abstract = sub[abstract])
