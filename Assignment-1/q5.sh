#!/bin/bash
read string
echo $string|rev
strlen=${#string}
for((i=$strlen-1; i>=0; i--))
do
 subsequentstring=$(echo "${string:$i:1}" | tr "0-9a-zA-ZA" "1-9a-zA-ZA")
 reverse="$reverse$subsequentstring"
done
echo $reverse
b=$((strlen / 2))
for((i=$b-1; i>=0; i--))
do
   reve="$reve${string:$i:1}"
done
for((i=$b; i<=$strlen-1; i++))
do
   as_it_is="$as_it_is${string:$i:1}"
done
ans="$reve$as_it_is"
echo $ans

