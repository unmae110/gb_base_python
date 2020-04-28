import sys

if __name__ == "__main__":
    def payment(a, b, c):
        return (a * b) + c


    if len(sys.argv) == 4:
        try:
            salary = int(sys.argv[1])
            rate = int(sys.argv[2])
            bounty = int(sys.argv[3])
            print(payment(salary, rate, bounty))
        except ValueError:
            print("неверные параметры")
    else:
        print("не верное кол-во параметров")
