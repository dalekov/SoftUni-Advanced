class NameTooShortError(Exception):
    """Raised when name is too short."""
    pass


class MustContainAtSymbolError(Exception):
    """Raised when name does not contain @."""



class InvalidDomainError(Exception):
    """Raised when domain is invalid."""
    pass


valid_domains = ['.com', '.bg', '.org', '.net']
while True:
    email = input()

    # Break if End is the input
    if email == 'End':
        break

    # If no @ sign in the email, raise Error:
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    # If the @ sign is found, extracting the name by slicing up until @ sign
    at_idx = email.index('@')
    name = email[:at_idx]

    # If name is less than or equal to 4 characters, raise Error:
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    # If all checks above are OK, we extract the domain by slicing from '.' until the end.
    dot_idx = email.index('.')
    domain = email[dot_idx:]

    # If domain is not found in the list of valid domains, raise Error:
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    # If no errors encountered, inform user that email is valid.
    print("Email is valid")

