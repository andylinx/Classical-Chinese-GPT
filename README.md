![image](https://github.com/andylinx/Classical-Chinese-GPT/blob/main/image/%E9%98%9F%E5%BE%BD.png)
# 问·道（Seeking The Classic）
Algorithm Comprehend Heritage



## 项目简介
**问·道**是一款面向广大中小学生开发的私人文言文学习助手，旨在帮助中小学生更好掌握文言文知识。

基于[ChatGLM3-6B](https://github.com/THUDM/ChatGLM3)，以及[wenyanwen-chinese-translate-to-ancient](https://huggingface.co/raynardj/wenyanwen-chinese-translate-to-ancient) 两个模型，使用了**Bigdl-llm**的INT4量化策略进行压缩部署。

第一代 **问·道** 能够支持无需gpu的部署，对RAM占用较小，且有着良好的对话质量。



## 内容说明

- ChatGLM3-int4 : 对话大模型
- TranslateModel : 翻译大模型
- crawler.py: 数据爬虫
- vocab.txt: 文言字词数据
- requirements.txt: 环境依赖文件
- bigdl_llm_lowbit.py: 模型压缩 (无需重复运行)
- main.py: 主体运行文件
- 问·道.pdf : 项目技术报告



## 使用教程

使用 pip 安装依赖：

```
pip install -r requirements.txt
```

- 为了保证 `torch` 的版本正确，请严格按照 [官方文档](https://pytorch.org/get-started/locally/) 的说明安装。



#### 模型压缩部分

可以直接从仓库下载压缩后的模型文件，亦可以从huggingface上获取完成版
而后运行我们的压缩程序进行压缩

```
python3 bigdl_llm_lowbit.py
```



#### 主体运行

```
python3 main.py
```

**即可开始对话学习啦~**





## Demo


![image](https://github.com/andylinx/Classical-Chinese-GPT/blob/main/image/demo1.png)

**文言字词教学模式**

![image](https://github.com/andylinx/Classical-Chinese-GPT/blob/main/image/demo2.png)
