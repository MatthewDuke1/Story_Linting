text = 'from a park to a park from a park to a park from a park to a park from the park to the park from the park to the park from the park to the park'

text = text.split()
UnigramCounts = {}
BigramCounts = {}

for n in range(len(text)-1):
  if text[n] in UnigramCounts:
    UnigramCounts[text[n]] = UnigramCounts[text[n]] + 1
  else:
    UnigramCounts[text[n]] = 1
  if (text[n],text[n+1]) in BigramCounts:
    BigramCounts[(text[n],text[n+1])] = BigramCounts[(text[n],text[n+1])] + 1
    print(n)
  else:
    BigramCounts[(text[n],text[n+1])] = 1

UnigramCounts[text[len(text)-1]] = UnigramCounts[text[len(text)-1]]  + 1

Words = sorted(list(set(text)))
FreqMat = [0] * len(Words)

for w1 in range(len(Words)):
  FreqMatRow = [0] * len(Words)
  for w2 in range(len(Words)):
    if (Words[w1],Words[w2]) in BigramCounts:
      FreqMatRow[w2] = BigramCounts[(Words[w1],Words[w2])]
  FreqMat[w1] = FreqMatRow

WordSimilarity = [0] * len(Words)

for w1 in range(len(Words)):
  WordSimilarityRow = [0] * len(Words)
  for w2 in range(len(Words)):
    sim = 0
    for n in range(len(Words)):
      sim = (FreqMat[w1][n] * FreqMat[w2][n]) + sim
    WordSimilarityRow[w2] = sim
  WordSimilarity[w1] = WordSimilarityRow
  
print(FreqMat) 
print('---------')