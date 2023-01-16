from colorama import Fore,Back,Style

def print_guess(tiles,guess):

    """
    Print Guess

    Print the guess shadiding in each letter according to the coloured tile

    Parameters
    ----------

    tiles: tiles that the guess word yielded arr (5 integers)
    guess: guess word just used str (5 letters)

    """


    #make guess upper case
    guess=guess.upper()

    #tile colours 
    cs=[Fore.WHITE,Fore.YELLOW,Fore.GREEN]

    #black background
    print(Back.BLACK)

    #print coloured letters according to each tile
    print(cs[tiles[0]]+guess[0]+cs[tiles[1]]+guess[1]+cs[tiles[2]]+guess[2]+cs[tiles[3]]+guess[3]+cs[tiles[4]]+guess[4])

    #reset colours and background
    print(Style.RESET_ALL)