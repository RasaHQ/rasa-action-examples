import typer
from clumper import Clumper 
from jina import Document, DocumentArray, Flow

app = typer.Typer(name="JinaDemo", add_completion=False, help="This is demo application for Jina.")
recipes = Clumper.read_jsonl("static/recipes.jsonl").collect()

# A DocumentArray is a list of Documents.
docs = DocumentArray(
    [Document(text=d['name']) for d in recipes]
)

# Create a new Flow to process our Documents
flow = (
    Flow(protocol="http", port_expose=12345)
    .add(uses="jinahub://TransformerTorchEncoder", name="encoder", install_requirements=True)
    .add(uses="jinahub://SimpleIndexer", install_requirements=True, name="indexer", workspace="workspace")
)

def print_search_results(response, number=5):
    matches = response[0].data.docs[0].matches

    print("\nYour search results")
    print("===================\n")

    for match in matches[0:number]:
        print(f"- {match.text}")


@app.command()
def index():
    """Use Jina to index the recipe data."""
    with flow:
        flow.index(inputs=docs)

@app.command()
def search():
    """Use Jina to search in the recipe data."""
    with flow:
        while True:
            query = Document(text=input("Enter a query: "))
            response = flow.search(inputs=query, return_results=True)
            print_search_results(response)

@app.command()
def serve():
    """Use Jina to search in the recipe data."""
    with flow:
        flow.block()

if __name__ == "__main__":
    app()
