from transformers import AutoTokenizer, AutoModel


def predict(prompt: str) -> str:
    tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)
    model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True, device='cuda')
    model = model.eval()
    response, history = model.chat(tokenizer, prompt, history=[])
    return response
