def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature<800 and neutrons_emitted>500 and temperature*neutrons_emitted<500000
def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = ((voltage * current )/theoretical_max_power)*100
    if efficiency>=80:
        return "green"
    elif 60<=efficiency<80:
        return "orange"
    elif 30<=efficiency<60:
        return "red"
    elif efficiency<30:
        return "black"
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature * neutrons_produced_per_second < 0.9*threshold:
        return "LOW"
    elif 0.9 * threshold<=temperature * neutrons_produced_per_second<=1.1 *threshold :
        return "NORMAL"
    else:
        return "DANGER"
        
   