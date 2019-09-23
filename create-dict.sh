#!/bin/bash


python genFST.py $1
fstcompile --isymbols=isymsq1.txt --osymbols=osymsq1.txt --keep_isymbols --keep_osymbols transq1.txt
