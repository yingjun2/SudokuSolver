#!/usr/bin/python3.6
 
print('Content-Type: text/html\n\n')
 
# The following 2 lines of code are necessary for the CGI execution
# of this script to be able to import user-installed Python modules.
# Also, it is required that the ~.local/lib and ~.local/lib/python3.6
# directories both have had permissions changed to allow world x (so 
# that the 'nobody' web server user can descend into them.  Finally
# the site-packages subdirectory must have both world read and execute
# privileges enabled.

# import sys
# sys.path.append('/home/jweible/.local/lib/python3.6/site-packages/')
 
print('<HTML><Head><Title>Example Page</Title></Head>')
print('<Body>')
 
print('<Table style="border: 2px black">')
print('<tr><th>i</th><th>i squared</th></tr>')
 
x = [1, 2, 3]
 
for i in x:
    print('<tr><td>', i, '</td><td>', i * i, '</td></tr>')
 
print('</Table>')
print('</Body></HTML>')