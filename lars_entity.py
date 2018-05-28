#!/usr/bin/env python3

import sys
import os
import requests

def req(inpstr):
	r = requests.post("https://api.nb.no/ngram/ner", json = {'text': inpstr})
	print(r.json())

if __name__ == '__main__':
	input_text_file = "test_tekst.txt"
	with open(input_text_file, "r") as f:
		inp_str = f.read()


	req(inp_str)

