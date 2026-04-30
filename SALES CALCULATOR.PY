# PROG101 Assignment 1 - Small Business Sales Calculator

TAX_RATE = 0.15  # 15% VAT
DISCOUNT_LIMIT = 10000  # Discount applies for sales above this amount
HIGH_DISCOUNT_RATE = 0.05
MID_DISCOUNT_LIMIT = 5000
MID_DISCOUNT_RATE = 0.02
CURRENCY = "$"

def calculate_subtotal(item_list):
    """Calculate the total price of all items before discount or tax is applied """
    subtotal = 0.0
    for item in item_list:
        item_total = item['price'] * item['quantity']
        subtotal += item_total
    return subtotal


def calculate_discount(subtotal):
    """Returns a discount based on subtotal.
    5% for orders above $10,000.
    2% for orders of $5,000 or more."""
    discount = 0.0
    if subtotal > DISCOUNT_LIMIT:
        discount = subtotal * HIGH_DISCOUNT_RATE  # 5%
    elif subtotal >= MID_DISCOUNT_LIMIT:
        discount = subtotal * MID_DISCOUNT_RATE  # 2%
    return discount


def calculate_tax(amount):
    """Returns 15% VAT tax on the given amount."""
    return amount * TAX_RATE


def print_receipt(item_list, subtotal, discount, tax, total):
    """Prints a formatted receipt showing all items,subtotal,discount,tax and final total."""
    print("\n" + "=" * 45)
    print("       KAL ENTERPRISE SALES RECEIPT")
    print("=" * 45)
    print(f"{'Item':<15} {'Qty':<5} {'Price':<10} {'Total':<10}")
    print("-" * 45)

    for item in item_list:
        item_name = item['name']
        qty = item['quantity']
        price = item['price']
        line_total = qty * price
        print(f"{item_name:<15} {qty:<5} {CURRENCY}{price:<9.2f} {CURRENCY}{line_total:<9.2f}")

    print("-" * 45)
    print(f"{'Subtotal:' :<31}   {CURRENCY}{subtotal:.2f}")
    print(f"{'Discount:' :<31}   -{CURRENCY}{discount:.2f}")
    print(f"{'Tax (15%):' :<31}  +{CURRENCY}{tax:.2f}")
    print("-" * 45)
    print(f"{'TOTAL:' :<31}     {CURRENCY}{total:.2f}")
    print("=" * 45)
    print("Thank you for shopping with us!")
    print("=" * 45 + "\n")


def main():
    """Runs the sales calculator. Collects items from the user, calculates totals and prints the receipt"""
    items = []
    print("=== Small Business Sales Calculator ===")

    while True:
        item_name = input("Enter item name (or 'end' to finish): ").strip()

        if item_name.lower() == 'end':
            if len(items) == 0:
                print("No items entered. Exiting.")
                return
            break

        try:
            price = float(input("Enter price per unit: "))
            quantity = int(input("Enter quantity: "))

            if price <= 0 or quantity <= 0:
                print("Price and quantity must be positive. Try again.\n")
                continue

        except ValueError:
            print("Invalid input. Try again.\n")
            continue

        item_record = {
            'name': item_name,
            'price': price,
            'quantity': quantity
        }

        items.append(item_record)
        print(f"Added: {quantity} x {item_name} @ {CURRENCY}{price:.2f} each\n")

    # === CALCULATIONS ===
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount)
    total = taxable_amount + tax

    # === PRINT RECEIPT ===
    print_receipt(items, subtotal, discount, tax, total)


if __name__ == "__main__":
    main()