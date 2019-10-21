FROM python:3.8
MAINTAINER René Bod "https://github.com/renebod"

RUN apt-get update
RUN apt-get install -y sshpass

RUN pip install --upgrade pip
RUN pip install ansible
RUN pip install ansible_runner
RUN pip install couchdb
RUN pip install jupyter

EXPOSE 8888

WORKDIR "/home/ansible"
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
