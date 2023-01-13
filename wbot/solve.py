import numpy as np
import sys

sys.path.append('../')
sys.path.append('./')
sys.path.append('wbot/')
sys.path.append('WordleBot/wbot/')


import play

def reduce(guess,tiles,tgrid,plist,glist):
    
    
    g_id=np.where(glist==guess)[0][0]

    w=np.where(np.prod(tgrid[g_id,:,:] == tiles, axis = -1))[0]
    
    return tgrid[:,w,:],plist[w]



def prob_grid(tgrid):
    
    gs,ps,_=tgrid.shape
    
    egrid=np.zeros(gs)
    
    for i in range(gs):
        
        un_pat=np.unique(tgrid[i,:,:],axis=0)
        mean_inf=0
        
        for j in range(un_pat.shape[0]):
            
           
            p=len(np.where(np.prod(tgrid[i,:,:] == un_pat[j,:], axis = -1))[0])/ps
            mean_inf+=-p*np.log2(p)

        egrid[i]=mean_inf
    return egrid

def cut_off(w,tgrid,plist,glist,igrid,count):
    ids=[]
    info_list=[]
    for p in plist:
        
        ids=np.where(glist==p)[0][0]
        
        info_list+=[igrid[ids]]
    
    guess=plist[np.argmax(info_list)]
    
    count+=1
    tiles=play.tiles(w,guess)
    if tiles==[2,2,2,2,2]:
        print(w,guess,count)
        return count        
    else:
        tgrid,plist_=reduce(guess,tiles,tgrid,plist,glist)
        
        if len(plist_)==1:
            count+=1
            print(w,plist_[0],count)
            return count
        else:
            return cut_off(w,tgrid,plist_,glist,igrid,count)
        
def manual_cut_off(tgrid,plist,glist,igrid):
    
    print('Possible Answers:', len(plist))
    ids=[]
    info_list=[]
    for p in plist:
        
        ids=np.where(glist==p)[0][0]
        
        info_list+=[igrid[ids]]
    
    guess=plist[np.argmax(info_list)]

    print('Guess:',guess)

    ts=input('Type Tiles')
    if [int(ts[0]),int(ts[1]),int(ts[2]),int(ts[3]),int(ts[4])]==[2,2,2,2,2]:
        print('Done')     
    else:
        tgrid,plist_=reduce(guess,[int(ts[0]),int(ts[1]),int(ts[2]),int(ts[3]),int(ts[4])],tgrid,plist,glist)
        if len(plist_)==1:
            print('Answer:', plist_[0])
        else:
            manual_cut_off(tgrid,plist_,glist,igrid)