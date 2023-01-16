from wbot import read,play,solve,printing
import numpy as np


def auto_solve(true_word,tiles_grid,plist,glist,sal_patterns,sal_guess,cut_off=5):

    """
    Auto Solve

    Function automatically simulates a game of Wordle using best guesses given that the true word is known.

    Parameters
    ----------
    true_word 5 letter string containing the true word
    tiles_grid numpy array of size (N,M,5) for every grid tile combination for every guess and true word pair
    plist numpy array of size (M,) containing every possible wordle answer word
    glist numpy array of size (N,) containing every possible wordle guess word
    sal_patterns numpy array of size (L,5) containing all L unique tile patterns for the starting word 'salet'
    sal_guess numpy array of size (L,) contaning the best second guess word given the first word is 'salet'
    cut_off=5 int, the number of possible words remaaning where only possible wordle answers are used as guesses
    
    Returns
    ----------
      guess 5 letter string answer to wordle
      count number of guesses taken

    """


    #make sure true word is lower case
    w=true_word.lower()

    print('True Word:'  ,true_word.upper())
    
    #simulate tils given first guess is salet
    ts=play.tiles(w,'salet')

    #ouput tile outcome
    printing.print_guess(ts,'salet') 
    
    #reduce new tile grid and new word list given new information
    tgrid,new_plist=solve.reduce('salet',ts,tiles_grid,plist,glist)

    #find precomputed best second guess for the given tile outcome
    guess=sal_guess[np.where(np.prod(sal_patterns ==ts, axis = -1))[0][0]]

    count=1

    #while possible wordle answers remaining is greater than the cut-off point
    while len(new_plist)>cut_off:
        
        count+=1
        
        #simulate tiles given true word and guess word
        ts=play.tiles(w,guess)

        #ouput tile outcome
        printing.print_guess(ts,guess)

        #reduce new tile grid and new word list given new information
        tgrid,new_plist=solve.reduce(guess,ts,tgrid,new_plist,glist)
        
        #if wordle is not solved yet
        if ts!=[2,2,2,2,2]:
            
            #calculate the expected information for the next guess
            info_grid=solve.info_grid(tgrid)
            
            #use guess with the highest expected information as next guess
            guess=glist[np.argmax(info_grid)]
            
        else:
            #break out of loop if Wordle is solved
            break
            
    #if Wordle is not yet soled
    if ts!=[2,2,2,2,2]:

        #if only one  guess has been made 
        if count==1:
            #calculate the expected information of each second guess
            info_grid=solve.info_grid(tgrid)

        #apply cut off routine to only guess from the remaining possible words, but still maximise information
        guess,count=solve.cut_off(w,tgrid,new_plist,glist,info_grid,count)  
    
    #output total guesses
    print('Total Guesses: ',count) 
    #return wordle answer and total number of guesses
    return guess,count


if __name__ == "__main__":
    #load numpy array containing every possible wordle answer
    plist=np.array(read.word_list('possible'))

    #load numpy array containing every allowed wordle guess 
    glist=np.array(read.word_list('allowed'))

    #load pre-computed grid containing all tile combinations for each guess and possible answer word pair
    tiles_grid=np.load('wbot/all_tiles.npz')['data']

    #load pre-computed unique tile patterns given the first word is 'salet'
    sal_patterns=np.load('wbot/salet_patterns.npy')

    #load each of the precomputed best second guess words for each tile pattern, given the first word was 'salet'.
    sal_guess=np.load('wbot/salet_guess.npy')
    

    invalid=True

    #while true word is not a valid wordle answer
    while invalid:
        #take true word as input
        true_word=input('Word to guess: ')
        #if true word is in possible wordle answer list
        if true_word in plist:
            #break
            invalid=False
        else:
            #tell user the word is not a possible answer
            print('Word is not a possible Wordle answer.')
    #run auto solve script to solve wordle in fewest guesses given true word is known    
    auto_solve(true_word,tiles_grid,plist,glist,sal_patterns,sal_guess)