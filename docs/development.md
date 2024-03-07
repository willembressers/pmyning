# Development


## Documentation
Good code documentation will automatically lead to good documentation, so let's update the documentation.
```console
poetry run mkdocs serve
```

publish the code to github pages
```console
poetry run mkdocs gh-pages
```

## Tests
Run the unittests
```console
poetry run python -m unittest discover
```

## Publication
First we need to bump the version number.
```console
poetry version 0.0.2
```

Now we can build the sdist & wheel.
```console
poetry build
```

You will need an API token to publish the package to pypi. Create one [here](https://pypi.org/manage/account/), and set it in the poetry config.
```console
poetry config pypi-token.pypi [your-api-token]
```

Once the:
- documentation is updated
- all the unittests are succesfull
- the version number is updated
- package is build

We can deploy the package.
```console
poetry publish
```