# fake-news-bot

This is a reddit bot which scrapes a news article when posted to any of a number of subreddits, and analyzes it for fake news with 96% accuracy (deviates roughly 0.5% each way). The training dataset used contains 20,799 articles.

### Built with:
#### Web Scraping
- BeautifulSoup4
- Requests

#### Machine Learning
- Pandas
- Scikit-learn (sklearn)
- Pickle

#### Reddit bot connection
- Praw

# Getting Started
### Prerequisites
- Pipenv

### Installation
```
$ git clone https://github.com/danielrshackleton/fake-news-bot.git
$ pipenv install
```

# Usage
### In Reddit
To call FakeNewsBot on a reddit post, just comment `!FakeNewsBot`

### To use custom URL links outside of Reddit
To use the article analysis functionality, simply clone the repository, comment out the reddit connection on `main.py`, swap out out the URL string for your article URL and run.
