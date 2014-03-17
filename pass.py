#!/bin/python

import os, sys
from hashlib import sha1
from getpass import getpass
import argparse

SUFFIX = '$#' # Additional punctuation to avoid dumb bruteforcer

# Capitalize first alphabet
def cap_first(pwd):
    new_pwd = []
    caps = False
    for s in pwd:
        new_pwd.append(s if s.isdigit() or caps else s.upper())
        if not s.isdigit(): caps = True
    return ''.join(new_pwd)

# Default salt is stored in home dir
# Create if not exists
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
parser.add_argument('-n', '--new', 
        help="Confirmation mode (good when you're creating a new password)", action='store_true')
parser.add_argument('-s', '--salt', help='Custom salt', action='store_true')
parser.add_argument('-l', '--length', help='Set final length of the password', type=int)
parser.add_argument('-o', '--out', help='Output generated pass', action='store_true')
args = parser.parse_args()

length = args.length - 1 if args.length else 9999
if not args.salt:
    salt = get_salt()
else:
    salt = getpass("Enter salt: ")

p = getpass("Enter your phrase: ")

if args.new:
    confirm = getpass("Confirm your phrase: ")
    if p != confirm:
        sys.stdout.write("Phrase not matched!\n")
        exit()

p = '%s%s' % (p, salt)
p = sha1(p).hexdigest()
p = p[:length - len(SUFFIX)]
p = '%s%s' % (p, SUFFIX)
p = cap_first(p)

clip = os.popen('pbcopy', 'w')
clip.write(p)
clip.close()

if args.out: print p
