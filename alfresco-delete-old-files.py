#!/usr/bin/python

import requests, json, urllib, datetime

dryrun = True
debug = True
maxiter = 100
url = 'http://localhost:8080/alfresco/api/-default-/public/cmis/versions/1.1/browser'
username = "admin"
password = 'DiN8quahkaequahc'
maxitems = "3"
startdate = "2022-01-29T10:00+0300"
enddate = "2022-01-29T22:10+0300"
headers = {'Accept': 'application/json'}

for _ in range(maxiter):

        f = {   "cmisaction": "query",
                "maxItems": maxitems,
                "statement": "select * from cmis:document where cmis:lastModificationDate > '" + \
                        startdate + "' and cmis:lastModificationDate < '" + enddate + "' " + \
                        "and cmis:name not like 'page.%' and cmis:name not like 'dashboard.%' " + \
                        "and cmis:lastModifiedBy <> '" + username + "' and cmis:lastModifiedBy <> 'System'" }

        data = urllib.urlencode(f)
        if debug: print(data)

        r = requests.post(url, headers=headers, auth=(username, password), data=data)
        obj = r.json()
        # json_formatted_str = json.dumps(obj, indent=4)
        # print(json_formatted_str)

        procitems = 0

        for x in obj["results"]:
                if debug:
                        print(x["properties"]["cmis:objectId"]["value"])
                        print(x["properties"]["cmis:createdBy"]["value"])
                        print(x["properties"]["cmis:name"]["value"])
                        print(datetime.datetime.fromtimestamp(x["properties"]["cmis:lastModificationDate"]["value"] / 1000))
                        print("")
                f = {   "cmisaction": "delete",
                        "objectId": x["properties"]["cmis:objectId"]["value"] }
                data = urllib.urlencode(f)
                if not dryrun: requests.post(url + "/root", headers=headers, auth=(username, password), data=data)
                procitems += 1

        if procitems < int(maxitems): break


