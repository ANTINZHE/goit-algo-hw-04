def total_salary(path: str) -> tuple[float, float]:
    total_sum = 0
    number_of_workers = 0

    try:
        with open(path, "r", encoding="UTF-8") as file:
            for line in file:
                name, payment_str = line.strip().split(",")
                payment = float(payment_str)
                total_sum += payment
                number_of_workers += 1
            average = total_sum / number_of_workers if number_of_workers else 0

        return total_sum, average

    except FileNotFoundError:
        print("Файл не знайдено")
        return None, None


total, average = total_salary("list_of paymintents.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")