from llms.baidu_llm import predict

u_score_prompt = '''You are a dictionary.
You rate the word in terms of frequency of use, from 0 to 10, with 0 indicating not commonly used, and 10 indicating very commonly used.
You're now going to rate 4 words.
When you see [LAST ONE], the next word is your last word, then you only write one word.

Hi
answer: 8 / reason: This word is often used in English when greeting.

world
answer: 6 / reason: This word will be used as a part of a phrase or just a noun.

teacher
answer: 8 / reason: When discussing school matters, this word is likely to be used.

[LAST ONE]
{word}
answer: '''

w_score_prompt = '''You are an intermediate English learner. You know some basic words, but you want to learn those words that are not frequently used, yet are quite important.
You rate the word in terms of necessity to mark down, from 0 to 10, with 0 indicating not necessary or not worth marking down at all, and 10 indicating very necessary.
You're now going to rate 5 words.
When you see [LAST ONE], the next word is your last word, then you only write one word.

mirror
answer: 2 / reason: A tool we use our daily life. But i've already known.

orchestra
answer: 8 / reason: This word comes not so oftenly but if you don't get it, you're not going to understand the whole sentence.

Hi
answer: 0 / reason: I've learned that before.

what
answer: 0 / reason: I've learned that before.

[LAST ONE]
{word}
answer: '''

e_score_prompt = '''You rate the word in terms of being an English word, from 0 to 10, with 0 indicating not an English word at all, and 10 indicating absolutely an English word.
You're now going to rate 9 words.
When you see [LAST ONE], the next word is your last word, then you only write one word.

Baidu
answer: 0 / reason: It's a Chinese company.

D.O.A
answer: 10 / reason: It's an abbreviation of dead on arrival.

EMO
answer: 10 / reason: It's an abbreviation.

Bonjour
answer: 0 / reason: It's how they say hello in French.

6
answer: 2 / reason: It's a number.

Book
answer: 10 / reason: It's an English word.

.
answer: 2 / reason: It is a punctuation mark.

]
answer: 1 / reason: It is a punctuation mark.

[LAST ONE]
{word}
answer: '''

s_content_prompt = '''
You are restoring the word to its original form, like you want to write it in a dictionary.
You're going to write 7 more. 
When you see [LAST ONE], the next word is your last word, then you only write one word.
For the word "Book", is: book
For the word "Numbers" is: number
For the word "O-okay" is: ok
For the word "Hiiii" is: hi
For the word "-fitting" is: fit
For the word "-of-work" is: off-work
[LAST ONE]
For the word "{word}" is:
'''

p_content_prompt = '''
You are an excellent English teacher.
You are preparing to write the phonetic transcriptions for 5 words. 
When you see [LAST ONE], the next word is your last word, then you only write one word.
The pronunciation of the word "symbol" in IPA is: /ˈsɪmbəl/
The pronunciation of the word "robot" in IPA is: /ˈroʊbɑːt/
The pronunciation of the word "robot" in IPA is: /ˈroʊbɑːt/
The pronunciation of the word "orchestra" in IPA is: /ˈɔːrkɪstrə/
[LAST ONE]
The pronunciation of the word "{word}" in IPA is: 
'''

m_content_prompt = '''
You are an excellent English teacher.
You're going to explain the meanings of "{word}"
The meaning is:
'''

e_content_prompt = '''
You are an excellent English teacher.
For the word '{word}',
Here are three example sentences:
'''


def get_score(score_source: str):
    return int(score_source.split(":")[1].strip())


def eng_word_score(word):
    prompt = e_score_prompt.format(word=word)
    result = predict(prompt)
    return int(result)


def worth_to_learn_score(word):
    prompt = w_score_prompt.format(word=word)
    result = predict(prompt)
    return int(result)


def usual_word_score(word):
    prompt = u_score_prompt.format(word=word)
    result = predict(prompt)
    return int(result)


def spell_format(word):
    prompt = s_content_prompt.format(word=word)
    result = predict(prompt)
    return result


def pronounce(word):
    prompt = p_content_prompt.format(word=word)
    result = predict(prompt)
    return result


def meaning(word):
    prompt = m_content_prompt.format(word=word)
    result = predict(prompt)
    return result


def examples(word):
    prompt = e_content_prompt.format(word=word)
    result = predict(prompt)
    return result


def feed(word: str, th=3) -> dict:
    e_score = eng_word_score(word)
    if e_score <= th:
        return None
    else:
        ret = dict()
        ret['e_score'] = e_score
        ret['w_score'] = worth_to_learn_score(word)
        ret['u_score'] = usual_word_score(word)

        ret['pronounce'] = pronounce(word)
        ret['meaning'] = meaning(word)
        ret['examples'] = examples(word)
        # ret['word'] = spell_format(word)
        ret['word'] = word

        return ret
