import secrets
import string

def generate_password(length=32):
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password.extend(
        secrets.choice(chars)
        for _ in range(length - 4)
    )

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

print(generate_password())
