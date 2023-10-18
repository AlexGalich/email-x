from email_extractor_func import extract_emails


def main():
    email , facebook  = extract_emails(
       "https://www.macapartments.com/"
        )
    print(email, facebook)
    return email , facebook

if __name__ == '__main__':
    main()