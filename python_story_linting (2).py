import numpy

#filename = 'Austen.txt'
#text = open(filename, 'r')
#text = text.read()
#text = text.lower()

text = 'it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness'

text = text.split()

Words = sorted(list(set(text)))

BGM = numpy.zeros((len(Words), len(Words)))
IPM = numpy.zeros((len(Words), len(Words)))

for n in range(len(text)-1):
  BGM[Words.index(text[n])][Words.index(text[n+1])] = BGM[Words.index(text[n])][Words.index(text[n+1])] + 1
  if n < 11:
  	print(BGM[Words.index(text[n])][Words.index(text[n+1])])

for w1 in range(len(Words)):
  for w2 in range(len(Words)):
    IPM[w1][w2] = numpy.inner(BGM[w1], BGM[w2])