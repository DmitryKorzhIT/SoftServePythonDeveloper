# Shows the time (sorted by minutes) with the highest amount of requests.
awk -F':' '{print $2 ":" $3}' < $1 | uniq -c | sort -gr | head -1
