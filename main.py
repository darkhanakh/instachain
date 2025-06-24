import instaloader

L = instaloader.Instaloader()

USER = input("Enter username: ")
PASSWORD = input("Enter password: ")

L.login(USER, PASSWORD)