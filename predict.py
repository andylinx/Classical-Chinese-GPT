import warnings
warnings.filterwarnings ("ignore")

import torch

from bigdl.llm.transformers import AutoModelForCausalLM

save_path = "/mnt/d/cs_courses/Classical-Chinese-GPT/ChatGLM3-int4"
model_path = "/mnt/d/cs_courses/Classical-Chinese-GPT/ChatGLM3-int4"

model = AutoModelForCausalLM.load_low_bit(save_path,
                                          trust_remote_code=True)

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(model_path,
                                          trust_remote_code=True)

CHATGLM_V2_PROMPT_TEMPLATE = "问:{prompt}\n\n中文回答:"

n_predict = 32 #max_new_tokens parameter in the generate function defines the maximum number of tokens to predict.

from transformers import EncoderDecoderModel

PRETRAINED = "./TranslateModel"

trans_tokenizer = AutoTokenizer.from_pretrained(PRETRAINED)
trans_model = EncoderDecoderModel.from_pretrained(PRETRAINED)

def inference(text):
    tk_kwargs = dict(
      truncation=True,
      max_length=256,
      padding="max_length",
      return_tensors='pt')

    inputs = trans_tokenizer([text,],**tk_kwargs)
    with torch.no_grad():
        return trans_tokenizer.batch_decode(
            trans_model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            num_beams=3,
            max_length=512,
            bos_token_id=101,
            eos_token_id=102,
            pad_token_id=trans_tokenizer.pad_token_id,
        ), skip_special_tokens=True)

def get_answer(prompt):
  with torch.inference_mode():
    prompt = CHATGLM_V2_PROMPT_TEMPLATE.format(prompt=prompt)
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids,
                            max_new_tokens=n_predict)
    res = tokenizer.decode(output[0], skip_special_tokens=True)
    return res[len(prompt)+11:]


prompt = input("今天想聊点什么呢？\n")
while 1:
  res = get_answer(prompt)
  print(inference(res))
  prompt = input()