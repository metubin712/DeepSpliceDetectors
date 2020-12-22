#!/bin/bash

while true; do
    read -p "Warning! This code might override the data in logs directory. Continue? (y/N)? " yn
    case $yn in
        [Yy]* ) break;;
        * ) echo "Aborted!"; exit;;
    esac
done

project=$(pwd);

directory=~/.DeepSpliceDetectors
mkdir -p "$directory"

sha="$directory/logs.sha256"
cp ./logs.sha256 "$directory"

cd "$directory" || exit

output="$directory/logs.tar.gz"
if ! shasum --quiet --status -a 256 -c "$sha"; then
  curl -sL -o $output "https://drive.google.com/uc?export=download&id=1aPcXoVQEezFP_SsvEkX9XiDxhPXI5vmO"
fi

cd "$project" || exit

if tar -xf $output -C ./; then
  echo "Done!"
else
  echo "Something went wrong! Try again."
fi
