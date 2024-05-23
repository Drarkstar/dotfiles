#!/bin/bash
echo 'scale=1000; e(1)' | bc -l > neper.txt
for i in {2..100}; do if [ $(dd if=neper.txt bs=1 count=10 skip=$i 2>/dev/null | factor | wc -w) = 2 ]; then dd if=neper.txt of=bstxt$i.txt bs=1 count=10 skip=$i 2>/dev/null; fi; done
rm neper.txt
