from main import Product

try:
    product_price = input("Enter price \n")
    product_quantity = input("Enter quantity \n")
    product_colour = input("Enter colour \n")


    Product.create (prod_price=product_price, product_quantity=product_quantity, product_colour=product_colour)
    print("Product created successfully")
except:
    print("failed to create Product")
