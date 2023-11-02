import openai
import os
openai.api_key = os.environ["openai_key"]


def predict(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    ret = completion.choices[0].message
    return ret["content"]
