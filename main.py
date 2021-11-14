# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:47:37 2021

@author: indhu
"""

#main.py
from flask import Flask, jsonify, request
from db import get_songs, add_songs

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def songs():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400  

        add_songs(request.get_json())
        return 'Song Added'

    return get_songs()    

if __name__ == '__main__':
    app.run()
