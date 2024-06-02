from time import sleep

index = []
inv = []
craftlist = []

def indexing(item_index, indexed_item):
    global index
    index.insert(item_index, indexed_item)


def farm(name, index, farmed):
    global inv
    invhelper = [name, 0]
    if farming == str(index):
        print('Farming ' + name + '...')
        if invhelper not in inv:
            inv.append([name, 0])
        if invhelper in inv:
            inv[index - 1][1] += farmed
        if [name, 0] in inv:
            inv.pop(-1)
        print('Done!\n')

        print(inv)


def craft(name, index, crafted, reqs):
    global craftlist
    craftlisthelper = [name, 0]
    if crafting == str(index):
        print('Crafting ' + name + '...')
        if craftlisthelper not in craftlist:
            craftlist.append([name, 0])
        if craftlisthelper in craftlist and reqs[0][0] in inv:
            craftlist[index - 1][1] += crafted


        if [name, 0] in craftlist:
            craftlist.pop(-1)
        print('Done!\n')

        print(craftlist)


name = input('Your Factories name: ')
print(name + " Factory")
print('\n')
while True:
    print('1. Craft')
    print('2. Farm')
    print('3. Inventory')
    option = input('Option: ')
    print('\n')
    if option == '1':
        print('1. Planks')
        crafting = input('Crafting: ')
        print('\n')
        craft('Planks', 1, 4, [('wood', 1)])
        craft('Furnace', 2, 1, [('stone', 8)])

    if option == '2':
        print('1. Wood')
        print('2. Stone')
        farming = input('Farm: ')
        print('\n')
        farm('wood', 1, 1)
        farm('stone', 2, 1)

    if option == '3':
        for i in range(len(inv)):
            print(str(inv[i][0]).upper() + ': ' + str(inv[i][1]))
        sleep(0.5)
        print('\n')
