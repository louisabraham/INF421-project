#!/usr/bin/env bash

# this is a script we made to launch several instances of compute_reach.py
# usage: launch.sh number_of_instances number_of_vertices

for (( i = 0; i < $1; i++ )); do
    screen -dm bash -c "{ time pypy3 ./compute_reach.py $2 2>&1 ; } 2>> ~/inf421/time.log;"
done
