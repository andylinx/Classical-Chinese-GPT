# The initial model of ChatGLM2 is about 12G in total which is space pricey.
# It also need 13GB RAM to make inferences, which is always unaffordable for a PC.
# So we can use bigdl-llm model to perform model compression.
# After that, under 6GB is required for INT4 quantized reasoning.

!pip install --pre --upgrade bigdl-llm[all]

# load the model from huggingface 

from bigdl.llm.transformers import AutoModel

model_path = "THUDM/chatglm2-6b"
model = AutoModel.from_pretrained(model_path,
                                  load_in_4bit=True,
                                  trust_remote_code=True)

# Save the low bit model

save_directory = './ChatGLM2-int4'

model.save_low_bit(save_directory)

del(model)

#We can load the model via the save_directory