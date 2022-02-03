# apipy

ApiPy was created for api testing with Python **pytest framework** which has also **requests**, **assertpy** libraries using Page Object Model pattern. With this framework you can create api tests to call http **GET**, **POST**, **UPDATE** and **DELETE** methods.

- **requests:** for calling http methods
- **asserpy:** for making assertions

These api tests are run on GitHub Actions for each push request.

# Install

Pipenv is used to create a virtual env. So just clone this project, go to the directory of the project and run below commands.

```sh
- python3 -m venv env
- source env/bin/activate
- pip install -r requirements.txt
- pytest
```

**Note:** In order to run sample tests https://gorest.co.in/ endpoints was used. Before start to test don't forget to get an access token from gorest.co to be able to run these tests.
