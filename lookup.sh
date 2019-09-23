#!/usr/bin/env bash

if [ $1 -eq 1 ]
then
    python acceptor.py $2
    fstcompile --isymbols=isymsq1.txt --osymbols=isymsq1.txt --keep_isymbols --keep_osymbols tA.txt A.fst
    fstarcsort --sort_type=olabel A.fst input_sorted.fst

    fstarcsort --sort_type=ilabel L.fst model_sorted.fst




    # Creates the composed FST.
    fstcompose input_sorted.fst model_sorted.fst comp.fst
    fstprint --isymbols=isymsq1.txt --osymbols=osymsq1.txt comp.fst | awk  '{print $NF}' | while read line; do echo -n $line " "; done | awk '{$NF=""; print $0}'



    # Just keeps the    output label
#    $ fstproject --project_output comp.fst result.fst
elif [ $1 -eq 2 ]
then
    echo "Not implemented error"
elif [ $1 -eq 3 ]
then
    python acceptLet.py $3
    fstcompile --isymbols=osymsq2.txt --osymbols=osymsq2.txt --keep_isymbols --keep_osymbols tA.txt A.fst
    fstarcsort --sort_type=olabel A.fst input_sorted.fst
    fstepsnormalize $2 Qprefixnorm.fst
#    fstarcsort --sort_type=ilabel Qprefixnorm.fst model_sorted.fst
    fstcompose input_sorted.fst Qprefixnorm.fst comp.fst
    fstrandgen  comp.fst out.fst
    fstprint out.fst | awk  '{print $NF}' | while read line; do echo -n $line " "; done | awk '{$NF=""; print $0}'
elif [ $1 -eq 4 ]
then
#    echo $3 | rev | python acceptLetin.py
    python acceptLet.py $3
    fstcompile --isymbols=osymsq2.txt --osymbols=osymsq2.txt --keep_isymbols --keep_osymbols tA.txt A.fst
    fstarcsort --sort_type=olabel A.fst input_sorted.fst
#    fstepsnormalize $2 Qsuffixnorm.fst
#    fstarcsort --sort_type=ilabel Qprefixnorm.fst model_sorted.fst
    fstcompose input_sorted.fst $2 comp.fst
    fstrandgen  comp.fst out.fst
    fstprint out.fst | awk  '{print $NF}' | while read line; do echo -n $line " "; done | awk '{$NF=""; print $0}'

else
    echo "Not implemented error"
fi
