import string

class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

while True:
    password = input()

    if password == 'Done':
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password.isalpha() or password.isnumeric() or all(char in string.punctuation for char in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if sum(1 for ch in password if ch in '@*&%') < 1:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if ' ' in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")