#!/bin/bash
# Script para iniciar uma sessão tmux com layout e comandos específicos

SESSION_NAME="Main"

# Iniciar a sessão tmux
tmux new-session -d -s $SESSION_NAME

# Dividir a janela em dois panes
tmux split-window -v

# Redimensionar os panes (ajuste conforme necessário)
tmux resize-pane -t 0 -y 6   # Redimensionar o primeiro pane para 21 linhas de altura

# Executar comandos nos panes
tmux send-keys -t $SESSION_NAME:0.0 'cd ~/.tmux && env/bin/python3 neofetch.py; exit' C-m   # Primeiro pane

# Anexar à sessão tmux
tmux attach-session -t $SESSION_NAME
