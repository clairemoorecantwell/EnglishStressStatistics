# EnglishStressStatistics
Here you can find a series of tools for doing analysis of the English stress system using the CMU pronouncing dictionary.

You can get the pronouncing dictionary directly from the source at:
http://www.speech.cs.cmu.edu/cgi-bin/cmudict

Bruce Hayes also has his own, somewhat cleaned-up version, available on this page:
http://www.linguistics.ucla.edu/people/hayes/BLICK/CMUDictionaryEditedWithCELEXFrequenciesPublicVersion2.xls

In the main folder, you can see my annotated cmu: newCMU.txt, and use the R script corpusAnalysis.R to analyze it in R.  Also see the R script for explanations of the column names if they are opaque

Inside 'corpusGenerate' you will find a series of python scripts useful for generating files like newCMU.txt.  You can use these scripts to create your own specialized annotation of CMU.
