# Shows the names of bots that meets in the log file.
awk -F'"' '{print $6}' < $1 | grep -o "\w*bot\w*" | sort | uniq | sort -gr
