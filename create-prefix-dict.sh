#!/bin/bash

#fstminimize --allow_nondet Q.fst Qmin.fst
fstepsnormalize --eps_norm_output $1 Qnorm.fst
fstprint  Qnorm.fst outputnorm.txt
python generatePrefixFiles.py outputnorm.txt
fstcompile --isymbols=osymsq2.txt --osymbols=osymsq1.txt --keep_isymbols --keep_osymbols transq3.txt

