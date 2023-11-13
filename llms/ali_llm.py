from http import HTTPStatus
import dashscope

VERSION = "alibaba"


def predict(prompt: str):
    response = dashscope.Generation.call(
        model=dashscope.Generation.Models.qwen_turbo,
        prompt=prompt,
    )

    if response.status_code == HTTPStatus.OK:
        return response.output.text
    else:
        raise Exception('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == '__main__':
    print(predict("广州在哪里？"))
