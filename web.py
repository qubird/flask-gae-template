import flask


def create_app(config):
    """
    :param config: optional configuration dictionary
    :return: the Flask instance
    """

    app = flask.Flask(__name__)
    app.config.update(config)

    return app

app = create_app({
    'debug': True
    })

@app.route('/')
def index():
	return 'Home'
