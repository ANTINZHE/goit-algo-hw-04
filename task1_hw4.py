from pathlib import Path

def total_salary(path: Path) -> tuple[int, int]:
    if path.exists() and path.is_file():

        total_sum = 0
        number_of_workers = 0

        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                name, payment_str = line.split(",")
                payment = int(payment_str)
                total_sum += payment
                number_of_workers += 1

        middle_payment = total_sum / number_of_workers
        return total_sum, int(middle_payment)
    else:
        print("File not found.")

# Створення файлу з оплатами
list_of_payments = "Alex Korp,6000\nNikita Borisenko,2000\nSitarama Raju,1000"
with open('list_of payments.txt', "w") as file:
    file.write(list_of_payments)

path = Path("list_of payments.txt")

# Виклик функції
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")