import sys
import numpy as np
from pytest import approx

sys.path.append('../')
sys.path.append('./')
sys.path.append('wbot/')
sys.path.append('WordleBot/wbot/')

import play


def test_find_pos():

    """

    Test Find Position

    """

    #test double occurance    
    t1=play.find_pos('hello','l')

    #test no occurance
    t2= play.find_pos('abcde','z')

    #test single occurance
    t3= play.find_pos('lands','s')

    #test triple occurance
    t4=play.find_pos('daddy','d')

    assert((t1==[2,3] and t2==[]) and ( t3==[4] and t4==[0,2,3]))

def test_tiles1():

    """

    Test tiles on simple word pairs

    """

    t1=play.tiles('rebus','arise')
    r1=t1==[0,1,0,1,1]

    t2=play.tiles('rebus','route')
    r2=t2==[2,0,1,0,1]

    t3=play.tiles('rebus','rules')
    r3=t3==[2,1,0,1,2]

    t4=play.tiles('rebus','rebus')
    r4=t4==[2,2,2,2,2]

    assert((r1 and r2) and ( r3 and r4))

def test_tiles2():

    """

    Test tiles on more complex doulbe letter pairs

    """

    t1=play.tiles('shoal','books')
    r1=t1==[0,0,2,0,1]

    t2=play.tiles('abide','speed')
    r2=t2==[0,0,1,0,1]
    
    t3=play.tiles('erase','speed')
    r3=t3==[1,0,1,1,0]

    t4=play.tiles('steal','speed')
    r4=t4==[2,0,2,0,0]

    t5=play.tiles('crepe','speed')
    r5=t5==[0,1,2,1,0]


    assert(((r1 and r2) and ( r3 and r4)) and r5)

