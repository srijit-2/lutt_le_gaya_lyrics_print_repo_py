# import time
# import sys
# import os
# GREEN = '\033[38;5;46m' 
# YELLOW = '\033[93m'
# BOLD = '\033[1m'
# RESET = '\033[0m'
# def typing_effect(text, speed=0.1):
#     for char in text:
#         sys.stdout.write(f"{BOLD}{GREEN}{char}{RESET}")
#         sys.stdout.flush()
#         time.sleep(speed)
# def run_performance():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("\n\n")
#     lyrics = [
#         ("Haye Sajan Meri", 0.1),
#         ("Akkhan Taras Di", 0.12),
#         ("Haye Imaan Mera", 0.1),
#         ("Tutt Pai Gaya", 0.15),
#         ("Mennu Lutt Le Gaya", 0.18)
#     ]
#     for line, speed in lyrics:
#         sys.stdout.write("    ") 
#         typing_effect(line, speed)
#         print("\n") 
#         time.sleep(1.2) 
#     print("\n")
# if __name__ == "__main__":
#     run_performance()
    
    
    
import time
import sys

RED = '\033[91m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'


def print_lyrics():
    lyrics = [
        ("Haye Sajan Meri"),
        ("Akkhan Taras Di"),
        ("Haye Imaan Mera"),
        ("Tutt Pai Gaya"),
        ("Mennu Lutt Le Gaya")
    ]
    delays = [0.1, 0.12, 0.1, 0.15, 0.18]

    print(f"\n{BOLD}{RED}❤ Playing: LUTT LE GAYA ❤{RESET}\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):

        color = YELLOW if i % 2 == 0 else RED

        for char in line:
            sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.08)

        print()

        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(1.0)


print_lyrics()