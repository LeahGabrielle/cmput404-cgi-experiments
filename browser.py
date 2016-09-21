#!/usr/bin/env python

import os


user_agent = os.environ['HTTP_USER_AGENT']

print "Content-Type: text/html"


print
print "<h1>Hello, World!</h1>"

if 'Chrome' in user_agent:
    print "You're using Chrome!"
elif 'Firefox' in user_agent:
    print "You're using Firefox!"
else:
    print "I don't know what you're using"
