#!/bin/python

import os, sys
from hashlib import sha1
from getpass import getpass
import argparse

SUFFIX = '$#'

def cap_first(pwd):
    new_pwd = []
    caps = False
    for s in pwd:
        new_pwd.append(s if s.isdigit() or caps else s.upper())
        if not s.isdigit(): caps = True
    return ''.join(new_pwd)

def get_salt():
    filename = '%s/.saltpass' % os.path.expanduser('~')
    try:
        open(filename, 'r')
    except IOError:
        sys.stdout.write("No default salt specified in %s, specify first.\n" % filename)
        salt = getpass('New default salt: ')
        f = open(filename, 'w').write(salt)

    f = open(filename, 'r')
    for s in f: return s


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--new', help='Generate-mode', action='store_true')
parser.add_argument('-s', '--salt', help='Custom salt')
parser.add_argument('-l', '--length', help='Set final length', type=int)
parser.add_argument('-o', '--out', help='Output generated pass', action='store_true')

args = parser.parse_args()

salt = args.salt if args.salt else get_salt()
length = args.length - 1 if args.length else 9999

p = getpass()
if args.new:
    confirm = getpass()
    if p != confirm:
        sys.stdout.write("Password not matched!\n")
        exit()

p = '%s%s' % (p, salt)
p = sha1(p).hexdigest()

p = p[:length - len(SUFFIX)]

p = '%s%s' % (p, SUFFIX)

#uppercase_length = 8
#p = "%s%s" % (p[:uppercase_length].upper(), p[uppercase_length:])

p = cap_first(p)

clip = os.popen('pbcopy', 'w')
clip.write(p)
clip.close()

if args.out:
    print p
