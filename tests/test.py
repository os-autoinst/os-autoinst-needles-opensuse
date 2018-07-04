#!/usr/bin/python3

import os
import sys
import re
import json

scriptdir = os.path.dirname(os.path.realpath(__file__))
needledir = os.path.join(scriptdir, "..")

returncode = 0

def error(msg):
    global returncode
    returncode = 1
    print(msg, file=sys.stderr)

# Get all needles
needles = set()
for f in os.listdir(needledir):
    if f.endswith('.json') or f.endswith('.png'):
        needle, ext = f.rsplit('.', 1)
        needles.add(needle)

# Check for missing parts
for needle in sorted(needles):
    jsonfile = os.path.join(needledir, needle + '.json')
    pngfile = os.path.join(needledir, needle + '.png')

    # Check for file existence
    if not os.path.isfile(jsonfile):
        error("Needle '{}' is missing its JSON file!".format(needle))
        continue # parsing the json makes no sense

    if not os.path.isfile(pngfile):
        error("Needle '{}' is missing its PNG file!".format(needle))

    # Check JSON content
    n = {}
    with open(jsonfile) as f:
        n = json.load(f)

    # Check if workaround tag exists if bugref is in name
    if 'workaround' in n.get('properties', '') and not re.search(r'(poo|bsc|bnc|boo)#?[0-9]+', needle):
        error("Needle '{}' includes a workaround tag but has no bug-ID in filename!".format(needle))

sys.exit(returncode)
