
class sumPrimer:

    def calc_prime_number(self):
        list_numbers = []
        x_number = int(input("Enter a number between (2-100): "))
        if 1 < x_number <= 100:
            for num in range(x_number):
                if num > 1:
                    for i in range(2, num):
                        if (num % i) == 0:
                            break
                    else:
                        list_numbers.append(num)
            return list_numbers
        else:
            print("not valid")

