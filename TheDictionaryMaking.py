# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:52:05 2018

@author: Melvin, Daddy, Jado
"""
#import Counter and OderedDict object from the collections library
from collections import Counter
from collections import OrderedDict
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

#create the LinesAttempt.txt file and CountedWords.txt file as the files
#which are ready to be written.
file_name1 = "F:\WebCrawler\LinesAttempt.txt"
file_name1_5 = "F:\WebCrawler\TheCleaning.txt"
file_name2 = "F:\WebCrawler\CountedWords.txt"
Wfile1 = open(file_name1,"w")
Wfile1_5 = open(file_name1_5,"w")
Wfile2 = open(file_name2,"w")

#read the RawData.txt file and processed the sentences by separating paragraphs
#into sentences, differentiated by the fullstop symbol.
with open('F:\WebCrawler\RawData.txt','r') as f:
    for line in f:
        parts = line.strip().split('.')
        for part in parts:
            results = part.strip('\n')
            Wfile1.write(results + '\n')
            tokenizedRs = tokenizer.tokenize(results)
            for tokenizedR in tokenizedRs:
                TheClean = tokenizedR.strip()
                Wfile1_5.write(TheClean + '\n')
                

#crete the dictioary and write it down in the CountedWords.txt file as the final
#result in the ascending sort format
file=open("F:\WebCrawler\TheCleaning.txt","r+")

wordcount = Counter(file.read().split())
wordcounts = OrderedDict(sorted(wordcount.items()))
for item in wordcounts.items(): Wfile2.write("{}\t\t{}\n".format(*item)) 

file.close()
Wfile1.close()
Wfile1_5.close()
Wfile2.close()