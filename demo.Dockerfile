FROM continuumio/miniconda3


RUN git clone https://github.com/benboyd97/WordleBot.git \
    && cd WordleBot \
    && git pull \
    && conda env create -f environment.yml --name wordlebot_env \
    && conda run -n wordlebot_env pytest wbot/UnitTesting/





