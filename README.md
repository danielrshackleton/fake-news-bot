# fake-news-bot

This is a reddit bot which scrapes a news article when posted to any of a number of subreddits, and analyzes it for fake news with 96% accuracy (deviates roughly 0.5% each way). The training dataset used contains 20,799 articles.

### Built with:
#### Web Scraping
- BeautifulSoup4
- Requests

#### Machine Learning
- Pandas
- Scikit-learn (sklearn)

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
To use the article analysis functionality, simply comment out the reddit connection on `main.py`, swap out out the URL string for your article URL and run.
