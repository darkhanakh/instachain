import instaloader

def main():
    L = instaloader.Instaloader()
    USER = input("Enter username: ")
    PASSWORD = input("Enter password: ")
    L.login(USER, PASSWORD)

if __name__ == "__main__":
    main()