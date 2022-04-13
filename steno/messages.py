"""This is meant to pass rudimentary messages."""
#from crypt import methods
#import functools, random, string

from unittest.mock import DEFAULT
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

from steno.db import get_db
#from flaskr.auth import login, login_required

bp = Blueprint('messages_blueprint', __name__)

@bp.route("/messages", methods=['GET'])
def getmessages():
    """Display all messages."""
    db = get_db()
    messages = db.execute(
        'SELECT s.title, body, id, created'
        ' FROM steno s'
        ' ORDER BY created DESC'
    ).fetchall()
    return messages

# This is how "/messages GET" was supposed to be first, and it works.
#    """This gets all messages."""
#    return 'This gets all messages'
@bp.route("/messages", methods=['POST'])
def postmessage():
    """Create a new message."""
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, id, created)'
                ' VALUES (?, ?, ?, ?)',
                (title, body, DEFAULT, DEFAULT)
            )
            db.commit()
            return db
    return db

#The next 2 lines are how I was supposed to do this for now.
#    """This posts a new message."""
#    return(request.data)

@bp.route("/messages/<int:id>", methods=['GET'])
def getmessage(id):
    message = (
        get_db()
        .execute(
            "SELECT s.title, body, id, created"
            "   FROM steno s"
            "   WHERE id = ?",
            (id,),
        )
        .fetchone()
    )

    if message is None:
        abort(404, f"Post id {id} doesn't exist.")

    return message

# This is how I did this to begin with and didn't work anyways.
#    """This gets a specific message"""
#    return ('This gets message ',id,'.')
@bp.route("/messages/<int:id>", methods=['PATCH'])
def updatemessage():
    """Update a message."""
    message = getmessage(id)

    if request.method == "PATCH":
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE steno SET title = ?, body = ? WHERE id = ?", (title, body, id)
            )
            db.commit()
            return message

    return message

#    return message, f("Message ID {id} has been updated.")

# This is how I did this to begin with and didn't work anyways.
#    """This updates a specific message."""
#    return(request.data)
