import sys
import numpy as np
from pytest import approx

sys.path.append('../')
sys.path.append('./')
sys.path.append('wbot/')
sys.path.append('WordleBot/wbot/')

import read


def test_wordlist1():

    """

    Test Word List Length

    """

    assert(len(read.word_list('allowed'))==12947 and len(read.word_list('possible'))==2309)


def test_wordlist2():

    """

    Test All Words Are 5 Letters

    """

    allowed_words= read.word_list('allowed')
    possible_words= read.word_list('possible')

    
    #calculate average letter length of allowed words
    av_al_len = np.mean([len(word) for word in allowed_words])

    #calculate average letter length of possible words
    av_pos_len = np.mean([len(word) for word in possible_words])


    assert(av_al_len == approx(5) and av_pos_len==approx(5))



