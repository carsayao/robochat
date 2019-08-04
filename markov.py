import markovify
import re
import os.path
from pathlib import Path
try:
    import simplejson as json
except:
    import json

def main():
    # test
    def get_json():
        out = { 'key': 'value', 'key2': 'value2' }
        print(json.dumps(out))

    def clean_text(text):

        # Strip and replace special characters
        cleaned = text.replace('"', '')
        cleaned = cleaned.replace('”', '')
        cleaned = cleaned.replace('“', '')
        cleaned = cleaned.replace('’', "'")
        cleaned = cleaned.replace('‘', "'")
        cleaned = cleaned.replace('#', "'")
        cleaned = cleaned.lower()
        return cleaned

    def gen_model(person):
        # Get raw text as string.
        directory = person
        concat = ''
        for file in os.listdir(directory + '/'):
            with open(directory+ '/' + file) as f:
                concat += '\n' + f.read()

        # Clean transcript        
        cleaned = clean_text(concat)
        # Build the model.
        text_model = markovify.Text(cleaned, state_size=2)
        # Turn into json
        model_json = text_model.to_json()
        # Write model to json
        with open(directory + "_model.json", "w+") as fpjson:
            json.dump(model_json, fpjson)
        # out = { 'text': text_model.make_sentence() }

        # print(json.dumps(out))
        
        # Print three randomly-generated sentences of no more than 280 characters
        # for i in range(3):
        #     print(text_model.make_short_sentence(280))
    
    def load_model(person):
        # Load model from json
        with open(person + '_model.json') as fprecon:
            recon_json = json.load(fprecon)
        recon_model = markovify.Text.from_json(recon_json)
        out = { 'text': recon_model.make_sentence() }
        print(json.dumps(out))
    
    def get_text(person):
        myfile = Path('./' + person + '_' + 'model.json')
        if myfile.is_file():
            # print('"' + person + '_model.json" exists')
            load_model(person)
        else:
            # print('"' + person + '_model.json" does not exist')
            gen_model(person)
            load_model(person)

    # gen_model()
    get_text('iliza')


if __name__ == '__main__':
    main()
