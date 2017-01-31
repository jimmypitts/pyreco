actions = [
    {
        'action': 'email',
        'email-id': 123,
        'customer-id': 1,
        'email-action': 'open'
    },
    {
        'action': 'email',
        'email-id': 123,
        'customer-id': 1,
        'email-action': 'receive'
    },
    {
        'action': 'email',
        'email-id': 123,
        'customer-id': 2,
        'email-action': 'receive'
    }
]


class Item():

    def __init__(self):
        raise NotImplementedError

    def get_row_id(self):
        raise NotImplementedError

    def get_column_id(self):
        raise NotImplementedError

    def get_score(self):
        raise NotImplementedError

    def is_valid(self):
        raise NotImplementedError


class EmailItem(Item):

    def __init__(self, data):
        self.row_id = data['customer-id']
        self.column_id = "{}-{}".format(data['email-id'], data['email-action'])
        self.email_action = data['email-action']

    def get_row_id(self):
        return self.row_id

    def get_column_id(self):
        return self.column_id

    def get_score(self):
        if self.email_action == 'click':
            return 1
        if self.email_action == 'open':
            return 0.5
        if self.email_action == 'receive':
            return 0.25

    def is_valid(self):
        return True

class Neighborhood:

    def __init__(self, items, row_func):
        self.matrix = {}
        self.items = items
        self._load_matrix(items)


    def _load_matrix(self, items):
        for item in items:
            if not item.is_valid():
                continue

    def process(self):
        raise NotImplementedError



items = []
for action in actions:
    item = EmailItem(action)
    items.append(item)

for item in items:
    score = item.get_score()
    print(score)
    error = item.is_valid_item()
