FROM continuumio/miniconda3

RUN mkdir -p /motion_backend

COPY ./motion_backend/requirements.yml /motion_backend/requirements.yml

WORKDIR /motion_backend

RUN /opt/conda/bin/conda env create -f requirements.yml

ENV PYTHONDONTWRITEBYTECODE=1

ENV PATH /opt/conda/envs/backend_motion/bin:$PATH

RUN echo "source activate backend_motion" > ~/.bashrc

COPY ./motion_backend /motion_backend
