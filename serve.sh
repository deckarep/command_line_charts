#!/bin/sh
rm -rf log.txt
sudo nice -20 python generate.py > log.txt &

websocketd --port=8080 --staticdir=./static --sameorigin=true tail -f log.txt

