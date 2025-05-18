def calculator():
    memory = None

    while True:
        print("\n--- Calculator ---")
        try:
            num1_str = input("Enter the first number (or 'recall'): ").lower()
            if num1_str == 'recall':
                if memory is None:
                    print("Memory is empty.")
                    continue
                num1 = memory
                print(f"Using {num1} from memory.")
            else:
                num1 = float(num1_str)

            operation = input("Enter the operation (+, -, *, /, **, %, store, recall): ").lower()

            if operation == 'store':
                memory = num1
                print(f"{num1} stored in memory.")
                continue
            elif operation == 'recall':
                num2_str = input("Enter the second number (or 'recall'): ").lower()
                if num2_str == 'recall':
                    if memory is None:
                        print("Memory is empty.")
                        continue
                    num2 = memory
                    print(f"Using {num2} from memory.")
                else:
                    num2 = float(num2_str)
            else:
                num2 = float(input("Enter the second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                else:
                    result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            elif operation == '%':
                result = num1 % num2
            else:
                print("Invalid operation!")
                continue

            print(f"{num1} {operation} {num2} = {result}\n")
            memory_choice = input("Do you want to store this result in memory? (yes/no): ").lower()
            if memory_choice == 'yes':
                memory = result
                print(f"{result} stored in memory.")

        except ValueError:
            print("Invalid input. Please enter numbers or 'recall'.\n")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break

if __name__ == "__main__":
    calculator()