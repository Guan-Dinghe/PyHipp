#!/bin/bash

echo "Number of hkl files"
find . -name "*.hkl" | grep -v -e spiketrain -e mountains | wc -l

echo "Number of mda files"
find mountains -name "firings.mda" | wc -l

echo "#==========================================================="

echo "Start Times"
for file in rpl*pl-slurm*.out; do
    echo "==> $file <=="
    grep -e "time.struct_time" $file | head -n 1
done

# Extract and display end times
echo "End Times"
for file in rpl*pl-slurm*.out; do
    echo "==> $file <=="
    tail -n 5 $file
done

echo "#==========================================================="
