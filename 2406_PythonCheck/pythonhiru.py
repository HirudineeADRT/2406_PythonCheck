from pythonsub.test import add

def handler(event, context):

    print (context)
    ///test123
    return {"message": "Successfully executed",add(1,3)}
