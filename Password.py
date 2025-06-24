import random
import string

special_chars = string.punctuation
specialchar1 = random.choice(special_chars)
num1 = str(random.randint(1, 10))
letter1 = random.choice(string.ascii_letters)
num2 = str(random.randint(1, 10))
letter2 = random.choice(string.ascii_letters)
num3 = str(random.randint(1, 10))
letter3 = random.choice(string.ascii_letters)
num4 = str(random.randint(1, 10))
letter4 = random.choice(string.ascii_letters)
password = [num1, letter1, num2, letter2, num3, letter3, num4, letter4, specialchar1]
random.shuffle(password)
password = "".join(
    [num1, letter1, num2, letter2, num3, letter3, num4, letter4, specialchar1]
)
print(password)
