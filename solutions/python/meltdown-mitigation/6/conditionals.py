"""Functions to prevent a nuclear meltdown."""
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced"""
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone"""
    eff = ((voltage*current)/theoretical_max_power)
    if  eff >= 0.8 :
        return 'green'
    if eff < 0.8 and eff >= 0.6 :
        return 'orange'
    if eff < 0.6 and eff >= 0.3 :
        return 'red'
    return 'black'
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor """
    t_n = temperature*neutrons_produced_per_second 
    if t_n < (threshold*0.9) :
        return 'LOW'
    if t_n <= (threshold*1.1 ):
        return 'NORMAL'
    return 'DANGER'