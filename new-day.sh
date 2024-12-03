#!/usr/bin/env bash

mkdir -p $1/a
cp template.py $1/a/script.py
mkdir $1/b
cp template.py $1/b/script.py
touch $1/input.txt