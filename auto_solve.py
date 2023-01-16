from wbot import read,play,solve,printing
import numpy as np


def auto_solve(true_word,tiles_grid,plist,glist,sal_patterns,sal_guess,cut_off=5):
    w=true_word.lower()

    print('True Word:'  ,true_word.upper())
    ts=play.tiles(w,'salet')

    printing.print_guess(ts,'salet') 
    
    tgrid,new_plist=solve.reduce('salet',ts,tiles_grid,plist,glist)

    guess=sal_guess[np.where(np.prod(sal_patterns ==ts, axis = -1))[0][0]]

    count=1

    while len(new_plist)>cut_off:
        
        count+=1
        
        ts=play.tiles(w,guess)

        printing.print_guess(ts,guess)

        tgrid,new_plist=solve.reduce(guess,ts,tgrid,new_plist,glist)
        
        if ts!=[2,2,2,2,2]:

            info_grid=solve.info_grid(tgrid)

            guess=glist[np.argmax(info_grid)]
            
        else:
            break
            
    
    if ts!=[2,2,2,2,2]:

        if count==1:
            info_grid=solve.info_grid(tgrid)
        guess,count=solve.cut_off(w,tgrid,new_plist,glist,info_grid,count)  
    
    print('Total Guesses: ',count) 

    return guess,count


if __name__ == "__main__":
    plist=np.array(read.word_list('possible'))
    glist=np.array(read.word_list('allowed'))
    tiles_grid=np.load('wbot/all_tiles.npz')['data']
    sal_patterns=np.load('wbot/salet_patterns.npy')
    sal_guess=np.load('wbot/salet_guess.npy')
    
    true_word=input('Word to guess: ')
    
    auto_solve(true_word,tiles_grid,plist,glist,sal_patterns,sal_guess)