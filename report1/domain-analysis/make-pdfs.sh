#!/bin/zsh

for im in *.svg ; do
    convert "$im" "$(basename $im .svg).pdf"
done

