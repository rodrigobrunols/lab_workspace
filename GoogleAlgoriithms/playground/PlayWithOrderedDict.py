from _collections import OrderedDict

od = OrderedDict()
od["banana"] = 3
od["apple"] = 4
od["orange"] = 5

od.move_to_end("banana")
# od.popitem(last=False)
print(od)
for key in od:
    print(key)
