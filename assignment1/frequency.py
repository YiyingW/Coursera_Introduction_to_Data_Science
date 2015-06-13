import sys
import json


def frequency(tweet_file):
	

	line=tweet_file.readlines()
	# use list words to store each tweet
	words=[]
	for i in range(0, len(line)):
		words.append(json.loads(line[i]))
	wordlist=[]
	for i in range(0,len(words)):
		if 'text' in words[i].keys():
			strs=words[i]['text'].split(' ')
			for item in strs:
				wordlist.append(item)
	pair={}
	for i in range(0, len(wordlist)):
		if wordlist[i] not in pair.keys():
			pair[wordlist[i]]=1
		else:
			pair[wordlist[i]]=pair[wordlist[i]]+1

	length=len(wordlist)
	result={}
	for i in pair.keys():
		result[i]=pair[i]/float(length)

	for key in result.keys():
		print key, ' ', result[key]



def main():
    tweet_file = open(sys.argv[1])
    frequency(tweet_file)


if __name__ == '__main__':
    main()
