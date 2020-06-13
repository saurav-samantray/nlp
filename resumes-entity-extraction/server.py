from flask import Flask, render_template, request, json, send_from_directory, Response
from flask_caching import Cache

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

config = {
	"CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

@app.route("/health", methods=["GET"])
def heath():
    return Response(json.dumps({"status":"UP"}), status=200, mimetype='application/json')


@app.route("/cache-flush", methods=["POST"])
def cache_flush():
	cache.clear()
	return Response(json.dumps({"success":True}), status=200, mimetype='application/json')

@app.route('/text-ner')
def text_ner_view():
	return render_template('text-ner.html')