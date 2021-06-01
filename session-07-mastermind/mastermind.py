class Mastermind:
    def call(self, secret: list, guess: list) -> list:
        if guess == secret:
            return [4, 0]

        if sorted(guess) == sorted(secret):
            return [0, 4]

        well_placed_colors = 0
        misplaced_colors = 0
        count = 0
        for element in secret:
            if element == guess[count]:
                well_placed_colors += 1
            elif element in guess:
                misplaced_colors += 1
            count += 1

        return [well_placed_colors, misplaced_colors]
