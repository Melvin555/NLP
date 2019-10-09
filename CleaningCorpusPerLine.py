# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:20:00 2018

@author: Melvin
"""

with open('F:\WebCrawler\RawData.txt','r') as f:
    for line in f:
        clean = line.strip()
        for line in clean:
            clean2 = clean.split('.')
            print(clean2)