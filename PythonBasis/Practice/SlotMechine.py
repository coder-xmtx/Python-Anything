# 练习：制作一个简易的老虎机程序

import random
import time


def spin_row():
    """
    老虎机转动
    """
    symbols = ["🍒", "🍇", "🍊", "🍌", "🍓", "🍉"]

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    """
    输出转动后的结果
    """
    print(" | ".join(row))


def get_payout(row, bet):
    """
    计算赔率
    """
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍇":
            return bet * 3
        elif row[0] == "🍊":
            return bet * 4
        elif row[0] == "🍌":
            return bet * 5
        elif row[0] == "🍓":
            return bet * 6
        elif row[0] == "🍉":
            return bet * 7

    return 0


def main():
    balence = 100

    print("---------------------------")
    print("Welcome to the Slot Machine")
    print("---------------------------")

    while balence > 0:
        print("\nCurrent balance: ", balence)

        bet = input("Please enter your bet: ")

        if not bet.isdigit():
            print("Please enter a number")
            continue

        bet = int(bet)

        if bet > balence:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Please enter a positive number")
            continue

        balence -= bet

        row = spin_row()
        print("Spinning...")
        time.sleep(1)
        print_row(row)

        payout = get_payout(row, bet)

        if payout == 0:
            print("You lost")
        else:
            print(f"You won ${payout}")

        balence += payout

        play_again = input("Do you want to play again? (y/n): ")

        if play_again.lower() != "y":
            break

    print(f"Game over. Final balance: ${balence}")


if __name__ == "__main__":
    main()
