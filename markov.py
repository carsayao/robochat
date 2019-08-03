import markovify
import re
try:
    import simplejson as json
except:
    import json

def main():
    # test
    def get_json():
        out = { 'key': 'value', 'key2': 'value2' }
        print(json.dumps(out))

    def get_text():
        # Get raw text as string.
        with open("iliza-shlesinger_freezing-hot.txt") as f:
            text = f.read()
        # print(text)
        
        # Strip " and '
        cleaned = text.replace('"', '')
        cleaned = cleaned.replace('”', '')
        cleaned = cleaned.replace('“', '')
        # print(cleaned)
        # cleaned = cleaned.replace("'", '')

        # Build the model.
        # text_model = markovify.Text(text, well_formed=True, reject_reg="[\'|\"]")
        # text_model = markovify.Text(text)
        text_model = markovify.Text(cleaned)

        out = { 'text': text_model.make_sentence() }

        print(json.dumps(out))
        
        # Print three randomly-generated sentences of no more than 280 characters
        # for i in range(3):
        #     print(text_model.make_short_sentence(280))

    get_text()


if __name__ == '__main__':
    main()
