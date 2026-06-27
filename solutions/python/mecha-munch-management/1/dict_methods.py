"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    for item in items_to_add:
        current_cart[item]=current_cart.get(item,0)+1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry."""
    new_dict={}
    for item in notes:
        new_dict[item]=notes.count(item)
    return new_dict

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    for recipe,ingredients in recipe_updates:
        ideas[recipe]=ingredients
    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order."""
    sorting=dict(sorted(cart.items()))
    return sorting

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information."""
    news={}
    for key in cart.keys():
        if key in aisle_mapping:
            news.update({key:[cart[key],*aisle_mapping[key]]})
    new_one=dict(sorted(news.items(),reverse=True))
    return new_one
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""
    for key in fulfillment_cart.keys():
        if key in  store_inventory:
            store_inventory[key][0]-= fulfillment_cart[key][0] 
            if store_inventory[key][0]<=0:
                store_inventory[key][0]= 'Out of Stock'
    return dict(sorted(store_inventory.items()))