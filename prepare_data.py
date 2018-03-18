"""Prepare data for shakesperification training"""
import codecs
import re

from os import listdir, path

ALLOWED_SPECIAL = ['.', ',', '?', '!', '“', '”', '-']
KEEP_CHAR = "[^ a-zA-Z0-9'’{}]".format(''.join(ALLOWED_SPECIAL))
DATA_PATH = './data'


def get_matching_files(data_path):
    """Returns aligned files with original and modern."""
    files = listdir(data_path)
    modern = [x for x in files if ('modern' in x and 'aligned' in x)]
    original = [x for x in files if ('original' in x and 'aligned' in x)]
    return original, modern


def read_files(data_path, files):
    """Load files."""
    total_content = []
    for file in files:
        with open(path.join(data_path, file), encoding='utf8') as file_handle:
            content = [line.strip() for line in file_handle]
        total_content = total_content + content
    return total_content


def preprocess_data(data):
    """Preprocess every sentence in dataset."""
    data_processed = data
    for idx, sentence in enumerate(data):
        sentence_processed = first_char_lower(sentence)
        sentence_processed = space_around_special(sentence_processed)
        sentence_processed = remove_forbidden_special(sentence_processed)
        data_processed[idx] = sentence_processed
    return data_processed


def first_char_lower(sentence):
    """Makes fist char in sentence lowercase unless it starts with I."""
    if sentence[0:1] != 'I':
        return sentence[0].lower() + sentence[1:]
    return sentence


def space_around_special(sentence):
    """Places a spaces around allowed special chars to see them as words"""
    for special in ALLOWED_SPECIAL:
        sentence = sentence.replace(special, (' ' + special + ' '))
    return sentence


def remove_forbidden_special(sentence):
    """Remove all special characters except the ones in WORD_CHARS"""
    return re.sub(KEEP_CHAR, '', sentence)


def prepare_data():
    """Prepares data"""
    original_files, modern_files = get_matching_files(DATA_PATH)

    original_data = read_files(DATA_PATH, original_files)
    original_data_processed = preprocess_data(original_data)

    modern_data = read_files(DATA_PATH, modern_files)
    modern_data_processed = preprocess_data(modern_data)

    training_data = codecs.open('training_data.txt', 'w', 'utf-8')
    for idx, _ in enumerate(original_data_processed):
        training_data.write(original_data_processed[idx] + '\t' + modern_data_processed[idx] + '\n')
    training_data.close()


if __name__ == "__main__":
    prepare_data()
