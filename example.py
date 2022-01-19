from py3dbp import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('Container', 100, 100, 100, 100))

packer.add_item(Item('50g [powder 1]', 20, 20, 20, 50))
packer.add_item(Item('50g [powder 2]', 20, 20, 20, 10))
packer.add_item(Item('50g [powder 3]', 100, 20, 20, 10))

packer.pack()

for b in packer.bins:
    print(":::::::::::", b.string())

    print("FITTED ITEMS:")
    for item in b.items:
        print("====> ", item.string())

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    print("***************************************************")
    print("***************************************************")

# for item in packer.bins[0].items:
#     print(item.position)

