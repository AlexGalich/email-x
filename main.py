from email_extractor_func import extract_emails

import time
def main():
    time_1 = time.time()
    email , facebook  = extract_emails(
    "https://cardinalrealtygroup.com/"
        )
    

    time_2 = time.time()
    print("time for finding", time_2- time_1 )
    print(email, facebook)
    return email , facebook

if __name__ == '__main__':
    main()