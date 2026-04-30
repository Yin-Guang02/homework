import random
import string

def generate_password(length=12):
    characters = (
        string.ascii_lowercase + 
        string.ascii_uppercase + 
        string.digits + 
        string.punctuation
    )
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

new_password = generate_password(16)
print(f"Meghan's new password: {new_password}")