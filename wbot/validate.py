import numpy as np


def guess_input(suggested_word,glist):
    invalid=True
    while invalid:
        guess=input('Enter Y for '+suggested_word.upper()+' or type another guess: ').lower()
        if guess=='y' or guess=='yes':
            invalid=False
            guess=suggested_word
        elif guess in glist:
            invalid=False
        else:
            print('Invalid Guess Word')
    return guess


def tiles_input():
    invalid=True
    while invalid:
        ts=input('Type Tiles: ')
        if len(ts)!=5:
            print('Invalid Tiles')

        else:
            ts_=np.array([int(ts[0]),int(ts[1]),int(ts[2]),int(ts[3]),int(ts[4])])
            if len(ts_[np.logical_or(ts_<0,ts_>2)])>0:
                print('Invalid Tiles')
            else:
                invalid=False

    return [int(ts[0]),int(ts[1]),int(ts[2]),int(ts[3]),int(ts[4])]

