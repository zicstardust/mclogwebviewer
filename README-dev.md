# Dev environment

### Python version
Recommended to use asdf to keep the same python version

Python version used in `.tool-versions` file

### Install dependencies
``` shell
pip install -r requirements-dev.txt
```

### Create `.env` file

``` shell
cp .env_exemple .env
```

### Run app
``` shell
flask --app src/app.py --debug run
```