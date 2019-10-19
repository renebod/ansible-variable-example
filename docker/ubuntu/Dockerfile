FROM ubuntu:18.04
MAINTAINER René Bod "https://github.com/renebod"

RUN apt-get update

RUN apt-get install -y openssh-server apt-transport-https
RUN mkdir /var/run/sshd

RUN echo 'root:secret123' | chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22

# Define default command.
CMD ["/usr/sbin/sshd", "-D"]
