'''
Map-Reduce

Mapper

sample_dict.txt will have word to id mapping.

for every line in input file
split text and convert to array of ids using the word to id mapping file.
for every id compute minimum hash value
split the array of min hash values into multiple equally sized chunks a.k.a, bands.
 assign id to bands and emit hash of band, band-id and doc-id
Reducer

group by band-hash and band-id to get list of similar doc-ids.
'''
# lsh_mapper.py
__author__ = 'raj'

import sys
from random import randrange

word_ids = dict()
num_hashes = 10
num_per_band = 2

DEBUG = False
# a_hash and b_hash cannot be generated on the fly if running in a
# distributed env. they should be same across all nodes
a_hash = [randrange(sys.maxsize) for _ in range(0, num_hashes)]
b_hash = [randrange(sys.maxsize) for _ in range(0, num_hashes)]
if DEBUG: print(a_hash, b_hash)

def min_hash_fn(a, b, words):
    if DEBUG: print(a, b, words)
    signature = map(lambda x: word_ids.get(x), words)
    signature = filter(lambda x: x is not None, signature)
    hashes = [((a * x) + b) % len(word_ids) for x in signature]
    if DEBUG: print(hashes, min(hashes))
    return min(hashes)

def get_min_hash_row(words):
    hashes = [min_hash_fn(a, b, words) for a, b in zip(a_hash, b_hash)]
    return hashes

def get_band(l, n):
    for i in range(0, len(l), n):
        yield frozenset(l[i:i+n])

for word, wid in map(lambda x: x.split(), open("sample_dict.txt").readlines()):
    word_ids[word] = int(wid)

for doc_id, doc in enumerate(sys.stdin):
    words = doc.strip().lower().split()
    if DEBUG: print(words)

    min_hash_row = get_min_hash_row(words)
    if DEBUG: print(min_hash_row)

    banded = get_band(min_hash_row, num_per_band)
    if DEBUG: print(banded)

    for band_id, band in enumerate(banded):
        print("%d\t%d\t%d" % (band_id, hash(band), doc_id))
