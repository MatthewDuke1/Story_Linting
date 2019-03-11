S = ['my','mother','says','that','the','cat','chased','a','mouse']
Chart = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
Lexicon = [['V','saw'],['D','a'],['DP','Mary'],['A','fluffy'],['NP','cat'],['D','the'],['C','that'],['NP','mouse'],['NP','mother'],['D','my'],['V','says'],['V','chased'],['V','likes'],['NP','house']]
Grammar = [['S','DP','VP'],['DP','D','NP'],['NP','NP','PP'],['PP','P','DP'],['VP','V','DP'],['VP','V','PP'],['VP','V','CP'],['CP','C','S']]

for c in range(len(S)):
	for r in range(len(S)-1,-1,-1):
		if c == r:
			for L in range(len(Lexicon)):
				if S[c] == Lexicon[L][1]:
					Chart[r][c] = Lexicon[L][0]
					print (L)
		if c > r:
			for b in range(c-1,r-1,-1):
				for g in range(len(Grammar)):
					if Chart[r][b] == Grammar[g][1] and Chart[b+1][c] == Grammar[g][2]:
						Chart[r][c] = Grammar[g][0]