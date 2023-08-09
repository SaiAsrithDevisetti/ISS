#!/bin/bash
if(($# != 2))
then
echo Error
else
c=$(($1 * $2))
echo $c
fi
