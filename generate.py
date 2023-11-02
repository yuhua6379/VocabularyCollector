import logging

from log_conf import conf
from sentence_extrator import get_extractor
import os
import json
import llm_dictionary


def extract_word_collection(source: str):
    output = source + ".wc.json"
    if os.path.exists(output):
        with open(output, "r") as fp:
            return output, json.loads(fp.read())

    extractor = get_extractor(source)
    word_collection = extractor.run()

    with open(output, "w") as fp:
        fp.write(json.dumps(word_collection))

    return output, word_collection


def rating_and_explaining(source: str):
    if source.find(".wc.json") == -1:
        raise RuntimeError(f"source file ({source}) has error format which needs '*.wc.json'")

    with open(source, "r") as fp:
        word_collection = json.loads(fp.read())

        output = source.replace(".wc.json", "")
        output = output + ".re.json"

        word_dictionary = dict()
        for word in word_collection:
            try:
                ret = llm_dictionary.feed(word)
                print(ret)
                if ret is None:
                    continue
            except Exception as e:
                import traceback
                logging.warning(f"{word} comes an exception {traceback.format_exception(e)}")
        with open(output, "w") as fp:
            fp.write(json.dumps(word_dictionary))

        return output, word_dictionary


if __name__ == '__main__':
    conf()
    path = 'resources./friends_scripts_10_seasons.pdf'
    output, word_collection = extract_word_collection(path)
    print(f"we've got {len(word_collection)} words from file '{path}'!")

    output, word_dictionary = rating_and_explaining(output)