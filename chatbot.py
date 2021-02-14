'''
Using the Chatterbot -corpus
Gets input from the user
Processes the input and returns value that generated the highest confidence value from logic adapters
Returns response to the user
'''
from flask import Flask, render_template, request
from chatterbot import Chatterbot
