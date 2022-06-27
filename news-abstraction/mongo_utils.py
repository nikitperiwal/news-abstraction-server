from pymongo import MongoClient
from secret_keys import mongo_username, mongo_password

mongo_url = f"mongodb+srv://{mongo_username}:{mongo_password}@shortly.autde.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_url)


def persist_to_mongo(items: list, collection_name: str, db_name: str = "news_db"):
    """
    Stores the curated news articles into the MongoDB.

    Parameters
    ----------
    items           -> The list of news articles to be stored.
    collection_name -> Name of the collection to store the articles in.
    db_name         -> Name of the MongoDB database to store the articles in.
    """
    global client
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(items)


def read_from_mongo(collection_name: str, db_name: str = "news_db"):
    """
    Retrieves the stored news articles into the MongoDB.

    Parameters
    ----------
    collection_name -> Name of the collection to read the articles from.
    db_name         -> Name of the MongoDB database to read the articles from.

    Returns
    -------
    cursor -> the cursor to the selected collection.
    """
    global client

    db = client[db_name]
    cursor = db[collection_name].find()
    return cursor


def drop_from_mongo(collection_name: str, db_name: str = "news_db"):
    """
    Drops collection from database in MongoDB.

    Parameters
    ----------
    collection_name -> Name of the collection to drop.
    db_name         -> Name of the MongoDB database to drop from.
    """
    global client

    db = client[db_name]
    db[collection_name].drop()


def remove_from_collection(id_list: list, collection_name: str, db_name: str = "news_db"):
    """
    Removes all objects in id_list from the passed collection.

    Parameters
    ----------
    collection_name -> Name of the collection to remove from.
    db_name         -> Name of the MongoDB database to drop from.

    Returns
    -------
    items -> The list of news articles stored in db.
    """
    global client

    db = client[db_name]
    db[collection_name].delete_many({"_id": {"$in": id_list}})
