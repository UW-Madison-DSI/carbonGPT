#!/bin/bash

config_git() {
    echo "Configuring Git..."
    git config --global --add safe.directory /workspace/proto_carbongpt
    git config --global user.name "Jason Lo"
    git config --global user.email "lcmjlo@gmail.com"
    git config --global pull.rebase true
    git config --global core.filemode false
    git config --global core.eol lf
    git config --global credential.helper store
    echo "Git configured."
}

maybe_init_git() {
    git config --global --add safe.directory $(pwd)
    if [ ! -d .git ]; then
        echo "Initializing a new Git repository..."
        git init -b main
        echo "Git repository initialized."
    else
        echo "Git repository already initialized."
    fi
}

maybe_init_uv() {
    # Create the virtual environment if it doesn't exist
    if [ ! -d .venv ]; then
        echo "Creating the virtual environment..."
        uv venv
        echo "Virtual environment created."
    else
        echo "Virtual environment already exists."
    fi
    
    # Initialize the uv project if it doesn't exist
    if [ ! -f pyproject.toml ]; then
        echo "Initializing a uv project..."
        uv init
        echo "uv project initialized."
        rm hello.py
    else
        echo "uv project already initialized."
    fi
}

install_ansible() {
    echo "Installing Ansible..."
    apt update
    apt install ansible -y

    # Add aliases for Ansible Vault
    echo "alias enc='ansible-vault encrypt .env --output .env.enc'" >> ~/.bashrc
    echo "alias dec='ansible-vault decrypt .env.enc --output .env'" >> ~/.bashrc

    echo "Ansible installed."
}

# Configure development tools
set -e
config_git
maybe_init_git
maybe_init_uv
install_ansible

uv add streamlit
uv tool install streamlit


echo "Post-create script complete."

