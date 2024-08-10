#!/bin/bash

directory=~/.DeepSpliceDetectors
mkdir -p "$directory"

project=$(pwd);
sha="$directory/data.sha256"
cp ./data.sha256 "$directory"
cd "$directory" || exit

output="$directory/data.tar.gz"
if ! shasum --quiet --status -a 256 -c "$sha"; then
  # https://drive.google.com/uc?export=download&id=[ID]
  curl -sL -o "$directory/data.tar.gz.minamin00" "https://cloud.aminzabardast.com/dsd/data.tar.gz.minamin00"
  curl -sL -o "$directory/data.tar.gz.minamin01" "https://cloud.aminzabardast.com/dsd/data.tar.gz.minamin01"
fi

cd "$project" || exit

cat "$output".minamin* > $output

if tar -xf $output -C $directory; then
  echo "Data is downloaded and extracted!"
else
  echo "Something went wrong! try again."
fi