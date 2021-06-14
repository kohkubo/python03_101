if [ $# -eq 1 ]; then
	find . -type f -name '*'"$1"'*' | sort
fi
