import string
import random
import logging


KEY_SIZE = 8
MAX_ATTEMPTS = 30

links = {}


def _generate_key():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        characters = string.ascii_letters + string.digits
        key = ''.join(random.choice(characters) for _ in range(KEY_SIZE))
        if key not in links:
            return key
        attempts += 1

    return None


def _save_url(key, url):
    logging.info('Saved url: {} with key: {}'.format(url, key))
    links[key] = url


def handle_create_link(url: str):
    key = _generate_key()
    if not key:
        logging.info('Can not generate unique id for url: {}'.format(url))
        return {"error": "Can't generate unique id"}

    _save_url(key, url)

    return {"id": key}


def handle_get_link(key: str):
    if key in links:
        return {'url': links[key]}
    else:
        return {"error": "Link not found"}
