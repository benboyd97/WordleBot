FROM continuumio/miniconda3

RUN git clone https://github.com/benboyd97/WordleBot.git 
    &&  cd WordleBot
    && ls -a
    &&git switch dev_brach
    &&git pull
    &&conda env update --file environment.yml --name base
    &&conda activate base
    &&pytest wbot/UnitTesting/







