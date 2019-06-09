import spacy
from vaderSentiment import vaderSentiment
import flask


app = flask.Flask(__name__)
english = spacy.load("en_core_web_md")
analyzer = vaderSentiment.SentimentIntensityAnalyzer()

def get_sentiments(text):
    result = english(text)
    sentences = [str(s) for s in result.sents]
    sentiments = [analyzer.polarity_scores(str(s)) for s in sentences]
    return sentiments


@app.route("/", methods=["POST", "GET"])
def index():
    if flask.request.method == "GET":
        return "To access this service send a POST with the text you want to analyze"
    body = flask.request.data.decode("utf-8")
    sentiments = get_sentiments(body)
    return flask.json.dumps(sentiments)
