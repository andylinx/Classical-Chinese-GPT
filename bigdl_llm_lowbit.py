import torch

from bigdl.llm.transformers import AutoModel

model_path = "THUDM/chatglm3-6b"

model = AutoModel.from_pretrained(model_path,
                                  load_in_4bit=True,
                                  trust_remote_code=True)

save_path = "./ChatGLM3-int4"
model.save_low_bit(save_path)
