def line_up(name, number):
    if number % 10 == 1:
        ord_str = 'st'
    elif number % 10 == 2:
        ord_str = 'nd'
    elif number % 10 == 3:
        ord_str = 'rd'
    else: ord_str = 'th'    
    
    if number % 100 in (11, 12, 13):
        ord_str = 'th'    

    return f'{name}, you are the {number}{ord_str} customer we serve today. Thank you!'
