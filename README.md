<br />
<p align="center">
  <h2 align="center">Onepiecelang</h2>

  <p align="center">
    ·
    <a href="./Report.pdf">Report</a>
    ·
  </p>
</p>


Text segmentation solution using natural language processing.  
It is concerned with splitting text into tokens. For example, “This is a whole sentence.” can be segmented into  
[“This”, “is”, “a”, “whole”,“sentence”, “.”].  
## Dataset

It​ ​is included in the folder “./data” which represents the ​ **unigram** ​of most
frequent words ordered ascendingly

## Description of the code attached

The code is divided into 4 functions

- read_unigrams
- find_spaces
- minimize_sentence_cost
- clean_sentence
- score

**read_unigrams:** ​ This function is used to read the data-set which contains
most frequent words in english words and

**Inputs:**

- Path of the data-set file.

**Returns:**

- Dictionary for each word in the data-set as key and it’s value is the
    cost of it with respect to it’s order in the file, cost function is
    implemented as the following:
       _Cost_ ( _wi_ ) = _Log_ 10 ( _i_ + 1 ) ​(1)
- Maximum word length

**Description:**

- Read the file
- Counting the words
- For each word in the file set it’s key in the dictionary of words and set
    its weight as mentioned in equation (1)
- Check length of current iteration word if it’s length is greater than
    maximum length word set it to current word length.


**find_spaces:** ​This the main core, used to take user’s input (concatenated
sentence)

**Inputs** ​:

- sentence: string the sentence/url before processing (concatenated
    sentence)
- unigrams: dict the words in the data-set with corresponding weight
- window_size: maximum word length in the dict

**Returns** ​:

- separated: list of strings words after separation

**Description** ​:
Preprocessing

1. remove all spaces in the sentence e.g. sentence = “welcometomy
    world” , became “welcometomyworld”

Initializations

2. set s_lower copy of the sentence as lowercase to match the
    dictionary entries
3. Set weights array for cost of the sentence at each letter index
4. Set index array that matches each cost what letters included for that
    word
5. Set empty array for the words to store the sentence there after
    splitting

Algorithm

6. For every letter in the sentence go and find minimum cost of the
    sentence with respect to it find the count of letters precedes it and
    makes the whole sentence is minimum cost, cost function is as
    mentioned before in read function e.g sentence = “heyworld”, first
    time iterator standing at ‘h’ and the cost function returns cost(‘h’) is
    minimum, then at next iteration iterator goes to ‘e’ and checks
    sentence within the window that matches (max_word_length)
    minimum cost as the following


```
min ( cost (′ h ′+ cost (′ e ′), cost (′ he ′))
That returns the minimum cost of that iteration is cost(“he”) and count
of prefix letters included is 2 letters and so on, it will be explained
more in the next function description ​ minimize_cost_function
```
7. After iteration over all letters of the sentence we go over back from
    last to minimize cost of the last letter which minimizes the whole
    sentence and takes over the letters which correspond to its weight.
    E.g. sentence = “heyworld” after finished step 6 we will have at splits
    array (which corresponding to each letter’s minimum cost howmany
    letters taken) We go over from last index and backtrack till reach first
    of sentence, it returns the separated words in descending order
8. Reverse order of the separated list and return it

**minimize_sentence_cost:** ​Utility function for ​ **find_spaces** ​ used to
minimize the sentence cost at a certain letter index in the sentence with
respect to the prefix window size letters

**Inputs:**

- sentence: string the sentence/url before processing (concatenated
    sentence)
- unigrams: dictionary of the words in the data-set with corresponding
    weight
- I: is the end of the ptr of current processing word
- weights: list the cost of the sentence at each index with respect to
    each split of each letter.
- window_size: maximum word length in the dictionary or the data-set

**Returns:**

- cost_min: cost computed due to split happened at this letter with its
    prefixes letters
- letters_count: the count of letters precedes the current letter index
    those minimize the cost of the sentence

**Description:**


Minimize the sentence cost at the current index by looking backwards and
trying to find the best word that can minimize the cost of the sentence e.g.
sentence: He is good, and my ptr is standing at 's'.
It will try to split all previous letters in window of size
i is the end of the ptr of current processing word
We look before it letter by letter and split the subword incrementally, and try
to find a subword which minimizes cost of sentence, and cost of splitting
this word in addition to the cost of sentence.
Initialization

1. start of the window set it to max(0, i - window_size)
2. Costs/Weights array from ‘start’ to i, Look at all previous letters cost.
3. Set cost_min to inf (some cost that is greater than any possible value)
    and set letters_count = -1 ; not set yet.
Algorithm
4. From the letter at current index (i-1) look at all letters preceding it and
within window size, each of them has computed the cost before.
Recalling: Foreach letter precedes I
A.Wj = costs[-j-1] Cost of the sentence at this letter
B.Wji = cost of the word from the unigram that starting at j and
ends at i
C.If the cost of this split (Wj + Wji) < min_cost, then assign min
cost to it and assign letters count to the j iterator.
5. Return min_cost and letters_count

**clean_sentence:** ​This function is used removing any special character or
number in the sentence, as assumed it is ignored but for assurance of not
bad testing
Inputs: - sentence
Returns: - sentence after cleaning

**score:** ​This function is used for testing and returns a score of the test
dataset

**Inputs** ​:

- X: list of sentences


- Y: list of lists, for each sentence its corresponding actual output
    separated list.
- unigrams: dictionary the words in the data-set with corresponding
    weight
- window_size: maximum word length in the dictionary

**Returns** ​:

- score: number of correctly separated words in exact place
    corresponding to same place and value in the actual output list
    divided by the total number of tested words, and multiplied by 100

**Description** ​:
Initialization

1. Set total_words = 0 and correct = 0
2. Loop over each example and call find_space on the input sentence
    and compare each word of the expected output list of this sentence
    and the actual output of that.
    And increment if expected word == actual word

## The relationship between files.

“/src/Notebook.ipynb” and “/src/script.py” “Both are equivalent but notebook
contains cells or testing and script is for end to end usage”

Both of those files are using “/data/unigrams.txt”
And Notebook.ipynb uses “/data/test_sentences,txt”
“/scrapper” is only used for scrapping sentences for testing. I just included it
to ensure my work.


## How to run the code and required dependencies

Python version used is 3
Dependencies:

- **numpy** ​for mathematical operations (needs installation)
- **time** ​built in module for used for performance measurements
**- re** ​built in module (regular expression library)

There are two ways to run the code at “./src” directory:

1. Using jupyter notebook and you will find instructions inside
    **(Notebook.ipynb)**
2. Using python script as the following command ​ **“python script.py”**

## How I wrote the code and how it helps you solve the problem

I've watched some of natural language processing specialization courses
And reading beautiful data book chapter 14 has good intuition about the
problem.
Words ninja library of python
Some blogs about natural language problem and similar problems


## Results and conclusions

I have scraped test-set from the internet from this sentences generator,
If you want to run the scrapper you need have ​ **node** ​installed in your
environment (javascript code)
And go to scrapper folder and run the following command
“node index.js >> sentences.txt”
Each run appends 560 new sentence to file sentences.txt
https://randomwordgenerator.com/json/sentences.json

No. of sentences: 7840
No. of total words: 95648
No. of completely correct words: 91098
Score : 95.24 %
Time cost is 9.6 seconds for testing those whole test-set and comparing the
model output with the actual output
Total time cost = (Cost of compare outputs + Cost of find spaces)

**Note**
The test set is not 100% correct, as it scraped as mentioned before so we
may have some outliers, which refers to some error in the test score

### Random picked results (correct)

**Testcase (1)
Sentence** ​: Thequickbrownfoxjumpsoverthelazydog
**Actual output as string** ​: The quick brown fox jumps over the lazy dog
**Actual output** ​: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
**Model output** ​: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

**Testcase (2)
Sentence** ​:
Hesaidhewasnotthereyesterdayhowevermanypeoplesawhimthere
**Actual output as string** ​: He said he was not there yesterday however
many people saw him there


**Actual output** ​: ['He', 'said', 'he', 'was', 'not', 'there', 'yesterday', 'however',
'many', 'people', 'saw', 'him', 'there']
**Model output** ​: ['He', 'said', 'he', 'was', 'not', 'there', 'yesterday', 'however',
'many', 'people', 'saw', 'him', 'there']

**Testcase (3)
Sentence** ​: Ashelookedoutthewindowhesawaclownwalkby
**Actual output as string** ​: As he looked out the window he saw a clown
walk by
**Actual output** ​: ['As', 'he', 'looked', 'out', 'the', 'window', 'he', 'saw', 'a',
'clown', 'walk', 'by']
**Model output** ​: ['As', 'he', 'looked', 'out', 'the', 'window', 'he', 'saw', 'a',
'clown', 'walk', 'by']

**Testcase (4)
Sentence:** ​ Thisisawholesentence.
**Actual output as string** ​: This is a whole sentence.
**Actual output** ​: ['This', 'is', 'a', 'whole', 'sentence', '.']
**Model output** ​: ['This', 'is', 'a', 'whole', 'sentence', '.']

**Testcase (5)
Sentence:** ​ Hedranklifebeforespittingitout
**Actual output as string:** ​ He drank life before spitting it out
**Actual output:** ​ ['He', 'drank', 'life', 'before', 'spitting', 'it', 'out']
**Model output:** ​ ['He', 'drank', 'life', 'before', 'spitting', 'it', 'out']

### Random picked results (incorrect)

**Testcase (1)
Sentence** ​:
IwasveryproudofmynicknamethroughouthighschoolbuttodayIcouldntbeanydi
fferenttowhatmynicknamewas


**Actual output** ​: ['I', 'was', 'very', 'proud', 'of', 'my', 'nickname', 'throughout',
'high', 'school', 'but', 'today', 'I', 'couldnt', 'be', 'any', 'different', 'to', 'what',
'my', 'nickname', 'was']

**Model output** ​: ['I', 'was', 'very', 'proud', 'of', 'my', 'nickname', 'throughout',
'highschool', 'but', 'today', 'I', 'couldnt', 'be', 'any', 'different', 'to', 'what', 'my',
'nickname', 'was']

**Notice** ​: High School is printed as Highschool, because it is in the unigram
model as an entry

**Testcase (2)
Sentence** ​: Shealwaysspeakstohiminaloudvoice
**Actual output** ​: ['She', 'always', 'speaks', 'to', 'him', 'in', 'a', 'loud', 'voice']
**Model output** ​: ['She', 'always', 'speaks', 'to', 'him', 'in', 'aloud', 'voice']
**Notice** ​the output is expected aloud instead of a loud due to the unigram
model also, and It may be there some incorrect test examples may expect
something and there is more than one way to express that.

**Testcase (3)
Sentence** ​: Allyouneedtodoispickupthepenandbegin
**Actual output** ​: ['All', 'you', 'need', 'to', 'do', 'is', 'pick', 'up', 'the', 'pen', 'and',
'begin']
**Model output** ​: ['All', 'you', 'need', 'to', 'do', 'is', 'pickup', 'the', 'pen', 'and',
'begin']

**Notice** ​: It is similar to previous example the model used ‘pickup’ without
space together instead of ‘pick up’. That demonstrates the most effect
comes out from the unigram/data-set used for building the model.

```
More test cases can be tested on the notebook.
```

## Assumptions

The following list represents my assumptions.

- There is no ​ **numbers or any special characters** ​in the url will be
    provided or sentence
- The domain of the sentences/urls will be used matches my used
    dictionary and the most frequent words in English
- Words spellings are correct


