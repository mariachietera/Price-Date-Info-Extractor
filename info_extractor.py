import re
import dateparser

DM_DMY_PATTERN = r"\s\d{1,2}[-/.](?:\d{1,2}[-/.])?\d{1,4}\s"
D_MONTH_Y_PATTERN = r"(\d{1,2}(?:rd|th)?\s(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s(?:\d{2,4})?)"
PRICE_PATTERN = r"\d+[.\d+]?[,\d+]*"
CURRENCY_PRICE_PATTERN = r"({0}\s?" + PRICE_PATTERN + "|" + PRICE_PATTERN + "\s?{0})"


def extract_dates(text):
    all_results = []
    all_results.extend(re.findall(DM_DMY_PATTERN, text))
    all_results.extend(re.findall(D_MONTH_Y_PATTERN, text))

    parsed_results = []
    for result in all_results:
        try:
            #TODO: extract user locale to better estimate expected data format
            valid_date = dateparser.parse(result, settings={'DATE_ORDER': 'DMY'})  # detect locale
            parsed_results.append(valid_date)
        except ValueError:
            pass

    return parsed_results


def extract_prices(text):
    # TODO: extract user locale to better estimate expected currency
    currencies_list = ["€", "\$", "euro", "dollars"]
    tot_results = []
    for currency in currencies_list:
        results = re.findall(CURRENCY_PRICE_PATTERN.format(currency), text, re.IGNORECASE)
        tot_results.extend(results)

    return tot_results


if __name__ == "__main__":

    # live testing
    print("\nEnter text and I will extract prices and dates (Q for exit):")
    new_post = input("> ")
    while new_post != "Q":
        print(extract_prices(new_post))
        print(extract_dates(new_post))
        new_post = input("> ")

    exit(0)