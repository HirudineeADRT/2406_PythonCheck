from pythonsub.test import add

def handler(event, context):

    print (context)
    ///test123 123 sample
    return {"message": "Successfully executed",add(1,3)}
