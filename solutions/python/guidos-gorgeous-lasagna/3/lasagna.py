EXPECTED_BAKE_TIME=40
def bake_time_remaining(elapsed_bake_time):
    """Calculate the elapsed cooking time."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """each layer takes two minute"""
    return number_of_layers*2
    
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """every thing together basically"""
    return (number_of_layers*2)+elapsed_bake_time