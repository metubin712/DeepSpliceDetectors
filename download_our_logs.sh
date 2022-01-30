#!/bin/bash

while true; do
    read -p "Warning! This code might override the data in logs directory. Continue? (y/N)? " yn
    case $yn in
        [Yy]* ) break;;
        * ) echo "Nothing to do!"; exit;;
    esac
done

project=$(pwd);

directory=~/.DeepSpliceDetectors
mkdir -p "$directory"

sha="$directory/logs.sha256"
cp ./logs.sha256 "$directory"

cd "$directory" || exit

logs="$directory/logs.tar.gz"
if ! shasum --quiet --status -a 256 -c "$sha"; then
  curl -sL -o "$logs.aa" "https://drive.google.com/uc?export=download&id=1kU01Y3ckixYvTHY_1rCXNoPLjWlCRdCN"
  curl -sL -o "$logs.ab" "https://drive.google.com/uc?export=download&id=10rcIiU120X85XJxfM16vEYguQYTAIxFH"
  curl -sL -o "$logs.ac" "https://drive.google.com/uc?export=download&id=1-lFz1Z3x_fQFtMcJf7yQn9qBWx2kqxra"
fi

cd "$project" || exit

cat "$logs.aa" "$logs.ab" "$logs.ac" > $logs

if tar -xf $logs -C ./; then
  echo "Done!"
else
  echo "Something went wrong! Try again."
fi
