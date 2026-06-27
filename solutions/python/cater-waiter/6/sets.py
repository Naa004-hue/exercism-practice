"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`."""
    de_duped_ing=set(dish_ingredients)
    final=(dish_name,de_duped_ing)
    return final

def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name"""
    if set(ALCOHOLS) & set(drink_ingredients) :
        return drink_name + ' ' + 'Cocktail'
    if not set(ALCOHOLS) & set(drink_ingredients):
        return drink_name + ' ' + 'Mocktail'
    return drink_name + ': ' + 'UNKNOWN'

def categorize_dish(dish_name, dish_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name""" 
    if dish_ingredients.issubset(VEGAN): 
        return dish_name + ': ' + 'VEGAN' 
    if dish_ingredients.issubset(VEGETARIAN):
        return dish_name + ': ' + 'VEGETARIAN' 
    if dish_ingredients.issubset(PALEO) :
        return dish_name + ': ' + 'PALEO' 
    if dish_ingredients.issubset(KETO) :
        return dish_name + ': ' + 'KETO' 
    if dish_ingredients.issubset(OMNIVORE):
        return dish_name + ': ' + 'OMNIVORE' 
    return dish_name + ': ' + 'UNKNOWN'
        
def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`."""
    name , ingrd = dish 
    special = set(ingrd) & SPECIAL_INGREDIENTS
    return (name,special)

def compile_ingredients(dishes):
    """Create a master list of ingredients"""
    return set.union(*dishes)
    
def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them."""
    return list( set(dishes) - set(appetizers))
    
def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient"""
    return set.union(*dishes)-intersection
