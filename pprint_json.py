import json

def load_data(filepath):
    parsed_json = json.loads(filepath, encoding='utf-8')
    return parsed_json


def pretty_print_json(data):
    form_json = json.dumps(parsed_json, indent=4, sort_keys=True)
    print(form_json)


if __name__ == '__main__':
    parsed_json = load_data(filepath)
    pretty_print_json(parsed_json)