import string
import random
import logging

from app.services import Service


KEY_SIZE = 8
MAX_ATTEMPTS = 30

service = Service()


def _generate_key():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        characters = string.ascii_letters + string.digits
        key = ''.join(random.choice(characters) for _ in range(KEY_SIZE))
        if not service.exists(key):
            return key
        attempts += 1

    return None


def _save_url(key, url):
    logging.info('Saved url: {} with key: {}'.format(url, key))
    service.put(key, url)


def handle_create_link(url: str):
    key = _generate_key()
    if not key:
        logging.info('Can not generate unique id for url: {}'.format(url))
        return {"error": "Can't generate unique id"}

    _save_url(key, url)

    return {"id": key}


def handle_get_link(key: str):
    if service.exists(key):
        return {'url': service.get(key)}
    else:
        return {"error": "Link not found"}
