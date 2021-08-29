from config import config

def get_google_group_request(email: str) -> str:

    link_email = email.replace("@", "%40")
    search_results_link = f"{config.google_group_link}/pending-members?q=email%3A{link_email}"

    return search_results_link


def get_google_group_member(email: str) -> str:

    link_email = email.replace("@", "%40")
    search_results_link = f"{config.google_group_link}/members?q=email%3A{link_email}"

    return search_results_link
