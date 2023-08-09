#!/bin/bash
awk -F~ '{print $2 " once said, \042" substr($1, 1, length($1)-2) "\042."}' quotes.txt
