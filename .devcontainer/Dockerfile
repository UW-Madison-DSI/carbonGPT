# Devcontainer Dockerfile
FROM python:3.12-slim

WORKDIR /workspace

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl build-essential git unzip fontconfig wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install nerd-fonts
RUN mkdir -p ~/.local/share/fonts && \
    cd ~/.local/share/fonts && \
    wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/0xProto.zip && \
    unzip 0xProto.zip && \
    rm 0xProto.zip && \
    fc-cache -f -v

# Install Starship
RUN curl -sS https://starship.rs/install.sh | sh -s -- -y && \
    mkdir -p ~/.config && \
    echo 'eval "$(starship init bash)"' >> ~/.bashrc && \
    starship preset pure-preset -o ~/.config/starship.toml

# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.cargo/bin:${PATH}"
