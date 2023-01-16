import numpy as np
import solve,printing


def guess_input(suggested_word,glist):

    """
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

    """

    invalid=True

    #while the entered guess is invalid
    while invalid:

        #user enters guess
        guess=input('Press Enter for '+suggested_word.upper()+' or type another guess: ').lower()

        #choose suggested guess word
        if guess=='':
            invalid=False
            guess=suggested_word

        #if alternative word is in guess list
        elif guess in glist:
            invalid=False
        else:
        #tell user their guess word is invalid
            print('Invalid Guess Word')

    #return validated guess
    return guess


def tiles_input():


    """
    validation.tiles_input()

    Ensure the tiles being entered in interactive solver are valid

    
    Returns
    ----------
      validated guess

    """
    invalid=True
    
    #while the tiles entered are invalid
    while invalid:

        #take tile inputs
        ts=input('Type Tiles: ')
        #if input is not 5 characters long
        if len(ts)!=5:
            print('Invalid Tiles')

        #if input contains non-digits
        elif ts.isdigit()==False:
            print('Invalid Tiles')
        else:
            
            ts_=np.array([int(ts[0]),int(ts[1]),int(ts[2]),int(ts[3]),int(ts[4])])
            
            #make sure digits are 0,1 or 2
            if len(ts_[np.logical_or(ts_<0,ts_>2)])>0:
                print('Invalid Tiles')
            else:
                invalid=False
    #return validated tiles
    return [int(ts[0]),int(ts[1]),int(ts[2]),int(ts[3]),int(ts[4])]


def possible_reduce(guess,tiles_grid,plist,glist):

    """
    Possible

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

    

    """

    impossible=True

    #while tiles are impossible given the possible words remaining 
    while impossible:
        #check inputted tiles are a valid format
        ts=tiles_input()
        
        #output guess word given tiles
        printing.print_guess(ts,guess)

        #reduce tiles grid and possible answers list further given new information
        tgrid,new_plist=solve.reduce(guess,ts,tiles_grid,plist,glist)
        
        #if no remaining words match this patters
        if len(new_plist)==0:
            #inform user that patterns must be wrong
            print('No words match these patterns. Type again or rerun script.')

        else:
            #validatee tiles
            impossible=False

    #new tile grid,new list of possible words and validated inputted tiles.
    return tgrid,new_plist,ts





