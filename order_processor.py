def calc(p, d, m, l):
    # p is price, d is discount, m is member status, l is location
    if m == 'vip':
        x = p * 0.8
    elif m == 'regular':
        x = p * 0.95
    else:
        x = p
    
    if l == 'NY':
        x = x + (x * 0.08)
    # BUG: CA tax is missing!
    
    return x