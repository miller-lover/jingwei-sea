# serialization
entry = {}
entry['title'] = 'Dive into history, 2009 edition'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True

import time
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')

import pickle
with open('entry.pickle', 'wb') as f:
    pickle.dump(entry, f)

# deserialization
with open('entry.pickle', 'rb') as f:
    entry_read = pickle.load(f)

print(entry_read)

# pickling without a file
b = pickle.dumps(entry)
entry_read = pickle.loads(b)
print(entry == entry_read)

# DEBUGGING PICKLE FILES
import pickletools
with open('entry.pickle', 'rb') as f:
    pickletools.dis(f)

def protocol_version(file_object):
    maxproto = -1
    for opcode, arg, pos in pickletools.genops(file_object):
        maxproto = max(maxproto, opcode.proto)
    return maxproto

with open('entry.pickle', 'rb') as f:
    v = protocol_version(f)
    print(v)
