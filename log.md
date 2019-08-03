# log
## jul 31 wed
Starting off, we wanted to use the MLH workshop code to build a chatbot that allows users to chat with an @ of their choice. However, considering rate limitations of the Twitter API, we've decided to instead use transcripts of people (such as stand up comedians) to build the Markov chain bot. From the homepage, a user will be able to select who they would like to chat to.

The plan is to host content from a nodejs server with socketio handling io. A python program will use markovify to turn a transcript into a text model. The front end will be built based off all the tools we have utilized throughout the quarter.

A stretch goal: We want the client to be able to ask question, grab meaningful words from that input (to be further researched) and use it as a seed for the sentence generation.

So far, we have been able to run a python script to markovify text and generate sentences and paragraphs. Secondly, we are able to access this data from the server. What needs to be done now is set up a solid client/server.

### todo
get proper json format from python into server

- miguel

## aug 03 sat
I needed to remove quotations from the text since markovify recognized quotations as part of a word. Used `import re` to replace double quotes but for some reason there were still double quotes in the outputted text. Then I realized there were different types of double quotations so I opened the text file and copied them directly into markov.py. That seemed to do the trick.
