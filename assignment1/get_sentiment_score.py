afinnfile=open("AFINN-111.txt")
scores={}
for line in afinnfile:
	term,score=line.split("\t")
	scores[term]=int(score)

print scores.items()