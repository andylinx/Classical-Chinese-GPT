import warnings
warnings.filterwarnings ("ignore")
import sys
import torch
from bigdl.llm.transformers import AutoModelForCausalLM
#print("成功接入程序")
save_path = "D:\cs_courses\Classical-Chinese-GPT\ChatGLM3-int4"
model_path = "D:\cs_courses\Classical-Chinese-GPT\ChatGLM3-int4"

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

import re

word_dic={}
with open('vocab.txt', 'r',encoding='utf-8') as file:
    for line in file:
        split_points = [match.start() for match in re.finditer(r'\d+', line)]
        split_points.append(len(line))
        start = 0
        pos=1
        word=""
        for point in split_points:
            substring = line[start:point]
            if len(substring)>=1:
                if pos==1:
                    word=substring[-1]
                    pos=0
                    word_dic.setdefault(word, [])
                else:
                    word_dic[word].append(substring)
            start = point

import time

def output(messa = ""):
   message = messa
   message = message.encode('utf-8')
   sys.stdout.buffer.write(message)
   sys.stdout.flush()
   time.sleep(0.1)

def get_keywords(sentence):
    key_words = {}
    for i in sentence[0]:
     if i in word_dic.keys():
        res = ""
        value = word_dic[i]
        res = res + str(i) + ":\n"
        for item in value:
           res = res + str(item) + "\n"
        key_words[i] = res
    for _,ele in key_words.items():
       output(ele)

output("准备就绪，快来和我聊天吧\n")

while 1:
  prompt = sys.stdin.buffer.readline()
  prompt = prompt.strip().decode('utf-8')
  res = get_answer(prompt)
  res_out = ''.join(res) + "\n"
  output(res_out)
  result = inference(res)
  result_out = ''.join(result) + "\n"
  output(result_out)
  get_keywords(result)