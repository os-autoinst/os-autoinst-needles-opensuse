#!/usr/bin/python3

import os
import pytest
import re
import json

scriptdir = os.path.dirname(os.path.realpath(__file__))
needledir = os.path.join(scriptdir, "..")

# Get all needles
needles = set()
for f in os.listdir(needledir):
    if f.endswith('.json') or f.endswith('.png'):
        needle, ext = f.rsplit('.', 1)
        needles.add(needle)


def test_missing_parts():
    for needle in sorted(needles):
        jsonfile = os.path.join(needledir, needle + '.json')
        pngfile = os.path.join(needledir, needle + '.png')

        # Check for file existence
        assert os.path.isfile(jsonfile), "Needle '{}' is missing its JSON file!".format(needle)
        assert os.path.isfile(pngfile), "Needle '{}' is missing its PNG file!".format(needle)

        # Check JSON content
        n = {}
        with open(jsonfile) as f:
            n = json.load(f)
            assert n

        # Check if workaround tag exists if bugref is in name
        if 'workaround' in n.get('properties', ''):
            assert re.search(r'(poo|bsc|bnc|boo)#?[0-9]+', needle), "Needle '{}' includes a workaround tag but has no bug-ID in filename!".format(needle)
