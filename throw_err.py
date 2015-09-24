#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument
import os
import sys

def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision\n")
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
    assert 2*4==12
elif error_type == "io":
    open("aintnuthinhere")
elif error_type == "import":
    import asdfghjkl;
elif error_type == "index":
    swoop = "shmoop"
    boop = swoop[42]
elif error_type == "key":
    shmoop = {"x" : 1, "y" : 2}
    print shmoop[42]
elif error_type == "name":
    assert boop(bloop) == nope
elif error_type == "os":
    for i in range(42):
        print i, os.ttyname(i)
elif error_type == "type":
    print "whaaaat"^2
elif error_type == "value":
    print(int("whyyyyyyyyyyyyyyyyyyyy"))
elif error_type == "zerodivision":
    print 42/0 
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
