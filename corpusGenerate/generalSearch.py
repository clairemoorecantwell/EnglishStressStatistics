
################## How to use this script: #####################
# First: you must run cmuprosody.py to create the prosodified version of CMU.
#		Further directions are in the header of that file.
#		You will need a syllabification algorithm
#		And the nltk CMU library 
#
# After you've got that sorted out, you're ready to use this script here.
#
# Here's how it works:
#	
# 		separate out individual potential searches as much as possible
#	should be website-able soonish (17 Nov, 2013)
#
#	Next: perform a search for the alligator rule
#		(for the future)

# Import some things
import re
import time
import string
import pickle
from searchCMU import searchCMU
import morphology

# Define the function that will return TRUE for a match to the pattern
# and FALSE for a nonmatch.

# Key: cmuprosody[0] = spelling (one string)
#	   cmuprosody[1] = cmu transcription (array of strings, one string per phoneme)
#	   cmuprosody[2] = prosodic form (array of strings, one string per syllable)
#	   cmuprosody[3] = syllabification (array of strings, one string per syllable, phonemes separated by spaces)
#	   cmuprosody[4] = syllabic form (array of strings, one string per syllable)

# cmuprosody at this point will be a dictionary
#>>> cmuprosody['unencumbered']
#[u'unencumbered', [u'AH2', u'N', u'EH0', u'N', u'K', u'AH1', u'M', u'B', u'ER0', u'D'], [u'2', u'0', u'1', u'0'], [u'AH', u'n EH n', u'k AN', u'b ER d'], ['L', 'CLC', 'CL', 'CLC']]
#>>> cmuprosody['hello']
#[u'hello', [u'HH', u'EH0', u'L', u'OW1'], [u'0', u'1'], [u'hh EH', u'l OW'], ['CL', 'CT']]

# Pre-defined syllable types
light='C*L$'
opensyll='C*[LT]$'
heavy='C*TC*$|C*LCC*$'
Tsingleton='C*TC$'
Lsingleton='C*LC$'
finalLcluster='C*LCCC*$'
finalTcluster='C*TCCC*$'

# for searching the transcription
lightspecial='.*AH [nml]$'

# word-level things
###### If subNasalsLiquids is turned off
finali = '.*IY[^\)]*$'
finalschwa = '.*AH[^lmn]*$'
finalr='.*ER.*$'
finall='.*AH l$'
finalnas='.*AH [mn]$'

# set of characters used in vowels [AEHORIUNLYW]

# onset info
######
finalNoOnset = lambda cmue: bool(re.match('^[LT]',cmue[4][-1]))
finalOnsetC = lambda cmue: bool(re.match('^C[LT]',cmue[4][-1]))
finalOnsetCC = lambda cmue: bool(re.match('^CC[LT]',cmue[4][-1]))
finalOnsetCCC = lambda cmue: bool(re.match('^CCC[LT]',cmue[4][-1]))

penultNoOnset = lambda cmue: bool(re.match('^[LT]',cmue[4][-2]))
penultOnsetC = lambda cmue: bool(re.match('^C[LT]',cmue[4][-2]))
penultOnsetCC = lambda cmue: bool(re.match('^CC[LT]',cmue[4][-2]))
penultOnsetCCC = lambda cmue: bool(re.match('^CCC[LT]',cmue[4][-2]))

antepenultNoOnset = lambda cmue: bool(re.match('^[LT]',cmue[4][-3])) if len(cmue[4])>2 else False
antepenultOnsetC = lambda cmue: bool(re.match('^C[LT]',cmue[4][-3])) if len(cmue[4])>2 else False
antepenultOnsetCC = lambda cmue: bool(re.match('^CC[LT]',cmue[4][-3])) if len(cmue[4])>2 else False
antepenultOnsetCCC = lambda cmue: bool(re.match('^CCC[LT]',cmue[4][-3])) if len(cmue[4])>2 else False

######### If subNasalsLiquids is on
####### Meaning that (monosyllabic) AH [nm] sequences have been converted to 'AN' and 'AH l' sequences have been converted to 'AL'
finalshortV='(.*AA$)|(.*AE$)|(.*AH$)|(.*AO$)|(.*EH$)|(.*ER$)|(.*IH$)|(.*UH$)|(.*AN$)|(.*AL$)|(.*IY$)|(.*UW$)'
finallongV='(.*EY$)|(.*AY$)|(.*OW$)|(.*AW$)|(.*OY$)'
finalS='.*[AEHORIUNLYW] s.*$'  #This captures s in final position, and at the beginning of a cluster

check_aa = lambda cmue: bool(re.match('(.*AA.*$)',cmue[3][-1]))
check_ae = lambda cmue: bool(re.match('(.*AE.*$)',cmue[3][-1]))
check_ah = lambda cmue: bool(re.match('(.*AH.*$)',cmue[3][-1]))
check_ao = lambda cmue: bool(re.match('(.*AO.*$)',cmue[3][-1]))
check_eh = lambda cmue: bool(re.match('(.*EH.*$)',cmue[3][-1]))
check_er = lambda cmue: bool(re.match('(.*ER.*$)',cmue[3][-1]))
check_ih = lambda cmue: bool(re.match('(.*IH.*$)',cmue[3][-1]))
check_uh = lambda cmue: bool(re.match('(.*UH.*$)',cmue[3][-1]))
check_an = lambda cmue: bool(re.match('(.*AN.*$)',cmue[3][-1]))
check_al = lambda cmue: bool(re.match('(.*AL.*$)',cmue[3][-1]))
check_ey = lambda cmue: bool(re.match('(.*EY.*$)',cmue[3][-1]))
check_ay = lambda cmue: bool(re.match('(.*AY.*$)',cmue[3][-1]))
check_ow = lambda cmue: bool(re.match('(.*OW.*$)',cmue[3][-1]))
check_aw = lambda cmue: bool(re.match('(.*AW.*$)',cmue[3][-1]))
check_oy = lambda cmue: bool(re.match('(.*OY.*$)',cmue[3][-1]))
check_iy = lambda cmue: bool(re.match('(.*IY.*$)',cmue[3][-1]))
check_uw = lambda cmue: bool(re.match('(.*UW.*$)',cmue[3][-1]))

finalV={
	'aa':check_aa,
	'ae':check_ae,
	'ah':check_ah,
	'ao':check_ao,
	'eh':check_eh,
	'er':check_er,
	'ih':check_ih,
	'uh':check_uh,
	'an':check_an,
	'al':check_al,
	'ey':check_ey,
	'ay':check_ay,
	'ow':check_ow,
	'aw':check_aw,
	'oy':check_oy,
	'iy':check_iy,
	'uw':check_uw
		}


# final consonants.  try just returning a final consonant
def coda(syllable):
	m=re.search('[^AEHORIUNLYW]*$',syllable)
	return m.group()

finalCoda = lambda cmue: coda(cmue[3][-1])
codaLength = lambda cmue: len(re.sub('^ ',"",coda(cmue[3][-1])).split(" ")) if len(re.sub('^ ',"",coda(cmue[3][-1])))>0 else 0
	# Find the length in phonemes of the coda.  The re.sub bit removes a leading space which would throw of the count
	

# syllable weight
check_lightInclusive = lambda cmue: not bool([bool(re.match(light,cmue[4][r])) or bool(re.match(lightspecial,cmue[3][r])) for r in range(len(cmue[4]))].count(False))
#`Inclusive' means it includes syllabic l's and nasals.

check_finalNas = lambda cmue: bool(re.match(finalnas,cmue[3]))
check_finalLiq = lambda cmue: bool(re.match(finall,cmue[3]))
check_finalS = lambda cmue: bool(re.match(finalS,str(cmue[3])))




check_alllight = lambda cmue: not bool([bool(re.match(light,cmue[4][r])) for r in range(len(cmue[4]))].count(False))

check_penultHeavy = lambda cmue: (bool(re.match(heavy,cmue[4][-2])) and not bool(re.match(lightspecial,cmue[3][-2]))) and (bool(re.match(lightspecial,cmue[3][-3])) or bool(re.match(light,cmue[4][-3]))) if len(cmue[4])>2 else False
# Checks if the penult is heavy, AND the antepenult is light

check_penultHeavySimple = lambda cmue: bool(re.match(heavy,cmue[4][-2]) and not bool(re.match(lightspecial,cmue[3][-2]))) if len(cmue[4])>1 else False
# Checks if the penult is heavy

check_penultLight = lambda cmue: (bool(re.match(light,cmue[4][-2])) or bool(re.match(lightspecial,cmue[3][-2]))) if len(cmue[4])>2 else False



check_finalH=lambda cmue: (bool(re.match(heavy,cmue[4][-1])) and not(bool(re.match(lightspecial, cmue[3][-1]))))
check_finalL=lambda cmue: (bool(re.match(light,cmue[4][-1])) or bool(re.match(lightspecial,cmue[3][-1])))
check_finalTSingleton=lambda cmue: bool(re.match(Tsingleton,cmue[4][-1]))
check_finalLSingleton=lambda cmue: (bool(re.match(Lsingleton,cmue[4][-1])))
check_finalTCluster=lambda cmue: bool(re.match(finalTcluster,cmue[4][-1]))
check_finalLCluster=lambda cmue: bool(re.match(finalLcluster,cmue[4][-1]))

check_penultH=lambda cmue: (bool(re.match(heavy,cmue[4][-2])) and not(bool(re.match(lightspecial, cmue[3][-2])))) if len(cmue[4])>1 else False
check_penultL=lambda cmue: (bool(re.match(light,cmue[4][-2])) or bool(re.match(lightspecial,cmue[3][-2]))) if len(cmue[4])>1 else False
check_penultTSingleton=lambda cmue: bool(re.match(Tsingleton,cmue[4][-2])) if len(cmue[4])>1 else False
check_penultLSingleton=lambda cmue: (bool(re.match(Lsingleton,cmue[4][-2]))) if len(cmue[4])>1 else False
check_penultTCluster=lambda cmue: bool(re.match(finalTcluster,cmue[4][-2])) if len(cmue[4])>1 else False
check_penultLCluster=lambda cmue: bool(re.match(finalLcluster,cmue[4][-2])) if len(cmue[4])>1 else False
check_penultShortv = lambda cmue: bool(re.match(finalshortV,cmue[3][-2])) if len(cmue[4])>1 else False
check_penultLongv = lambda cmue: bool(re.match(finallongV,cmue[3][-2])) if len(cmue[4])>1 else False


check_apH=lambda cmue: (bool(re.match(heavy,cmue[4][-3])) and not(bool(re.match(lightspecial, cmue[3][-2])))) if len(cmue[4])>2 else False
check_apL=lambda cmue: (bool(re.match(light,cmue[4][-3])) or bool(re.match(lightspecial,cmue[3][-2]))) if len(cmue[4])>2 else False
check_apTSingleton=lambda cmue: bool(re.match(Tsingleton,cmue[4][-3])) if len(cmue[4])>2 else False
check_apLSingleton=lambda cmue: (bool(re.match(Lsingleton,cmue[4][-3]))) if len(cmue[4])>2 else False
check_apTCluster=lambda cmue: bool(re.match(finalTcluster,cmue[4][-3])) if len(cmue[4])>2 else False
check_apLCluster=lambda cmue: bool(re.match(finalLcluster,cmue[4][-3])) if len(cmue[4])>2 else False
check_apShortv = lambda cmue: bool(re.match(finalshortV,cmue[3][-3])) if len(cmue[4])>2 else False
check_apLongv = lambda cmue: bool(re.match(finallongV,cmue[3][-3])) if len(cmue[4])>2 else False

check_papH=lambda cmue: (bool(re.match(heavy,cmue[4][-4])) and not(bool(re.match(lightspecial, cmue[3][-2])))) if len(cmue[4])>3 else False
check_papL=lambda cmue: (bool(re.match(light,cmue[4][-4])) or bool(re.match(lightspecial,cmue[3][-2]))) if len(cmue[4])>3 else False
check_papTSingleton=lambda cmue: bool(re.match(Tsingleton,cmue[4][-4])) if len(cmue[4])>3 else False
check_papLSingleton=lambda cmue: (bool(re.match(Lsingleton,cmue[4][-4]))) if len(cmue[4])>3 else False
check_papTCluster=lambda cmue: bool(re.match(finalTcluster,cmue[4][-4])) if len(cmue[4])>3 else False
check_papLCluster=lambda cmue: bool(re.match(finalLcluster,cmue[4][-4])) if len(cmue[4])>3 else False
check_papShortv = lambda cmue: bool(re.match(finalshortV,cmue[3][-4])) if len(cmue[4])>3 else False
check_papLongv = lambda cmue: bool(re.match(finallongV,cmue[3][-4])) if len(cmue[4])>3 else False


check_finalCluster=lambda cmue: (check_finalLCluster(cmue) or check_finalTCluster(cmue))
check_finalSingleton=lambda cmue: (check_finalLSingleton(cmue) or check_finalTSingleton(cmue))
check_finalOpen=lambda cmue: bool(re.match(opensyll,cmue[4][-1]))

check_nonSsing=lambda cmue: (check_finalSingleton(cmue) and not(check_finalS(cmue)))
check_nonScluster=lambda cmue: (check_finalCluster(cmue) and not(check_finalS(cmue)))

check_Ssing=lambda cmue: (check_finalSingleton(cmue) and check_finalS(cmue))

check_Scluster=lambda cmue: (check_finalCluster(cmue) and check_finalS(cmue))



# final vowel
check_endsi = lambda cmue: bool(re.match(finali,cmue[3][-1]))
check_endsah= lambda cmue: bool(re.match(finalschwa,cmue[3][-1]))
check_endsliq=lambda cmue: bool(re.match(finalr,cmue[3][-1])) or bool(re.match(finall,cmue[3][-1]))
check_endsnas=lambda cmue: bool(re.match(finalnas,cmue[3][-1]))

check_endsshortv = lambda cmue: bool(re.match(finalshortV,cmue[3][-1]))
check_endslongv = lambda cmue: bool(re.match(finallongV,cmue[3][-1]))

check_L=lambda cmue: (check_endsshortv(cmue) or check_finalLSingleton(cmue) or check_finalLCluster(cmue))
check_H=lambda cmue: (check_endslongv(cmue) or check_finalTSingleton(cmue) or check_finalTCluster(cmue))


# stress pattern
check_Istress= lambda cmue: cmue[2]==['1','0','0']
check_Pstress= lambda cmue: cmue[2]==['0','1','0']
check_secondaryClash= lambda cmue: bool(re.match('22',''.join(cmue[2])))
check_primaryClash= lambda cmue: bool(re.match('12|21',''.join(cmue[2])))

check_antePenultStress= lambda cmue: cmue[2][-3:]==['1','0','0']
check_penultStress= lambda cmue: cmue[2][-3:]==['0','1','0']

check_mainStressFinal= lambda cmue: cmue[2][-1]=='1' and cmue[2].count('1')==1
check_mainStressPenult= lambda cmue: cmue[2][-2]=='1' and cmue[2].count('1')==1
check_mainStressAntepenult = lambda cmue: (cmue[2][-3]=='1' and cmue[2].count('1')==1) if len(cmue[2])>2 else False
check_mainStressPreantepenult = lambda cmue: (cmue[2][-4]=='1' and cmue[2].count('1')==1) if len(cmue[2])>3 else False

check_final0= lambda cmue: cmue[2][-1]=='0'
check_final1= lambda cmue: cmue[2][-1]=='1'
check_final2= lambda cmue: cmue[2][-1]=='2'

check_penult0= lambda cmue: cmue[2][-2]=='0' if len(cmue[2])>1 else False
check_penult1= lambda cmue: cmue[2][-2]=='1' if len(cmue[2])>1 else False
check_penult2= lambda cmue: cmue[2][-2]=='2' if len(cmue[2])>1 else False

check_ap0= lambda cmue: cmue[2][-3]=='0' if len(cmue[2])>2 else False
check_ap1= lambda cmue: cmue[2][-3]=='1' if len(cmue[2])>2 else False
check_ap2= lambda cmue: cmue[2][-3]=='2' if len(cmue[2])>2 else False

check_pap0= lambda cmue: cmue[2][-4]=='0' if len(cmue[2])>3 else False
check_pap1= lambda cmue: cmue[2][-4]=='1' if len(cmue[2])>3 else False
check_pap2= lambda cmue: cmue[2][-4]=='2' if len(cmue[2])>3 else False







# Function to check the scope
# 3 syllables, all light:
check_inScope = lambda cmue: len(cmue[2]) > 1
#cmue: len(cmue[2])==2  
# and check_lightInclusive(cmue) and check_monomorphemic(cmue)

# List of levels to record for each factor
#vowel={
#	'IY':check_endsi,
#	'AH':check_endsah,
#	'liq':check_endsliq,
#	'nas':check_endsnas
#	}

mainStress={
	'final':check_mainStressFinal,
	'penult':check_mainStressPenult,
	'antepenult':check_mainStressAntepenult,
	'preante':check_mainStressPreantepenult
	}

finalStress={
	'0':check_final0,
	'1':check_final1,
	'2':check_final2
	}
	
penultStress={
	'0':check_penult0,
	'1':check_penult1,
	'2':check_penult2
	}
	
apStress={
	'0':check_ap0,
	'1':check_ap1,
	'2':check_ap2
	}
	
papStress={
	'0':check_pap0,
	'1':check_pap1,
	'2':check_pap2
	}
	
finalHLweight={
	'H':check_finalH,
	'L':check_finalL
	}

penultHLweight={
	'H':check_penultH,
	'L':check_penultL
	}
	
antepenultHLweight={
	'H':check_apH,
	'L':check_apL
	}
	
preantepenultHLweight={
	'H':check_papH,
	'L':check_papL
	}
	
finalWeight={
	'-V':check_endsshortv,
	'-VV':check_endslongv,
	'-TC':check_finalTSingleton,
	'-LC':check_finalLSingleton,
	'-LCC': check_finalLCluster,
	'-TCC': check_finalTCluster
	}

penultWeight={
	'-V':check_penultShortv,
	'-VV':check_penultLongv,
	'-TC':check_penultTSingleton,
	'-LC':check_penultLSingleton,
	'-LCC': check_penultLCluster,
	'-TCC': check_penultTCluster
	}
	
antepenultWeight={
	'-V':check_apShortv,
	'-VV':check_apLongv,
	'-TC':check_apTSingleton,
	'-LC':check_apLSingleton,
	'-LCC': check_apLCluster,
	'-TCC': check_apTCluster
	}

preantepenultWeight={
	'-V':check_papShortv,
	'-VV':check_papLongv,
	'-TC':check_papTSingleton,
	'-LC':check_papLSingleton,
	'-LCC': check_papLCluster,
	'-TCC': check_papTCluster
	}

finalOns={
	'0':finalNoOnset,
	'C':finalOnsetC,
	'CC':finalOnsetCC,
	'CCC':finalOnsetCCC
}

penultOns={
	'0':penultNoOnset,
	'C':penultOnsetC,
	'CC':penultOnsetCC,
	'CCC':penultOnsetCCC
}

antepenultOns={
	'0':antepenultNoOnset,
	'C':antepenultOnsetC,
	'CC':antepenultOnsetCC,
	'CCC':antepenultOnsetCCC
}
	
vowelLength={
	'longV':check_H,
	'shortV':check_L
	}
	
finalC={
	'open':check_finalOpen,
	'Singleton': check_finalSingleton,
	'Cluster': check_finalCluster
	}

endsS={
	'S':check_Ssing,
	'SCluster':check_Scluster,
	'otherSingleton':check_nonSsing,
	'otherCluster': check_nonScluster
	}


# List of factors to record
factors={
	'mainStress':mainStress,
	'finalStress':finalStress,
	'penultStress':penultStress,
	'apStress':apStress,
	'papStress':papStress,
	'finalWeight':finalWeight,
	'finalHLweight':finalHLweight,
	'penultWeight':penultWeight,
	'penultHLweight':penultHLweight,
	'antepenultWeight':antepenultWeight,
	'antepenultHLweight':antepenultHLweight,
	'preantepenultWeight':preantepenultWeight,
	'preantepenultHLweight':preantepenultHLweight,
	'vowelLength':vowelLength,
	'finalOnset':finalOns,
	'penultOnset':penultOns,
	'antepenultOnset':antepenultOns,
	'finalV':finalV,
	'finalC': finalC,
	'S': endsS,
	'morphology':morphology.morphology,
	'suffixType':morphology.suffixType,
	'prefixType':morphology.prefixType,
	'Prefix':morphology.Prefix,
	'Suffix':morphology.Suffix
	#'affix':morphology.affixes
	}
	
specifiers={
	'coda':finalCoda,
	'codaLength':codaLength
	}
			
res=searchCMU(factors,specifiers,check_inScope,output='newCMU.txt')
