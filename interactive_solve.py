from wbot import read,play,solve,printing
import numpy as np

def interactive_solve(tiles_grid,plist,glist,sal_patterns,sal_guess,cut_off=5):

    print('Guess: SALET')
    ts=input('Type Tiles: ')
    ts=[int(ts[0]),int(ts[1]),int(ts[2]),int(ts[3]),int(ts[4])]
    
    printing.print_guess(ts,'salet') 

    tgrid,new_plist=solve.reduce('salet',ts,tiles_grid,plist,glist)

    info_grid=solve.info_grid(tgrid)

    guess=glist[np.argmax(info_grid)]

    count=1

    while len(new_plist)>cut_off:
    
        count+=1
    
        print('Possible Answers: ', len(new_plist))
        print('Next Guess: ',guess.upper())
    
        ts=input('Type Tiles:')
    
        ts=[int(ts[0]),int(ts[1]),int(ts[2]),int(ts[3]),int(ts[4])]

        printing.print_guess(ts,guess)        

        tgrid,new_plist=solve.reduce(guess,ts,tgrid,new_plist,glist)
    
        if ts!=[2,2,2,2,2]:
            info_grid=solve.info_grid(tgrid)

            guess=glist[np.argmax(info_grid)]
        
        else:
            break
    

    if ts==[2,2,2,2,2]:
        print('Total Guesses: ',count) 
        return guess,count

    elif len(new_plist)==1:
        count+=1
        print('Possible Answers: 1')
        print('Final Answer:')
        printing.print_guess([2,2,2,2,2],new_plist[0])
        print('Total Guesses: ',count) 
        return guess,count
    elif ts!=[2,2,2,2,2]:
        if count==1:
            info_grid=solve.info_grid(tgrid)
        guess,count=solve.manual_cut_off(tgrid,new_plist,glist,info_grid,count) 
        print('Total Guesses: ',count)  
        return guess,count


if __name__ == "__main__":
    plist=np.array(read.word_list('possible'))
    glist=np.array(read.word_list('allowed'))
    tiles_grid=np.load('wbot/all_tiles.npz')['data']
    sal_patterns=np.load('wbot/salet_patterns.npy')
    sal_guess=np.load('wbot/salet_guess.npy')
    
    interactive_solve(tiles_grid,plist,glist,sal_patterns,sal_guess)