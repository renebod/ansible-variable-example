FROM jupyter/datascience-notebook

USER root
RUN apt-get update
RUN apt-get install -y ssh sshpass
#RUN apt-get install -y openssh-server apt-transport-https ansible sshpass

USER jovyan

RUN pip install couchdb
RUN pip install ansible
RUN pip install ansible_runner
