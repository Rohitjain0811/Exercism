def is_valid(isbn:str):
    isbn = isbn.replace('-','')
    isbn_list = [i for i in isbn]
    
    if len(isbn_list) != 10:
        return False

    if isbn_list[-1] == 'X':
        isbn_list[-1] = 10
  
    try:
        isbn_list = [int(i) for i in isbn_list]

    except ValueError:
        return False

    check = 0

    for i in range(10):
        k = isbn_list[i] * (10 - i)
        check += k

    return check % 11 == 0