# HG2051 (AY22/23) Project 1: Individual assignment

##   Introduction

This project constitutes 30% of your final grade for HG2051. Please work on the
final program and report individually. Your code will be assessed based on its
functionality and simplicity/efficiency.

- The goal of this assignment is to demonstrate your programming and reasoning
abilities by working on a problem individually. If you have an idea for another
project that you would like to do instead, talk to me for approval.

- This project involves sorting, searching, and classifying lexical resources.
Submission requirements include your data, output, and annotated code along
with a short writeup describing your goals, process, and results.

## Project 1: Multilingual search

While it is relatively easy to search through a corpus of text to find
particular words/collocations/phrases in a single language, there are very few
search tools that will allow you to find matches based on multiple languages.
For this project you will develop a program that will return matches from
multiple levels of an interlinear text. The `project1.py` script in this
repository has some basic code to get you started. Keep in mind that the basic
code provides one direction out of many possible directions you can take in
developing your program/solution.

1. Find a language with interlinear texts that have been glossed in
English. You can find individual language resources such as for [Pnar](https://researchdata.ntu.edu.sg/file.xhtml?fileId=263&version=1.1)
online, as well as aggregated data such as the [ODIN](https://depts.washington.edu/uwcl/odin/)
project. Make sure you choose a language that has multiple texts available, as
you will need two or more texts which together contain at least 20
interlinearized sentences. Once you have chosen the language, select one of
the linguistic texts for testing your tool. Keep in mind that depending on
your source text you may need to consider encoding/decoding strategies.

2. Write a Python script that will read in the text, store it, and
allow for a user to search the data on multiple levels simultaneously, i.e.
*text*, *gloss*, *part of speech (POS)*. The idea here is that the user should
be able to query for all `nouns` that have the gloss **dog**, and look at all
sentences with those forms in order to observe the context in which they occur.
The implementation should enable searching using at least two levels of
annotation (i.e. *text*, *gloss*), but will receive a higher score if more than
two annotation levels are supported, as well as if forward and backward
searches (i.e. "all words with POS `n` preceded by POS `clitic`") are possible.

> The search query can be implemented either through user interaction or via
editing the script itself or some other method - whichever way you choose, this
should be clearly documented. The script should also return data in some way,
either by printing to the terminal or writing to a file.

3. Once your Python script is working for the first text you selected,
test it on the second text to make sure that it works, and make any necessary
changes so that it works for both texts. Finally, modify your program so that
you can search across both texts simultaneously.
> **Bonus:** get it to work on multiple additional texts in the same format.

4. Write a short paper (no longer than 5 pages) describing your goals,
data, process, and results. This paper should include some background
information on the language you chose, with relevant linguistic information and
citations for your sources. Submit this paper as a PDF along with your
annotated/commented Python code and the texts you chose in a Github repository.
The PDF should also be submitted via TurnItIn. Make sure to provide examples of
your queries and results in the paper or as separate files, and describe any
challenges you faced. Also ensure that your name and matric number are clearly
indicated in your code and in your PDF submission.
