import glob #imports all files
from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier

spam = {}
ham = {}
probSpam = {}
words = 0
newfile = 0
value = 0
filevalue = 0
spamemail = 0
hamemail = 0

#get unigrams

#For Ham Files - ngram and put into hash map
for filename in glob.glob('./ham/*.txt'):
	with open(filename) as file:
		for line in file:
			for word in line.split(): #tokenizes the line on whitespace
				word = word.lower()
                		word = word.replace('.', '')
                		word = word.replace('\'', '')
                		word = word.replace('"', '')
                		word = word.replace(']', '')
                		word = word.replace('[', '')
                		word = word.replace('-', '')
                		word = word.replace('_', '')
				if(word in ham):
					ham[word]+=1
				else:
					ham[word]=1
'''
for element in ham:
    print element+" "+str(ham[element])
'''

'''
for word in ham:
    print ham[word]
'''

#For spam files - ngram and put into hash map

for filename2 in glob.glob('./spam/*.txt'):
	with open(filename2) as file2:
		for line in file2:
			for word in line.split(): #tokenizes the line on whitespace
				word = word.lower()
				word = word.replace('.', '')
				word = word.replace('\'', '')
				word = word.replace('"', '')
				word = word.replace(']', '')
				word = word.replace('[', '')
				word = word.replace('-', '')
				word = word.replace('_', '')
				if(word in spam):
					spam[word]+=1
				else:
					spam[word]=1
'''
for element in spam:
    print element +" "+str(spam[element])
'''

#spam probability
for word in spam:
	if(word in ham):
		probSpam[word] = float(spam[word])/(float(spam[word])+float(ham[word]))
	else:
		probSpam[word] = float(.999999) #only in spam

for word in ham:
	if(word not in spam):
		probSpam[word] = float(.000001) #only in ham

'''
for element in probSpam:
    print element+" "+str(probSpam[element])
'''
correct_count = 0
#For spam files - ngram and put into hash map
for filename3 in glob.glob('./test/*.txt'):
	with open(filename3) as file3:
        	for line in file3:
			for word in line.split(): #tokenizes the line on whitespace
				word = word.lower()
				word = word.replace('.', '')
				word = word.replace('\'', '')
				word = word.replace('"', '')
				word = word.replace(']', '')
				word = word.replace('[', '')
				word = word.replace('-', '')
				word = word.replace('_', '')
				
				if(word in probSpam and (probSpam[word] > 0.8 or probSpam[word] < 0.2)):
					value += probSpam[word]
					words+=1
				#else:
					#print "bug"
		print str(filename3) + " " + str(float(value)/float(words))
        	newfile+=1
        	filevalue+=(float(value)/float(words))
		if(float(value)/float(words) > .5):
			spamemail+=1
			if 'spam' in filename3:
				correct_count += 1
		else:
			hamemail+=1
			if 'ham' in filename3:
				correct_count += 1
		words = 0
		value = 0

#print "Average spam" + str(float(filevalue)/float(newfile))
#print str(spamemail) + " " + str( hamemail)
print "Accuracy", float(correct_count) / float(spamemail + hamemail) * 100
