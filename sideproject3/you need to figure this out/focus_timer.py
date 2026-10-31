#!/usr/bin/env python

import time
import subprocess
import os

columns, lines = os.get_terminal_size()

def countdown(seconds: int):
    ''' countdown() '''
    for seconds_remaining in range(seconds,-1,-1):
        mins, secs = divmod(seconds_remaining, 60)
        print('\033[K', f'{mins:02d}:{secs:02d}'.center(columns),
                sep='', end="\r", flush=True)
        time.sleep(1)

def main():
    ''' main() '''
    minutes = input("How many minutes do you want to focus?")

    try:
        minutes = int(minutes)
        subprocess.run("clear")
        print('\n' * (int(lines)//2))
        countdown(minutes * 60)
        subprocess.run("clear")
        print("Time's up! Take a break!")
    except ValueError:
        print("You enter a string, not a number. Please enter a number.")


if __name__ == "__main__":
    main()