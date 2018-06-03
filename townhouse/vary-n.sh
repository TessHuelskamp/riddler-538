#!/bin/bash

sequence="$(seq 10 99) $(seq 100 10 190) $(seq 200 100 1000)"
export HIST=0
export STATS=1

for N in $sequence; do

    export NUM_HOUSES=$N
    if [[ $N -le 100 ]]; then
        export NUM_TESTS=10000
    else
        export NUM_TESTS=1000
    fi

    ./houses.py
done

unset NUM_TESTS NUM_HOUSES HIST STATS

