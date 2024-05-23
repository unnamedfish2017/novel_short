from openai import OpenAI
import os
import sys
ROOT_PATH=sys.argv[1]
# 初始化 OpenAI 客户端，使用你的 API 密钥
client = OpenAI(api_key="sk-3sq88ly5bVhIQNbuqPi7xPiLlG5mtNrucHI0LbHK6RnDmDGb", base_url="https://api.moonshot.cn/v1")

# 初始系统消息，定义助手的角色和能力
system_message = {
    "role": "system",
    "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。"
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
        model="moonshot-v1-32k",
        messages=history,
        temperature=0.3,
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

with open(os.path.join(ROOT_PATH,'故事背景.txt'), 'r', encoding='utf-8') as file:
    故事背景 = file.read()

result=chat("假设你是一名优秀的网络小说写手，擅长渡边淳一的写作风格\
    要创作一部小说，小说的故事大致如下：%s\
        ,请帮我设定整部小说出现的人物,每个人要有具体姓名,以 姓名，性别，年龄，外貌描写，性格特点，爱好 的格式输出"%故事背景, history)
func(result,filename = '人物设定.txt',slp=10)
