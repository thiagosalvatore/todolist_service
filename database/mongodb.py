from pymongo import MongoClient

client = None


def connect(url):
    global client
    if not client:
        client = MongoClient(url, connect=False)
    return client


def db(db_name):
    return client[db_name]


def set_client(cli):
    global client
    client = cli


def get_client():
    return client
