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
  curl -sL -o "$logs.aa" "https://drive.google.com/uc?export=download&id=1aKYip4pDWI9S0hIhKwhgCLmDqZ-wpZBf"
  curl -sL -o "$logs.ab" "https://drive.google.com/uc?export=download&id=1SX0tU6g_YaiUSr2Vg-mpZPKYlUKVDAoW"
  curl -sL -o "$logs.ac" "https://drive.google.com/uc?export=download&id=1_EvwAzF5A5LBH3bY1CIAhQb_UCXqbf6H"
fi

cd "$project" || exit

cat "$logs.aa" "$logs.ab" "$logs.ac" > $logs

if tar -xf $logs -C ./; then
  echo "Done!"
else
  echo "Something went wrong! Try again."
fi
