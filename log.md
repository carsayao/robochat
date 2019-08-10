# log
## jul 31 wed
Starting off, we wanted to use the MLH workshop code to build a chatbot that allows users to chat with an @ of their choice. However, considering rate limitations of the Twitter API, we've decided to instead use transcripts of people (such as stand up comedians) to build the Markov chain bot. From the homepage, a user will be able to select who they would like to chat to.

The plan is to host content from a nodejs server with socketio handling io. A python program will use markovify to turn a transcript into a text model. The front end will be built based off all the tools we have utilized throughout the quarter.

A stretch goal: We want the client to be able to ask question, grab meaningful words from that input (to be further researched) and use it as a seed for the sentence generation.

So far, we have been able to run a python script to markovify text and generate sentences and paragraphs. Secondly, we are able to access this data from the server. What needs to be done now is set up a solid client/server.

### todo
get proper json format from python into server

## aug 1 thu
I am now able to use python to generate a string, format it into json, pass it to the server, convert to a string, and finally pass it to the client. My only problem was that I wasn't turning the buffer stream from python into a proper json object.

### todo
see if we can seed the markov bot, if we can, see how to extract the most meaningful phrases or words from a sentence to seed it

## aug 03 sat
I needed to remove quotations from the text since markovify recognized quotations as part of a word. Used `import re` to replace double quotes but for some reason there were still double quotes in the outputted text. Then I realized there were different types of double quotations so I opened the text file and copied them directly into markov.py. That seemed to do the trick.

I was able to also combine all the text of a single person's transcripts located in a dir to create a larger markov model. We can also store that model as a json to disk, and load it from disk. This should help with performance.

However, I'm still trying to see if we can seed the generated text from user input. So far, Text.make_sentence_with_start() looks promising, but it seems that the word must be from a word the transcript begins a sentence with.

### todo
see if we can seed the bot

## aug 05 mon
Basic tidying after React lecture. Created /src to hold all source code. Placed texts into /texts. Modified code to handle new directories.

### todo
see if we can seed the bot.
can we assign a BEGIN to each word in the json model?

## aug 8 thu
Got close.

To seed a generated sentence, we may pass in an init_state when calling the markovify.Text.make_sentence(state) from markov.py, where state must be a tuple that exists in the keys of the markovify model dictionary. I modified the markovify lib file chain.py so that when Text.make_sentence() calls self.chain.walk(init_state), it accepts init_state with only the first arg filled in. This is done with the function find_state(state) in chain.py. It takes the first arg of state, which should be what the user passed in, and iteratese through the keys of the dictionary until it finds an instance of the input in a key. The found key is then passed back as the inital state.

It works, but spelling has to be exact. For instance `init_state=('standing','')` works, but `init_state=('standi','')` does not. `('family','') ` does not work but `('family,','')` does. We need to work on being able to account for these discrepencies.

One way to do this is to find the Levenshtein distance between two strings. The shorter the distance, the closer the match.

I found a Levenshtein implementation in the pyAudioAnalysis library that I've copied into src/test. Haven't got this working yet, but once it's finished, we should be just about done with the back end. The nltk (natural language toolkit) may be worthwhile to look at but I haven't yet had a chance to look at it.

To find my code, go to lib/markovify and run the command `grep -rnw './' -e 'M:'`. I marked where user input would be added with a `TODO` in markov.py.

### todo
use a levenshtein, or similar, implementation to match user input strings to the closest match in the generated markov model's keys.

## aug 9 fri
Found a working Levenshtein implementation and it tested great. Added nltk (natural language toolkit) to find nouns of a sentence, then randomly choose one noun to seed generation.

Also got to set up a virtualenv that includes my forked markovify library that allows for seeding sentence generation.

### todo
add the Levenshtein function and nltk methods to forked lib and we can have a somewhat engaging chatroom. 
