FROM continuumio/miniconda3

RUN git clone https://github.com/benboyd97/WordleBot.git \ 
    &&  cd WordleBot \
    &&git switch dev_branch \
    &&git pull \
    &&conda init base\
    &&conda env update --file environment.yml --name base \
    &&conda activate base \
    &&pytest wbot/UnitTesting/







