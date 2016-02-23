## Edited by Claire: makeNucleus and building V syllables within syllabify
# removed the use of the 'beginning' group as it was somehow leading to vowels being parsed as codas

import re
from nltk.corpus import cmudict

# Functions to build regular expression strings from descriptions of phonological classes or sequences of classes

# Take set and return string for regex to match any item in list
def classRegex(phonologicalClass):
    ret = '(' + '|'.join(phonologicalClass) + ')'
    # Want to match no strings for empty set, not empty string
    if ret == '()':
        return '([^\w\W])'
    else:
        return ret

# Take list of sets and build regex string for sequence represented
def sequenceRegex(sequence):
    return '(' + ' '.join([classRegex(pClass) for pClass in sequence]) + ')'



##################################################
# ENGLISH PARAMETERS
##################################################

ANY = set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'B', 'CH', 'D', 'DH', 'EH', 'ER', 'EY', 'F', 'G', 'HH', 'IH', 'IY', 'JH', 'K', 'L', 'M', 'N', 'NG', 'OW', 'OY', 'P', 'R', 'S', 'SH', 'T', 'TH', 'UH', 'UW', 'V', 'W', 'Y', 'Z', 'ZH'])
VOICED = set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'B', 'D', 'DH', 'EH', 'ER', 'EY', 'G', 'IH', 'IY', 'JH', 'L', 'M', 'N', 'NG', 'OW', 'OY', 'R', 'UH', 'UW', 'V', 'W', 'Y', 'Z', 'ZH'])
VOICELESS = set(['CH', 'F', 'HH', 'K', 'P', 'S', 'SH', 'T', 'TH'])
SONORANTS = set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW','L', 'M', 'N', 'NG', 'R'])
VOWELS = set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'])
TENSE = set(['EY', 'AY', 'OW', 'AW', 'OY'])
CONSONANTS = set(['B', 'CH', 'D', 'DH', 'F', 'G', 'HH', 'JH', 'K', 'L', 'M', 'N', 'NG', 'P', 'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'Y', 'Z', 'ZH'])
NASALS = set(['M', 'N', 'NG'])
LIQUIDS = set(['L', 'R'])
APPROXIMANTS = set(['L', 'R', 'W', 'Y'])
STOPS = set(['K', 'P', 'T', 'B', 'D', 'G'])
FRICATIVES = set(['F', 'V', 'S', 'Z', 'SH', 'ZH', 'TH', 'DH', 'HH'])

# Onset pattern from Wikipedia, which doesn't always specify classes well
# If errors crept in, probably from there http://en.wikipedia.org/wiki/English_phonology#Onset
#
# any consonant but NG initially
# plosive plus approximant other than Y
# voiceless fricative plus approximant other than Y        
# consonant plus Y
# S plus voiceless plosive        
# S plus nasal (not NG) 
# S plus F
# S plus voiceless plosive plus approximant
ENGLISH_ONSETS = \
               '(' + \
	       classRegex(CONSONANTS - set(['NG'])) \
	       + '|' + \
	       sequenceRegex([STOPS, APPROXIMANTS - set(['Y'])]) \
	       + '|' + \
	       sequenceRegex([FRICATIVES & VOICELESS, APPROXIMANTS - set(['Y'])]) \
	       + '|' + \
	       sequenceRegex([CONSONANTS, set(['Y'])]) \
	       + '|' + \
	       sequenceRegex([set(['S']), STOPS & VOICELESS]) \
	       + '|' + \
	       sequenceRegex([set(['S']), NASALS - set(['NG'])]) \
	       + '|' + \
	       '(S F)' \
	       + '|' + \
	       sequenceRegex([set(['S']), STOPS & VOICELESS, set(['R', 'Y'])]) \
	       + '|' + \
	       sequenceRegex([set(['S']), set(['K', 'P']), set(['L'])]) \
	       + '|' + \
	       sequenceRegex([set(['S']), set(['K']), set(['W'])]) \
	       + ')'

ENGLISH_SONORITY_SCALE = [VOWELS] #, LIQUIDS | NASALS]



##################################################
# BERBER PARAMETERS
##################################################

BERBER_ANY = set(['A', 'I', 'U', 'L', 'L@', 'R', 'R@', 'M', 'N', 'Z', 'Z@', 'ZH', 'QQH', 'QQHW', 'XX', 'F', 'S', 'S@', 'SH', 'QH', 'QHW', 'XH', 'H', 'B', 'D', 'D@', 'G', 'GW', 'T', 'T@', 'K', 'KW', 'Q', 'QW'])
BERBER_VOWELS = set(['A', 'I', 'U'])
BERBER_LOW_VOWELS = set(['A'])
BERBER_HIGH_VOWELS = set(['I', 'U'])
BERBER_LIQUIDS = set(['L', 'L@', 'R', 'R@'])
BERBER_NASALS = set(['M', 'N'])
BERBER_VOICED_FRICATIVES = set(['Z', 'Z@', 'ZH', 'QQH', 'QQHW', 'XX'])
BERBER_VOICELESS_FRICATIVES = set(['F', 'S', 'S@', 'SH', 'QH', 'QHW', 'XH', 'H'])
BERBER_VOICED_STOPS = set(['B', 'D', 'D@', 'G', 'GW'])
BERBER_VOICELESS_STOPS = set(['T', 'T@', 'K', 'KW', 'Q', 'QW'])

BERBER_ONSETS = \
             classRegex(BERBER_ANY - BERBER_LOW_VOWELS)

BERBER_SONORITY_SCALE = [BERBER_LOW_VOWELS, BERBER_HIGH_VOWELS, BERBER_LIQUIDS, BERBER_NASALS, BERBER_VOICED_FRICATIVES, BERBER_VOICELESS_FRICATIVES, BERBER_VOICED_STOPS, BERBER_VOICELESS_STOPS]

# Test set for Berber
BERBER_TEST = \
            [
                'r a t k t i', \
                'b d d l', \
                'm a r a t g t', \
                't f t k t', \
                't qh z n t', \
                't qh z n a k kw', \
                't z m t', \
                't m z xh', \
                't r g l t', \
                'i l d i', \
                'r a t l u l t', \
                't r b a'
            ]

# Runs test set
# Note this algorithm will give incorrect results for Berber as it does not follow the prohibition on final obstruent nuclei
# Thus it gives e.g. (t qh Z) (n A) (k KW) rather than (t qh Z) (n A k kw)
def testBerber():
    for word in BERBER_TEST:
        print syllabify(word, BERBER_SONORITY_SCALE, BERBER_ONSETS, BERBER_VOWELS)



# Helper functions for syllabification

# Take a match object, give a version back with matches surrounded by parens and second part capitalized
def makeCV(match):
    return ' (' + match.group('onset') + ' ' + match.group('nucleus').upper() + ')'

# Capitalize second part of match
def makeNucleus(match):
    return '(' + match.group('nucleus').upper() + ')'

#match.group('beginning') + 

# Take unsyllabified word as space-delimited CMUDict transcription
# Optional parameters:
# - relevant sonority hierarchy (list of sets corresponding to the classes)
# - regular expression string for onsets
# - set of sounds that can form onsetless syllables as nuclei (for hiatus and some phonotactic constraints)
# (defaults are as for English)
#
# Output syllabified form (uppercase = nucleus, parentheses = syllable boundaries)
#
# Algorithm is a modified DEA (allows hiatus and resolves unparsed initial segments)
def syllabify(form, sonorityScale=ENGLISH_SONORITY_SCALE, onsetPattern=ENGLISH_ONSETS, hiatusSet=ENGLISH_SONORITY_SCALE[0]):

    # normalization
    form = ' ' + form.lower() + ' '
    onsetPattern = onsetPattern.lower()

    # descend sonority hierarchy
    for sonorityLevel in sonorityScale:

        # regular expressions for this sonority level and its overlap with segments that can serve as onsetless syllables
        levelRegex = classRegex(sonorityLevel).lower()
        onsetlessRegex = classRegex(hiatusSet & sonorityLevel).lower()
        #print onsetlessRegex

        # build C+V syllables with nuclei of this sonority level
        form = re.sub(' (?P<onset>' + onsetPattern + ') (?P<nucleus>' + levelRegex + ')(?= [^)]*?(\(|$))', makeCV, form)
        #print form

        # build V syllables with nuclei of this sonority level
        form = re.sub('(?P<nucleus>' + onsetlessRegex + ')(?= [^)]*?(\(|$))', makeNucleus, form)
        #print form
        
    # build codas as all material between syllable boundaries
    form = re.sub('\)(.*?)( \(| $)', r'\1)\2', form)

    # extend initial onsets to make sure everything is parsed (languages like Berber)
    form = re.sub('(^ )([^(]+? )\(', r'\1(\2', form)
          
    return form[1:-1]


# (?P<beginning>(\)|^) )
# syllabify random word chosen from CMU Pronouncing Dictionary
# relies on having NLTK corpora
def syllabifyRandomEnglishWord():
    import random

    i = random.randrange(0,127069)
    w = cmudict.read()[i][2]
    w = [re.sub('[0-9]', '', p) for p in w]
    w = ' '.join(w)

    return syllabify(w)




