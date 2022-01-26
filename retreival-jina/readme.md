We use the `m3hrdadfi/recipe_nlg_lite` recipe dataset from huggingface.

We first need to index the dataset. We've made a script that can do this for you. 

```
python scripts/prepare.py index
```

Once the dataset is indexed, you can use the jina pipeline to find search.

```
python scripts/prepare.py search
```

Given an indexed dataset, we can now also use it inside of a custom action!
