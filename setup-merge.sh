#!/bin/bash

# $1 - lex.txt $2 fstdir

rm -r $2
mkdir $2

python genFST.py $1
fstcompile --isymbols=isymsq1.txt --osymbols=osymsq1.txt --keep_isymbols --keep_osymbols transq1.txt L.fst

python genFstlet.py $1
fstcompile --isymbols=isymsq2.txt --osymbols=osymsq2.txt --keep_isymbols --keep_osymbols transq2.txt letter.fst
fstinvert letter.fst invert.fst
#fstdeterminize invert.fst deterministic.fst
fstarcsort --sort_type=olabel invert.fst input_sorted.fst

fstarcsort --sort_type=ilabel L.fst model_sorted.fst

fstcompose input_sorted.fst model_sorted.fst Q.fst


fstepsnormalize --eps_norm_output Q.fst Qnorm.fst
fstprint  Qnorm.fst outputnorm.txt
python generatePrefixFiles.py outputnorm.txt
fstcompile --isymbols=osymsq2.txt --osymbols=osymsq1.txt --keep_isymbols --keep_osymbols transq3.txt $2/Qprefix.fst
fstprint $2/Qprefix.fst Qprefix.txt
python genSuffixFiles.py Qprefix.txt
fstcompile --isymbols=osymsq2.txt --osymbols=osymsq1.txt --keep_isymbols --keep_osymbols transq4.txt $2/Qsuffix.fst

