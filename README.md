# SIIM-ACR-PneumothoraMax-Classification


1. Установите pyenv
```bash 
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc 
```

2. Установить необходимую версию питона
```bash
make python
```

3. Создать окружение
```bash
make venv
```

4. Поставить поетри
```bash
make poetry
```

5. Инициализировать poetry
```bash
poetry init 
```

Правильно добавлять `torch` через `poetry`
```bash
poetry add torch --platform linux --python 3.9.13
```