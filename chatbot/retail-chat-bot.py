# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:51:55 2019

@author: Saurav Samantray
"""

from nltk.chat.util import Chat, reflections
from greetings import pairs as greetpair
from questions import pairs as quespair
pairs = [
 [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
# extending individual pairs to for the final set of pairs
pairs.extend(greetpair)
pairs.extend(quespair)
#print(pairs)
def retailchat():
    print("Hi, I'm Conver the chat bot\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    retailchat()
    pass