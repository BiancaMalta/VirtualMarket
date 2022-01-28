from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import format_str_currency

products: List[Product] = []
shopping_cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('==============================')
    print('========== Welcome ===========')
    print('========== Bia Shop ==========')
    print('==============================')

    print('Select an option below: ')
    print('1 - Register product')
    print('2 - List product')
    print('3 - Buy product')
    print('4 - View shopping cart ')
    print('5 - Checkout')
    print('6 - Exit')

    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_product()
    elif option == 3:
        buy_product()
    elif option == 4:
        view_shopping_cart()
    elif option == 5:
        checkout()
    elif option == 6:
        print('Thank you and welcome back!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option.')
        sleep(1)
        menu()


def register_product() -> None:
    print('Register of Product')
    print('===================')

    name: str = input('Enter the product name: ')
    price: float = float(input('Enter the price of the product: '))

    product: Product = Product(name, price)

    products.append(product)

    print(f'The product{product.name} was successfully registered!')
    sleep(2)
    menu()


def list_product() -> None:
    if len(products) > 0:
        print('List of products')
        print('================')
        for product in products:
            print(product)
            print('------------------')
            sleep(1)
            menu()
    else:
        print('There are no registered products yet.')
        sleep(2)
        menu()


def buy_product() -> None:
    if len(products) > 0:
        print('Enter the code of the product you want to add to cart')
        print('------------------------------------------------------------')
        print('===================== Available Products ===================')
        for product in products:
            print(product)
            print('------------------------------------------------------------')
            sleep(1)
        code: int = int(input())

        product: Product = get_product_by_code(code)

        if product:
            if len(shopping_cart) > 0:
                has_in_shopping_cart: bool = False
                for item in shopping_cart:
                    amount: int = item.get(product)
                    if amount:
                        item[product] = amount + 1
                        print(f'Product {product.name} now has {amount + 1} units in cart')
                        has_in_shopping_cart = True
                        sleep(2)
                        menu()
                if not has_in_shopping_cart:
                    prod = {product: 1}
                    shopping_cart.append(prod)
                    print(f'The product {product.name} has been added to cart.')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                shopping_cart.append(item)
                print(f'The product{product.name} has been added to the cart.')
            sleep(2)
            menu()
        else:
            print(f'The product with code {code} was not found.')
            sleep(2)
            menu()

    else:
        print('There are no products to sell yet.')
        sleep(2)
        menu()


def view_shopping_cart() -> None:
    if len(shopping_cart) > 0:
        print('Products in cart: ')

        for item in shopping_cart:
            for data in item.items():
                print(data[0])
                print(f'Amount: {data[1]}')
                print('----------------------')
                sleep(1)
                menu()
    else:
        print('There are no products in the cart yet.')
        sleep(2)
        menu()


def checkout() -> None:
    if len(shopping_cart) > 0:
        total_value: float = 0

        print('Products in Cart')
        for item in shopping_cart:
            for data in item.items():
                print(data[0])
                print(f'Amount: {data[1]}')
                total_value += data[0].price * data[1]
                print('------------------------')
                sleep(1)
        print(f'Your invoice is {format_str_currency(total_value)}')
        print('Thank you and welcome back!')
        shopping_cart.clear()
        sleep(5)
    else:
        print('There are no products in the cart yet.')
        sleep(2)
        menu()


def get_product_by_code(code: int) -> Product:
    p: Product = None
    for product in products:
        if product.code == code:
            p = product
    return p


if __name__ == '__main__':
    main()
