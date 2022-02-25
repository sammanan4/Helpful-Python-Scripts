"""
Get a list of possible formats of a datetime string
"""
import re
import itertools
from datetime import datetime
def get_date_format(date_str: str) -> set: 
        FORMAT_CODES = (
            r'%a', r'%A', r'%w', r'%d', r'%b', r'%B', r'%m', r'%y', r'%Y',
            r'%H', r'%I', r'%p', r'%M', r'%S', r'%f', r'%z', r'%Z', r'%j',
            r'%U', r'%W',
        )

        TWO_LETTERS_FORMATS = (
            r'%p',
        )

        THREE_LETTERS_FORMATS = (
            r'%a', r'%b'
        )

        LONG_LETTERS_FORMATS = (
            r'%A', r'%B', r'%z', r'%Z',
        )

        SINGLE_DIGITS_FORMATS = (
            r'w',
        )

        TWO_DIGITS_FORMATS = (
            r'%d', r'%m', r'%y', r'%H', r'%I', r'%M', r'%S', r'%U', r'%W',
        )

        THREE_DIGITS_FORMATS = (
            r'%j',
        )

        FOUR_DIGITS_FORMATS = (
            r'%Y',
        )

        LONG_DIGITS_FORMATS = (
            r'%f',
        )

        # Non format code symbols
        SYMBOLS = (
            '\\/',
            '\\-',
            ':',
            '+',
            'Z',
            ',',
            ' ',
        )

        date_str = date_str.upper()

        # Split with non format code symbols
        pattern = r'[^{}]+'.format(''.join(SYMBOLS))

        components = re.findall(pattern, date_str)

        # Create a format placeholder, eg. '{}-{}-{} {}:{}:{}+{}'
        placeholder = re.sub(pattern, '{}', date_str)

        formats = []
        for comp in components:
            if re.match(r'^\d{1}$', comp):
                formats.append(SINGLE_DIGITS_FORMATS)
            elif re.match(r'^\d{2}$', comp):
                formats.append(TWO_DIGITS_FORMATS)
            elif re.match(r'^\d{3}$', comp):
                formats.append(THREE_DIGITS_FORMATS)
            elif re.match(r'^\d{4}$', comp):
                formats.append(FOUR_DIGITS_FORMATS)
            elif re.match(r'^\d{5,}$', comp):
                formats.append(LONG_DIGITS_FORMATS)
            elif re.match(r'^[a-zA-Z]{2}$', comp):
                formats.append(TWO_LETTERS_FORMATS)
            elif re.match(r'^[a-zA-Z]{3}$', comp):
                formats.append(THREE_LETTERS_FORMATS)
            elif re.match(r'^[a-zA-Z]{4,}$', comp):
                formats.append(LONG_LETTERS_FORMATS)
            else:
                formats.append(FORMAT_CODES)

        # Create a possible format set
        possible_set = itertools.product(*formats)

        result_set = set()
        for possible_format in possible_set:
            # Create a format with possible format combination
            dt_format = placeholder.format(*possible_format)
            try:
                dt = datetime.strptime(date_str, dt_format)
                # Use the format to parse the date, and format the 
                # date back to string and compare with the origin one
                if dt.strftime(dt_format).upper() == date_str:
                    result_set.add(dt_format)
            except Exception:
                continue

        return result_set
if __name__=="__main__":
	print(get_date_format("22-10-2013"))
