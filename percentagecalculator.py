def main():
    print("=== Percentage Calculator ===")
    print("Type 'quit' to exit.\n")

    while True:
        print("Options:")
        print("1. What is X% of Y?")
        print("2. X is what percent of Y?")
        print("3. Percentage increase/decrease")
        print("4. Quit")

        choice = input("\nChoose an option (1-4): ").strip().lower()

        if choice == "4" or choice == "quit":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                percent = float(input("Enter percentage (X): ").strip())
                total = float(input("Enter total value (Y): ").strip())
                result = (percent / 100) * total
                print(f"\n{percent}% of {total} = {result:.2f}\n")

            elif choice == "2":
                part = float(input("Enter the part value (X): ").strip())
                total = float(input("Enter the total value (Y): ").strip())
                if total == 0:
                    print("Total cannot be zero.\n")
                    continue
                result = (part / total) * 100
                print(f"\n{part} is {result:.2f}% of {total}\n")

            elif choice == "3":
                old_value = float(input("Enter original value: ").strip())
                new_value = float(input("Enter new value: ").strip())
                if old_value == 0:
                    print("Original value cannot be zero.\n")
                    continue
                result = ((new_value - old_value) / old_value) * 100
                change_type = "increase" if result >= 0 else "decrease"
                print(f"\nPercentage {change_type}: {abs(result):.2f}%\n")

            else:
                print("Invalid option.\n")

        except ValueError:
            print("Please enter valid numbers.\n")


if __name__ == "__main__":
    main()