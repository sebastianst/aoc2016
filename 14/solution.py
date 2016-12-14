#!/usr/bin/env python
from hashlib import md5
from binascii import hexlify
inp, hazh = 'ahsbgdzn', []

def get_hash(idx):
    global hazh
    # We assert here that hashes are incrementally accessed
    if len(hazh) == idx:
        hazh.append(hexlify( md5((inp + str(idx)).encode()).digest() ).decode())
    return hazh[idx]

def is_key(idx):
    # Find first triplet
    h, t = get_hash(idx), ''
    for i in range(len(h)-2):
        if h[i] == h[i+1] == h[i+2]:
            t = h[i]
            break
    if not t: return False
    # Check following 1000 hashes
    for i in range(idx+1,idx+1001):
        if 5*t in get_hash(i): return True

    return False

ki, idx = 0, -1
while ki < 64:
    idx += 1
    ki += is_key(idx)

print(idx)
