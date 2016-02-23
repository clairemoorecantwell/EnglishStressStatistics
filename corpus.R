setwd("/Users/clairemoore-cantwell/Dropbox/Dissertation/")
source("styles.R")
source("functions.R")

data=read.table("/Users/clairemoore-cantwell/Dropbox/CanadaBanana/CorpusSearch/newCMU.txt",header=TRUE,colClasses=c('factor'),sep='\t')
data$freq=as.numeric(levels(data$freq))[data$freq]
data$nsylls=sapply(as.character(data$stressTrans),nchar)
data$weightPattern=paste(data$penultWeight,data$finalWeight)
data$weightPattern=as.factor(data$weightPattern)

data$mainStress=factor(data$mainStress,levels=c("other","preante","antepenult","penult","final"),ordered=TRUE)

data$leftEdgeStress=sapply(data$stressTrans,function(v){
	regexpr("1",as.character(v))[1]
	})
data$initStress=substring(data$stressTrans,1,1)


#########
# Distribution of different stress patterns: from right edge
# Message: penult stress is really common
#########

#View the percentages:
library(gmodels)
CrossTable(data$nsylls)

#Incorporated by hand into the barplot
plot='barplot(table(data$mainStress),names.arg=c("Other","Pre-antepenult","Antepenult","Penult","Final"),ylab="No. words",col=col[1],main="Main stress counts (all words)")
text(0.8,5000,"2 syllables: 45%")
text(0.8,4500,"3 syllables: 31%")
text(0.8,4000,"4 syllables: 18%")
text(0.8,3500,">4 syllables: 7%")
'
saveIt(plot,"mainStressHist",path="Pictures/",ps=FALSE,height=5,width=7)


#########
# Distribution of different stress patterns: from left edge
# Message: Initial stress is common
#########

#Incorporated by hand into the barplot
plot='barplot(table(data$leftEdgeStress),names.arg=c("Initial","Peninitial","Post-peninitial","4th syllable","5th syllable","6th syllable"),main="Main stress from left edge (all words)",ylab="No. words",col=col[1])
text(6,5000,"2 syllables: 45%")
text(6,4500,"3 syllables: 31%")
text(6,4000,"4 syllables: 18%")
text(6,3500,">4 syllables: 7%")
'

saveIt(plot,"leftEdgeStressHist",path="Pictures/",ps=FALSE,height=5,width=8)


##################################
######## Nouns vs. verbs in long words ###########
###########################################

plotMosaic(data$POS[data$nsylls>2],data$mainStress[data$nsylls>2],exclude=c("undefined","A","ADV","C","I","NUM","PREP","PRON","preante","other"),main="Part of Speech",savefile=TRUE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="NVlongWords",ps=FALSE,dimnames=list(c("N","V"),c("Antepenult","Penult","Final")),top=TRUE,textcol="white")


#####################################
#########  Latin stress plots #######
#####################################

#### make all the relevant factors into columns
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
data$penultHeaviness=ifelse(data$penultPossibleCoda=='mayHaveCoda'|data$penultVowel=="D","H","L")
data$penultHeaviness=as.factor(data$penultHeaviness)

#excluding tapestry words, including digestive words
data$penultHeaviness=ifelse((data$penultPossibleCoda=='mayHaveCoda'&data$mainStress=='penult')|data$penultVowel=="D"|data$penultCoda=='closed'|data$penultCoda=='cluster',"H","L")
data$penultHeaviness=as.factor(data$penultHeaviness)

#excluding tapestry words and digestive words
data$penultHeaviness=ifelse(data$penultVowel=="D"|data$penultCoda=='closed'|data$penultCoda=='cluster',"H","L")
data$penultHeaviness=as.factor(data$penultHeaviness)



table(data$penultWeight[data$nsylls>2&data$singleStress],data$stressTrans[data$nsylls>2&data$singleStress])

# singleton vs. diphthong
plotMosaic(data$penultVowel[data$nsylls>2],data$mainStress[data$nsylls>2],exclude=c("other","NA","final","preante"),main="", savefile=TRUE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="LSvowelLength",ps=FALSE,dimnames=list(c("VV","V"),c("Antepenult","Penult")))

# must have coda vs. may not have coda
plotMosaic(data$penultCoda[data$nsylls>2],data$mainStress[data$nsylls>2],exclude=c("other","cluster","final","preante","NA"),main="",savefile=TRUE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="LScoda",ps=FALSE,dimnames=list(c("Closed","Open"),c("Antepenult","Penult")))

# Heavy vs. Light
data$penultflippedH=as.character(data$penultHeaviness)
data$penultflippedH[data$penultHeaviness=="L"]="aL"
data$penultflippedH=as.factor(data$penultflippedH)
plotMosaic(data$penultflippedH[data$nsylls>2],data$mainStress[data$nsylls>2],exclude=c("other","cluster","final","preante","NA"),main="",savefile=TRUE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Defense/",filename="latinStress",ps=FALSE,dimnames=list(c("L","H"),c("Antepenult","Penult")),col=terrain.colors(4)[2:4])



# must have coda vs. may not have coda: ch5 reference
data$penultLH=ifelse(data$penultHeaviness=='H',"b","a")
data$penultLH=as.factor(data$penultLH)
plotMosaic(data$penultLH[data$nsylls>2],data$mainStress[data$nsylls>2],exclude=c("other","cluster","final","preante","NA"),main="Corpus counts",savefile=TRUE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="LScoda2",ps=FALSE,dimnames=list(c("L","H"),c("Antepenult","Penult")))

# may have coda vs. no possible coda (including 'travesty' words in the count)
# not using this one in the chapter
#quartz()
#plotMosaic(data$penultPossibleCoda[data$nsylls>2],data$mainStress[data$nsylls>2],exclude=c("other","final","preante"),main="Coda: Light penultimate vowels",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="LScoda",ps=FALSE,dimnames=list(c("CVC","CV"),c("Antepenult","Penult")))

# 'travesty' words alone: just open penults followed by complex vs. simple onset
quartz()
plotMosaic(data$finalComplexOnset[data$penultVowel=='M'&data$penultCoda=='open'&data$nsylls>2],data$mainStress[data$penultVowel=='M'&data$penultCoda=='open'&data$nsylls>2],exclude=c('NA','final','preante','other'), main="" ,savefile=TRUE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="LSonsets",ps=FALSE,dimnames=list(c("CV.CCV","CV.(C)V"),c("Antepenult","Penult")))
#### Note: this plot obscures the effect of complex onsets in the final syllable on the probability of final stress.  Remove 'final' from the exclude list to see it

# Including 'travesty' words in the count
plotMosaic(data$penultHeaviness[data$nsylls>2],data$mainStress[data$nsylls>2],exclude=c("NA","other","final","preante"),main="Penult Weight" ,savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="LSonsets",ps=FALSE,dimnames=list(c("H","L"),c("Antepenult","Penult")))


# The effects of final vowel, broken down by weight
data$finalSchwaCollapsedV=data$finalV
data$finalSchwaCollapsedV[data$finalV=='ih']='ah'
plotMosaic(data$finalSchwaCollapsedV[data$nsylls>2&data$penultHeaviness=="L"],data$mainStress[data$nsylls>2&data$penultHeaviness=="L"],exclude=c("final","preante","other","undefined","NA","","ae","aa","ao","aw","eh","ay","oy","uh","uw","ow","ih","ey","er"),main="L",savefile=FALSE,ps=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Analogy/Pictures",filename="finalVs",dimnames=list(c("-\u0259","-l","-N","-i"),c("Antepenult","Penult")),nums=FALSE)

tapply(data$freq[data$nsylls>2&data$penultHeaviness=="L"],list(data$finalSchwaCollapsedV[data$nsylls>2&data$penultHeaviness=="L"],data$mainStress[data$nsylls>2&data$penultHeaviness=="L"]),FUN=mean)

tapply(data$freq[data$nsylls>2&data$penultHeaviness=="L"],list(data$mainStress[data$nsylls>2&data$penultHeaviness=="L"]),FUN=mean)



# First, we recode final 'ih' as 'ah'
data$finalTwoV=ifelse(data$finalV=='iy','iy',ifelse(data$finalV=='ah'|data$finalV=='ih','ah','other'))
data$finalTwoV=as.factor(data$finalTwoV)
plot='
par(mfrow=c(1,2),mar=c(5,3,4,0))
plotMosaic(data$finalTwoV[data$nsylls>2&data$penultHeaviness=="H"],data$mainStress[data$nsylls>2&data$penultHeaviness=="H"],exclude=c("final","preante","other","undefined","NA",""),main="H",savefile=FALSE,ps=FALSE,dimnames=list(c("-\u0259","-i"),c("Antepenult","Penult")))

plotMosaic(data$finalTwoV[data$nsylls>2&data$penultHeaviness=="L"],data$mainStress[data$nsylls>2&data$penultHeaviness=="L"], exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,ps=FALSE,dimnames=list(c("-\u0259","-i"),c("Antepenult","Penult")),textcol="white")
'

saveIt(plot,"LScorpus_finalV",path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",ps=FALSE,height=5,width=9.5)


#########################################################
######### Defense picture: vowels, just light penults ###
#########################################################
plotMosaic(data$finalTwoV[data$nsylls>2&data$penultHeaviness=="L"],data$mainStress[data$nsylls>2&data$penultHeaviness=="L"], exclude=c("final","preante","other","undefined","NA",""),main="Lexicon: light penults",savefile=FALSE,ps=FALSE,dimnames=list(c("-\u0259","-i"),c("Antepenult","Penult")),textcol="black",col=terrain.colors(5)[2:3],path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Defense/",filename="finalVLightCorpus")


#######################################################
###### Phonology submission i/ah broken down by morphology #######################
#######################################################
plot='
par(mfrow=c(1,2),mar=c(5,3,4,0))
plotMosaic(data$finalTwoV[data$nsylls>2&data$penultHeaviness=="L"&data$morphology=="simple"],data$mainStress[data$nsylls>2&data$penultHeaviness=="L"&data$morphology=="simple"], exclude=c("final","preante","other","undefined","NA",""),main="Morphologically simple",savefile=FALSE,ps=FALSE,dimnames=list(c("-\u0259","-i"), c("Antepenult","Penult")),textcol="white",path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Defense/",filename="finalVLightCorpus")

plotMosaic(data$finalTwoV[data$nsylls>2&data$penultHeaviness=="L"&data$morphology=="complex"],data$mainStress[data$nsylls>2&data$penultHeaviness=="L"&data$morphology=="complex"], exclude=c("final","preante","other","undefined","NA",""),main="Morphologically complex",savefile=FALSE,ps=FALSE,dimnames=list(c("-\u0259","-i"),c("Antepenult","Penult")),textcol="white",path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Defense/",filename="finalVLightCorpus")
'

saveIt(plot,"trend_by_morphology",path="/Users/clairemoore-cantwell/Dropbox/Analogy/Pictures/",ps=FALSE,height=5,width=9.5)

################################################


#Showing all the final vowels which aren't stressed

plot=
data$finalVschwaFixed=ifelse(data$finalV=='ih','ah',as.character(data$finalV))
data$finalVschwaFixed=as.factor(data$finalVschwaFixed)
quartz()
par(mfrow=c(1,2),mar=c(5,3,4,0))
plotMosaic(data$finalVschwaFixed[data$nsylls>2&data$penultHeaviness=='H'],data$mainStress[data$nsylls>2&data$penultHeaviness=='H'],exclude=c("aa","ae","ao","ey","eh","oy","ow","uh","aw","ay","final","preante","other","undefined","NA",""),main="H",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE,dimnames=list(c("-\u0259","-l","-n","-r","-i","-u"),c("Antepenult","Penult")),text=FALSE)

plotMosaic(data$finalVschwaFixed[data$nsylls>2&data$penultHeaviness=='L'],data$mainStress[data$nsylls>2&data$penultHeaviness=='L'],exclude=c("aa","ae","ao","ey","eh","oy","ow","uh","aw","ay","uw","final","preante","other","undefined","NA",""),main="",savefile=TRUE,path="/Users/clairemoore-cantwell/Dropbox/Analogy/Pictures/",filename="finalVs",ps=FALSE,dimnames=list(c("-\u0259","-n","-i","-l","-r"), c("Antepenultimate","Penultimate")), order=list(c("ah","an","iy","al","er"),NULL),noNums=c(5),textcol="white",height=6,width=6)


saveIt(plot,"LatinStressMosaic_finalV",path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",ps=FALSE,height=5,width=9)



##############################################################################
########### Breaking probabilities down by frequency bracket #################
##############################################################################

hist(data$freq)

# Break frequency into quantiles
quants=quantile(data$freq)

# Make a four-part picture
par(mfrow=c(2,2),mar=c(5,3,4,0))
plotMosaic(data$penultHeaviness[data$nsylls>2&data$freq>quants[4]],data$mainStress[data$nsylls>2&data$freq>quants[4]],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)

plotMosaic(data$penultHeaviness[data$nsylls>2&data$freq<quants[4]&data$freq>quants[3]],data$mainStress[data$nsylls>2&data$freq<quants[4]&data$freq>quants[3]],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)

plotMosaic(data$penultHeaviness[data$nsylls>2&data$freq<quants[3]&data$freq>quants[2]],data$mainStress[data$nsylls>2&data$freq<quants[3]&data$freq>quants[2]],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)

plotMosaic(data$penultHeaviness[data$nsylls>2&data$freq<quants[2]&data$freq>quants[1]],data$mainStress[data$nsylls>2&data$freq<quants[2]&data$freq>quants[1]],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)





par(mfrow=c(2,2),mar=c(5,3,4,0))
plotMosaic(data$finalTwoV[data$nsylls>2&data$freq>quants[4]],data$mainStress[data$nsylls>2&data$freq>quants[4]],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)


plotMosaic(data$finalTwoV[data$nsylls>2&data$freq<quants[4]&data$freq>quants[3]],data$mainStress[data$nsylls>2&data$freq<quants[4]&data$freq>quants[3]],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)

plotMosaic(data$finalTwoV[data$nsylls>2&data$freq<quants[3]&data$freq>quants[2]],data$mainStress[data$nsylls>2&data$freq<quants[3]&data$freq>quants[2]],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)

plotMosaic(data$finalTwoV[data$nsylls>2&data$freq<quants[2]&data$freq>quants[1]],data$mainStress[data$nsylls>2&data$freq<quants[2]&data$freq>quants[1]],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)





plotMosaic(data$penultHeaviness[data$nsylls>2&data$freq>3],data$mainStress[data$nsylls>2&data$freq>3],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)


plotMosaic(data$penultHeaviness[data$nsylls>2&data$morphology=='complex'],data$mainStress[data$nsylls>2&data$morphology=='complex'],exclude=c("final","preante","other","undefined","NA",""),main="L",savefile=FALSE,path="/Users/clairemoore-cantwell/Dropbox/Dissertation/Pictures/",filename="test",ps=FALSE)



,dimnames=list(c("-\u0259","-l","-n","-r","-i","-u"),c("Antepenult","Penult")),text=FALSE)



#####################################################################
########## Modeling stats ###########################################
#####################################################################

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


x=table(data$weightPattern[data$nsylls>2&grepl("NA",data$weightPattern)==FALSE&data$finalTwoV=='ah'],data$final3stressTrans[data$nsylls>2&grepl("NA",data$weightPattern)==FALSE&data$finalTwoV=='ah'],exclude="other")

for(i in 1:5){
	
	print(x[i,]/sum(x[i,]))
}


table(data$finalV[data$nsylls>2],data$final3stressTrans[data$nsylls>2])



