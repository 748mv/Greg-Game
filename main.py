index = []
craftlist = []
allowed = True

def indexingres(item_index, indexed_item):
    global index
    index.insert(item_index, indexed_item)

indexingres(1, ['Wood', 0])
indexingres(2, ['Stone', 0])

def indexingcraft(item_index, indexed_item):
    global craftlist
    craftlist.insert(item_index, indexed_item)


indexingcraft(1, ['Planks', 0])
indexingcraft(2, ['Furnace', 0])

print(index, craftlist)
def farm(id, farmed, name = None):
    global index
    if farming == str(id):
        print('Farming ' + index[id - 1][0] + '...')
        index[id - 1][1] += farmed
        print('Done!\n')
        print(index)


def craft(name, item_index, craftid, crafted, reqs):
    global craftlist, index, allowed
    if crafting == str(craftid):
        print('Crafting ' + craftlist[item_index - 1][0] + '...')
        craftlist[item_index - 1][1] += crafted
        for reqs[0:len(reqs) - 1] in mixedlist[0:2]:
            if allowed:
                index[1][1] -= 8
                allowed = False
        print('Done!\n')
        print(craftlist)
        allowed = True



while True:
    craftindexstart = len(index)
    mixedlist = [index, craftlist]
    print(mixedlist)
    print('1. Craft')
    print('2. Farm')
    print('3. Inventory')
    option = input('Option: ')
    print('\n')

    if option == '1':
        print('1. Planks')
        print('2. Furnace')
        crafting = input('Crafting: ')
        print('\n')
        craft('Planks', 1, 1, 4, [('Wood', 1)])
        craft('Furnace', 2, 2, 1, [('Stone', 8)])

    if option == '2':
        print('1. Wood')
        print('2. Stone')
        farming = input('Farm: ')
        print('\n')
        farm(1, 1, 'Wood')
        farm(2, 1, 'Stone')

    if option == '3':
        print('1. Resources')
        print('2. Craftables')
        inventory = input('# ')
        print('\n')
        if inventory == '1':
            for i in range(len(index)):
                print(str(index[i][0]).upper() + ': ' + str(index[i][1]))

        if inventory == '2':
            for i in range(len(craftlist)):
                print(str(craftlist[i][0]).upper() + ': ' + str(craftlist[i][1]))

        print('\n')
