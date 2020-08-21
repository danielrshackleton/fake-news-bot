from functions import analyzer
from functions import scraper


if __name__ == '__main__':

    url = 'https://ahtribune.com/us/2016-election/242-trump-grandfather-pimp-father-kkk.html'
    text = scraper.get_data(url)
    result = analyzer.analyze(text)

    print(result)



