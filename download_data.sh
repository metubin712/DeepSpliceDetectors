#!/bin/bash

directory=~/.DeepSpliceDetectors
mkdir -p "$directory"

project=$(pwd);
md5="$directory/data.md5"
cp ./data.md5 "$md5"
cd "$directory" || exit

output="$directory/data.tar.gz"
if ! md5sum --quiet --status -c "$md5"; then
  curl -sL -o $output "https://drive.google.com/uc?export=download&id=1RY2n3sSciln3qIEVVFs-f5_lG-EXn9q1"
fi

if tar -xf $output -C $directory; then
  echo "Data is downloaded and extracted!"
else
  echo "Something went wrong! try again."
fi