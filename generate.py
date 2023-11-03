import logging
from log_conf import conf
from sentence_extrator import get_extractor
import os
import json
import llm_dictionary
from datasource.config import rdbms_instance
from datasource.rdbms.entities import WordModel

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


def has_word(session, word):

    filter_ = session.query(WordModel)
    filter_ = filter_.filter(WordModel.word == word)
    results = filter_.all()
    return len(results) > 0


def add_word(session, ret, prefix):
    word = WordModel()
    word.english_score = ret["e_score"]
    word.worth_score = ret["w_score"]
    word.usual_score = ret["u_score"]

    word.english_reason = ret["e_reason"]
    word.worth_reason = ret["w_reason"]
    word.usual_reason = ret["u_reason"]

    word.version = ret["version"]

    word.meaning = ret["meaning"]
    word.pronounce = ret["pronounce"]
    word.examples = ret["examples"]
    word.word = ret["word"]
    word.prefix = prefix

    session.add(word)
    session.commit()


def rating_and_explaining(source: str):
    if source.find(".wc.json") == -1:
        raise RuntimeError(f"source file ({source}) has error format which needs '*.wc.json'")
    prefix = os.path.split(source)[-1].split(".")[0]
    print(f"write to session {prefix}")
    with open(source, "r") as fp:
        word_collection = json.loads(fp.read())

        for word in word_collection:
            try:
                with rdbms_instance.get_session() as session:
                    if has_word(session, word):
                        # 跳过已经写入的word
                        print("skip", word)
                        continue
                    print("dealing", word)
                    ret = llm_dictionary.feed(word)
                    if ret is None:
                        continue

                    add_word(session, ret, prefix)

            except Exception as e:
                import traceback
                traceback.print_exc()


def run():
    conf()
    path = './resources/friends_scripts_10_seasons.pdf'
    output, word_collection = extract_word_collection(path)
    print(f"we've got {len(word_collection)} words from file '{path}'!")

    output, _ = rating_and_explaining(output)
    print("save to", output)


if __name__ == '__main__':
    run()
