#!/bin/bash
python gen.py > in
time python alc.py < in > out
python spr.py
