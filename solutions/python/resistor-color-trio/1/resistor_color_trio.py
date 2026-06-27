color_band={'black':'0','brown':'1','red':'2','orange':'3','yellow':'4','green':'5','blue':'6','violet':'7','grey':'8','white':'9'}

def label(colors):
    result=[color_band[colors[0]],color_band[colors[1]]]
    first=int(''.join(result))
    new_r=first*(10**(int(color_band[colors[2]])))
    if new_r == 0  :
        return '0 ohms'
    if new_r % 1000000000 == 0:
        return str(new_r //  1000000000)+' '+'gigaohms'
    if new_r % 1000000 == 0:
        return str(new_r // 1000000)+' '+'megaohms'
    if new_r % 1000 == 0:
        return str(new_r // 1000)+' '+'kiloohms'
    else :
        return str(new_r)+' '+'ohms'
