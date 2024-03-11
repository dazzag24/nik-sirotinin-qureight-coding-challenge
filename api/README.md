```
pyenv local 3.11.2
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-multipart
venv/bin/uvicorn main:app --reload
```

Since a collegue reported some issues with the existing requirements.txt, I decided to start again as the modules used looked simple enough.

```
rm requirements.txt
python -m pip freeze > requirements.txt
```
