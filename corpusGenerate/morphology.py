import re
import numpy


#########################
# morphology: From Richard V. Tescner and M. Stanley Whitley
#########################

#########################
# The actual morphology functions do not assume a cmuprosody entry, just a string.  You can then run them on any string you come up with.
#########################

suffixes=[]
shiftSuff=[]
preantepenultSuff=[]
antepenultSuff=[]
penultSuff=[]
ultSuff=[]
noshiftSuff=[]
noshiftOneSyll=[]
noshiftTwoSyll=[]
stressedPre=[]
unstressedPre=[]
prefixes=[]



#stress-shifting suffixes
# to pre-ante-penult

preantepenultSuff.append( lambda cmue: bool(re.match('.*ary$',cmue[0])))

check_preantepenultSuff=lambda cmue: any( f(cmue) for f in preantepenultSuff)

# to antepenult
antepenultSuff.append( lambda cmue: bool(re.match('.*ity$',cmue[0])))			#capability
antepenultSuff.append( lambda cmue: bool(re.match('.*iety$',cmue[0])))			#anxiety
antepenultSuff.append( lambda cmue: (bool(re.match('.*al$',cmue[0])) and not(bool(re.match('.*tial$',cmue[0]))) and not(bool(re.match('.*cial$',cmue[0]))) ))				#technical
antepenultSuff.append( lambda cmue: bool(re.match('.*ology$',cmue[0])))		#methodology
antepenultSuff.append( lambda cmue: bool(re.match('.*bian$',cmue[0])))			#microbian, Arabian
antepenultSuff.append( lambda cmue: bool(re.match('.*dian$',cmue[0])))			#tragedian, canadian
antepenultSuff.append( lambda cmue: bool(re.match('.*lian$',cmue[0])))			#reptilian
antepenultSuff.append( lambda cmue: bool(re.match('.*nian$',cmue[0])))			#amazonian, darwinian
antepenultSuff.append( lambda cmue: bool(re.match('.*rian$',cmue[0])))			#grammarian, barbarian
antepenultSuff.append( lambda cmue: bool(re.match('.*ean$',cmue[0])))			#epicurean
antepenultSuff.append( lambda cmue: bool(re.match('.*itan$',cmue[0])))			#metropolitan, cosmopolitan
antepenultSuff.append( lambda cmue: bool(re.match('.*icide$',cmue[0])))		#infanticide
antepenultSuff.append( lambda cmue: bool(re.match('.*ute$',cmue[0])))			#dissolute, resolute
antepenultSuff.append( lambda cmue: bool(re.match('.*neous$',cmue[0])))		#harmonious
antepenultSuff.append( lambda cmue: bool(re.match('.*nious$',cmue[0])))		#miscellanneous
antepenultSuff.append( lambda cmue: bool(re.match('.*dious$',cmue[0])))		#melodious
antepenultSuff.append( lambda cmue: bool(re.match('.*rious$',cmue[0])))		#laborious
antepenultSuff.append( lambda cmue: bool(re.match('.*lous$',cmue[0])))			#miraculous
antepenultSuff.append( lambda cmue: bool(re.match('.*mous$',cmue[0])))			#acronymous
antepenultSuff.append( lambda cmue: bool(re.match('.*nous$',cmue[0])))			#monotonous
antepenultSuff.append( lambda cmue: bool(re.match('.*rous$',cmue[0])))			#omnivorous
antepenultSuff.append( lambda cmue: bool(re.match('.*tous$',cmue[0])))			#gratuitous
antepenultSuff.append( lambda cmue: bool(re.match('.*uous$',cmue[0])))			#ambiguous
antepenultSuff.append( lambda cmue: bool(re.match('.*ius$',cmue[0])))			#aquarius
antepenultSuff.append( lambda cmue: bool(re.match('.*ograph$',cmue[0])))
#antepenultSuff.append( lambda cmue: bool(re.match('.*ographer$',cmue[0])))	#photographer
antepenultSuff.append( lambda cmue: bool(re.match('.*ography$',cmue[0])))	#photography
antepenultSuff.append( lambda cmue: bool(re.match('.*ient$',cmue[0])))			#nutrient
antepenultSuff.append( lambda cmue: bool(re.match('.*ify$',cmue[0])))			#solidify
antepenultSuff.append( lambda cmue: bool(re.match('.*ium$',cmue[0])))			#auditorium
antepenultSuff.append( lambda cmue: bool(re.match('.*cracy$',cmue[0])))		#democracy
antepenultSuff.append( lambda cmue: bool(re.match('.*crat$',cmue[0])))			#democrat
antepenultSuff.append( lambda cmue: (bool(re.match('.*ia$',cmue[0])) and not(bool(re.match('.*eria$',cmue[0]))) and not(bool(re.match('.*onia$',cmue[0]))) ))				#melancholia
antepenultSuff.append( lambda cmue: bool(re.match('.*omy$',cmue[0])))			#economy
antepenultSuff.append( lambda cmue: bool(re.match('.*pathy$',cmue[0])))		#homeopathy
antepenultSuff.append( lambda cmue: bool(re.match('.*eria$',cmue[0])))			#cafeteria
antepenultSuff.append( lambda cmue: bool(re.match('.*onia$',cmue[0])))			#catalonia
antepenultSuff.append( lambda cmue: bool(re.match('.*ica$',cmue[0])))			#harmonica
antepenultSuff.append( lambda cmue: bool(re.match('.*ometer$',cmue[0])))		#kilometer
antepenultSuff.append( lambda cmue: bool(re.match('.*ular$',cmue[0])))			#molecular

#def check_antepenultSuff(cmue[0]):
#	list=[]
#	for f in antepenultSuff:
#		list.append(f(cmue[0]))
#	return any(list)
		
check_antepenultSuff=lambda cmue: any( f(cmue) for f in antepenultSuff)

# to penult
penultSuff.append( lambda cmue: bool(re.match('.*tion$',cmue[0])))		#abbreviation
penultSuff.append( lambda cmue: bool(re.match('.*cion$',cmue[0])))		#
penultSuff.append( lambda cmue: bool(re.match('.*gion$',cmue[0])))		#
penultSuff.append( lambda cmue: bool(re.match('.*nion$',cmue[0])))		#
penultSuff.append( lambda cmue: bool(re.match('.*sion$',cmue[0])))		#
penultSuff.append( lambda cmue: bool(re.match('.*xion$',cmue[0])))		#
penultSuff.append( lambda cmue: bool(re.match('.*lion$',cmue[0])))		#medal medallion
penultSuff.append( lambda cmue: bool(re.match('.*ic$',cmue[0])))			#acidic
penultSuff.append( lambda cmue: bool(re.match('.*ics$',cmue[0])))		#acrobatics
penultSuff.append( lambda cmue: bool(re.match('.*cial$',cmue[0])))	#beneficial provincial
penultSuff.append( lambda cmue: bool(re.match('.*tial$',cmue[0])))		#
penultSuff.append( lambda cmue: bool(re.match('.*cian$',cmue[0])))		#magician
penultSuff.append( lambda cmue: bool(re.match('.*tian$',cmue[0])))		#dietitian
penultSuff.append( lambda cmue: bool(re.match('.*gian$',cmue[0])))		#norwegian
penultSuff.append( lambda cmue: bool(re.match('.*sian$',cmue[0])))		#caucasian, parisian
penultSuff.append( lambda cmue: bool(re.match('.*cious$',cmue[0])))	#judicious
penultSuff.append( lambda cmue: bool(re.match('.*tious$',cmue[0])))	#
penultSuff.append( lambda cmue: bool(re.match('.*aceous$',cmue[0])))	#curvaceous
penultSuff.append( lambda cmue: bool(re.match('.*geous$',cmue[0])))	#litigious, outrageous
penultSuff.append( lambda cmue: bool(re.match('.*gious$',cmue[0])))	#
penultSuff.append( lambda cmue: bool(re.match('.*sis$',cmue[0])))		#analysis
penultSuff.append( lambda cmue: bool(re.match('.*tis$',cmue[0])))		#appendicitis
penultSuff.append( lambda cmue: bool(re.match('.*nda$',cmue[0])))		#agenda propaganda
penultSuff.append( lambda cmue: bool(re.match('.*sive$',cmue[0])))		#impulsive progressive
penultSuff.append( lambda cmue: bool(re.match('.*ctive$',cmue[0])))	#instinctive
penultSuff.append( lambda cmue: bool(re.match('.*ata$',cmue[0])))		#errata
penultSuff.append( lambda cmue: bool(re.match('.*ella$',cmue[0])))		#cinderella
penultSuff.append( lambda cmue: bool(re.match('.*ina$',cmue[0])))		#ballerina
#penultSuff.append( lambda cmue: bool(re.match('.*o$',cmue[0])))			#concerto
penultSuff.append( lambda cmue: (bool(re.match('.*um$',cmue[0])) and not(bool(re.match('.*ium$',cmue[0]))) ))		#addendum
penultSuff.append( lambda cmue: bool(re.match('.*cent$',cmue[0])))		#phosphorescent

check_penultSuff=lambda cmue: any( f(cmue) for f in penultSuff)

#to ultimate
ultSuff.append( lambda cmue: bool(re.match('.*ade$',cmue[0])))		#lemonade arcade
ultSuff.append( lambda cmue: bool(re.match('.*ain$',cmue[0])))		#maintainance~maintain
ultSuff.append( lambda cmue: bool(re.match('.*aire$',cmue[0])))		#legionnaire
ultSuff.append( lambda cmue: bool(re.match('.*ane$',cmue[0])))		#human humane urban urbane
ultSuff.append( lambda cmue: bool(re.match('.*ee$',cmue[0])))			#examinee
#ultSuff.append( lambda cmue: bool(re.match('.*een$',cmue[0])))		#halloween
ultSuff.append( lambda cmue: bool(re.match('.*eer$',cmue[0])))		#engineer
ultSuff.append( lambda cmue: bool(re.match('.*ese$',cmue[0])))		#chinese, journalese
ultSuff.append( lambda cmue: bool(re.match('.*eze*$',cmue[0])))		#
ultSuff.append( lambda cmue: bool(re.match('.*esse$',cmue[0])))		#finesse
ultSuff.append( lambda cmue: bool(re.match('.*eur$',cmue[0])))		#restaurant~restauranteur
ultSuff.append( lambda cmue: bool(re.match('.*ique$',cmue[0])))		#technical~technique
#ultSuff.append( lambda cmue: bool(re.match('.*oon$',cmue[0])))		#spit~spitoon
ultSuff.append( lambda cmue: bool(re.match('.*sque$',cmue[0])))		#picturesque
ultSuff.append( lambda cmue: bool(re.match('.*ette$',cmue[0])))		#novelette

check_ultSuff=lambda cmue: any( f(cmue) for f in ultSuff)

shiftSuff=numpy.concatenate((preantepenultSuff,antepenultSuff,penultSuff,ultSuff),1)

check_shiftSuff=lambda cmue: any( f(cmue) for f in shiftSuff)

# Non stress-shifting
noshiftTwoSyll.append( lambda cmue: bool(re.match('.*able$',cmue[0])))		#agreeable
noshiftTwoSyll.append( lambda cmue: bool(re.match('.*ible$',cmue[0])))		#suggestible, ostensible  ######## NOTE not included in the pronouncing English book
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ant$',cmue[0])))		#assistant
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ate$',cmue[0])))		#rusticate
noshiftOneSyll.append( lambda cmue: (bool(re.match('.*cy$',cmue[0])) and not(bool(re.match('.*cracy$',cmue[0]))) ))			#literacy
noshiftOneSyll.append( lambda cmue: (bool(re.match('.*er$',cmue[0])) and not(bool(re.match('.*ometer$',cmue[0]))) and not(bool(re.match('.*eer$',cmue[0]))) ))			#officer
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ed$',cmue[0])))			#observed
noshiftOneSyll.append( lambda cmue: bool(re.match('.*es$',cmue[0])))			#wishes fishes slashes
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ess$',cmue[0])))		#stewardess
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ful$',cmue[0])))		#revengeful
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ing$',cmue[0])))		#singing
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ine$',cmue[0])))		#medicine porcine emeraldine
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ish$',cmue[0])))		#womanish
noshiftTwoSyll.append( lambda cmue: bool(re.match('.*ism$',cmue[0])))		#witticism tribalism
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ist$',cmue[0])))		#geologist pharmicist
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ite$',cmue[0])))		#metabolite tripartite
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ize$',cmue[0])))		#specialize
noshiftOneSyll.append( lambda cmue: bool(re.match('.*less$',cmue[0])))		#featureless
noshiftOneSyll.append( lambda cmue: bool(re.match('.*like$',cmue[0])))		#ladylike
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ly$',cmue[0])))			#assembly
noshiftOneSyll.append( lambda cmue: bool(re.match('.*man$',cmue[0])))		#policeman
noshiftTwoSyll.append( lambda cmue: bool(re.match('.*woman$',cmue[0])) and not(bool(re.match('.*man$',cmue[0]))))	#policewoman
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ment$',cmue[0])))		#amendment
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ness$',cmue[0])))		#charitableness
noshiftOneSyll.append( lambda cmue: bool(re.match('.*phile$',cmue[0])))	#anglophile
noshiftOneSyll.append( lambda cmue: bool(re.match('.*phobe$',cmue[0])))	#anglophobe
noshiftOneSyll.append( lambda cmue: bool(re.match('.*proof$',cmue[0])))	#fireproof
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ship$',cmue[0])))		#stewardship
noshiftOneSyll.append( lambda cmue: bool(re.match('.*some$',cmue[0])))		#frolicsome
noshiftOneSyll.append( lambda cmue: bool(re.match('.*sphere$',cmue[0])))	#biosphere
noshiftOneSyll.append( lambda cmue: bool(re.match('.*tor$',cmue[0])))		#indicator
noshiftTwoSyll.append( lambda cmue: bool(re.match('.*tory$',cmue[0])))		#investigatory predatory
noshiftOneSyll.append( lambda cmue: bool(re.match('.*ward$',cmue[0])))		#windward
noshiftOneSyll.append( lambda cmue: bool(re.match('.*wards$',cmue[0])))	#
noshiftOneSyll.append( lambda cmue: bool(re.match('.*wise$',cmue[0])))		#lengthwise
#noshiftOneSyll.append( lambda cmue: (bool(re.match('.*y$',cmue[0])) and not(bool(re.match('.*ography$',cmue[0]))) and not(bool(re.match('.*ity$',cmue[0]))) and not(bool(re.match('.*ary$',cmue[0]))) and not(bool(re.match('.*ify$',cmue[0]))) ))			#flabby

check_noshiftOneSyll=lambda cmue: any( f(cmue) for f in noshiftOneSyll)
check_noshiftTwoSyll=lambda cmue: any( f(cmue) for f in noshiftTwoSyll)

noshiftSuff=numpy.concatenate((noshiftOneSyll,noshiftTwoSyll),1)
check_noshiftSuff=lambda cmue: any( f(cmue) for f in noshiftSuff)

suffixes=numpy.concatenate((shiftSuff,noshiftSuff),1)

check_suffix=lambda cmue: any( f(cmue) for f in suffixes)

suffixType={
	'noshiftOneSyll':check_noshiftOneSyll,
	'noshiftTwoSyll':check_noshiftTwoSyll,
	'ultShift':check_ultSuff,
	'penultShift':check_penultSuff,
	'antepenultShift':check_antepenultSuff,
	'preantepenultShift':check_preantepenultSuff
	}


#prefixes (sometimes stressed)
#stressedPre.append( lambda cmue: bool(re.match('^ab',cmue[0])))		#abdicate
stressedPre.append( lambda cmue: bool(re.match('^anti',cmue[0])))		#antidote
stressedPre.append( lambda cmue: bool(re.match('^circum',cmue[0])))		#circumnavigate
stressedPre.append( lambda cmue: bool(re.match('^counter',cmue[0])))			#counterbalance
stressedPre.append( lambda cmue: bool(re.match('^down',cmue[0])))			#2/3 stressed (downfall)
stressedPre.append( lambda cmue: bool(re.match('^fore',cmue[0])))			#60% stressed: forecast
stressedPre.append( lambda cmue: bool(re.match('^grand',cmue[0])))			#grandparent wishes fishes slashes
stressedPre.append( lambda cmue: bool(re.match('^out',cmue[0])))		#2/3 stressed outback
stressedPre.append( lambda cmue: bool(re.match('^over',cmue[0])))		#1/3 stressed overboard
stressedPre.append( lambda cmue: bool(re.match('^tele',cmue[0])))		#telecast

check_stressedPre=lambda cmue: any( f(cmue) for f in stressedPre)

#prefixes ('not stressed')
unstressedPre.append( lambda cmue: bool(re.match('^ac',cmue[0])))
#unstressedPre.append( lambda cmue: bool(re.match('^ad',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^as',cmue[0])))
#unstressedPre.append( lambda cmue: bool(re.match('^be',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^bi',cmue[0])))
unstressedPre.append( lambda cmue: (bool(re.match('^co',cmue[0])) and not(bool(re.match('^counter',cmue[0]))) ))
unstressedPre.append( lambda cmue: bool(re.match('^com',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^con',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^de',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^des',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^dis',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^em',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^en',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^ex',cmue[0])))
unstressedPre.append( lambda cmue: (bool(re.match('^for',cmue[0])) and not(bool(re.match('^fore',cmue[0]))) ))
unstressedPre.append( lambda cmue: bool(re.match('^geo',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^homo',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^hyper',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^hypo',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^il',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^in',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^inter',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^intra',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^ir',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^macro',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^mal',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^meta',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^micro',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^mid',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^mis',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^mono',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^multi',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^non',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^ob',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^off',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^per',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^post',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^pre',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^pro',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^psycho',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^radio',cmue[0])))
#unstressedPre.append( lambda cmue: bool(re.match('^re',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^self',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^semi',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^sub',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^super',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^trans',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^ultra',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^under',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^up',cmue[0])))
unstressedPre.append( lambda cmue: bool(re.match('^vice',cmue[0])))

check_unstressedPre=lambda cmue: any( f(cmue) for f in unstressedPre)

prefixes=numpy.concatenate((unstressedPre,stressedPre),1)

prefixType={
	'unstressed':check_unstressedPre,
	'stressed':check_stressedPre
	}

check_prefix=lambda cmue: any( f(cmue) for f in prefixes)

Prefix={
	'prefix':check_prefix,
	'noPrefix':lambda cmue: not(check_prefix(cmue))
	}
	
Suffix={
	'suffix':check_suffix,
	'noSuffix':lambda cmue: not(check_suffix(cmue))
	}

Allaffixes=numpy.concatenate((prefixes,suffixes),1)

check_affix=lambda cmue: any( f(cmue) for f in Allaffixes)

morphology={
	'complex':check_affix,
	'simple':lambda cmue: not(check_affix(cmue))
	}

# to pre-ante-penult
check_ary = lambda cmue: bool(re.match('.*ary$',cmue[0]))

# to antepenult
check_ity= lambda cmue: bool(re.match('.*ity$',cmue[0]))			#capability
check_iety= lambda cmue: bool(re.match('.*iety$',cmue[0]))			#anxiety
check_al= lambda cmue: bool(re.match('.*al$',cmue[0]))				#technical
check_ology= lambda cmue: bool(re.match('.*ology$',cmue[0]))		#methodology
check_ian = lambda cmue: bool(re.match('.*[bdlnr]ian$',cmue[0]))	#microbian, Arabian
#check_dian = lambda cmue: bool(re.match('.*dian$',cmue[0]))			#tragedian, canadian
#check_lian = lambda cmue: bool(re.match('.*lian$',cmue[0]))			#reptilian
#check_nian = lambda cmue: bool(re.match('.*nian$',cmue[0]))			#amazonian, darwinian
#check_rian = lambda cmue: bool(re.match('.*rian$',cmue[0]))			#grammarian, barbarian
check_ean = lambda cmue: bool(re.match('.*ean$',cmue[0]))			#epicurean
check_itan = lambda cmue: bool(re.match('.*itan$',cmue[0]))			#metropolitan, cosmopolitan
check_icide = lambda cmue: bool(re.match('.*icide$',cmue[0]))		#infanticide
check_ute = lambda cmue: bool(re.match('.*ute$',cmue[0]))			#dissolute, resolute
check_neous= lambda cmue: bool(re.match('.*neous$',cmue[0]))		#harmonious
check_nious= lambda cmue: bool(re.match('.*nious$',cmue[0]))		#miscellanneous
check_dious= lambda cmue: bool(re.match('.*dious$',cmue[0]))		#melodious
check_rious= lambda cmue: bool(re.match('.*rious$',cmue[0]))		#laborious
check_lous = lambda cmue: bool(re.match('.*lous$',cmue[0]))			#miraculous
check_mous = lambda cmue: bool(re.match('.*mous$',cmue[0]))			#acronymous
check_nous = lambda cmue: bool(re.match('.*nous$',cmue[0]))			#monotonous
check_rous = lambda cmue: bool(re.match('.*rous$',cmue[0]))			#omnivorous
check_tous = lambda cmue: bool(re.match('.*tous$',cmue[0]))			#gratuitous
check_uous = lambda cmue: bool(re.match('.*uous$',cmue[0]))			#ambiguous
check_ius = lambda cmue: bool(re.match('.*ius$',cmue[0]))			#aquarius
check_ograph = lambda cmue: bool(re.match('.*ograph$',cmue[0]))		#photograph
check_ographer = lambda cmue: bool(re.match('.*ographer$',cmue[0]))	#photographer
check_ography= lambda cmue: bool(re.match('.*ography$',cmue[0]))	#photography
check_ient= lambda cmue: bool(re.match('.*ient$',cmue[0]))			#nutrient
check_ify= lambda cmue: bool(re.match('.*ify$',cmue[0]))			#solidify
check_ium= lambda cmue: bool(re.match('.*ium$',cmue[0]))			#auditorium
check_cracy = lambda cmue: bool(re.match('.*cracy$',cmue[0]))		#democracy
check_crat = lambda cmue: bool(re.match('.*crat$',cmue[0]))			#democrat
check_ia = lambda cmue: bool(re.match('.*ia$',cmue[0]))				#melancholia
check_omy = lambda cmue: bool(re.match('.*omy$',cmue[0]))			#economy
check_pathy = lambda cmue: bool(re.match('.*pathy$',cmue[0]))		#homeopathy
check_eria = lambda cmue: bool(re.match('.*eria$',cmue[0]))			#cafeteria
check_onia = lambda cmue: bool(re.match('.*onia$',cmue[0]))			#catalonia
check_ica = lambda cmue: bool(re.match('.*ica$',cmue[0]))			#harmonica
check_ometer = lambda cmue: bool(re.match('.*ometer$',cmue[0]))		#kilometer
check_ular= lambda cmue: bool(re.match('.*ular$',cmue[0]))			#molecular



# to penult
check_tion= lambda cmue: bool(re.match('.*tion$',cmue[0]))		#abbreviation
check_cion= lambda cmue: bool(re.match('.*cion$',cmue[0]))		#
check_gion= lambda cmue: bool(re.match('.*gion$',cmue[0]))		#
check_nion= lambda cmue: bool(re.match('.*nion$',cmue[0]))		#
check_sion = lambda cmue: bool(re.match('.*sion$',cmue[0]))		#
check_xion = lambda cmue: bool(re.match('.*xion$',cmue[0]))		#
check_lion = lambda cmue: bool(re.match('.*lion$',cmue[0]))		#medal medallion
check_ic = lambda cmue: bool(re.match('.*ic$',cmue[0]))			#acidic
check_ics = lambda cmue: bool(re.match('.*ics$',cmue[0]))		#acrobatics
check_cial = lambda cmue: bool(re.match('.*cial*$',cmue[0]))	#beneficial provincial
check_tial = lambda cmue: bool(re.match('.*tial$',cmue[0]))		#
check_cian = lambda cmue: bool(re.match('.*cian$',cmue[0]))		#magician
check_tian = lambda cmue: bool(re.match('.*tian$',cmue[0]))		#dietitian
check_gian= lambda cmue: bool(re.match('.*gian$',cmue[0]))		#norwegian
check_sian= lambda cmue: bool(re.match('.*sian$',cmue[0]))		#caucasian, parisian
check_cious= lambda cmue: bool(re.match('.*cious$',cmue[0]))	#judicious
check_tious= lambda cmue: bool(re.match('.*tious$',cmue[0]))	#
check_aceous= lambda cmue: bool(re.match('.*aceous$',cmue[0]))	#curvaceous
check_geous = lambda cmue: bool(re.match('.*geous$',cmue[0]))	#litigious, outrageous
check_gious = lambda cmue: bool(re.match('.*gious$',cmue[0]))	#
check_sis = lambda cmue: bool(re.match('.*sis$',cmue[0]))		#analysis
check_tis = lambda cmue: bool(re.match('.*tis$',cmue[0]))		#appendicitis
check_nda = lambda cmue: bool(re.match('.*nda$',cmue[0]))		#agenda propaganda
check_sive = lambda cmue: bool(re.match('.*sive$',cmue[0]))		#impulsive progressive
check_ctive = lambda cmue: bool(re.match('.*ctive$',cmue[0]))	#instinctive
check_ata= lambda cmue: bool(re.match('.*ata$',cmue[0]))		#errata
check_ella= lambda cmue: bool(re.match('.*ella$',cmue[0]))		#cinderella
check_ina= lambda cmue: bool(re.match('.*ina$',cmue[0]))		#ballerina
check_o= lambda cmue: bool(re.match('.*o$',cmue[0]))			#concerto
check_um = lambda cmue: bool(re.match('.*um$',cmue[0]))			#addendum
check_cent = lambda cmue: bool(re.match('.*cent$',cmue[0]))		#phosphorescent

#to ultimate
check_ade= lambda cmue: bool(re.match('.*ade$',cmue[0]))		#lemonade arcade
check_ain= lambda cmue: bool(re.match('.*ain$',cmue[0]))		#maintainance~maintain
check_aire= lambda cmue: bool(re.match('.*aire$',cmue[0]))		#legionnaire
check_ane = lambda cmue: bool(re.match('.*ane$',cmue[0]))		#human humane urban urbane
check_ee = lambda cmue: bool(re.match('.*ee$',cmue[0]))			#examinee
check_een = lambda cmue: bool(re.match('.*een$',cmue[0]))		#halloween
check_eer = lambda cmue: bool(re.match('.*eer$',cmue[0]))		#engineer
check_ese = lambda cmue: bool(re.match('.*ese$',cmue[0]))		#chinese, journalese
check_eze = lambda cmue: bool(re.match('.*eze*$',cmue[0]))		#
check_esse = lambda cmue: bool(re.match('.*esse$',cmue[0]))		#finesse
check_eur = lambda cmue: bool(re.match('.*eur$',cmue[0]))		#restaurant~restauranteur
check_ique= lambda cmue: bool(re.match('.*ique$',cmue[0]))		#technical~technique
check_oon= lambda cmue: bool(re.match('.*oon$',cmue[0]))		#spit~spitoon
check_sque= lambda cmue: bool(re.match('.*sque$',cmue[0]))		#picturesque
check_ette = lambda cmue: bool(re.match('.*ette$',cmue[0]))		#novelette

# Non stress-shifting
check_able= lambda cmue: bool(re.match('.*able$',cmue[0]))		#agreeable
check_ant= lambda cmue: bool(re.match('.*ant$',cmue[0]))		#assistant
check_ate= lambda cmue: bool(re.match('.*ate$',cmue[0]))		#rusticate
check_cy = lambda cmue: bool(re.match('.*cy$',cmue[0]))			#literacy
check_er = lambda cmue: bool(re.match('.*er$',cmue[0]))			#officer
check_ed = lambda cmue: bool(re.match('.*ed$',cmue[0]))			#observed
check_es = lambda cmue: bool(re.match('.*es$',cmue[0]))			#wishes fishes slashes
check_ess = lambda cmue: bool(re.match('.*ess$',cmue[0]))		#stewardess
check_ful = lambda cmue: bool(re.match('.*ful$',cmue[0]))		#revengeful
check_ing = lambda cmue: bool(re.match('.*ing$',cmue[0]))		#singing
check_ine = lambda cmue: bool(re.match('.*ine$',cmue[0]))		#medicine porcine emeraldine
check_ish= lambda cmue: bool(re.match('.*ish$',cmue[0]))		#womanish
check_ism= lambda cmue: bool(re.match('.*ism$',cmue[0]))		#witticism tribalism
check_ist= lambda cmue: bool(re.match('.*ist$',cmue[0]))		#geologist pharmicist
check_ite = lambda cmue: bool(re.match('.*ite$',cmue[0]))		#metabolite tripartite
check_ize = lambda cmue: bool(re.match('.*ize$',cmue[0]))		#specialize
check_less = lambda cmue: bool(re.match('.*less$',cmue[0]))		#featureless
check_like = lambda cmue: bool(re.match('.*like$',cmue[0]))		#ladylike
check_ly = lambda cmue: bool(re.match('.*ly$',cmue[0]))			#assembly
check_man = lambda cmue: bool(re.match('.*man$',cmue[0]))		#policeman
check_woman = lambda cmue: bool(re.match('.*woman$',cmue[0]))	#policewoman
check_ment = lambda cmue: bool(re.match('.*ment$',cmue[0]))		#amendment
check_ness= lambda cmue: bool(re.match('.*ness$',cmue[0]))		#charitableness
check_phile= lambda cmue: bool(re.match('.*phile$',cmue[0]))	#anglophile
check_phobe= lambda cmue: bool(re.match('.*phobe$',cmue[0]))	#anglophobe
check_proof = lambda cmue: bool(re.match('.*proof$',cmue[0]))	#fireproof
check_ship = lambda cmue: bool(re.match('.*ship$',cmue[0]))		#stewardship
check_some = lambda cmue: bool(re.match('.*some$',cmue[0]))		#frolicsome
check_sphere = lambda cmue: bool(re.match('.*sphere$',cmue[0]))	#biosphere
check_tor = lambda cmue: bool(re.match('.*tor$',cmue[0]))		#indicator
check_tory = lambda cmue: bool(re.match('.*tory$',cmue[0]))		#investigatory predatory
check_ward = lambda cmue: bool(re.match('.*ward$',cmue[0]))		#windward
check_wards = lambda cmue: bool(re.match('.*wards$',cmue[0]))	#
check_wise= lambda cmue: bool(re.match('.*wise$',cmue[0]))		#lengthwise
check_y= lambda cmue: bool(re.match('.*y$',cmue[0]))			#flabby


#prefixes (sometimes stressed)
check_ab= lambda cmue: bool(re.match('^ab',cmue[0]))		#abdicate
check_anti= lambda cmue: bool(re.match('^anti',cmue[0]))		#antidote
check_circum= lambda cmue: bool(re.match('^circum',cmue[0]))		#circumnavigate
check_counter = lambda cmue: bool(re.match('^counter',cmue[0]))			#counterbalance
check_down = lambda cmue: bool(re.match('^down',cmue[0]))			#2/3 stressed (downfall)
check_fore = lambda cmue: bool(re.match('^fore',cmue[0]))			#60% stressed: forecast
check_grand = lambda cmue: bool(re.match('^grand',cmue[0]))			#grandparent wishes fishes slashes
check_out = lambda cmue: bool(re.match('^out',cmue[0]))		#2/3 stressed outback
check_over = lambda cmue: bool(re.match('^over',cmue[0]))		#1/3 stressed overboard
check_tele = lambda cmue: bool(re.match('^tele',cmue[0]))		#telecast

#prefixes ('not stressed')
check_ac = lambda cmue: bool(re.match('^ac',cmue[0]))
check_ad= lambda cmue: bool(re.match('^ad',cmue[0]))
check_as= lambda cmue: bool(re.match('^as',cmue[0]))
check_be= lambda cmue: bool(re.match('^be',cmue[0]))
check_bi = lambda cmue: bool(re.match('^bi',cmue[0]))
check_co = lambda cmue: bool(re.match('^co',cmue[0]))
check_com = lambda cmue: bool(re.match('^com',cmue[0]))
check_con = lambda cmue: bool(re.match('^con',cmue[0]))
check_de= lambda cmue: bool(re.match('^de',cmue[0]))
check_des = lambda cmue: bool(re.match('^des',cmue[0]))
check_dis = lambda cmue: bool(re.match('^dis',cmue[0]))
check_em = lambda cmue: bool(re.match('^em',cmue[0]))
check_en= lambda cmue: bool(re.match('^en',cmue[0]))
check_ex= lambda cmue: bool(re.match('^ex',cmue[0]))
check_for= lambda cmue: bool(re.match('^for',cmue[0]))
check_geo = lambda cmue: bool(re.match('^geo',cmue[0]))
check_homo = lambda cmue: bool(re.match('^homo',cmue[0]))
check_hyper = lambda cmue: bool(re.match('^hyper',cmue[0]))
check_hypo = lambda cmue: bool(re.match('^hypo',cmue[0]))
check_il = lambda cmue: bool(re.match('^il',cmue[0]))
check_in = lambda cmue: bool(re.match('^in',cmue[0]))
check_inter = lambda cmue: bool(re.match('^inter',cmue[0]))
check_intra = lambda cmue: bool(re.match('^intra',cmue[0]))
check_ir = lambda cmue: bool(re.match('^ir',cmue[0]))
check_macro = lambda cmue: bool(re.match('^macro',cmue[0]))
check_mal = lambda cmue: bool(re.match('^mal',cmue[0]))
check_meta= lambda cmue: bool(re.match('^meta',cmue[0]))
check_micro= lambda cmue: bool(re.match('^micro',cmue[0]))
check_mid= lambda cmue: bool(re.match('^mid',cmue[0]))
check_mis = lambda cmue: bool(re.match('^mis',cmue[0]))
check_mono = lambda cmue: bool(re.match('^mono',cmue[0]))
check_multi = lambda cmue: bool(re.match('^multi',cmue[0]))
check_non = lambda cmue: bool(re.match('^non',cmue[0]))
check_ob = lambda cmue: bool(re.match('^ob',cmue[0]))
check_off = lambda cmue: bool(re.match('^off',cmue[0]))
check_per = lambda cmue: bool(re.match('^per',cmue[0]))
check_post = lambda cmue: bool(re.match('^post',cmue[0]))
check_pre = lambda cmue: bool(re.match('^pre',cmue[0]))
check_pro = lambda cmue: bool(re.match('^pro',cmue[0]))
check_psycho = lambda cmue: bool(re.match('^psycho',cmue[0]))
check_radio = lambda cmue: bool(re.match('^radio',cmue[0]))
check_re = lambda cmue: bool(re.match('^re',cmue[0]))
check_self = lambda cmue: bool(re.match('^self',cmue[0]))
check_semi = lambda cmue: bool(re.match('^semi',cmue[0]))
check_sub = lambda cmue: bool(re.match('^sub',cmue[0]))
check_super = lambda cmue: bool(re.match('^super',cmue[0]))
check_trans = lambda cmue: bool(re.match('^trans',cmue[0]))
check_ultra = lambda cmue: bool(re.match('^ultra',cmue[0]))
check_under = lambda cmue: bool(re.match('^under',cmue[0]))
check_up = lambda cmue: bool(re.match('^up',cmue[0]))
check_vice = lambda cmue: bool(re.match('^vice',cmue[0]))


affixes={

	'-ary':check_ary, 

# to antepenult
	'-ity':check_ity,	#capability
	'-iety':check_iety,	#anxiety
	'-al':check_al,	#technical
	'-ology':check_ology,	#methodology
	'-ian':check_ian,	#microbian, Arabian
	#'-dian':check_dian,	#tragedian, canadian
	#'-lian':check_lian,	#reptilian
	#'-nian':check_nian,	#amazonian, darwinian
	#'-rian':check_rian,	#grammarian, barbarian
	'-ean':check_ean,	#epicurean
	'-itan':check_itan,	#metropolitan, cosmopolitan
	'-icide':check_icide,	#infanticide
	'-ute':check_ute,	#dissolute, resolute
	'-neous':check_neous,	#harmonious
	'-nious':check_nious,	#miscellanneous
	'-dious':check_dious,	#melodious
	'-rious':check_rious,	#laborious
	'-lous':check_lous,	#miraculous
	'-mous':check_mous,	#acronymous
	'-nous':check_nous,	#monotonous
	'-rous':check_rous,	#omnivorous
	'-tous':check_tous,	#gratuitous
	'-uous':check_uous,	#ambiguous
	'-ius':check_ius,	#aquarius
	'-ograph':check_ograph,	#photograph
	'-ographer':check_ographer,	#photographer
	'-ography':check_ography,	#photography
	'-ient':check_ient,	#nutrient
	'-ify':check_ify,	#solidify
	'-ium':check_ium,	#auditorium
	'-cracy':check_cracy,	#democracy
	'-crat':check_crat,	#democrat
	'-ia':check_ia,	#melancholia
	'-omy':check_omy,	#economy
	'-pathy':check_pathy,	#homeopathy
	'-eria':check_eria,	#cafeteria
	'-onia':check_onia,	#catalonia
	'-ica':check_ica,	#harmonica
	'-ometer':check_ometer,	#kilometer
	'-ular':check_ular,	#molecular



 # to penult
	'-tion':check_tion,	#abbreviation
	'-cion':check_cion,	#
	'-gion':check_gion,	#
	'-nion':check_nion,	#
	'-sion':check_sion,	#
	'-xion':check_xion,	#
	'-lion':check_lion,	#medal medallion
	'-ic':check_ic,	#acidic
	'-ics':check_ics,	#acrobatics
	'-cial':check_cial,	#beneficial provincial
	'-tial':check_tial,	#
	'-cian':check_cian,	#magician
	'-tian':check_tian,	#dietitian
	'-gian':check_gian,	#norwegian
	'-sian':check_sian,	#caucasian, parisian
	'-cious':check_cious,	#judicious
	'-tious':check_tious,	#
	'-aceous':check_aceous,	#curvaceous
	'-geous':check_geous,	#litigious, outrageous
	'-gious':check_gious,	#
	'-sis':check_sis,	#analysis
	'-tis':check_tis,	#appendicitis
	'-nda':check_nda,	#agenda propaganda
	'-sive':check_sive,	#impulsive progressive
	'-ctive':check_ctive,	#instinctive
	'-ata':check_ata,	#errata
	'-ella':check_ella,	#cinderella
	'-ina':check_ina,	#ballerina
	'-o':check_o,	#concerto
	'-um':check_um,	#addendum
	'-cent':check_cent,	#phosphorescent

 #to ultimate
	'-ade':check_ade,	#lemonade arcade
	'-ain':check_ain,	#maintainance~maintain
	'-aire':check_aire,	#legionnaire
	'-ane':check_ane,	#human humane urban urbane
	'-ee':check_ee,	#examinee
	'-een':check_een,	#halloween
	'-eer':check_eer,	#engineer
	'-ese':check_ese,	#chinese, journalese
	'-eze':check_eze,	#
	'-esse':check_esse,	#finesse
	'-eur':check_eur,	#restaurant~restauranteur
	'-ique':check_ique,	#technical~technique
	'-oon':check_oon,	#spit~spitoon
	'-sque':check_sque,	#picturesque
	'-ette':check_ette,	#novelette

 # Non stress-shifting
	'-able':check_able,	#agreeable
	'-ant':check_ant,	#assistant
	'-ate':check_ate,	#rusticate
	'-cy':check_cy,	#literacy
	'-er':check_er,	#officer
	'-ed':check_ed,	#observed
	'-es':check_es,	#wishes fishes slashes
	'-ess':check_ess,	#stewardess
	'-ful':check_ful,	#revengeful
	'-ing':check_ing,	#singing
	'-ine':check_ine,	#medicine porcine emeraldine
	'-ish':check_ish,	#womanish
	'-ism':check_ism,	#witticism tribalism
	'-ist':check_ist,	#geologist pharmicist
	'-ite':check_ite,	#metabolite tripartite
	'-ize':check_ize,	#specialize
	'-less':check_less,	#featureless
	'-like':check_like,	#ladylike
	'-ly':check_ly,	#assembly
	'-man':check_man,	#policeman
	'-woman':check_woman,	#policewoman
	'-ment':check_ment,	#amendment
	'-ness':check_ness,	#charitableness
	'-phile':check_phile,	#anglophile
	'-phobe':check_phobe,	#anglophobe
	'-proof':check_proof,	#fireproof
	'-ship':check_ship,	#stewardship
	'-some':check_some,	#frolicsome
	'-sphere':check_sphere,	#biosphere
	'-tor':check_tor,	#indicator
	'-tory':check_tory,	#investigatory predatory
	'-ward':check_ward,	#windward
	'-wards':check_wards,	#
	'-wise':check_wise,	#lengthwise
	'-y':check_y,	#flabby


 #prefixes (sometimes stressed)
	'-ab':check_ab,	#abdicate
	'-anti':check_anti,	#antidote
	'-circum':check_circum,	#circumnavigate
	'-counter':check_counter,	#counterbalance
	'-down':check_down,	#2/3 stressed (downfall)
	'-fore':check_fore,	#60% stressed: forecast
	'-grand':check_grand,	#grandparent wishes fishes slashes
	'-out':check_out,	#2/3 stressed outback
	'-over':check_over,	#1/3 stressed overboard
	'-tele':check_tele,	#telecast

 #prefixes ('not stressed')
	'ac-':check_ac, 
	'ad-':check_ad, 
	'as-':check_as, 
	'be-':check_be, 
	'bi-':check_bi, 
	'co-':check_co, 
	'com-':check_com, 
	'con-':check_con, 
	'de-':check_de, 
	'des-':check_des, 
	'dis-':check_dis, 
	'em-':check_em, 
	'en-':check_en, 
	'ex-':check_ex, 
	'for-':check_for, 
	'geo-':check_geo, 
	'homo-':check_homo, 
	'hyper-':check_hyper, 
	'hypo-':check_hypo, 
	'il-':check_il, 
	'in-':check_in, 
	'inter-':check_inter, 
	'intra-':check_intra, 
	'ir-':check_ir, 
	'macro-':check_macro, 
	'mal-':check_mal, 
	'meta-':check_meta, 
	'micro-':check_micro, 
	'mid-':check_mid, 
	'mis-':check_mis, 
	'mono-':check_mono, 
	'multi-':check_multi, 
	'non-':check_non, 
	'ob-':check_ob, 
	'off-':check_off, 
	'per-':check_per, 
	'post-':check_post, 
	'pre-':check_pre, 
	'pro-':check_pro, 
	'psycho-':check_psycho, 
	'radio-':check_radio, 
	're-':check_re, 
	'self-':check_self, 
	'semi-':check_semi, 
	'sub-':check_sub, 
	'super-':check_super, 
	'trans-':check_trans, 
	'ultra-':check_ultra, 
	'under-':check_under, 
	'up-':check_up, 
	'vice-':check_vice 
}
