"""

wbot
=====

Package used in the WordleBot as desribed in https://github.com/benboyd97/WordleBot

Functions are as follows:

read.word_list(file)
------------------
    
Read words from text file and return list of strings.

Read the 12,947 allowed Wordle words or the 2,309 Wordle solutions.
    
Parameters
----------
file: "allowed" or "possible"
        
Returns
----------
list
    list of strings


play.find_pos(word,letter)
------------------------
    
Find all locations of a letter in a word
    
Parameters
----------
word: str (5 letters)
letter: str (1 letter)
        
Returns
----------
list
    list of letter positions (ints)

    
>>> find_pos('hello','l')
[2,3]

>>> find_pos('abcde','z')
[]

>>> find_pos('lands','s')
[5]


play.tiles(word,guess)
----------------------
    
Returns the colours of each of the five tiles associated with each guess letter given the true word.
    
Parameters
----------
word: str (5 letters)
guess: str (5 letters)
        
Returns
    ----------
list
    list of colours 0=Black, 1=yellow, 2=green (ints)

    
>>> tiles('rebus','arise')
[0,1,0,1,1]

>>> tiles('rebus','route')
[2,0,1,0,1]

>>> tiles('rebus','rules')
[2,1,0,1,2]

>>> tiles('rebus','rebus')
[2,2,2,2,2]

>>> tiles('shoal','books')
[0,0,2,0,1]

>>> tiles('abide','speed')
[0,0,1,0,1]

>>> tiles('erase','speed')
[1,0,1,1,0]

>>> tiles('steal','speed')
[2,0,2,0,0]

>>> tiles('crepe','speed')
[0,1,2,1,0]


solve.reduce(guess,tiles,tgrid,plist,glist)
-------------------------------------------
    
Find all words that match a set of tiles given a guess.
Cross out words that are not possible from the word list and tiles grid.
    
Parameters
----------
guess: guess word just used str (5 letters)
tiles: tiles that the guess word yielded arr (5 integers)
tgrid: array of size (N,M,5) with every combination of remaining tile cominations.
plist: array of 5 letter words that are still possible answers of size M
glist: array of 5 letter guess words of size N
    
Returns
----------
tgrid'
    returns array with all remaining tile combinations of size (N,M',5)

plist'
    returns array with all remaining possible words of size M'

solve.info_grid(tgrid)
----------------------

Find the expected informaton gain by choosing each guess.
    
Parameters
----------
tgrid: Tiles Grid every possible tiles combination for remaining words. Array of size (N,M,5)
    

Returns
---------
expeted_info
    returns one dimensional array of size (N,) giving expected information of each guess.


solve.cut_off(w,tgrid,plist,glist,igrid,count)
------------------------------------------------

Function for finding the true word by only guessing with words from the possible remaining answers. 
This function is used once the other possible list of words is reduced to a small number of words.
    
Parameters
----------
w: true word 5 letter string.
tgrid: array of size (N,M,5) with every combination of remaining tile cominations.
plist: array of 5 letter words that are still possible answers of size M
glist: array of 5 letter guess words of size N
igrid: array of size (N,) of expected information for each of the guess words produced by info_grid(.).
count: int how many guesses have already been made 
    

Returns
----------
expeted_info
    count: return integer of total number of guesses to find word.


  
solve.manual_cut_offtgrid,plist,glist,igrid,count)
--------------------------------------------------

Only to be used when the user is playing interactively, typing in the tile results and the true word is not knwon.
    
Function for finding the true word by only guessing with words from the possible remaining answers. 
This function is used once the other possible list of words is reduced to a small number of words.
    
Parameters
----------

tgrid: array of size (N,M,5) with every combination of remaining tile cominations.
plist: array of 5 letter words that are still possible answers of size M
glist: array of 5 letter guess words of size N
igrid: array of size (N,) of expected information for each of the guess words produced by info_grid(.).    

   
validation.guess_input(suggested_word,glist)
---------------------------------------------

Ensure the guess being entered in interactive solver is in word list
    
Parameters
----------
sugugested_guess: guess word calculated to have the most entropy
glist: array of 5 letter guess words of size N
    
Returns
----------
    validated guess


validation.tiles_input()
-------------------------

Ensure the tiles being entered in interactive solver are valid

    
Returns
----------
    validated guess


validation.possible_reduce(guess,tiles_grid,plist,glist)
-------------------------------------------------------

Ensures that it is possible to get interactive solver inputted tiles given possible words remaining
    
Parameters
----------
guess: guess word just used str (5 letters)
tiles_grid: array of size (N,M,5) with every combination of remaining tile cominations.
plist: array of 5 letter words that are still possible answers of size M
glist: array of 5 letter guess words of size N
    
Returns
----------
tgrid
    returns array with all remaining tile combinations of size (N,M',5)

new_plist
    returns array with all remaining possible words of size M'
ts
    validated tiles


printing.print_guess(tiles,guess)

Print the guess shadiding in each letter according to the coloured tile

Parameters
----------

tiles: tiles that the guess word yielded arr (5 integers)
guess: guess word just used str (5 letters)

"""











