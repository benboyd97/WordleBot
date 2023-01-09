def find_pos(word,letter):

    """
    Find Position
    
    Find all locations of a letter in a word
    
    Parameters
    ----------
    word: str (5 letters)
    letter: str (1 letter)
        
    Returns
    ----------
    list
        list of letter positions (ints)

    
    >>> find_pos('hello','l')
    [2,3]

    >>> find_pos('abcde','z')
    []

    >>> find_pos('lands','s')
    [5]
    """

    #see if letter is in word at all
    pos=word.find(letter,0,5)
    
    #if it is not there return empty list
    if pos==-1:
        return []
    
    #if the first occurance is the last letter then return [4]
    elif pos==4:
        return [4]
    
    else:
        #check between first occurance and end of the word for another occurance
        pos2=word.find(letter,pos+1,5)

        #if there is only one occurance
        if pos2==-1:
            return [pos]
        
        else:
            #chec between second occurance and end of word for another occurance
            pos3=word.find(letter,pos2+1,5)

            #if there is only two occurances
            if pos3==-1:
                return [pos,pos2]
            #if there are three occrances
            else:
                return [pos,pos2,pos3]
            
            #solution assumes no word has the same letter four times
        

def tiles(word,guess):

    """
    Tiles
    
    Returns the colours of each of the five tiles associated with each guess letter given the true word.
    
    Parameters
    ----------
    word: str (5 letters)
    guess: str (5 letters)
        
    Returns
    ----------
    list
        list of colours 0=Black, 1=yellow, 2=green (ints)

    
    >>> tiles('rebus','arise')
    [0,1,0,1,1]

    >>> tiles('rebus','route')
    [2,0,1,0,1]

    >>> tiles('rebus','rules')
    [2,1,0,1,2]

    >>> tiles('rebus','rebus')
    [2,2,2,2,2]

    >>> tiles('shoal','books')
    [0,0,2,0,1]

    >>> tiles('abide','speed')
    [0,0,1,0,1]

    >>> tiles('erase','speed')
    [1,0,1,1,0]

    >>> tiles('steal','speed')
    [2,0,2,0,0]

    >>> tiles('crepe','speed')
    [0,1,2,1,0]

    """


    #create empty list for coloured tiles
    col_arr=[]
    

    #cycle through each guess letter

    for l,letter in enumerate(guess):

        #find where guess letter lies in true word

        word_pos=find_pos(word,letter)
        
        #how many times guess letter is in true word
        word_freq=len(word_pos)

        #if the letter is not in true word
        if len(word_pos)==0:

            #add black tile
            col_arr+=[0]
            
        #if the letter's position in guess word matches a position in true word
        elif l in word_pos:

            #add green tile
            col_arr+=[2]
            
        #if the letter is in the true word but in a different position
        else:
            #find else the letter lies in the guess word
            guess_pos=find_pos(guess,letter)

            #find how often the letter lies in the guess word
            guess_freq=len(guess_pos)

            #if the letter appears more often or the same nubmer times in the real word compared to guess word
            if word_freq>=guess_freq:

                #add yellow tile 
                col_arr+=[1]

            #if the letter appears once in the real word
            elif word_freq==1:
                #if the same letter is found earlier in the guess word
                if letter in guess[0:l]:

                    #add black tile
                    col_arr+=[0]                  
                
                #if it is the first occurance of the letter in the guess word
                else:

                    #add yellow tile
                    col_arr+=[1]

            #if the letter appears twice in the real word but three times in the guess word       
            else:

                #if this is the first occurance of the letter 

                if letter not in guess[0:l]:

                    #add yellow tile
                    col_arr+=[1]

                #if this is the second occurance of the letter
                elif len(find_pos(guess[0:l],letter))==1:

                    #add yellow tile
                    col_arr+=[1]    

                #if this is the third occurance of the letter            
                else:
                    #add black tile
                    col_arr+=[0]


    #for the majority of word pairs the coloured tiles at this point will be correct.

    # we still need to account for some situations where a letter that appears more than once in the guess word
    # and is in the correct place for at least once
    # 
    # for examples at this point: tiles('shoal','books)=[0,1,2,0,1] which is wrong and should be  [0,0,2,0,1]  
    
    #cycle through unique letter in the guess word  
    for l,letter in enumerate(''.join(set(guess))):

        #find where letter lies in guess word
        guess_pos=find_pos(guess,letter)

        #find how often letter lies in guess word
        guess_freq=len(guess_pos)

        #if the letter appears more than once in the guess word
        if guess_freq>1:

            #find where the letter lies in true word
            word_pos=find_pos(word,letter) 

            #find how often the letter lies in the ture word
            word_freq=len(word_pos)

            #if the letter appears once in true word
            if word_freq==1:

                #if the letter appears twice in guess word
                if guess_freq==2:

                    #if the letter tiles add to make yellow+green=3 like for shoal example 
                    if col_arr[guess_pos[0]]+col_arr[guess_pos[1]]==3:

                        #change the first occurance tile from yellow to black
                        col_arr[guess_pos[0]]=0

                #if the letter appears three times in guess word
                if guess_freq==3:

                    #if the letter tiles add to make yellow+black+green=3
                    if col_arr[guess_pos[0]]+col_arr[guess_pos[1]]+col_arr[guess_pos[2]]==3:

                        #change the first occurance tile from yellow to black
                        col_arr[guess_pos[0]]=0
                        
            
            #if the letter appears twice in the real word and three times in the guess word
            elif word_freq==2 and  guess_freq==3:

                #add the three tiles where the letter is found
                tot=col_arr[guess_pos[0]]+col_arr[guess_pos[1]]+col_arr[guess_pos[2]]

                #if the total is equal to 5
                if tot==5:

                    #  yellow + green + green = 5
                    if col_arr[guess_pos[1]]==2 and col_arr[guess_pos[2]]==2:

                        #change the first occurance tile from yellow to black
                        col_arr[guess_pos[0]]=0

                    #  green + yellow + green = 5
                    else:
                        #change the first occurance tile from yellow to black
                        col_arr[guess_pos[1]]=0
                
                #if the total is equal to 4 and the second occurance is yellow
                elif tot==4 and col_arr[guess_pos[1]]==1:

                    #change the second occurance tile from yellow to black
                    col_arr[guess_pos[1]]=0

    return col_arr