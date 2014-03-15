This is the Basic Assimilation Evaluation Tookit.
Author - Binay Neekhra (neekhra.binay@gmail.com)

To run the program, type the command 
]$ python basicTookit.py

It takes sentences from 'Source Sentences.txt' file, 'Apertium Translation.txt' file, 'Reference Translation.txt' file,
and based on user chosen hint level, shows the relevant hints and ask to fill the cloze test.

user can choose the hint level.
0 = No hint
1 = Source Hint (Basque Sentence)
2 = Machine Translation Hint (Apertium Sentence)
3 = Both Source and Machine Translation Hint

A Cloze tests with masked reference trasnlation will be presented to the user.
	
	-----------
	|Sample Run|
	------------

]$ python basicToolkit.py 
##############################################################################
This is a Basic Assimilation Evaluation Toolkit for Basque-English Pair
Hint level
0 = No hint
1 = Source Hint (Basque Sentence)
2 = Machine Translation Hint (Apertium Sentence)
3 = Both Source and Machine Translation Hint
##############################################################################

Please choose the Hint Level: 2
You have selected "Machine Translation Hint (Apertium Sentence)"

-->Machine Translation Hint (Apertium Sentence):
*Fagor *Etxetresnen *konkurtsoa Managing he needed , he when knew last year, owner of the Trade part of Donostia Pedro *Malagon the judge he would think the big challenge he had , in front.

Fill the blanks:
Fagor know that he [1]_____ to manage the competition [2]_____ year , Commercial San [3]_____ Malagon holders before the [4]_____ that he should become [5]_____ great challenge. 

Plese enter your guess:
for 1th blank:  need
for 2th blank:  last
for 3th blank:  
for 4th blank:  Malagon
for 5th blank:  the
Thank You. Your response has been recorded

Press 1 to continue
Press 0 to exit
Enter your choice: 

	------------------
	|End of Sample Run|
	-----------------

User is asked to guess the masked words.
The response is recorded in a separate file(userOutput.txt),
e.g. 

---------------------
| Sentence Index = 8 |
---------------------
Ireland Fagor says that the company's most valuable asset and selling it , the French factories , but that does not necessarily buy Cevitalek the Basque Country , and this commitment has taken.

Hint Level = 2 "Machine Translation Hint (Apertium Sentence)"
Correct Responses = 50%
Blanks Left = 16%

Data:
the		 -->  the
and		 -->  by
French		 -->  Basque
does		 -->  does
the		 -->  
this		 -->  this
##############################################################################

