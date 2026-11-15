def main():
    user_input = input("Enter a positive decimal integer: ").strip()
    decimal_number = int(user_input)

    binary_value = bin(decimal_number)
    hex_value = hex(decimal_number)

    print(f"Decimal:     {decimal_number}")
    print(f"Binary:      {binary_value} (raw: {binary_value[2:]})")
    print(f"Hexadecimal: {hex_value} (raw: {hex_value[2:].upper()})")


if __name__ == "__main__":
    main()
