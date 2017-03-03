#!/bin/sh -e

MODULES=`find . -name '*.py'`

for m in $MODULES; do
	if ! grep has_builtin $m > /dev/null; then
		echo "Module $m does not have built-in check."
	fi
done

