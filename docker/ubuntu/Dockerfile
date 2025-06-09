FROM ubuntu:18.04
MAINTAINER René Bod "https://github.com/renebod"

RUN apt-get update && apt-get install -y openssh-server neofetch
RUN mkdir /var/run/sshd


# RUN adduser --system --disabled-password ansible
# RUN usermod -aG sudo ansible
# RUN echo 'ansible:secret123' | chpasswd

# USER ansible
# WORKDIR /home/ansible


RUN echo 'root:secret123' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
