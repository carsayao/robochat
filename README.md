# robochat

Speak to a person of your choice!

## install

Requires node, express, socketio.

### virtualenv
    pip3 install virtualenv

    virtualenv -p python3 env

This will install virtualenv using pip3 and create a an `env` folder that will contain the libraries brought it.

    source env/bin/activate

This will put your shell into the virtual environment where you will have the libraries brought it.

    pip3 install -r requirements.txt
    
This will install the libraries that are found in the `requirements.txt`
When you are done working, use `deactivate` to get out of the virtual environment

### additional required packages

Requirements for python:
- python3
- pip3 (package manager)
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
