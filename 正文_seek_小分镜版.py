from openai import OpenAI
import re
# 初始化 OpenAI 客户端，使用你的 API 密钥

client = OpenAI(api_key="sk-029ef31805dc4a2e944e89a161367a8e", base_url="https://api.deepseek.com")


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

def func(result,filename = 'output.txt',slp=5):
    #print(result)
    import time
    time.sleep(slp)
    # 使用'a'模式打开文件，这将允许你将内容追加到文件末尾
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(result + '\n')  # 将result追加到文件末尾，并添加换行符
        



# 开始对话
import time
N=10
time.sleep(N)

# 使用gbk编码打开文件
with open('人物设定.txt', 'r', encoding='utf-8') as file:
    人物设定 = file.read()

with open('故事背景.txt', 'r', encoding='utf-8') as file:
    故事背景 = file.read()
    
with open('小分镜.txt', 'r', encoding='utf-8') as file:
    分镜内容 = file.read()

# 正则表达式匹配章节和分镜

chinese_number_pattern = r'[零一二三四五六七八九十百千]+'
    
    # 构造正则表达式匹配模式
pattern = rf'第{chinese_number_pattern}章第{chinese_number_pattern}分镜第{chinese_number_pattern}小分镜'

# 使用正则表达式进行分割
split_results = re.split(pattern, 分镜内容)
# 用于存储分镜内容的列表
keywords = re.findall(pattern, 分镜内容)
scenes = []


# 输出分割后的结果
for result in split_results:
    scenes.append(result.strip())
    print(result.strip())

scenes=scenes[1:]
scenes=[(keywords[i],scenes[i]) for i in range(len(keywords))]
    
###
#print(chat("假设你是一名优秀的网络小说写手，请帮我按照下面的故事梗概，重新写小说内容，需要加入一些生动的对话，还有人物外貌心理描写。", history))
result=chat("假设你是一名优秀的网络小说写手，\
    小说的故事背景如下：%s\
        ,每一章的分镜内容如下%s,整部小说出现的主要人物包含%s，下面我每提示一个分镜，你帮我展开描写可以吗?"%(故事背景,分镜内容,人物设定), history)
print(result)

history.append(
    {"role": "system", "content": "假设你是一名优秀的网络小说写手，\
    小说的故事背景如下：%s\
        ,每一章的分镜内容如下%s,整部小说出现的主要人物包含%s，下面我会告诉你当前是第几章第几分镜第几小分镜，并用三重引号提示一小段内容，\
     请你将三重引号内的内容展开为一段大约3000字的小说描写，需要符合人物性格设定，根据需要加入一些语言外貌心理描写，语言生动,注意不要出现逻辑错误,注意不要写其他分镜的内容"%(故事背景,分镜内容,人物设定)},
    )

k=3
for scene in scenes[9*k-9:9*k]:
    #history=history_checkpoint.copy()
    result=chat('%s\n\"\"\"%s\"\"\""'%scene, history)
    func(result,filename = '正文chp%s.txt'%str(k),slp=10)
    print('chat length',len(history))

with open('正文chp%s.txt'%str(k), 'r', encoding='utf-8') as file:
    正文tmp = file.read()