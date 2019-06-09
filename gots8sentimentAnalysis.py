from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure
from vaderSentiment import vaderSentiment
import spacy
import pandas as pd

output_file("stacked_split.html")
sentiments = {}
negative = []
neutral = []
positive = []
com = []
english = spacy.load("en_core_web_lg")
analyzer = vaderSentiment.SentimentIntensityAnalyzer()
df = pd.read_csv("got_s8_sentiments.csv")
comments = df["Comment"]
users = df["User"]
dataSource = ColumnDataSource(df)
output_file("stacked_split.html")
classifiers = ["negative", "neutral", "positive"]

def get_sentiments(text):
    result = english(text)
    sentences = [str(s) for s in result.sents]
    sentiments = [analyzer.polarity_scores(str(s)) for s in sentences]
    return sentiments

for comment in comments:
    sentiment = get_sentiments(comment)[0]
    negative.append(sentiment['neg'] * -1)
    neutral.append(sentiment['neu'])
    positive.append(sentiment['pos'])
    com.append(sentiment['compound'])

factors = {'users' : users,
           'comments' : comments,
           'negative' : negative,
           'neutral' : neutral,
           'positive' : positive,
           'compound' : com }

p = figure(y_range=users, plot_height=800, plot_width=1200, x_range=(-1, 1), title="Sentiments of GoT S8 Finale",
           toolbar_location=None)

p.hbar_stack(classifiers, y='users', height=0.9, color=OrRd3, source=ColumnDataSource(factors),
             legend=["%s sentiments" % x for x in classifiers])


p.y_range.range_padding = 0.1
p.ygrid.grid_line_color = None
p.legend.location = "top_left"
p.axis.minor_tick_line_color = None
p.outline_line_color = None

hover = HoverTool()
hover.tooltips = """
  <div>
    <div><strong>Comment: </strong><span width=50 style="width: 42px">@comments</span></div>
    <div><strong>Negative: </strong>@negative</div>
    <div><strong>Neutral: </strong>@neutral</div>
    <div><strong>Positive: </strong>@positive</div>
    <div><strong>Compound: </strong>@compound</div>
  </div>
"""
p.add_tools(hover)

show(p)