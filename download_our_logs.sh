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
  # https://drive.google.com/uc?export=download&id=[ID]
  curl -sL -o "$logs.minamin00" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin00"
  curl -sL -o "$logs.minamin01" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin01"
  curl -sL -o "$logs.minamin02" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin02"
  curl -sL -o "$logs.minamin03" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin03"
  curl -sL -o "$logs.minamin04" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin04"
  curl -sL -o "$logs.minamin05" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin05"
  curl -sL -o "$logs.minamin06" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin06"
  curl -sL -o "$logs.minamin07" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin07"
  curl -sL -o "$logs.minamin08" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin08"
  curl -sL -o "$logs.minamin09" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin09"
  curl -sL -o "$logs.minamin10" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin10"
  curl -sL -o "$logs.minamin11" "https://cloud.aminzabardast.com/dsd/logs.tar.gz.minamin11"
fi

cd "$project" || exit

cat "$logs".minamin* > $logs

if tar -xf $logs -C ./; then
  echo "Done!"
else
  echo "Something went wrong! Try again."
fi
