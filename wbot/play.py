def find_pos(word,letter):

    
    pos=word.find(letter,0,5)
    
    if pos==-1:
        return []
    
    elif pos==4:
        return [4]
    
    else:
        pos2=word.find(letter,pos+1,5)
        if pos2==-1:
            return [pos]
        
        else:
            pos3=word.find(letter,pos2+1,5)
            if pos3==-1:
                return [pos,pos2]
            else:
                return [pos,pos2,pos3]
        

def tiles(word,guess):
    col_arr=[]
    for guess_pos,letter in enumerate(guess):
        word_pos=find_pos(word,letter)
        word_freq=len(word_pos)
        if len(word_pos)==0:
            col_arr+=[0]
            
        elif guess_pos in word_pos:
            col_arr+=[2]
            
        
        else:
            guess_pos_=find_pos(guess,letter)
            guess_freq=len(guess_pos_)
            if word_freq>=guess_freq:
                col_arr+=[1]
            elif word_freq==1:
                if letter in guess[0:guess_pos]:
                    col_arr+=[0]                  
                
                else:
                    col_arr+=[1]
                    
            else:
                if letter not in guess[0:guess_pos]:
                    col_arr+=[1]
                elif len(find_pos(guess[0:guess_pos],letter))==1:
                    col_arr+=[1]                
                else:
                    col_arr+=[0]
    
    for guess_pos,letter in enumerate(''.join(set(guess))):
        guess_freq=find_pos(guess,letter)
        if len(guess_freq)>1:
            word_freq=find_pos(word,letter) 
            if len(word_freq)==1:
                if len(guess_freq)==2:
                    if col_arr[guess_freq[0]]+col_arr[guess_freq[1]]==3:
                        col_arr[guess_freq[0]]=0
                if len(guess_freq)==3:
                    if col_arr[guess_freq[0]]+col_arr[guess_freq[1]]+col_arr[guess_freq[2]]==3:
                        col_arr[guess_freq[0]]=0
                        
            if len(word_freq)==2 and len(guess_freq)==3:
                tot=col_arr[guess_freq[0]]+col_arr[guess_freq[1]]+col_arr[guess_freq[2]]
                if tot==5:
                    if col_arr[guess_freq[1]]==2 and col_arr[guess_freq[2]]==2:
                        col_arr[guess_freq[0]]=0
                    else:
                        col_arr[guess_freq[1]]=0

                elif tot==4 and col_arr[guess_freq[1]]==1:
                    col_arr[guess_freq[1]]=0

    return col_arr