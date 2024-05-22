from openai import OpenAI
import os

# 初始化 OpenAI 客户端，使用你的 API 密钥

client = OpenAI(api_key="sk-029ef31805dc4a2e944e89a161367a8e", base_url="https://api.deepseek.com")
ROOT_PATH='./柳生'

# 初始系统消息，定义助手的角色和能力
system_message = {
    "role": "system",
    "content": "你是一名优秀的网络小说作家。"
}

# 多轮对话历史记录
history = [system_message]

def chat(query, history):
    # 将用户的问题添加到对话历史中
    history.append({
        "role": "user",
        "content": query
    })
    
    # 发送请求到 Moonshot AI
    completion = client.chat.completions.create(
        model="deepseek-chat",
        messages=history,
        temperature=1.25,
    )
    
    
    # 获取生成的回复
    result = completion.choices[0].message.content
    
    # 将助手的回复也添加到对话历史中
    history.append({
        "role": "assistant",
        "content": result
    })
    
    return result

def func(result,filename = 'output.txt',slp=5,ROOT_PATH=ROOT_PATH):
    print(result)
    import time
    time.sleep(slp)
    # 使用'a'模式打开文件，这将允许你将内容追加到文件末尾
    with open(os.path.join(ROOT_PATH,filename), 'a', encoding='utf-8') as file:
        file.write(result + '\n')  # 将result追加到文件末尾，并添加换行符


# 开始对话
import time
N=10
time.sleep(N)

with open(os.path.join(ROOT_PATH,'人物设定.txt'), 'r', encoding='utf-8') as file:
    人物设定 = file.read()

with open(os.path.join(ROOT_PATH,'故事背景.txt'), 'r', encoding='utf-8') as file:
    故事背景 = file.read()
    

result=chat("假设你是一名优秀的网络小说写手，\
    请帮我写一部小说，小说的故事背景如下：%s\
        ,请将整部小说内容分成10章，你只需要概括描述每一章的内容。整部小说出现的主要人物包含%s,不必每个人物都出现在每个章节中,故事情节需要比较曲折，富有悬念"%(故事背景,人物设定), history)
func(result,filename = '章节内容.txt',slp=10)

for i in range(1,10):
    result=chat("请将第%i章内容分3个场景分镜叙述。每个分镜需要描写出场人物及故事梗概,注意请以第几章第几分镜作为开头"%i, history)
    func(result,filename = '分镜.txt',slp=10)
