#!/bin/bash

while true; do
    read -p "Warning! This code might override the data in logs directory. Continue? (y/N)? " yn
    case $yn in
        [Yy]* ) break;;
        * ) echo "Aborted!."; exit;;
    esac
done

directory=~/.DeepSpliceDetectors
mkdir -p "$directory"

output="$directory/logs.tar.gz"
if ! [ -f $output ]; then
  curl -sL -o $output "https://drive.google.com/uc?export=download&id=1aPcXoVQEezFP_SsvEkX9XiDxhPXI5vmO"
fi

tar -xf $output -C ./
echo "Done!"
