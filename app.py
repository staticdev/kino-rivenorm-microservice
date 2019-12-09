# -*- coding: utf-8 -*-

""" Microservice for RiveNorm normalization method """

import flask
from rivescript import RiveScript


def create_app():
    """ Application factory """
    bot = RiveScript(
        debug=True,
        utf8=True
    )

    bot.load_directory("brain")
    bot.sort_replies()

    app = flask.Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # retrieve UTF-8 messages

    @app.route('/reply', methods=['POST'])
    def reply():
        """Fetch a reply from RiveScript.
        Parameters (JSON):
        * username
        * message
        """
        params = flask.request.json
        if not params:
            return flask.jsonify({
                "status": "error",
                "error": "Request must be of the application/json type!",
            })

        username = params.get("username")
        message = params.get("message")

        # Make sure the required params are present.
        if username is None or message is None:
            return flask.jsonify({
                "status": "error",
                "error": "username and message are required keys",
            })

        # Get a reply from the bot.
        reply = bot.reply(username, message)

        # Send the response.
        return flask.jsonify({
            "status": "ok",
            "reply": reply
        })

    return app
