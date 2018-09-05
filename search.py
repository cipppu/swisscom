#!/usr/bin/python

from googlesearch import search
for url in search('swisscom', stop=5):
    print(url)

