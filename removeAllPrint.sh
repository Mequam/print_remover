#!/bin/bash

#this file just runs the killprint script for every file in the directory

#TODO: we could fairly easily emulate this behavior in a python script
#but I am lazy and like linux :p

find $1 -name \*.gd -exec ./killprint.py {} \;
