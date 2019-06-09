### Sentiment Analysis ###

[VaderSentiment](https://github.com/cjhutto/vaderSentiment)

[Bokeh](https://bokeh.pydata.org/en/latest/)

[spaCy](https://spacy.io/models/en)

[Pandas](http://pandas.pydata.org/)

[Flask](http://flask.pocoo.org/)

### Usage: ###

##### Activate environment #####
```$ source bin/activate ```

##### Install requirements #####
```$ pip install -r requirements.txt```

##### Update dictionary #####
```$ python -m spacy download en_core_web_sm```  
```$ python -m spacy download en_core_web_md```  
```$ python -m spacy download en_core_web_lg```  

##### Snapshot Capture #####
![alt text](./img.png "GO8 Sentiment Analysis")


##### Run app #####
```$ python gots8sentimentAnalysis.py```

##### Run Flask Server: #####
```$ FLASK_APP=app.py flask run```

```$ curl http://localhost:5000 --header "Content-Type: application/json" --data "I love applesauce!"```


You can also use Postman if you like.

Note: not all the modules in requirements.txt is necessary, only whatever is stated in this README.md file.

