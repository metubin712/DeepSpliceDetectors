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
  curl -sL -o "$logs.minamin00" "https://drive.google.com/uc?export=download&id=1Tvyztq6S3mSZtX1lSianjg6md7FUjSzH"
  curl -sL -o "$logs.minamin01" "https://drive.google.com/uc?export=download&id=1KvIFfnj2-q0_UlAfqMDjhXup8wl7s9M4"
  curl -sL -o "$logs.minamin02" "https://drive.google.com/uc?export=download&id=13CjR6ERZuf8BLMjeY1POdEDdWSkqfOoZ"
  curl -sL -o "$logs.minamin03" "https://drive.google.com/uc?export=download&id=1eztQa_oAZAXiV5AQmKBwuKPD8XMLcVJ2"
  curl -sL -o "$logs.minamin04" "https://drive.google.com/uc?export=download&id=1JbVt2DHMZJwUyxPvkvHaCcgv8VbSuDYy"
  curl -sL -o "$logs.minamin05" "https://drive.google.com/uc?export=download&id=1Deqssgyk0fQYqC6k3c4PHPjznsmccI-s"
  curl -sL -o "$logs.minamin06" "https://drive.google.com/uc?export=download&id=1x-USPQbwWiJCmNp-lF4KIwupLF4rZEpO"
  curl -sL -o "$logs.minamin07" "https://drive.google.com/uc?export=download&id=17eKff_4DdKr1uRusk67G-oZpO-geVQYN"
  curl -sL -o "$logs.minamin08" "https://drive.google.com/uc?export=download&id=1RhWwowMvgtT6RJqtSl2jIwvraky4d_wJ"
  curl -sL -o "$logs.minamin09" "https://drive.google.com/uc?export=download&id=1wXHUFD0NKkPZeFm_FUksR-EjWxXsfkU1"
  curl -sL -o "$logs.minamin10" "https://drive.google.com/uc?export=download&id=1E4LFbK3KI1SbHoev1S-8gG8ddzp1GaFN"
  curl -sL -o "$logs.minamin11" "https://drive.google.com/uc?export=download&id=1bfL9WbP5WDprw9gwtoPHinn0h88PGNAA"
fi

cd "$project" || exit

cat "$logs".minamin* > $logs

if tar -xf $logs -C ./; then
  echo "Done!"
else
  echo "Something went wrong! Try again."
fi
