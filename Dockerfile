FROM continuumio/miniconda3

RUN cd home

RUN git clone https://github.com/benboyd97/WordleBot.git

RUN cd WordleBot

RUN ls -a

RUN git switch dev_brach



RUN git pull

RUN conda env update --file environment.yml --name base

RUN conda activate base

RUN pytest wbot/UnitTesting/







