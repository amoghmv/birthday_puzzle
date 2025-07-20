import time
from colorama import Fore, init

init(autoreset=True)

def boot_sequence():
    print(Fore.GREEN + "Booting Birthday Protocol...\n")
    time.sleep(2)
    print("Loading core modules: [██████████] 100%")
    time.sleep(2)
    print("Initializing protocol...bro is 28? 27? Aging Detected! lmfao")
    time.sleep(2)
    print("Cross-checking against 'Lazy guy' database... Match found")
    time.sleep(2)
    print("Verifying system uptime: 27 years. leg in healing process....")
    time.sleep(2)
    print("Authenticating user /zenhons101/....")
    time.sleep(2)
    print(Fore.CYAN + "\nAccess Granted.\n")
    time.sleep(1)

def puzzle_one():
    print(Fore.YELLOW + "Puzzle 1: Git gud.\n")
    time.sleep(1)

    print("You accidentally deleted tracked files locally.")
    print("Which git command can bring them back?")
    print("Answer with just the command name (no slashes). (Hint: it starts with 'c' or 'r')\n")

    answer = input("Your answer: ").strip().lower()

    if answer in ["checkout", "restore"]:
        print(Fore.GREEN + "\nnoice!.\n")
    else:
        print(Fore.RED + "bruhh! cmon. Try again.\n")
        time.sleep(1)
        return puzzle_one()

def puzzle_two():
    print(Fore.MAGENTA + "Puzzle 2: Pattern Recognition\n")
    time.sleep(1)

    print("What comes next in this sequence?")
    print("3, 6, 11, 18, ?")

    answer = input("Your answer: ").strip()

    if answer == "27":
        print(Fore.GREEN + "\nCorrect. Your age, by the way.\n")
    else:
        print(Fore.RED + "WRONG!! You ain't escaping 27 that easily.\n")
        time.sleep(1)
        return puzzle_two()

def puzzle_three():
    print(Fore.BLUE + "Puzzle 3: Regional Language Test\n")
    time.sleep(1)

    print('if statement == "neenu bassist ah racist ah?":')
    print("Translate this to English.\n")

    answer = input("Your answer: ").strip().lower()

    if "racist" in answer:
        print(Fore.GREEN + "\nGood.\n")
    else:
        print(Fore.RED + "Nice Try. But no.\n")
        time.sleep(1)
        return puzzle_three()

def puzzle_four():
    print(Fore.YELLOW + "Final Puzzle: The Truth\n")
    time.sleep(1)

    print("I come once a year, get forgotten the next day, and make you older without doing anything.\nWhat am I?")
    answer = input("Your answer: ").strip().lower()

    if "birthday" in answer:
        print(Fore.GREEN + "\nCorrect. And it’s yours. Happy Burth-a-day, namma huduga.\n")
    else:
        print(Fore.RED + "error!.\n")
        time.sleep(1)
        return puzzle_four()

def final_message():
    import pyfiglet
    print(Fore.MAGENTA + "\n" + "★" * 60)
    time.sleep(1)

    banner = pyfiglet.figlet_format("Happy Burth-a-day!", font="slant")
    print(Fore.CYAN + banner)
    time.sleep(1)

    print(Fore.YELLOW + "🎉 You answered everything!.")
    print(Fore.GREEN + "🎸 Have a great life ahead.")
    print(Fore.MAGENTA + "★" * 60 + "\n")


if __name__ == "__main__":
    boot_sequence()
    puzzle_one()
    puzzle_two()
    puzzle_three()
    puzzle_four()
    final_message()
