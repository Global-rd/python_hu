import number_guessing_game as ng


def main() -> None:

    settings = ng.load_settings()
    interval_start = settings.get("interval_start", 1)
    interval_end = settings.get("interval_end", 100)

    while True:
        ng.play_game(
            interval_start=interval_start,
            interval_end=interval_end,
        )
        play_again = input("Do you want to play again? (yes/y // no/n): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()