#!/bin/bash

ifconfig | grep ether | sed -e 's/^\tether//' | tr -d ' '
