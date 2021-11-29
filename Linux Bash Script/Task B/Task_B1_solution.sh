# Get the most frequent ip.
awk -F"-" '{ print $1 }' $1 | sort | uniq -c | sort -gr | head -1
