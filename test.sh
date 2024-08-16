##!/bin/bash

#if [ -z "$1"]; then
	#echo "No test class provided. Usage: ./test.sh <TestClassName>"
	#exit 1
#fi

#python3 -m unittest src.test_nodes.$1

python3 -m unittest discover -v -s src
