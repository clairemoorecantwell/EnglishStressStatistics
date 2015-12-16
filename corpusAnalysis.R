
#inside the quotes enter the path to the file on your machine
data=read.table("/Users/clairemoore-cantwell/Dropbox/CanadaBanana/CorpusSearch/newCMU.txt",header=TRUE,colClasses=c('factor'),sep='\t')

#################################################
########### Adding useful columns ###############
#################################################

data$freq=as.numeric(levels(data$freq))[data$freq]
data$nsylls=sapply(as.character(data$stressTrans),nchar)
data$weightPattern=paste(data$penultWeight,data$finalWeight)
data$weightPattern=as.factor(data$weightPattern)

data$mainStress=factor(data$mainStress,levels=c("other","preante","antepenult","penult","final"),ordered=TRUE)

data$leftEdgeStress=sapply(data$stressTrans,function(v){
	regexpr("1",as.character(v))[1]
	})
data$initStress=substring(data$stressTrans,1,1)

data$singleStress=ifelse(grepl("2",data$stressTrans),0,1)
data$penultVowel[data$penultWeight!='other']=ifelse((data$penultWeight[data$penultWeight!='other'] %in% c("-LC","-LCC","-V")),"M","D")
data$penultCoda[data$penultWeight!='other']=ifelse((data$penultWeight[data$penultWeight!='other'] %in% c("-V","-VV")),"open",ifelse((data$penultWeight[data$penultWeight!='other'] %in% c("-LC","-TC")),"closed","cluster"))
data$penultCoda=as.factor(data$penultCoda)
data$penultVowel=as.factor(data$penultVowel)
data$penultPossibleCoda[data$penultWeight!='other']=ifelse((data$penultWeight[data$penultWeight!='other'] %in% c("-LC","-LCC","-TC","-TCC"))|(data$finalOnset[data$penultWeight!='other'] %in% c("CC","CCC")),"mayHaveCoda","noCoda")
data$penultPossibleCoda=as.factor(data$penultPossibleCoda)
data$finalComplexOnset=ifelse((data$finalOnset %in% c("CC","CCC")),"complex","simple")
data$finalComplexOnset=as.factor(data$finalComplexOnset)

#including tapestry words
#data$penultHeaviness=ifelse(data$penultPossibleCoda=='mayHaveCoda'|data$penultVowel=="D","H","L")
#data$penultHeaviness=as.factor(data$penultHeaviness)

#excluding tapestry words, including digestive words
#data$penultHeaviness=ifelse((data$penultPossibleCoda=='mayHaveCoda'&data$mainStress=='penult')|data$penultVowel=="D"|data$penultCoda=='closed'|data$penultCoda=='cluster',"H","L")
#data$penultHeaviness=as.factor(data$penultHeaviness)

#excluding tapestry words and digestive words
data$penultHeaviness=ifelse(data$penultVowel=="D"|data$penultCoda=='closed'|data$penultCoda=='cluster',"H","L")
data$penultHeaviness=as.factor(data$penultHeaviness)

data$finalTwoV=ifelse(data$finalV=='iy','iy',ifelse(data$finalV=='ah'|data$finalV=='ih','ah','other'))



data$finalVowel[data$finalWeight!='other']=ifelse((data$finalWeight[data$finalWeight!='other'] %in% c("-LC","-LCC","-V")),"M","D")
data$finalCoda[data$finalWeight!='other']=ifelse((data$finalWeight[data$finalWeight!='other'] %in% c("-V","-VV")),"open",ifelse((data$finalWeight[data$finalWeight!='other'] %in% c("-LC","-TC")),"closed","cluster"))
data$penultCoda=as.factor(data$penultCoda)
data$penultVowel=as.factor(data$penultVowel)

data$finalHeaviness=ifelse(data$finalVowel=="D"|data$finalCoda=='cluster',"H","L")
data$finalHeaviness=as.factor(data$finalHeaviness)



data$antepenultVowel[data$antepenultWeight!='other']=ifelse((data$antepenultWeight[data$antepenultWeight!='other'] %in% c("-LC","-LCC","-V")),"M","D")
data$antepenultCoda[data$antepenultWeight!='other']=ifelse((data$antepenultWeight[data$antepenultWeight!='other'] %in% c("-V","-VV")),"open",ifelse((data$antepenultWeight[data$antepenultWeight!='other'] %in% c("-LC","-TC")),"closed","cluster"))
data$penultCoda=as.factor(data$penultCoda)
data$penultVowel=as.factor(data$penultVowel)

data$antepenultHeaviness=ifelse(data$antepenultVowel=="D"|data$antepenultCoda=='closed'|data$antepenultCoda=='cluster',"H","L")
data$antepenultHeaviness=as.factor(data$antepenultHeaviness)



data$weightPattern=paste(data$antepenultHeaviness,data$penultHeaviness,data$finalHeaviness)

sapply(as.character(data$stressTrans),nchar)

final3<- function(string){
	last3=substr(string,nchar(string)-2,nchar(string))
	last3
}

data$final3stressTrans=as.factor(sapply(as.character(data$stressTrans),final3))

######################################################
########## Finished making new columns ###############
######################################################

summary(data)

# spelling
# transcription: CMU transcription
# stressTrans: CMU stress transcription
#				Here and elsewhere: 1=primary, 2=secondary, 0=no stress
# syllStruct: CV transcription of each syllable, separated by .'s.  L means lax vowel, T means tense
# syllabification: syllabification according to Maximal Onset.  Capitals are nucleii
# antepenultOnset: CV transcription of the onset of the antepenult syllable
# apStress: stress of the antepenult syllable
# penultHLweight: obsolete
# preantepenultHLweight: weight of the preantepenult
# finalHLweight: obsolete
# morphology: simple=morphologically simple; complex=morphologically complex
# vowelLength: mystery
# preantepenultWeight: weight of preantepenult broken down by rhyme type L is the same as V, and T is the same as V
# antepenultWeight: weight of antepenult broken down by rhyme type L is the same as V, and T is the same as V
# mainStress: location of the main stress of the word
# finalStress: stress of final syllable
# papStress: stress of preantepenult
# penultOnset: CV transcription of the penult onset
# suffixType: stress-shift type of the suffix
# penultWeight: weight of penult broken down by rhyme type L is the same as V, and T is the same as V
# antepenultHLweight: obsolete
# S: does the word's final cluster have an s in it?
# finalWeight: weight of final syllable broken down by rhyme type L is the same as V, and T is the same as V
# Suffix: is there a suffix?
# finalC: what's the final coda like?
# Prefix: prefix or not?
# prefixType: prefix stressed or not?
# finalOnset: CV transcription of the onset of the final syllable
# finalV: final vowel of the word
# penultStress: stress of the penult
# codaLength: how many phonemes in the final syllable's coda?
# coda: coda of the final syllable
# freq: log frequency from SubtLex
# POS: part of speech from CELEX
# nsylls: number of syllables
# weightPattern: Weight pattern of the last three syllables (NA in first position indicates a two syllable word)
# leftEdgeStress: 1 means initial stress, 2=peninitial, 3=postpeninitial, etc.
# initStress: stress of initial syllable
# singleStress: 1=word has only one stressed syllable, 0=word has at least two stressed syllables
# penultVowel: D=diphthong, M=monophthong
# penultCoda: closed, cluster, or open
# penultPossibleCoda: mayHaveCoda=penult ends in a singleton or cluster, or is followed by an onset cluster in the next syllable (which could be attracted to the penult as a coda should the penult be stressed)
# finalComplexOnset: is the onset of the final syllable complex?
# penultHeaviness: weight of penult syllable
# finalTwoV: final vowel divided into -i, -ah, and other
# finalVowel: D=diphthong, M=monophthong
# finalCoda: closed, cluster, or open
# finalHeaviness: weight of final syllable
# antepenultVowel: D=diphthong, M=monophthong
# antepenultCoda: closed, cluster, or open
# antepenultHeaviness: weight of antepenult
# final3stressTrans: stress of the final three syllables


######################################################
# Example of possible use:
#
# Question: how does syllable weight affect main stress placement?

table(data$weightPattern,data$mainStress)

table(data$weightPattern,data$final3stressTrans)

# In words at least three syllables long?

x=table(data$weightPattern[data$nsylls>2&grepl("NA",data$weightPattern)==FALSE],data$mainStress[data$nsylls>2&grepl("NA",data$weightPattern)==FALSE],exclude="other")

# List all HHL words with antepenult stress

data$spelling[data$weightPattern=="H H L"&data$mainStress=="antepenult"]



