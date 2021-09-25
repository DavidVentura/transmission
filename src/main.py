import pyotherside
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))

vendored = os.path.join(here, '..', 'vendored')
sys.path.insert(0, vendored)

from transmission_rpc import Client

def m():
    c = Client(protocol='https', host='a', port=443)
    for t in c.get_torrents():
        print(t, flush=True)
        pyotherside.send('add', [t.id, "adr", t.name, t.status, t.status, "_down", 0])
