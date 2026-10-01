from lib import add_numbers, greet_user, multiply_numbers


def main() -> None:
    # Перевірка роботи функції привітання
    greeting = greet_user("Влад")
    print(greeting)

    # Перевірка роботи функції додавання
    a, b = 5.0, 3.0
    sum_result = add_numbers(a, b)
    print(f"Сума {a} + {b} = {sum_result}")

    # Перевірка роботи функції множення
    mult_result = multiply_numbers(a, b)
    print(f"Добуток {a} * {b} = {mult_result}")


if __name__ == "__main__":
    main()