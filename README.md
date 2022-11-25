# fake-news-bot

This is a machine learning project which runs on a Reddit bot. It scrapes a news article when called on a number of subreddits, and analyzes language patterns using machine learning packages for bias and reliability with roughly 70% accuracy on unseen articles. The Passive Aggressive Classifier runs on a training dataset of 20,799 articles found [here](https://www.kaggle.com/c/fake-news/data?select=train.csv).

### Built with:
#### Web Scraping
- BeautifulSoup4
- Requests

#### Machine Learning
- Pandas
- Scikit-learn (sklearn)
- Pickle

#### Reddit bot connection
- PRAW

# Getting Started
### Prerequisites
- Python 3
- Pip

### Installation
```
$ git clone https://github.com/danielrshackleton/fake-news-bot.git
$ pip install -r requirements.txt
```

## Usage
### In Reddit
To call FakeNewsBot on a reddit post, just comment `!FakeNewsBot` on r/worldnews (will be adding additional subreddits soon).

### To use custom URL links outside of Reddit

This program uses pickled Passive Aggressive Classifier and Vectorizer objects. If there is an issue with these, download train.csv from [here](https://www.kaggle.com/c/fake-news/data?select=train.csv) and move to the data_set directory. 

To use only the article analysis functionality locally: clone the repository, comment out `reddit_conn.connect()` on `fake_news.py` and uncomment `test_run()`, then swap out out the URL string for your article URL and run. 
