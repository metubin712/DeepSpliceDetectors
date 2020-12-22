#!/bin/bash

directory=~/.DeepSpliceDetectors
mkdir -p "$directory"

output="$directory/logs.tar.gz"
if ! [ -f $output ]; then
  curl -sL -o $output "https://drive.google.com/uc?export=download&id=1aPcXoVQEezFP_SsvEkX9XiDxhPXI5vmO"
fi

tar -xf $output -C ./
