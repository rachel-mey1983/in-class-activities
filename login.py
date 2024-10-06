def login(username, password):
    # Simple login logic
    if username == 'Rachel' and password == 'password':
        return 'Hi Rachel!'
    else:
        return 'Login failed!'

# Example usage
user = input("Enter username: ")
pwd = input("Enter password: ")
print(login(user, pwd))
