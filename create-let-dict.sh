#!/usr/bin/env bash

python genFstlet.py $1
fstcompile --isymbols=isymsq2.txt --osymbols=osymsq2.txt --keep_isymbols --keep_osymbols transq2.txt letter.fst
fstinvert letter.fst invert.fst
#fstdeterminize invert.fst deterministic.fst
fstarcsort --sort_type=olabel invert.fst input_sorted.fst

fstarcsort --sort_type=ilabel L.fst model_sorted.fst

fstcompose input_sorted.fst model_sorted.fst
#fstepsnormalize Qunmin.fst Qnorm.fst
#fstdeterminize Qunmin.fst Q.fst
#fstprint --isymbols=osymsq2.txt --osymbols=osymsq1.txt Q.fst output.txt


