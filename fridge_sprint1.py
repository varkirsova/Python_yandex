import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


def normalize_date(expiration_date):
    if expiration_date:
        expiration_date_formatted = datetime.datetime.strptime(
            expiration_date, DATE_FORMAT
        )
        expiration_only_date = expiration_date_formatted.date()
        return expiration_only_date
    else:
        return None


def add(items, title, amount, expiration_date=None):
    if title in items.keys():
        for key, value in items.items():
            if key == title:
                new_dict = {
                    'amount': amount,
                    'expiration_date': normalize_date(expiration_date)
                }
                value.append(new_dict)

    else:
        new_list = list()
        items[title] = new_list
        new_dict = {
            'amount': amount,
            'expiration_date': normalize_date(expiration_date)
        }
        new_list.append(new_dict)


def add_by_note(items, note):
    list_goods = note.split()
    if '-' in list_goods[-1]:
        expiration_date = list_goods[-1]
        list_goods.pop(-1)
    else:
        expiration_date = None
    amount = Decimal(list_goods[-1])
    list_goods.pop(-1)
    title = ' '.join(list_goods)
    add(items, title, amount, expiration_date)


def find(items, needle):
    list_finded = []
    for keys in items.keys():
        if needle.lower() in keys.lower():
            list_finded.append(keys)
    return list_finded


def get_amount(items, needle):
    total = Decimal('0')
    titles = find(items, needle)

    for title in titles:
        for purchase in items[title]:
            total += purchase['amount']

    return total


def get_expired(items, in_advance_days=0):
    expired_products = []
    date_today = (datetime.date.today()
                  + datetime.timedelta(days=in_advance_days))
    for key, lists in items.items():
        total_count = Decimal('0')
        expired_product_list = list()

        for purchase in lists:
            if purchase['expiration_date'] is None:
                continue
            if date_today >= purchase['expiration_date']:
                total_count += purchase['amount']
        expired_product_list.append(key)
        expired_product_list.append(total_count)
        if total_count > 0:
            expired_products.append(tuple(expired_product_list))

    return expired_products
