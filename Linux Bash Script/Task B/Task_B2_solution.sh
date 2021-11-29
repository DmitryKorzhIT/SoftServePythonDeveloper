# Make a file with only website domains.
awk -F'"' '{print $2}' $1 | awk -F" " '{print $2}' > apache_logs2.txt

# Get the most frequent website domain.
sort apache_logs2.txt| uniq -c | sort -gr | head -1

# Remove temporary created file apache_logs2.txt.
rm apache_logs2.txt
