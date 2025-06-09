import couchdb
import json
import pandas as pd
from datetime import datetime


def getdb(dbname):
    user = "admin"
    password = "password"
    couchserver = couchdb.Server("http://%s:%s@couchdb:5984/" % (user, password))
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
    getdb('mydb').update([new_doc])
    dumpdata()
    return listdocs()


def listdocs():
    rows = getdb('mydb').view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    df = pd.DataFrame(data)
    df = df.drop(columns="_id")
    df = df.drop(columns="_rev")
    return df


def dumpdata():
    rows = getdb('mydb').view('_all_docs', include_docs=True)
    index = []
    for row in rows:
        if row['doc']['doc_type'] not in index:
            index.append(row['doc']['doc_type'])
    output = []
    for i in index:
        docs = [row['doc'] for row in rows if row['doc']['doc_type'] == i]
        dict = {}
        dict[i] = docs
        output.append(dict)
    f = open("roles/demo/vars/main/couch_vars.yml", "w")
    f.write("---" + '\n')
    for var in output:
        for key, value in var.items():
            f.write(key + ": " +  "[")
            for i in value:
                f.write(json.dumps(i, indent=4, sort_keys=True) + ",")
            f.write("]" + '\n' * 2)
    f.close()


def updateuser(user):
    rows = getdb('mydb').view('_all_docs', include_docs=True)
    user = [row['doc'] for row in rows if row['doc']['key'] == user][0]
    print("Current status for " + user['name'] + " is . . . " + user['state'])
    change = input("Do you want to change state? (y/n) ")
    if change == 'y':
        if user['state'] == 'present':
            user['state'] = 'absent'
        else:
            user['state'] = 'present'
        getdb('mydb').update([user])
        dumpdata()
    return listdocs()
