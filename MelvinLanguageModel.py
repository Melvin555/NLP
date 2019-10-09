# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:33:52 2018

@author: Melvin, Jado, Daddy
"""
import re
import math
import fileinput
import random

file_name1 = "F:\WebCrawler\OurCorpusAfterAddS.txt"
file_name1_5 = "F:\WebCrawler\OurCorpusFin.txt"
file_name1_5_x = "F:\WebCrawler\OurCorpusFin2.txt"
file_name1Test = "F:\WebCrawler\OurTest.txt"
file_name1Train = "F:\WebCrawler\OurTrain.txt"
file_name2 = "F:\WebCrawler\OtherCorpus2AfterAddS.txt"
file_name2_5 = "F:\WebCrawler\OtherCorpus2Fin.txt"
file_name2_5_x = "F:\WebCrawler\OtherCorpus2Fin2.txt"
file_name2Test = "F:\WebCrawler\OtherTest.txt"
file_name2Train = "F:\WebCrawler\OtherTrain.txt"
Wfile1 = open(file_name1,'w')
Wfile1_5 = open(file_name1_5,'w')
Wfile1_5_x = open(file_name1_5_x,'w')
Wfile1Test = open(file_name1Test,'w')
Wfile1Train = open(file_name1Train,'w')
Wfile2 = open(file_name2,'w')
Wfile2_5 = open(file_name2_5,'w')
Wfile2_5_x = open(file_name2_5_x,'w')
Wfile2Test = open(file_name2Test,'w')
Wfile2Train = open(file_name2Train,'w')            
UNK = None
beginning = "<s>"
ending = "</s>"

def reading(file_path):
    with open(file_path, "r") as f:
        return [re.split("\s+", line.rstrip('\n')) for line in f]

class Unigram:
    def __init__(self, sentences, smoothing=False):
        self.unigram_frequencies = dict()
        self.corpus_length = 0
        for sentence in sentences:
            for word in sentence:
                self.unigram_frequencies[word] = self.unigram_frequencies.get(word, 0) + 1
                if word != beginning and word != ending:
                    self.corpus_length += 1
        # subtract 2 because unigram_frequencies dictionary contains values for SENTENCE_START and SENTENCE_END
        self.unique_words = len(self.unigram_frequencies) - 2
        self.smoothing = smoothing

    def calculate_unigram_probability(self, word):
            word_probability_numerator = self.unigram_frequencies.get(word, 0)
            word_probability_denominator = self.corpus_length
            if self.smoothing:
                word_probability_numerator += 1
                # add one more to total number of seen unique words for UNK - unseen events
                word_probability_denominator += self.unique_words + 1
            return float(word_probability_numerator) / float(word_probability_denominator)

    def calculate_sentence_probability(self, sentence, normalize_probability=True):
        sentence_probability_log_sum = 0
        for word in sentence:
            if word != beginning and word != ending:
                word_probability = self.calculate_unigram_probability(word)
                sentence_probability_log_sum += math.log(word_probability, 2)
        return math.pow(2, sentence_probability_log_sum) if normalize_probability else sentence_probability_log_sum                

    def sorted_vocabulary(self):
        full_vocab = list(self.unigram_frequencies.keys())
        full_vocab.remove(beginning)
        full_vocab.remove(ending)
        full_vocab.sort()
        full_vocab.append(UNK)
        full_vocab.append(beginning)
        full_vocab.append(ending)
        return full_vocab

class Bigram(Unigram):
    def __init__(self, sentences, smoothing=False):
        Unigram.__init__(self, sentences, smoothing)
        self.bigram_frequencies = dict()
        self.unique_bigrams = set()
        for sentence in sentences:
            previous_word = None
            for word in sentence:
                if previous_word != None:
                    self.bigram_frequencies[(previous_word, word)] = self.bigram_frequencies.get((previous_word, word),
                                                                                                 0) + 1
                    if previous_word != beginning and word != ending:
                        self.unique_bigrams.add((previous_word, word))
                previous_word = word
        # we subtracted two for the Unigram model as the unigram_frequencies dictionary
        # contains values for SENTENCE_START and SENTENCE_END but these need to be included in Bigram
        self.unique__bigram_words = len(self.unigram_frequencies)

    def calculate_bigram_probabilty(self, previous_word, word):
        bigram_word_probability_numerator = self.bigram_frequencies.get((previous_word, word), 0)
        bigram_word_probability_denominator = self.unigram_frequencies.get(previous_word, 0)
        if self.smoothing:
            bigram_word_probability_numerator += 1
            bigram_word_probability_denominator += self.unique__bigram_words
        return 0.0 if bigram_word_probability_numerator == 0 or bigram_word_probability_denominator == 0 else float(
            bigram_word_probability_numerator) / float(bigram_word_probability_denominator)

    def calculate_bigram_sentence_probability(self, sentence, normalize_probability=True):
        bigram_sentence_probability_log_sum = 0
        previous_word = None
        for word in sentence:
            if previous_word != None:
                bigram_word_probability = self.calculate_bigram_probabilty(previous_word, word)
                bigram_sentence_probability_log_sum += math.log(bigram_word_probability, 2)
            previous_word = word
        return math.pow(2,
                        bigram_sentence_probability_log_sum) if normalize_probability else bigram_sentence_probability_log_sum

def calculate_number_of_bigrams(sentences):
        bigram_count = 0
        for sentence in sentences:
            # remove one for number of bigrams in sentence
            bigram_count += len(sentence) - 1
        return bigram_count

def calculate_bigram_perplexity(model, sentences):
    number_of_bigrams = calculate_number_of_bigrams(sentences)
    bigram_sentence_probability_log_sum = 0
    for sentence in sentences:
        try:
            bigram_sentence_probability_log_sum -= math.log(model.calculate_bigram_sentence_probability(sentence), 2)
        except:
            bigram_sentence_probability_log_sum -= float('-inf')
            
    return math.pow(2, (bigram_sentence_probability_log_sum / number_of_bigrams))

############################################################################

with open('F:\WebCrawler\LinesAttempt.txt','r') as f:
    for line in f:
        parts = line.strip().split('.')
        for part in parts:
            results = part.strip('\n')
            results2 = results.strip('\t')
            results3 = re.sub(r'[^\w\s]','',results2)
            results4 = results3.lower()
            NewLine = "<s> "+results4+" </s>"
            Wfile1.write(NewLine+'\n')
Wfile1.close()
with open('F:\WebCrawler\OurCorpusAfterAddS.txt','r') as f:
    for line in f:
        line = line.replace("<s>  </s>","")
        Wfile1_5.write(line) 
Wfile1_5.close()
for line in fileinput.FileInput("F:\WebCrawler\OurCorpusFin.txt",inplace=1):
    if line.rstrip():
        Wfile1_5_x.write(line)
Wfile1_5_x.close()

############################################################################

with open('F:\WebCrawler\OurCorpusFin2.txt','r') as f:
    tset = []; indexTest = []
    for line in f:
        tset.append(line)
    for i in range(100):
        randIndex = int(random.uniform(0,len(tset)))
        Wfile1Test.write(tset[randIndex])
        del(tset[randIndex])
        indexTest.append(randIndex)
Wfile1Test.close()
with open('F:\WebCrawler\OurCorpusFin2.txt','r') as f:
    for line in tset:
        Wfile1Train.write(line)
Wfile1Train.close()

############################################################################


with open('F:\WebCrawler\OtherCorpus2.txt','r') as f:
    for line in f:
        parts = line.strip().split('.')
        for part in parts:
            results = re.sub(r'[^\w\s]','',part)
            results2 = results.lower()
            NewLine = "<s> "+results2+" </s>"
            Wfile2.write(NewLine+'\n')
Wfile2.close()
with open('F:\WebCrawler\OtherCorpus2AfterAddS.txt','r') as f:
    for line in f:
        line = line.replace("<s>  </s>","")
        Wfile2_5.write(line) 
Wfile2_5.close()
for line in fileinput.FileInput("F:\WebCrawler\OtherCorpus2Fin.txt",inplace=1):
    if line.rstrip():
        Wfile2_5_x.write(line)
Wfile2_5_x.close()

###########################################################################

with open('F:\WebCrawler\OtherCorpus2Fin2.txt','r') as f:
    tset = []; indexTest = []
    for line in f:
        tset.append(line)
    for i in range(100):
        randIndex = int(random.uniform(0,len(tset)))
        Wfile2Test.write(tset[randIndex])
        del(tset[randIndex])
        indexTest.append(randIndex)
Wfile2Test.close()
with open('F:\WebCrawler\OtherCorpus2Fin2.txt','r') as f:
    for line in tset:
        Wfile2Train.write(line)
Wfile2Train.close()

############################################################################

DatasetOur = reading('F:\WebCrawler/OurTrain.txt')
testDatasetOur = reading('F:\WebCrawler/OurTest.txt')
Our = Bigram(DatasetOur, smoothing=True)
#print("PERPLEXITY of train [OUR].txt")
#print("bigram: ", calculate_bigram_perplexity(Our, DatasetOur))
print("The Perplexity of [OUR] test.txt")
print("bigram: ", calculate_bigram_perplexity(Our, testDatasetOur))
print()
print()
print("OtherCorpus")
DatasetOther = reading('F:\WebCrawler\OtherTrain.txt')
testDatasetOther = reading('F:\WebCrawler\OtherTest.txt')
Other = Bigram(DatasetOther, smoothing=True)
#print("PERPLEXITY of train.txt [OTHER]")
#print("bigram: ", calculate_bigram_perplexity(Other, DatasetOther))
print("The Perplexity of [Other] test.txt")
print("bigram: ", calculate_bigram_perplexity(Other, testDatasetOther))
print("The Perplexity of test.txt [using OUR test]")
print("bigram: ", calculate_bigram_perplexity(Other, testDatasetOur))

