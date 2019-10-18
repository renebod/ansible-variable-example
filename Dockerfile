FROM jupyter/datascience-notebook

RUN pip install couchdb
RUN pip install ansible
RUN pip install ansible_runner
