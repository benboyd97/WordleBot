import sys
import numpy as np
from pytest import approx

sys.path.append('../')
sys.path.append('./')
sys.path.append('wbot/')
sys.path.append('WordleBot/wbot/')

import solve,play


def test_reduce():

    """

    Test Reduce Table

    """

    #create grid of all guess word and true word tile possiblities
    tgrid=np.array([[play.tiles('happy','books'),play.tiles('camps','books'),play.tiles('north','books')],
    [play.tiles('happy','salet'),play.tiles('camps','salet'),play.tiles('north','salet')],
    [play.tiles('happy','audio'),play.tiles('camps','aduio'),play.tiles('north','audio')]],dtype=object)

    #create list of guess words
    glist=np.array(['books','salet','audio'])

    #create list of possible answers
    plist=np.array(['happy','camps','north'])

    #guess word is books
    guess='books'

    #simulate tiles of guess word books given true word north
    tiles=play.tiles('north','books')
    

    #give inputs to reduce function
    new_tgrid,new_plist=solve.reduce(guess,tiles,tgrid,plist,glist)

    
    #what the new tile grid should look like
    tgrid_ans=np.zeros((3,1,5),dtype=int)
    tgrid_ans[0,0,:]=play.tiles('north','books')
    tgrid_ans[1,0,:]=play.tiles('north','salet')
    tgrid_ans[2,0,:]=play.tiles('north','audio')

    #the only possible word remaining in the list should be north
    plist_ans=np.array(['north'],dtype=object)

    #are the new tile grids and possible word lists correct.
    assert(np.array_equal(tgrid_ans,new_tgrid) and np.array_equal(plist_ans,new_plist))


def test_info_gird():
    """

    Test Information Grid

    """
    #create grid of all guess word and true word tile possiblities
    tgrid=np.array([[play.tiles('happy','books'),play.tiles('camps','books'),play.tiles('north','books')],
    [play.tiles('happy','salet'),play.tiles('camps','salet'),play.tiles('north','salet')],
    [play.tiles('happy','audio'),play.tiles('camps','aduio'),play.tiles('north','audio')]])

    #calculate the expect information gain for each guess word
    info_grid=solve.info_grid(tgrid)

    #compare calculated expected information with answers
    assert info_grid==approx([1.5849625,1.5849625,0.91829583])


def test_cut_off():

    """

    Test Cut Off

    """
    #create grid of all guess word and true word tile possiblities
    tgrid=np.array([[play.tiles('happy','books'),play.tiles('camps','books'),play.tiles('north','books')],
    [play.tiles('happy','salet'),play.tiles('camps','salet'),play.tiles('north','salet')],
    [play.tiles('happy','audio'),play.tiles('camps','aduio'),play.tiles('north','audio')],
    [play.tiles('happy','happy'),play.tiles('camps','happy'),play.tiles('north','happy')],
    [play.tiles('happy','camps'),play.tiles('camps','camps'),play.tiles('north','camps')],
    [play.tiles('happy','north'),play.tiles('camps','north'),play.tiles('north','north')]
    ])


    #create list of guess words
    glist=np.array(['books','salet','audio','happy','camps','north'])

    #create list of possible answers
    plist=np.array(['happy','camps','north'])

    #set true word
    w='camps'

    #calculate the expect information gain for each guess word
    igrid=solve.info_grid(tgrid)

    count=0

    #find true word in list by only considering guess words from possible list
    guess,count=solve.cut_off(w,tgrid,plist,glist,igrid,count)

    #if guess word matches true word and finds answer in exected number of guesses
    assert guess==w and count==2




