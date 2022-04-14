# steno
API for sending secure messages.


## Running locally
Setup your venv, activate it, and install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Setup your inital db:
```bash
source venv/bin/activate
mkdir instance
flask init-db
```

Run app.py through your IDE or locally
```bash
source venv/bin/activate
python3 app.py
```