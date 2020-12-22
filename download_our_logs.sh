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

md5="$directory/logs.md5"
cp ./logs.md5 "$directory/logs.md5"

cd "$directory" || exit

output="$directory/logs.tar.gz"
if ! md5sum --quiet --status -c "$md5"; then
  curl -sL -o $output "https://drive.google.com/uc?export=download&id=1aPcXoVQEezFP_SsvEkX9XiDxhPXI5vmO"
fi

cd "$project" || exit

if tar -xf $output -C ./; then
  echo "Done!"
else
  echo "Something went wrong! Try again."
fi
