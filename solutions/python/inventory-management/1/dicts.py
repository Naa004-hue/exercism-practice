"""Functions to keep track and alter inventory."""

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list."""
    tracking={}
    for element in items :
        quantity=items.count(element)
        tracking[element]=quantity
    return tracking

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`."""
    for item in items :
        inventory[item]=inventory.get(item,0)+1
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list."""
    tracker=create_inventory(items)
    for key in tracker:
        if key in inventory:
            value=inventory[key]-tracker[key]
            if value>=0:
                inventory[key]=value
            else:
                inventory[key]=0
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string."""
    inventory.pop(item,None)
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs """
    new_list=list(inventory.items())
    for key,value in new_list :
        if value == 0:
            new_list.remove((key,value))
    return new_list

