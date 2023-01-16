from colorama import Fore, Back,Style

def print_guess(ts,g):

    g=g.upper()

    cs=[Fore.WHITE,Fore.YELLOW,Fore.GREEN]

    print(Back.BLACK)
    print(cs[ts[0]]+g[0]+cs[ts[1]]+g[1]+cs[ts[2]]+g[2]+cs[ts[3]]+g[3]+cs[ts[4]]+g[4])
    print(Style.RESET_ALL)