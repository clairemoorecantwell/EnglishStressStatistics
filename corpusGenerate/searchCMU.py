import re
import time
import string
import pickle


def searchCMU(factors,specifiers,check_inScope,output='output.txt',inSubtlex=1,subNasalsLiquids=1):
	try:
		subtlex={}
		with open('subtlex','r') as f:  #use subtlex to get some lexical frequencies
			for line in f:
				x=line.split('\\')
				subtlex[x[0]]=x
	except:
		inSubtlex=0
		print "It looks like you don't have the subtlex file. Ignoring lexical frequency information."
		
	inCelex=1	
	try:
		celex={}
		with open('celex','r') as f:  #use celex for part of speech, and as sanity check for frequencies
			for line in f:
				x=line.split('\\')
				celex[x[0]]=x
	except:
		inCelex=0
		print "It looks like you don't have the celex file.  Ignoring part of speech information."
		
	
	with open('cmuprosody','r') as f:
		cmuprosody=pickle.load(f)
	results=[]
	resultview=[]

	headerRow=['spelling','transcription','stressTrans','syllStruct',"syllabification"]
	for key in range(0,len(factors.keys())):
		headerRow.append(factors.keys()[key])
	for key in range(0,len(specifiers.keys())):
		headerRow.append(specifiers.keys()[key])
	headerRow.append('freq')
	headerRow.append('POS')
	results.append('\t'.join(headerRow))

	for entry in cmuprosody:
		ent=cmuprosody[entry]
		# Check if it's a well-formed CMU entry actually:
		if len(ent)!=5 or len(ent[0])==0 or len(ent[1])==0 or len(ent[2])==0 or len(ent[3])==0 or len(ent[4])==0:
			print "This entry is not well-formed! Let's skip it."
			print ent
			continue
		if check_inScope(ent):
			if inSubtlex:			# If you care about the word being listed in subtlex
				if entry in subtlex:# check whether it is, and only use it if it is.
					useThisOne=1
				else:
					useThisOne=0
			else:
				useThisOne=1
						
			if useThisOne:	
				if inSubtlex==1:		
					freq=subtlex[entry][8]		# If y, record its frequency as 'freq'
				else:
					freq='NA'
				if inCelex==1:
					if entry in celex:
						POS=celex[entry][2]
					else:
						POS='NA'
				else:
					POS='NA'
					
				# Initialize this line of output with the first few columns of info from the cmu entry
				resultlineSeed=[ent[0],''.join(ent[1]),''.join(ent[2]),'.'.join(ent[4])]
				resultline=resultlineSeed
				resultline.append("("+")(".join(ent[3])+")")
				#print resultline
			
			
				#######
				# Record values for all the factors
				for factor in factors:
					factorIsDefined=0
					for flab in factors[factor]:
						if factors[factor][flab](ent):
							if factorIsDefined:
								# Because of the way this script conceptualizes factors
								# It will throw an error whenever two levels of a factor 
								# 		both return true
								# So, you must build your functions well.
							
								print 'ERROR: two functions return true for the same entry\n'
								print '\t'.join(resultlineSeed)
								print '\n'
								print 'Factor involved:\n'
								print factor
								print '\n Problem level:\n'
								print flab
								print '\n Please fix your functions and try again'
								quit()
						
							else:
								# Add the correct level of this factor to the resultline as a new column
								resultline.append(flab)
								factorIsDefined=1
								
					# After cycling through all the levels of a factor, 
					# if that factor hasn't been defined
					# label it 'other'
					if (not factorIsDefined):
						resultline.append('other')
	
				for specifier in specifiers:
					resultline.append(str(specifiers[specifier](ent)))

				# Add this entry to the total results file
				resultline.append(freq)
				resultline.append(POS)
				results.append('\t'.join(resultline))
				resultview.append(resultline)

				
	# Write results to text file				
	with open(output,'w') as f:
		for line in results:
			f.write(line)
			f.write('\n')
	
	return resultview
			
	with open('new','w') as f:
		pickle.dump(results,f)
