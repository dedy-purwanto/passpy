#!/bin/python

import os, sys
from hashlib import sha1
from getpass import getpass

SALT = 'abdul'
suffix = '$#'
uppercase_length = 8

p = getpass()
confirm = getpass()

if p == confirm:
    p = '%s%s' % (p, SALT)
    p = sha1(p).hexdigest()
    p = '%s%s' % (p, suffix)


    p = "%s%s" % (p[:uppercase_length].upper(), p[uppercase_length:])
    clip = os.popen('pbcopy', 'w')
    clip.write(p)
    clip.close()

    sys.stdout.write("Show? [yes/NO] : ")
    if raw_input().lower() == 'yes':
        print p
else:
    print "Not matched, try again."
