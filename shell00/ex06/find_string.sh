#!/bin/bash

if [ $# -eq 1 ]; then
	find . -type f  "$1" | sort
fi
