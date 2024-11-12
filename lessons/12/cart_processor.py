def calculate_total(prices: list[int]) -> float:
    return sum(prices)



def process_cart_items(customer_name: str, prices: list[int]) -> float:

    total_price = calculate_total(prices)
    print(f"Total prices for {customer_name}: ${total_price:.2f}")
    return total_price
