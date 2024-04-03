#!/bin/bash

set -eu

foo () {
    ls $var
}


res=$(foo)
ls
