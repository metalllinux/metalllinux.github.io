---
title: "Setup Privategpt On Rocky Linux 9.X"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "privategpt", "rocky", "linux"]
---

* Install `git`:
```
sudo dnf install -y gi
```
* Clone the PrivateGPT repository:
```
git clone https://github.com/zylon-ai/private-gpt
```
* Change into the directory:
```
cd private-gpt
```
* Set up `pyenv`:
```
curl -fsSL https://pyenv.run | bash
```
* Add the following to your `~/.bashrc` and `~/.profile` files:
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init - bash)"' >> ~/.profile
```
* Source `~/.bashrc` and `~/.profile`
```
source ~/.bashrc
source ~/.profile
```
* Run:
```
exec "$SHELL"
```
* Install Python version `3.11`:
```
pyenv install 3.11
```
* Set the version of Python to `3.11`:
```
pyenv local 3.11
```
* Install Poetry:
```
curl -sSL https://install.python-poetry.org | python3 -
```
* For the LLM, install Ollama:
```
curl -fsSL https://ollama.com/install.sh | sh
```
* Install PrivateGPT
```
poetry install --extras "ui llms-ollama embeddings-ollama vector-stores-qdrant"
```