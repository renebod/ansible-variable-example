FROM jupyter/datascience-notebook

RUN pip install couchdb
RUN pip install ansible
