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
see if we can seed the bot.
can we assign a BEGIN to each word in the json model?
