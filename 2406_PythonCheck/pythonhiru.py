from pythonsub/test.py import add

def handler(event, context):
    print (context)
    return {"message": "Successfully executed"}
