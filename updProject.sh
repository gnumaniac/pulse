#!/bin/bash

# This script is used to update the solution
# Usage: run it from core and pulse folder --> ..\updProject.sh

./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --disable-conf && make clean && make && make install

exit 0