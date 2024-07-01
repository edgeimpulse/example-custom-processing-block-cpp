#!/bin/bash
set -e

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

cd $SCRIPTPATH
mkdir -p build
cd build
cmake ../py
cmake --build .
