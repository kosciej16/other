#!/bin/bash

# set -xe

for f in teste_final/small_n/*.in
do
    echo $f
    # cp $f in
    base=${f%%.in}
    python des.py < $f > $base.myout
    # cp $base.myout out
    diff -w $base.out $base.myout
done
