# -*- coding: utf-8 -*-
"""
Created on Mon May  28 10:54:35 2018

@author: Melvin, Daddy, Jado
"""
#importing modules to operate the stemming and dictionary creation
from collections import Counter
from collections import OrderedDict
from nltk.stem import PorterStemmer
ps = PorterStemmer()

#Creating file that will be written in for the stemming activity
file_name1 = "F:\WebCrawler\AfterStemming.txt"
file_name2 = "F:\WebCrawler\DictAfterStem.txt"
Wfile1 = open(file_name1,"w")
Wfile2 = open(file_name2,"w")

#importing a file from the previous experiment named TheCleaning.txt which 
#is basically a collection of words that is unsorted but cleaned of any signs;
#Processing the stemming by calling upon the stem from Porter Stemmer function
with open('F:\WebCrawler\TheCleaning.txt','r') as g:
    for word in g:
        cleaned = word.strip()
        stemmed = ps.stem(cleaned)
        Wfile1.write(stemmed + '\n')
Wfile1.close()

#Reading the Stemmed file named AfterStemming.txt that derived from the
#previously TheCleaning.txt; After reading, the file is sorted and counted of
#how many words exists in the file as a new dictionary
file=open("F:\WebCrawler\AfterStemming.txt","r+")
wordcount = Counter(file.read().split())
wordcounts = OrderedDict(sorted(wordcount.items()))
for item in wordcounts.items(): Wfile2.write("{}\t\t{}\n".format(*item))
Wfile2.close()




