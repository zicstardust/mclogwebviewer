# Dev environment

### Python version
Recommended to use asdf to keep the same python version

Python version used in `.tool-versions` file

### Install dependencies
```
pip install -r requirements-dev.txt
```

### Create `.env` file

```
cp .env_exemple .env
```

### Run app
```
flask --app src/app.py --debug run
```