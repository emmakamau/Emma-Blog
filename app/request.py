import urllib.request,json
from .models import Quote

def get_quotes():
    quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(quote_url) as url:
        data = url.read()
        get_json = json.loads(data)

        if get_json['id'] and get_json['author'] and get_json['quote']:

            id = get_json['id']
            author = get_json['author']
            quote = get_json['quote']

            quote = Quote(author,id,quote)

            return quote
        return None