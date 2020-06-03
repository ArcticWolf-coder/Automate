#!/bin/bash


> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

for file in $files; do
if test -e ~/$file; then echo /home/student-03-631478850cbd/$file  >> oldFiles.txt; fi
done;
