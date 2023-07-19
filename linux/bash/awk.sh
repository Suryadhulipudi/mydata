#Average
awk '{sum += $1} END {print "Sum:", sum; print "Average:", sum/NR}' numbers.txt

#Counting Occurrences of Unique Values
awk '{count[$1]++} END {for (val in count) print val, count[val]}' input.txt
