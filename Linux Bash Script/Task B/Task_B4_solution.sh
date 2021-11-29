# Shows only links on pages with "error404".
grep error404 < $1 | awk -F' ' '{print $15}' | uniq
