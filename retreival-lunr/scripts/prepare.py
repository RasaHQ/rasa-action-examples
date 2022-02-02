import typer
import json
from clumper import Clumper 
from lunr import lunr
from lunr.index import Index

app = typer.Typer(name="LunrDemo", add_completion=False, help="This is demo application for Lunr.")
recipes = Clumper.read_jsonl("static/recipes.jsonl").collect()


@app.command()
def index():
    """Use lunr to index the recipe data."""
    idx = lunr(
        ref='uid', fields=('name',), documents=recipes
    )
    with open("static/index.json", "w") as f:
        f.write(json.dumps(idx.serialize()))


def query_db(query):
    db = {d['uid']: d for d in recipes}
    with open("static/index.json", "r") as f:
        idx = Index.load(json.loads(f.read()))
    matches = idx.search(query)
    results = [] 
    for match in matches[:5]:
        item = db[match['ref']]
        results.append(
            {
                'score': match['score'], 
                'name': item['name'], 
                'link': item['link']
            }
        )
    return results


@app.command()
def search():
    """Use lunr to search in the recipe data."""
    db = {d['uid']: d for d in recipes}
    with open("static/index.json") as f:
        idx = Index.load(json.loads(f.read()))
    while True:
        res = idx.search(input("Enter a query: "))
        for d in res[:5]:
            item = db[d['ref']]
            # print({'score': d['score'], 'name': item['name'], 'link': item['link']})
            print(item['name'])


if __name__ == "__main__":
    app()
