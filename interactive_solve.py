from wbot import read,play,solve,printing,validation
import numpy as np

def interactive_solve(tiles_grid,plist,glist,sal_patterns,sal_guess,cut_off=5):

    """
    Interactive Solve

    Function to provide suggested guesses and number of words remaining to user, given that they input the tile outcomes and chosen guess word.

    Parameters
    ----------
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


    print('Suggested Guess: SALET')

    #allow user to select suggested starter word or input their own valid guess
    guess=validation.guess_input('salet',glist)
    
    #reduce new tile grid and new word list given new information
    tgrid,new_plist,ts=validation.possible_reduce(guess,tiles_grid,plist,glist)

    #if suggested starter word is used
    if guess=='salet':

        #pick precomputed best second guess given the tile pattern
        guess=sal_guess[np.where(np.prod(sal_patterns ==ts, axis = -1))[0][0]]

    #if alternative starter word is chosen
    else:
        #calculate the expected informaiton of each of the second guesses
        info_grid=solve.info_grid(tgrid)

        #pick word with most expected information to be second suggested guess
        guess=glist[np.argmax(info_grid)]

    count=1

    #while possible wordle answers remaining is greater than the cut-off point
    while len(new_plist)>cut_off:
    
        count+=1

        #let user know how many possible Wordle answers remain
        print('Possible Answers: ', len(new_plist))
        
        #let user know the next suggested guess
        print('Next Suggested Guess: ',guess.upper())

        #allow user to select suggested guess word or input their own valid guess
        guess=validation.guess_input(guess,glist)

        #reduce new tile grid and new word list given new information
        tgrid,new_plist,ts=validation.possible_reduce(guess,tgrid,new_plist,glist)
        
        #if wordle is not yet solved
        if ts!=[2,2,2,2,2]:
            #calculate the expected information of all guess words
            info_grid=solve.info_grid(tgrid)

            #pick guess word with highest expected information
            guess=glist[np.argmax(info_grid)]
        
        else:
            #break out of loop if Wordle is solved
            break
    
    
    #if wordle is solved
    if ts==[2,2,2,2,2]:
        #output total guesses
        print('Total Guesses: ',count) 
        #output answer and count
        return guess,count

    #if only one possible word remains
    elif len(new_plist)==1:
        #let user know the only possible answer
        count+=1
        print('Possible Answers: 1')
        print('Final Answer:')
        printing.print_guess([2,2,2,2,2],new_plist[0])

        #output total guesses
        print('Total Guesses: ',count) 

        #output possible answer and count
        return guess,count

    #if wordle still not solved
    elif ts!=[2,2,2,2,2]:
        #if only one  guess has been made 
        if count==1:
            #calculate the expected information of each second guess
            info_grid=solve.info_grid(tgrid)
        #apply cut off routine to only guess from the remaining possible words, but still maximise information
        guess,count=solve.manual_cut_off(tgrid,new_plist,glist,info_grid,count) 

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
    
    #run interactive solve script allowing the user to input their choice of guess word and tile outcomes.
    interactive_solve(tiles_grid,plist,glist,sal_patterns,sal_guess)