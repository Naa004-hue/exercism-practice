color_band = {
    'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
    'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'
}
tolerance_band = {
    'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%', 'green': '0.5%',
    'brown': '1%', 'red': '2%', 'gold': '5%', 'silver': '10%'
}

def resistor_label(colors):
    if len(colors) == 1:
        return color_band[colors[0]] + ' ohms'
    
    first = int(''.join([color_band[colors[0]], color_band[colors[1]]]))
    
    if len(colors) == 2:
        return str(first)
    
    new_r = first * (10 ** int(color_band[colors[2]]))
    
    if len(colors) == 3:
        return str(new_r) + ' ohms'
    
    if len(colors) == 4 :
        triple = tolerance_band[colors[3]]
        if new_r < 1000 :
            return str(new_r) + ' ohms'+ ' ' + '±' + triple 
        if new_r >= 1000000: 
            return str(new_r // 1000000) + ' megaohms' + ' ' + '±' + triple
        else: 
            return  str(new_r / 1000).rstrip('0').rstrip('.') + ' kiloohms' + ' ' + '±' + triple
        
    if len(colors) == 5 and colors[4] in tolerance_band:
        triple = tolerance_band[colors[4]]
        for_five = (int(''.join([color_band[colors[0]], color_band[colors[1]], color_band[colors[2]]])))* (10 ** int(color_band[colors[3]]))
        if for_five < 1000:
            return str(for_five) + ' ohms' + ' ' + '±' + triple
        if for_five >= 1000000:
            return str(for_five / 1000000) + ' megaohms' + ' ' + '±' + triple
        else:
            return str(for_five / 1000) + ' kiloohms' + ' ' + '±' + triple
        



        
