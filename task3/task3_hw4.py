import sys
from pathlib import Path
from colorama import init, Fore, Style

# Автоматичне скидання кольору кожного рядка
init(autoreset=True)

# Рекурсивна функція для відображення структури у консолі
def print_directory_tree(path: Path, prefix: str = ""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}/")
                print_directory_tree(item, prefix + "    ")
            else:
                print(f"{prefix}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}{"Доступ закритий"}")

# Головна функція
def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED} Помилка, вкажіть вірний шлях до директорії")
        return

    path_str = sys.argv[1]
    path = Path(path_str)

    if not path.exists():
        print(f"{Fore.RED} Помилка, вказаний шлях не існує")
        return
    if not path.is_dir():
        print(f"{Fore.RED} Помилка, вказаний шлях не директорія")
        return

    print(f"{Fore.CYAN}Стурктура директорії: {path.resolve()}")
    print_directory_tree(path)

if __name__ == "__main__":
    main()