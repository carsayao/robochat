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
        cleaned = cleaned.replace('”', '"')
        cleaned = cleaned.replace('“', '"')
        cleaned = cleaned.replace('’', "'")
        cleaned = cleaned.replace('‘', "'")
        cleaned = cleaned.replace('#', "'")
        cleaned = cleaned.lower()
        return cleaned

    def gen_model(person):
        # Get raw text as string.
        text = ''
        onlyfiles = next(os.walk(inputDir+person+'/'))[2]
        print('onlyfiles', onlyfiles)
        print("inputDir+person+'/'",inputDir+person+'/')
        print('onlyfiles',len(onlyfiles))
        for file in os.listdir(inputDir + person + '/'):
            with open(inputDir + person + '/' + file) as f:
                if len(onlyfiles) > 1:
                    text += '\n' + f.read()
                else:
                    text = f.read()
        # Check what the text is
        with open(inputDir+person+'_cat.txt','w+') as test:
            test.write(text)
        # Clean transcript        
        cleaned = clean_text(text)
        with open(inputDir+person+'_cleancat.txt','w+') as fclean:
            fclean.write(cleaned)
        # Build the model, reject_reg rejects bracketed text
        text_model = markovify.Text(cleaned, state_size=2)#, reject_reg='\[.*?\][ \t\n]*')
        # Turn into json
        model_json = text_model.to_json()
        # Write model to json
        with open(outputDir + person + '_model.json', 'w+') as fpjson:
            json.dump(model_json, fpjson)
        # out = { 'text': text_model.make_sentence() }

        # print(json.dumps(out))
        
        # Print three randomly-generated sentences of no more than 280 characters
        # for i in range(3):
        #     print(text_model.make_short_sentence(280))
    
    def load_model(person):
        # Load model from json
        with open(outputDir + person + '_model.json') as fprecon:
            recon_json = json.load(fprecon)
        recon_model = markovify.Text.from_json(recon_json)

        response = recon_model.make_sentence(init_state=('standing', 'in'))
        # response = recon_model.make_sentence() 
        out = { 'text': response }

        # out = { 'text': recon_model.make_sentence_with_start('a') }
        print(json.dumps(out))
    
    def get_text(person):
        myfile = Path(outputDir + person + '_' + 'model.json')
        if myfile.is_file():
            # print('"' + person + '_model.json" exists')
            load_model(person)
            print('load')
        else:
            # print('"' + person + '_model.json" does not exist')
            gen_model(person)
            load_model(person)
            print('gen')
            print('load')

    # Setup our input/output
    path = os.path.dirname(os.path.realpath(__file__))
    print('path', path)
    inputDir = path + '/../texts/'
    print('inputDir', inputDir)
    outputDir = path + '/../models/'
    print('outputDir', outputDir)
    person = 'iliza'

    if not os.path.exists(outputDir):
        os.mkdir(outputDir)
    get_text(person)


if __name__ == '__main__':
    main()
