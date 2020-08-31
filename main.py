#!/usr/bin/env python3

from functions import analyzer, scraper, reddit_conn


def test_run(url):
    text = scraper.get_data(url)
    print(f'\n\nURL: {url}')
    result = analyzer.analyze(text)
    print(result)


if __name__ == '__main__':
    # Run with custom URL (uncomment this to run)
    url = 'https://www.reuters.com/article/us-japan-politics-abe/ailing-abe-quits-as-japan-pm-as-covid-19-slams-economy-key-goals-unmet-idUSKBN25O00F'
    test_run(url)

    # reddit_conn.connect()
