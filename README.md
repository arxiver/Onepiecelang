# Onepiecelang
Text segmentation solution using natural language processing.  
It is concerned with splitting text into tokens. For example, “This is a whole sentence.” can be segmented into  
[“This”, “is”, “a”, “whole”,“sentence”, “.”].  


While most of english is “almost” already segmented by white spaces, some languages such as chinese and some text sources such URLs may not have such a helpful property.  
I will be concerned with segmenting text with no spaces.  

> It can be solved with a unigram or bigram word model  
> and a dynamic programming algorithm similar to the Viterbi algorithm.
