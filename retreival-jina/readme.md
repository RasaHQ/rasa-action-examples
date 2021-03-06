We use the `m3hrdadfi/recipe_nlg_lite` recipe dataset from huggingface for this demo. Note that this demo was made with Rasa 3.0.5 in mind.

Before running anything, be sure to install Rasa as well as the extra dependencies.

```
python -m pip install rasa==3.0.5
python -m pip install -r requirements.txt
```

To get started, we first need to index the dataset. We've made a script that can do this for you. 

```
python scripts/prepare.py index
```

Once the dataset is indexed, you can use the jina pipeline to find search.

```
python scripts/prepare.py search
```

Given an indexed dataset, we can now also use it inside of a custom action too. The custom action is implemented as a proxy, so you'll need to run a jina server to use it.

```
python scripts/prepare.py search
```

Once it's active you can talk to the assitant by running the Rasa shell. Don't forget to run the action server too!

```
python -m rasa run actions
python -m rasa shell
```