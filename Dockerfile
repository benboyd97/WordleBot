FROM continuumio/miniconda3

RUN git clone https://github.com/benboyd97/WordleBot.git \ 
    &&  cd WordleBot \
    &&git switch dev_branch \
    &&git pull \
    &&conda\
    &&conda env create -f environment.yml \
    &&conda activate basic \
    &&pytest wbot/UnitTesting/







