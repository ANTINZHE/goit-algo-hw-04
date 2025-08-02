def total_salary(path: str) -> tuple[int, int]:
    total_sum = 0
    number_of_workers = 0

    try:
        with open(path, "r", encoding="UTF-8") as file:
            for line in file:
                name, payment_str = line.strip().split(",")
                payment = int(payment_str)
                total_sum += payment
                number_of_workers += 1

        average = total_sum / number_of_workers
        return total_sum, int(average)

    except FileNotFoundError:
        return "Файл не знайдено"

total, average = total_salary("list_of payments.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")