import logging
import azure.functions as func
from . import sumNums

def main(req: func.HttpRequest) -> func.HttpResponse:
    headers = {"my-http-header": "some-value"}

    name = req.params.get('name')
    v1 = int(req.params.get('val1'))
    v2 = int(req.params.get('val2'))
    print("Hey you are in live straming logs.")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}! Sum of {v1} + {v2} = {sumNums.nums(v1,v2)}", headers=headers)
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             headers=headers, status_code=400
        )