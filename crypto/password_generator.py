import secrets
import string


class PasswordGenerator:

    @staticmethod
    def generate(
        length=16,
        include_uppercase=True,
        include_lowercase=True,
        include_digits=True,
        include_special=True
    ):

        characters = ""

        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        if not characters:
            raise ValueError("At least one character class must be enabled")

        password = "".join(
            secrets.choice(characters) for _ in range(length)
        )

        return password