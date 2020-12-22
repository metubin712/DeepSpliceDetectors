#!/bin/bash

directory=~/.DeepSpliceDetectors
mkdir -p "$directory"

project=$(pwd);
sha="$directory/data.sha256"
cp ./data.sha256 "$directory"
cd "$directory" || exit

output="$directory/data.tar.gz"
if ! shasum --quiet --status -a 256 -c "$sha"; then
  curl -sL -o $output "https://drive.google.com/uc?export=download&id=1RY2n3sSciln3qIEVVFs-f5_lG-EXn9q1"
fi

if tar -xf $output -C $directory; then
  echo "Data is downloaded and extracted!"
else
  echo "Something went wrong! try again."
fi