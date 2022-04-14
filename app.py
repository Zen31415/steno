"""."""
import os
from flask import Flask
from flask import request
from flask import g
from steno.messages import bp as messages_blueprint
from steno.db import init_app

application = Flask(__name__, static_folder='static', template_folder='templates')
application.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(application.instance_path, 'steno.sqlite'),
)
init_app(application)
application.register_blueprint(messages_blueprint)

@application.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return "404 not found", 404

if __name__ == '__main__':
    application.run(port=6969, host='0.0.0.0')
