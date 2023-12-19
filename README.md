# robochat

Speak to a person of your choice!

## install

Requires node, express, socketio.

### virtualenv

    python3 -m pip install virtualenv

    virtualenv -p python3 env

This will install virtualenv using pip and create a an `env` folder that will contain the libraries brought it.

_Note_: Invoking pip on its own will use the system python (`python3 -m pip install`) rather than `pip3 install virtualenv`, which may use a different pip3 package.

    source env/bin/activate

This will put your shell into the virtual environment where you will have the libraries brought it.

    python3 -m pip install -r requirements.txt
    
This will install the libraries that are found in the `requirements.txt`. When you are done working, use `deactivate` to get out of the virtual environment.

### additional required packages

Requirements for python:
- python3
- markovify (custom)
- simplejson 3.16.0
- nltk 3.4.4
- numpy 1.16.4

To install required nltk packages, run python3 interpreter:

```python
import nltk
nltk.download('punkt')
nltk.download('maxent_treebank_pos_tagger')
nltk.download('averaged_perceptron_tagger')
```

## run

Run `node server.js` then open localhost:8080/

## todo

- journal pdf
  - log of progess
  - add github repo link
- try to deploy
