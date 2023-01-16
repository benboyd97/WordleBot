import sys
import numpy as np
from pytest import approx

sys.path.append('../')
sys.path.append('./')
sys.path.append('wbot/')
sys.path.append('WordleBot/wbot/')
sys.path.append('WordleBot/')

import read
from auto_solve import auto_solve



def test_auto_solve1():

    """

    Test Auto Solve on 'hello'

    """

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

    true_word='hello'

    #run auto solve script to solve wordle in fewest guesses given true word is known  
    final_guess,count=auto_solve(true_word,tiles_grid,plist,glist,sal_patterns,sal_guess)

    assert (true_word==final_guess and count==3)

def test_auto_solve2():

    """

    Test Auto Solve on 'wight'

    """

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

    true_word='wight'

    #run auto solve script to solve wordle in fewest guesses given true word is known  
    final_guess,count=auto_solve(true_word,tiles_grid,plist,glist,sal_patterns,sal_guess)

    assert (true_word==final_guess and count==6)


def test_auto_solve3():

    """

    Test Auto Solve on 'human'

    """

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

    true_word='human'

    #run auto solve script to solve wordle in fewest guesses given true word is known  
    final_guess,count=auto_solve(true_word,tiles_grid,plist,glist,sal_patterns,sal_guess)

    assert (true_word==final_guess and count==4)

def test_auto_solve4():

    """

    Test Auto Solve on 'abled'

    """

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

    true_word='abled'

    #run auto solve script to solve wordle in fewest guesses given true word is known  
    final_guess,count=auto_solve(true_word,tiles_grid,plist,glist,sal_patterns,sal_guess)

    assert (true_word==final_guess and count==2)