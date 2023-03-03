from main import Product

products = Product.select()

for Product in products:
    print(Product.prod_price, Product.prod_quantity, Product.prod_colour)
