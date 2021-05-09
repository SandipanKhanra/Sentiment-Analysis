
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
#This function is used to strip down the unnecessary characters
def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s=s.replace(i,"")
    return s

# lists of words to use
#As part of the project this hypothetical .txt file was given
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
#This function returns number of positive words in the tweet
def get_pos(s):
    count=0
    s=s.lower()
    x=[]
    x=s.split()
    for i in x:
        i=strip_punctuation(i)
        if i in positive_words:
            count+=1
    return count


#As part of the project this hypothetical .txt file was given
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#This function returns number of negitive words in the tweet
def get_neg(s):
    count=0
    s=s.lower()
    x=[]
    x=s.split()
    for i in x:
        i=strip_punctuation(i)
        if i in negative_words:
            count+=1
    return count

#This hypothetical .csv file containing some fake tweets was given for analysi
filedName = None
file = open("project_twitter_data.csv")
lines = file.readlines()
fieldName = lines[0].strip().split(',')
#print(fieldName)

'''here we are iterating over each line, considering only the tweet
then processing it with the previous functions
storing positive word count, negative word count, net score(how much positiive or negative)
'''
ans = []
for line in lines[1:]:
    tweet= line.strip().split(',')
    tempTweet = strip_punctuation(tweet[0])
    posCount = get_pos(tempTweet)
    negCount  = get_neg(tempTweet)
    net = posCount - negCount
    #Making a tuple containing Number of retweets,number of replies,posCount,negCount,Net score
    t = (int(tweet[1]),int(tweet[2]),posCount,negCount,net)
    ans.append(t)
#print(ans[4])



#Making the header of the new csv file
outputHeader = "{},{},{},{},{}".format('Number of Retweets','Number of Replies',
                                    'Positive Score','Negative Score','Net Score')
#writing data in the new csv file
output = open('resulting_data.csv','w')
output.write(outputHeader)
output.write('\n')
for i in ans:
    raw = '{},{},{},{},{}'.format(i[0],i[1],i[2],i[3],i[4])
    output.write(raw)
    output.write('\n')

