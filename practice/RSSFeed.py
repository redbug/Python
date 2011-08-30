'''
Created on Mar 30, 2011

@author: redbug
'''

import feedparser

parsedData = feedparser.parse( "http://feeds.feedburner.com/blogspot/yOoIQ.xml" )
print "feed.title: %s " % parsedData.feed.title
print "feed.link: %s " % parsedData.feed.link
print "feed.descripton: %s " % parsedData.feed.description
#print parsedData.feed.date
#print parsedData.feed.date_parsed

for entry in parsedData.entries:
    print "entry.title: %s" % entry.title
    print "entry.description: %s" % entry.description
    print "entry.link: %s" % entry.link
    print "entry.date: %s" % entry.date
    print "entry.date_parsed: %s" % entry.date_parsed
#print parsedData.entries[0].id



