import time

print "##############################################################################"
print 'This is a Basic Assimilation Evaluation Toolkit for Basque-English Pair'
print 'Hint level'
print '0 = No hint'
print '1 = Source Hint (Basque Sentence)'
print '2 = Machine Translation Hint (Apertium Sentence)'
print '3 = Both Source and Machine Translation Hint'
print '##############################################################################'

hintLevel = input('\nPlease choose the Hint Level: ')

print 'You have selected',
if hintLevel == 0:
    print "\"No hint\"\n"
elif hintLevel== 1:
    print "\"Source Hint (Basque Sentence)\""
elif hintLevel == 2:
    print "\"Machine Translation Hint (Apertium Sentence)\""
elif  hintLevel == 3:
    print "\"Both Source and Machine Translation Hint\""

#printInstruction() print relevent instruction to the user
sourceFile = open('Source Sentences.txt', 'r')
sourceSentences = sourceFile.readlines()

ApertiumFile = open('Apertium Translation.txt', 'r')
ApertiumSentences = ApertiumFile.readlines()

ReferenceFile = open('Reference Translation.txt', 'r')
ReferenceSentences = ReferenceFile.readlines()

choice=1 #option to continue, if choice ==0, exit

index=0 #sentence index, for assimilation evaluation
index=input('select index: ')

while(choice!=0):
	#if(hintLevel==0):
		#print reference sentence;
	if(hintLevel==1):
		print "\n--> Source Hint (Basque Sentence):"
		print sourceSentences[index]

	elif(hintLevel==2):
		print "\n-->Machine Translation Hint (Apertium Sentence):"
		print ApertiumSentences[index]

	elif(hintLevel==3):
		print "\n-->Source Hint (Basque Sentence):"
		print sourceSentences[index]
		time.sleep(1) #for usability
	
		print "\n-->Machine Translation Hint (Apertium Sentence):"
		print ApertiumSentences[index]

	time.sleep(1) #show the instructions, step by step For better user experience

	print 'Fill the blanks:'
	#print ReferenceSentences[index]

	#print masked reference traslation
	words = ReferenceSentences[index].split() #this should be from reference

	cloze=[] #words to be clozed

	Nthblank=1
	for i in range(len(words)):
		if((i+1)%5==0):
			print '['+str(Nthblank) +']'+"_____",
			Nthblank+=1
			cloze.append(words[i])
		else:
			print words[i],
	print '\n'

	userGuess=[]
	noBlanks=0
	correctResponses=0

	print 'Plese enter your guess:'
	for i in range(Nthblank-1):
			print 'for '+ str(i+1) +  'th blank: ',
			guess  = raw_input()
			userGuess.append(guess)
			if(guess==''):
				noBlanks+=1
			elif(guess==cloze[i]):
				correctResponses +=1

	outputfile = open('userOutput.txt', 'a')

	
	print>>outputfile, '---------------------'
	print>>outputfile, '| Sentence Index = '+str(index)+' |'
	print>>outputfile, '---------------------'
	print>>outputfile, ReferenceSentences[index]

	print>>outputfile, 'Hint Level = ' + str(hintLevel),
	if hintLevel == 0:
   		print>>outputfile, "\"No hint\"\n"
	elif hintLevel== 1:
		print>>outputfile, "\"Source Hint (Basque Sentence)\""
	elif hintLevel == 2:
		print>>outputfile, "\"Machine Translation Hint (Apertium Sentence)\""
	elif  hintLevel == 3:
    		print>>outputfile, "\"Both Source and Machine Translation Hint\""
	
	#print>>outputfile, 'Holes sucessfully filled (exactly as in Reference) = ' + str(correctResponses*100/(Nthblank-1)) + '%'
	
	print>>outputfile, 'Correct Responses = ' + str(correctResponses*100/(Nthblank-1)) + '%'
	print>>outputfile, 'Blanks Left = ' + str(noBlanks*100/(Nthblank-1)) + '%'

	print>>outputfile, '\nData:'
	for i in range(Nthblank-1):
			  print>>outputfile, cloze[i] + '\t\t',
			  print>>outputfile, ' --> ',
			  print>>outputfile, userGuess[i]

	
	print>>outputfile, '##############################################################################\n'
	
	print 'Thank You. Your response has been recorded\n'
	print 'Press 1 to continue'
	print 'Press 0 to exit'

	choice = input('Enter your choice: ')

	if(1==choice):
		index +=1
		print '\n##################################################'
		print 'Hint level'
		print '0 = No hint'
		print '1 = Source Hint (Basque Sentence)'
		print '2 = Machine Translation Hint (Apertium Sentence)'
		print '3 = Both Source and Machine Translation Hint'
		print '##################################################'

		hintLevel = input('\nPlease choose the Hint Level: ')

		print 'You have selected',
		if hintLevel == 0:
		    print "[No hint]\n"
		elif hintLevel== 1:
		    print "[Source Hint (Basque Sentence)]"
		elif hintLevel == 2:
		    print "[Machine Translation Hint (Apertium Sentence)]"
		elif  hintLevel == 3:
		    print "[Both Source and Machine Translation Hint]"


