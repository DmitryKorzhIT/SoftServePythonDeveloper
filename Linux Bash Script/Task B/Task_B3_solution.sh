# Get the ips with frequencies.
awk -F"-" '{ print $1 }' $1 | sort | uniq -c | sort -gr
