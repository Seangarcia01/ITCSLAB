def display(product):
    count = 1
    for name, price, stock in product:
        print(f"Product {count}: {name}, Price: ${price}, Stock: {stock}")
        count += 1

product1 = ("Laptop", 999.99, 5)
product2 = ("Smartphone", 499.5, 10)
product3 = ("Headphones", 79.99, 25)

product = (product1, product2, product3)
display(product)
