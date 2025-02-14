def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    if not numbers:
        return 0  # Devuelve 0 si la lista está vacía
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    return isinstance(num, int) and num % 2 == 0

def isitaninteger(num):
    return isinstance(num, int)

def main():
    print("Calculator program")
    print("Adding [1, 2, 3, 4]:", addmultiplenumbers([1, 2, 3, 4]))
    print("Multiplying [1, 2, 3, 4]:", multiplymultiplenumbers([1, 2, 3, 4]))
    print("Is 4 even?:", isiteven(4))
    print("Is 4.5 an integer?:", isitaninteger(4.5))
    
if __name__ == "__main__":
    main()

def main():
  print("Hello learners!")

if __name__=="__main__":
  main()