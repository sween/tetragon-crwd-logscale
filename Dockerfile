# Meh, could be better, but this is easy
FROM ubuntu:noble

# Set the working directory in the container
WORKDIR /tetragon-crwd

# Copy the current directory contents into the container at /app
COPY src/. /tetragon-crwd

# Envs
ENV PYTHONUNBUFFERED=1

# Install kubectl and logscale python library, yadda yadda yadda

RUN chmod +x /tetragon-crwd/tetragon-crwd-logscale.py
RUN apt update -y
RUN apt install python3 python3-pip pipx curl -y
# RUN pipx install humiolib <---time suck
RUN pip3 install humiolib --break-system-packages
# RUN pipx ensurepath <---time suck
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
RUN kubectl version --client
RUN curl -L https://github.com/cilium/tetragon/releases/latest/download/tetra-linux-amd64.tar.gz | tar -xz
RUN mv tetra /usr/local/bin