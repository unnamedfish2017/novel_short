# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:25:19 2024

@author: admin
"""
import time
import subprocess
ROOT_PATH='黄粱梦'

脚本流=['人物设定.py','章节分镜.py','正文_seek.py']
for v in 脚本流:
    subprocess.run(['python', v, ROOT_PATH])
    print(v,'finished!')
    time.sleep(10)