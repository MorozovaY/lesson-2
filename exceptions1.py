def discounted(price, discount, max_discount):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
        print(price + discount + max_discount)
    except (ValueError, TypeError):
        print("Некорректные аргументы")
    
discounted(1, 1, 1)
discounted('привет', 1, 1)