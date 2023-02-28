#!/bin/bash

# Language and interpreter developed by 'Àngel Lluís Novo Fernando'

clear
if [ $# -ne 1 ]; then
    echo "Filename must be provided"
    exit 1
fi

python3 core.py $1