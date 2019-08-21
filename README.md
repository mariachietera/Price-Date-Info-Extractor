# Price and Dates Info Extractor

This folder contains a script meant to extract info regarding Prices and Dates out ouf texts - for example Facebook Posts in housing groups.
Mainly based on regular expressions but also using [dateparser](https://dateparser.readthedocs.io/en/latest/) to increase data recognition.

## Setup

Create a virtualenv with python 3.* (tested on Python3.7.2) and install [dateparser](https://dateparser.readthedocs.io/en/latest/).

### Usage:
Run:
```
> info_extractor.py 
> Enter text and I will extract prices and dates (Q for exit):
```

  Test the functions inserting any string or try the following example post:
```
> I need to leave my apartment on 30/06 so I am looking for a free room starting from 30th Jun 2019 or 15 Jul at latest. Price range from 400€ to max euro 500 ($570). Please call me only on 20.06.19 afternoon. Thanks!
```

Output:
```
['400€', '$570', 'euro 500']
[datetime.datetime(2019, 6, 30, 0, 0), datetime.datetime(2019, 6, 20, 0, 0), datetime.datetime(2019, 6, 30, 0, 0), datetime.datetime(2019, 7, 15, 0, 0)]
```