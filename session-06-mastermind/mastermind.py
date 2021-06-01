class Mastermind:
    def call(secret: list, guess: list)-> list:
        good_color = 0
        misplaced_color = 0
        index = 0

        for color in guess:
            if secret[index] == color:
                good_color += 1
            elif (color in secret):
                misplaced_color += 1
            index += 1

        return [good_color, misplaced_color]