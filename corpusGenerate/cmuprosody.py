##WARNING: overwrites the output file (cmuprosody) with every run!!


import re
import nltk
from nltk.corpus import cmudict
import time
import string
import pickle
from syllabify import syllabify



ANY = set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'B', 'CH', 'D', 'DH', 'EH', 'ER', 'EY', 'F', 'G', 'HH', 'IH', 'IY', 'JH', 'K', 'L', 'M', 'N', 'NG', 'OW', 'OY', 'P', 'R', 'S', 'SH', 'T', 'TH', 'UH', 'UW', 'V', 'W', 'Y', 'Z', 'ZH'])
VOICED = set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'B', 'D', 'DH', 'EH', 'ER', 'EY', 'G', 'IH', 'IY', 'JH', 'L', 'M', 'N', 'NG', 'OW', 'OY', 'R', 'UH', 'UW', 'V', 'W', 'Y', 'Z', 'ZH'])
VOICELESS = set(['CH', 'F', 'HH', 'K', 'P', 'S', 'SH', 'T', 'TH'])
SONORANTS = set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW','L', 'M', 'N', 'NG', 'R','AN','AL'])
VOWELS = set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW', 'AN','AL'])
TENSE = set(['EY', 'AY', 'OW', 'AW', 'OY'])
CONSONANTS = set(['B', 'CH', 'D', 'DH', 'F', 'G', 'HH', 'JH', 'K', 'L', 'M', 'N', 'NG', 'P', 'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'Y', 'Z', 'ZH'])
NASALS = set(['M', 'N', 'NG'])
LIQUIDS = set(['L', 'R'])
APPROXIMANTS = set(['L', 'R', 'W', 'Y'])
STOPS = set(['K', 'P', 'T', 'B', 'D', 'G'])
FRICATIVES = set(['F', 'V', 'S', 'Z', 'SH', 'ZH', 'TH', 'DH', 'HH'])
		

# For loop:
# For every entry in cmu
start=time.time() #note the time when you started

cmubh=[]
with open('cmubh','r') as f:  #tab-delimited file with spelling, transcription, CELEX lemma freq, CELEX lemma freq divided among homographs, length
	for line in f:
		x=line.split('\t')
		entry=[]
		entry.append(x[0])
		entry.append(x[1].split(' '))
		entry.append(x[2])
		entry.append(x[3])
		entry.append(x[4])
		cmubh.append(entry)
		
#What do you want to use?  the bruce dictionary or the full dictionary?
cmuversion=cmubh #cmudict.entries() #cmubh
cmuprosody={} #we're making a new giant big old array to hold our new cmudict with prosodic annotations
for x in cmuversion: # There are 127069 entries in cmudict
		## xx is an entry of cmuprosody, which we will now populate
	xx=[x[0],x[1]] #initialize the array; make it start off with the original cmu dictionary entry
		
		### Prosodic form array ###
	pform=[] #initialize an empty array - this will contain the prosodic form
	for e in x[1]: #loop through the 'array' of phonemes
		m=re.search('([012])',e) #search each one for a stress mark
		if m: #if you found one
			pform.append(m.group()) #append the stress mark to the prosodic form array
	xx.append(pform) # append the prosodic form to the entry
		
		### Syllabifying ###
	w = x[1]  #Now, create a new array of phonemes
	w = [re.sub('[0-9]', '', p) for p in w] #Strip out the numbers
	w = ' '.join(w)	#Make one string
	syl=syllabify(w) #syllabify the string
	syl=[re.sub('[(,)]','', p) for p in syl.split(' (')] #Split the syl into an array of strings, and remove parentheses
	subNasalsLiquids=1
	if subNasalsLiquids==1:
		for r in range(len(syl)):
			syl[r]=re.sub('AH [mn]','AN',syl[r])
			syl[r]=re.sub('AH l','AL',syl[r])
	xx.append(syl) #Now, append the syllabification
		
		### Making the syllabic form array ###
		#xx.append(syl) #For checking if this worked
	sform=[]		#Initialize an array to hold the syllabic forms
	for s in syl: #loop through the syllables
		ss=s.split() #split each syllable into segments
		ff=''		 #this is the string that holds the syllable's form
		for i in ss: #for each segment in the syllable
			if i.isupper(): #If it's the nucleus
				if i in CONSONANTS:#find out whether it's a consonant or vowel
					ff+='L'#and add that to the string
				elif i in VOWELS:
#					ff+='V'			#If you don't care what kind of vowel
				
					if i in TENSE:	#If you do.
						ff+='T'
					else:
						ff+='L'
			else:
				ff+='C'
						
		sform.append(ff)
	xx.append(sform)
	cmuprosody[x[0]]=xx
	
with open('cmuprosody','w') as f:
	pickle.dump(cmuprosody,f)