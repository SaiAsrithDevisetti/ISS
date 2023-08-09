#!/bin/bash
read file
a=$(wc -c $file)
echo $a
a=$(wc -l $file)
echo "$a"
a=$(wc -w $file)
echo $a
awk '{print NR, NF}' $file
sort $file | uniq -c | sort -nr | while read count word
do
   if [ ${count} -gt 1 ]
   then
     echo "${word} : ${count}"
   fi
done

