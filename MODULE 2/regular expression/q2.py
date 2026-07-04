import re


def extract_email_parts(email):
    match = re.fullmatch(r"([\w.+-]+)@([\w.-]+)\.([a-zA-Z]{2,})", email)
    if not match:
        return None
    return {
        'user_id': match.group(1),
        'domain_name': match.group(2),
        'suffix': match.group(3)
    }


if __name__ == "__main__":
    emails = [
        'zuck@facebook.com',
        'sunder33@google.com',
        'jeff42@amazon.com'
    ]

    extracted = [extract_email_parts(email) for email in emails]
    print("Emails:", emails)
    print("Extracted parts:")
    for email, parts in zip(emails, extracted):
        print(email, '->', parts)
