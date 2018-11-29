#!/usr/bin/env python3

import sys
import os

def split(p: str):
    f = open(p, 'r', encoding='cp932')
    content = f.read()
    f.close()

    channels = [v.replace('\t', ',') for v in content.split('\n\n')]

    for c in channels:
        lines = c.split('\n')
        if not lines[0].startswith('[LC Chromatogram(Detector '):
            continue

        for i,l in enumerate(lines):
            lines[i] = '#' + l
            if l.startswith('R.Time'):
                break

        suffix = lines[0][2:-1].replace('LC Chromatogram(Detector ', '').replace(')', '')
        base, ext = os.path.splitext(p)

        f = open(base + '_' + suffix + ext, 'w')
        f.write('\n'.join(lines))
        f.close()

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        split(arg)

