import couchdb
import pandas as pd
from pprint import pprint
from datetime import datetime


def getdb():
    user = "admin"
    password = "password"
    couchserver = couchdb.Server("http://%s:%s@couchdb:5984/" % (user, password))
    dbname = "mydb"
    # del couchserver[dbname]
    if dbname in couchserver:
        db = couchserver[dbname]
    else:
        db = couchserver.create(dbname)
    return db


def newdoc():
    doc_type = input("Please enter a document type ")
    new_doc = {}
    new_doc['doc_type'] = doc_type
    while True:
        add = input("Do you want to add another field? (y/n) ")
        if add == 'n':
            break
        key = input("What field would you like to add? ")
        value = input("What value would you like to add? ")
        new_doc[key] = value
    getdb().update([new_doc])
    pprint(new_doc)


def listdocs():
    rows = getdb().view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    df = pd.DataFrame(data)
    df = df.drop(columns="_id")
    df = df.drop(columns="_rev")
    return df
