class FizzBuzz:
    def call(given_number: int)-> str:
        result = ''
        for number in range(1, given_number + 1):
            if number % 3 == 0 and number % 5 == 0:
                result += 'FIZZBUZZ'
                continue
            if number % 3 == 0:
                result += 'FIZZ'
                continue
            if number % 5 == 0:
                result += 'BUZZ'
                continue
            result += str(number);
        return result