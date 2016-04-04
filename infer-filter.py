#!/usr/bin/env python
from itertools import islice
import re
import urllib2

SERVER = 'https://people.mozilla.org/~sledru/reports/fennec-infer/bugs.txt'
FILTERS = map(lambda s: re.compile(s), [
    '/mobile/android/tests/',
    '/mobile/android/thirdparty/',
    '/mobile/android/base/java/org/mozilla/gecko/GeckoSmsManager.java',
])


def should_filter(line):
    filtered = filter(lambda regex: regex.search(line), FILTERS)
    return len(filtered) > 0


line_iter = iter(urllib2.urlopen(SERVER))
for line in line_iter:
    if should_filter(line):
        next(line_iter)  # Skip description
        next(line_iter)  # Skip blank
    else:
        print line.replace('\n', '')
