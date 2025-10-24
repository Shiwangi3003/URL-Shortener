from configuration import collection

def short_url(data):
    return {
        "surl" : data["surl"],
        "lurl" : data["lurl"]
    }

# Conversion of data into list is compulsory and _id into string
def response_parser(data):
    data = list(collection.find())
    for e in data:
        e["_id"] = str(e["_id"])
    
    return data