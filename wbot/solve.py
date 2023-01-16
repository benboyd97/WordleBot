import numpy as np
import sys

sys.path.append('../')
sys.path.append('./')
sys.path.append('wbot/')
sys.path.append('WordleBot/wbot/')


import play,printing,validation

def reduce(guess,tiles,tgrid,plist,glist):

    """
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

    """
        
    #find location of guess word in guess list
    g_id=np.where(glist==guess)[0][0]
    
    #find where ids in possible answers list that are consistent with these tiles given the guess.
    w=np.where(np.prod(tgrid[g_id,:,:] == tiles, axis = -1))[0]
    
    #output the tile grid and word lists containing only these possible tiles.

    return tgrid[:,w,:],plist[w]



def info_grid(tgrid):
    """
    solve.info_grid(tgrid)
    ----------------------

    Find the expected informaton gain by choosing each guess.
    
    Parameters
    ----------
    tgrid: Tiles Grid every possible tiles combination for remaining words. Array of size (N,M,5)
    

    Returns
    ----------
    expeted_info
        Returns one dimensional array of size (N,) giving expected information of each guess.
    """


    #find number of guesses and number of possible remaining answers from tgrid dimensions.
    gs,ps,_=tgrid.shape

    #create array of zeros to hold expected info for each guess word
    expected_info=np.zeros(gs)
    
    #for each guess word
    for i in range(gs):
        
        #list of unique tile patterns that guess word could make
        un_pat=np.unique(tgrid[i,:,:],axis=0)

        #initialise mean information gain
        mean_inf=0
        
        #for each unique tile pattern
        for j in range(un_pat.shape[0]):
            
            #calculate the probability of getting this pattern given the guess word
            p=len(np.where(np.prod(tgrid[i,:,:] == un_pat[j,:], axis = -1))[0])/ps
            
            #update mean information gain
            mean_inf+=-p*np.log2(p)

        #save mean information gain for this guess word
        expected_info[i]=mean_inf

    #return expected information gain for each word.
    return expected_info

def cut_off(w,tgrid,plist,glist,igrid,count):

    """
    solve.cut_off
    -------------

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
    """


    
    #create lists to store ids and expected information of possible words from larger guess name and information lists.
    pids=[]
    info_list=[]
    
    #for each possible remaining answer
    for p in plist:
        
        #find location in guess list
        pids=np.where(glist==p)[0][0]
        
        #find the expected information gain of the word
        info_list+=[igrid[pids]]
    
    #choose word with the highest iformation gain to be the guess
    guess=plist[np.argmax(info_list)]
    
    #update guess counter
    count+=1

    #simulate tiles of the guess given the true word
    tiles=play.tiles(w,guess)

    #output outcome of guess
    printing.print_guess(tiles,guess)

    #if the true word and guess match
    if tiles==[2,2,2,2,2]:

        return guess,count

    #if the guess does not match the true word            
    else:
        #reduce tiles grid and possible answers list further given new information
        tgrid,plist_=reduce(guess,tiles,tgrid,plist,glist)

        #if the answer list only has one possible answer       
        if len(plist_)==1:

            #output that answer and return guess count
            count+=1
            #output outcome of guess
            printing.print_guess([2,2,2,2,2],plist_[0])
            return plist_[0],count
        else:
            #apply cut_off(.) again to find word amongst shorter possile list
            return cut_off(w,tgrid,plist_,glist,igrid,count)


    
def manual_cut_off(tgrid,plist,glist,igrid,count):


    """
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

    """



    #output the number of possible words remaining
    print('Possible Answers:', len(plist))
    
    #print the remaining words
    if len(plist)>1:
        print_str=''
        for p in plist:
            print_str+=p.upper()+'  '

        print(print_str)

    #create lists to store ids and expected information of possible words from larger guess name and information lists.
    ids=[]
    info_list=[]
    for p in plist:
        
        #find location in guess list
        ids=np.where(glist==p)[0][0]

        #find the expected information gain of the word        
        info_list+=[igrid[ids]]
    
    #choose word with the highest iformation gain to be the guess
    guess=plist[np.argmax(info_list)]

    #output guess to try
    print('Next Suggesed Guess: ',guess.upper())
    count+=1

    #allow user to pick suggested guess or pick another
    guess=validation.guess_input(guess,glist)

    #allow user to input tiles and reduce tiles grid according to the new information
    tgrid,plist_,ts=validation.possible_reduce(guess,tgrid,plist,glist)

    #if the true word and guess match
    if ts==[2,2,2,2,2]:
        return guess,count

    #if the guess does not match the true word      
    else:

        #if the answer list only has one possible answer   
        if len(plist_)==1:

            count+=1
            print('Possible Answers: 1')
            #output answer and finish
            printing.print_guess([2,2,2,2,2],plist_[0])

            return plist_[0],count
        
        #apply manual_cut_off(.) again to find word amongst shorter possile list
        else:
            return manual_cut_off(tgrid,plist_,glist,igrid,count)

