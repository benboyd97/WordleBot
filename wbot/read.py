import os.path

def word_list(file):

    """
    read.word_list(file)
    ------------------
    
    Read words from text file and return list of strings.

    Read the 12,947 allowed Wordle words or the 2,309 Wordle solutions.
    
    Parameters
    ----------
    file: "allowed" or "possible"
        
    Returns
    ----------
    list
        list of strings
    """

    #read either the allowed or possible txt file from the parent directory
    with open(os.path.dirname(__file__) + '/../'+file+'_words.txt') as f:
        words = f.readlines()
    
    #remove the \n from each word
    words = [word.strip() for word in words]
    

    return words