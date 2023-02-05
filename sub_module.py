def slicer(email):
    user_emailname = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    # print(f"Your user name is{user_emailname}")
    return [user_emailname,email_domain]
def print_ans(user_name,email_domain):
    print(f"Your user name is {user_name}")
    print(f"Your email domain is {email_domain}")

def main():
    email = input("Input your email here: ").strip()
    print(f"This is your email: {email}")
    user_name, email_domain = slicer(email)
    print_ans(user_name, email_domain)

if __name__ == "__main__":
    main()