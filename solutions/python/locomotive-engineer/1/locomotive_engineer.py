"""Functions which helps the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*args):
    """Return a list of wagons."""
    wagons=list(args)
    return wagons

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons."""
    wagon_a , wagon_b , the_loco , *the_rest = each_wagons_id
    ordred= [the_loco,*missing_wagons,*the_rest, wagon_a,wagon_b] 
    return ordred
    
def add_missing_stops(*args,**kwargs):
    """Add missing stops to route dict."""
    route=args[0]
    if len(args)> 1:
        stops={ "stops" : list(args[1].values())}
    else:
        stops={ "stops" : list(kwargs.values())}
    hi_wag={**route, **stops}
    return hi_wag
    
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information."""
    consolidate={**route, **more_route_information}
    return consolidate

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons."""
    [first,second,third] = wagons_rows
    correct=[[first[0],second[0],third[0]],[first[1],second[1],third[1]],[first[2],second[2],third[2]]]
    return correct

    
 