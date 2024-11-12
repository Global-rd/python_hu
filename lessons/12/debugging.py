from cart_processor import process_cart_items


def main() -> None:

    shopping_cart = {
        "Alice": [10, 5, 6, 7, 4],
        "Bob": [1, 4, 6],
        "Jimmy": [10, 6, 6, 8, 4],
    }

    for customer, prices in shopping_cart.items():
        process_cart_items(customer, prices)


if __name__ == "__main__":
    main()


