import datetime
from concurrent.futures import ProcessPoolExecutor


def is_perfect_number(num: int):
    if num <= 0:
        return False

    sum_of_divisors = 0

    for n in range(1, num):
        if num % n == 0:
            sum_of_divisors += n

    if sum_of_divisors == num:
        return True

    return False


def get_perfect_numbers_from_and_up_to(start_from: int, to: int):
    results = []
    for i in range(start_from, to):
        if is_perfect_number(i):
            results.append(i)

        print(f"checked {i}")

    return results


if __name__ == "__main__":
    check_up_to = int(input("Enter the number to check up to: "))

    start_time = datetime.datetime.now()

    quarter = check_up_to // 4

    ranges = [
        (1, quarter),
        (quarter, quarter * 2),
        (quarter * 2, quarter * 3),
        (quarter * 3, check_up_to),
    ]

    perfect_numbers = []

    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(get_perfect_numbers_from_and_up_to, start, end)
            for start, end in ranges
        ]

        for future in futures:
            perfect_numbers.extend(future.result())

    print("\nPerfect numbers up to the specified number:")
    for perfect_number in perfect_numbers:
        print(perfect_number)

    end_time = datetime.datetime.now() - start_time
    print(f"\nRan for {end_time}")
