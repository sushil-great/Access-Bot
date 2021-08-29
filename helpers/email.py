import re
from typing import Pattern

email_regex_str = '[a-z0-9.]+@([a-z0-9]+\.)+[a-z0-9]+'


def has_email(msg: str) -> bool:

    msg_has_email = False
    email_regex: Pattern[str] = re.compile(
        email_regex_str,
        re.IGNORECASE
    )
    regex_search_results = email_regex.search(msg)

    if regex_search_results:
        msg_has_email = True

    return msg_has_email


def has_gmail_email(msg: str) -> bool:

    msg_has_gmail_email = False
    gmail_email_regex: Pattern[str] = re.compile(
        '[a-z0-9.]+@gmail.com',
        re.IGNORECASE
    )
    regex_search_results = gmail_email_regex.search(msg)

    if regex_search_results:
        msg_has_gmail_email = True

    return msg_has_gmail_email


def extract_email(msg: str) -> str:

    email: str = ''
    email_regex: Pattern[str] = re.compile(
        email_regex_str,
        re.IGNORECASE
    )
    regex_search_results = email_regex.search(msg)

    if regex_search_results:
        email = regex_search_results[0]

    return email.lower()


def extract_gmail_email(msg: str) -> str:

    gmail_email: str = ''
    gmail_email_regex: Pattern[str] = re.compile(
        '[a-z0-9.]+@gmail.com',
        re.IGNORECASE
    )
    regex_search_results = gmail_email_regex.search(msg)

    if regex_search_results:
        gmail_email = regex_search_results[0]

    return gmail_email.lower()
