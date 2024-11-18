'''QUESTION 1'''
def calculate_discount(price, discount_percent):    
    if discount_percent >= 20:
        divide_discount = discount_percent / 100
        multiply_discount = divide_discount * price
        total_discount = price - multiply_discount
        print( f'{discount_percent}% added \nPrice payment is: {total_discount}')
    else:
        print(f'{discount_percent}% below discount!!\nPrice payment is: {price}')


'''QUESTION 2'''
def calculate_discount():
    price = float(input('Enter price: '))
    discount_percent = float(input('Enter discount: '))
    
    if discount_percent >= 20:
        divide_discount = discount_percent / 100
        multiply_discount = divide_discount * price
        total_discount = price - multiply_discount
        print( f'{discount_percent}% added \nPrice payment is: {total_discount}')
    else:
        print(f'{discount_percent}% below discount!!\nPrice payment is: {price}')

