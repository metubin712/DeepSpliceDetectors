#!/bin/bash

directory=~/.DeepSpliceDetectors
mkdir -p "$directory"

output="$directory/data.tar.gz"
if ! [ -f $output ]; then
  curl -sL -o $output "https://drive.google.com/uc?export=download&id=1RY2n3sSciln3qIEVVFs-f5_lG-EXn9q1"
fi

tar -xf $output -C $directory
echo "Data is downloaded and extracted!"
