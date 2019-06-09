### Sentiment Analysis ###

[VaderSentiment](https://github.com/cjhutto/vaderSentiment)

[Bokeh](https://bokeh.pydata.org/en/latest/)

[spaCy](https://spacy.io/models/en)

[Pandas](http://pandas.pydata.org/)

[Flask](http://flask.pocoo.org/)

##### Usage: ####
__Activate environment__
```$ source bin/activate ```

__Install requirements__
```$ pip install -r requirements.txt```

__Update dictionary__
```$ python -m spacy download en_core_web_sm```

__Run app__
```$ python gots8sentimentAnalysis.py```

#### Run Flask Server: ####
```FLASK_APP=app.py flask run```

```curl http://localhost:5000 --header "Content-Type: application/json" --data "I love applesauce!"```

Note: not all the modules in requirements.txt is necessary, only whatever is stated in this README.me file