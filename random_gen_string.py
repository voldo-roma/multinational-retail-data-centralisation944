import random 
import string 
def random_string_generator(size=2500, chars=string.ascii_letters + string.digits + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
print(random_string_generator())
