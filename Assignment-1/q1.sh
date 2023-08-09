#!/bin/bash
sed -i '/^$/d' quotes.txt
awk '!seen[$0]++' quotes.txt
