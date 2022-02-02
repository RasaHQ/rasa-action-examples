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

Once the dataset is indexed, you can use lunr search in our data.

```
python scripts/prepare.py search
```

Given an indexed dataset, we can now also use it inside of a custom action too. You can talk to the assitant by running the Rasa shell. Don't forget to run the action server too!

```
python -m rasa run actions
python -m rasa shell
```