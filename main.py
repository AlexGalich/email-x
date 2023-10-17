from email_extractor_func import extract_emails


def main():
    email , facebook  = extract_emails(
       # site url here
    )

    return email , facebook

if __name__ == '__main__':
    main()