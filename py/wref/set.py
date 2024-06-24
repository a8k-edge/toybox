import weakref

class DataItem:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"DataItem({self.data})"

large_collection = [DataItem(i) for i in range(1000)]
weak_collection = weakref.WeakSet(large_collection)

print(len(weak_collection))
del large_collection[0]
print(len(weak_collection))
del large_collection
print(len(weak_collection))
