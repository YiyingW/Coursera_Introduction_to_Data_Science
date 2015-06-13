import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def get_sentiment_score(sent_file, tweet_file):
	#making a dictionary to store the score for each word
	scores={}
	for line in sent_file:
		term,score=line.split("\t")
		scores[term]=int(score)
	# calculate the sentiment score for each tweet
	line=tweet_file.readlines()
	# use list words to store each tweet
	words=[]
	for i in range(0, len(line)):
		words.append(json.loads(line[i]))
	result=[]
	for i in range(0,len(words)):
		if 'text' not in words[i].keys():
			result.append(0)
		else:
			strs=words[i]['text'].split(' ')
			tweet_score=0
			for item in strs:
				if item in scores.keys():
					tweet_score+=scores[item]
				else:
					True
			result.append(tweet_score)
	for item in result:
		print item


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    get_sentiment_score(sent_file,tweet_file)


if __name__ == '__main__':
    main()
