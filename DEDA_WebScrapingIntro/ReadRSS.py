"""
Description:
 - A simple demo to get RSS feed from Financial Times Journal.

Usage: Executing this whole file in your IDE or from Terminal or executing line by line in IPython.

Author:
 - Junjie Hu, hujunjie@hu-berlin.de
 - Cathy Chen
Last modified date: 19-11-2017
"""

import feedparser

# retrieve RSS feedback
content = feedparser.parse("https://www.ft.com/?edition=international&format=rss")

# list all titles
print("\nTitles-------------------------\n")
for index, item in enumerate(content.entries):
    print("{0}.{1}".format(index, item["title"]))

# list all description
print("\r\nDescriptions-------------------\r\n")
for index, item in enumerate(content.entries):
    print("{0}.{1}\n".format(index, item["description"]))
