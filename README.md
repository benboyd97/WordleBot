# WordleBot
Wordle Bot built to solve [Wordle](https://www.nytimes.com/games/wordle/index.html) in fewest number of guesses using Information Theory.

The bot calculates the expected information gain for each possible guess word and picks the maximum. The bot takes on average 3.448 guesses to answer all possible Wordle words. You can choose to play interactively with the WordleBot using `interactive_solve.py` or allow it to simulate games automatically using `auto_solve.py`. The corresponding report that describes background, methodology, development and final results can be found in the `WordleBot_Report.pdf` file.

## Setting up WordleBot Using Docker
If you use `docker` you can setup a portable version of WordleBot by copy and pasting the code below into terminal. Alternatively you can `git clone` the repository and make sure your environment is consistent with the `environment.yml` packages and versions.

```
git clone https://github.com/benboyd97/WordleBot.git && cd WordleBot
docker build -f demo.Dockerfile -t conda .
docker run --rm -ti conda
```

## Running WordleBot

### Auto-Solve

You can run an automatic version of WordleBot by running the following code:
```
cd WordleBot
python auto_solve.py
```
This will rely on you inputting the true Wordle word that is on the offical list of possible answers in `possible_words.txt`. WordleBot will then simulate the tiles after each guess and pick the next guess that will maximise the expected information gain.

Example:
> python auto_solve.py

>> Word to guess: adopt

>>> True Word: ADOPT

>>> SALET

>>> CRUDO


>>> ADOPT

>>> Total Guesses:  3

### Interactive Solve

You can also choose to play WordleBot interactively:
```
cd WordleBot
python interactive_solve.py
```
This feature does not require the true word being known and can be used to play along with a live Wordle game. The Bot will first suggest a starting word that you can either choose or pick a different word for the offical alowed guess list found in `guess_words.txt`. You are then expected to input the outcome of the chosen guess word's tiles. `0` represents a grey tile, `1` represents a yellow tile and `2` represents a green tile. So for green, yellow, yellow, green and grey, you would input `21120`. After these results are inputted, WordleBot will say how many possible answers are remaining and suggests the next guess that would maximise expected information. Again you can choose this suggested next gues or pick your own. The process continues until unkown word is found. 

Example:

> python interactive_solve.py

>>> Suggested Guess: SALET

>> Press Enter for SALET or type another guess: <ENTER>

>> Type Tiles: 00100

>>> Possible Answers: 98

>>> Next Suggested Guess: COURD

>> Press Enter for COURD or type another guess: CAMPS

>> Type Tiles: 10000

>>> Possible Answers:10

>>> Next Suggested Guess: UNIFY

>> Press Enter for UNIFY or type another guess: <ENTER>

>> Type Tiles: 00210

>>> Possible Answers: 1

>>> Final Answer: FLICK

>>> Total Guesses: 4
  
 If you would like to read about the specific custom modules used to make WordleBot, please refer to the docstring in `wbot/__init__.py`.

## Data Analysis Pipeline
  
 The `Data_Experiments.ipynb` contains a data pipeline that applies WordleBot to every posible Wordle answer. There are also profiling tests in order to test the time efficiency of the bot. The results of these experiments are presented in `Results_Data_Analysis.ipynb`.
  
## Unit Testing and Conintous Integration

In the directory `WordleBot/wbot/UnitTesting/` there are a series of 12 unit tests that test all the modules used in the Wordle Bot. These tests can run locally from the `WordleBot` parent file using the following commands:

  ```
  pytest wbot/UnitTesting/
  ```
These unit tests all also integrated into the version control framework. Each time a local repository is edited and then `push`-ed to the remote GitHub repository, the UnitTests are ran in a virtual Docker hosted by GitHub using workflow actions. Details of these continous integration scripts can be found  in `.github/workflows/actions.yml` and `Dockerfile` files.

 
### Credits
Author: [Ben Boyd](https://github.com/benboyd97), PhD Student at the University of Cambridge

WordleBot Solution Idea: 3Blue1Brown's [YouTube video](https://www.youtube.com/watch?v=v68zYyaEmEA)

Made for James Fergusson's Cambridge course in [Research-Computing](https://github.com/JamesFergusson/Research-Computing)

Helpful Discussion: [Samuel Turner](https://github.com/turnersam96)









