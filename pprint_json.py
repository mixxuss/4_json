import json, argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')
    return parser


def load_data(filepath):
    parsed_json = json.loads(filepath, encoding='utf-8')
    return parsed_json


def pretty_print_json(data):
    form_json = json.dumps(parsed_json, indent=4, sort_keys=True)
    return form_json


if __name__ == '__main__':
    parsed_args = create_parser()
    filepath = parsed_args.parse_args()
    print(filepath.filepath)
    parsed_json = load_data(filepath.filepath)
    pretty_print_json(parsed_json)