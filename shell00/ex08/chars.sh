#!/bin/bash

for arg in "$@";
do
	if [ -e "$arg" ]; then
		echo "$arg":$(cat "$arg" | wc -c | tr -d ' ' )
	else
		echo "$arg:No such file or directory"
	fi
done
