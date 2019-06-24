from pythonsub.test import add

def handler(event, context):

    print (context)
    return {"message": "Successfully executed",add(1,3)}
