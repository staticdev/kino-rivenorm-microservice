# -*- coding: utf-8 -*-
from sys import argv
from flask import Flask, request, jsonify
from rivescript import RiveScript


def create_app(test_config=None):
    bot = RiveScript(
        debug=True,
        utf8=True
    )

    bot.load_directory("brain")
    bot.sort_replies()

    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # retrieve UTF-8 messages

    @app.route('/reply', methods=['POST'])
    def reply():
        """Fetch a reply from RiveScript.
        Parameters (JSON):
        * username
        * message
        * vars
        """
        params = request.json
        if not params:
            return jsonify({
                "status": "error",
                "error": "Request must be of the application/json type!",
            })

        username = params.get("username")
        message = params.get("message")
        uservars = params.get("vars", dict())

        # Make sure the required params are present.
        if username is None or message is None:
            return jsonify({
                "status": "error",
                "error": "username and message are required keys",
            })

        # Copy and user vars from the post into RiveScript.
        if type(uservars) is dict:
            for key, value in uservars.items():
                bot.set_uservar(username, key, value)

        # Get a reply from the bot.
        reply = bot.reply(username, message)

        # Send the response.
        return jsonify({
            "status": "ok",
            "reply": reply
        })

    return app
