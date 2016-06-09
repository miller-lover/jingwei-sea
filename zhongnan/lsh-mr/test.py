def get_band(l, n):
    for i in range(0, len(l), n):
        print(frozenset(l[i:i+n]))
        yield frozenset(l[i:i+n])

a = [1, 0, 3, 2, 7, 0]
banded = get_band(a, 2)

for band_id, band in enumerate(banded):
    print("%d\t%s" %(band_id, band))
