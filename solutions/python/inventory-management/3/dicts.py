def create_inventory(items):
    track={}
    for elm in items:
        num= items.count(elm)
        track.update({elm:num})
    return track

def add_items(inventory, items):
    for item in items :
        inventory[item]=inventory.get(item,0)+1
    return inventory

def decrement_items(inventory, items):
    track=create_inventory(items)
    for k in list(inventory) :
        inventory[k]=inventory[k]-track.get(k, 0)
        if inventory[k]<0:
            inventory[k] = 0 
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item) 
    return inventory

def list_inventory(inventory):
    for k in list(inventory):
        if inventory[k]<=0 :
            inventory.pop(k)
    return list(inventory.items())