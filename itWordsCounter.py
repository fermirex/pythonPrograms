from multiprocessing import Process, Pool, Queue
from concurrent.futures import ProcessPoolExecutor
import os

dir = r"C:/Users/86155/Desktop/rsm/it_words_counter/"
words_file = "IT_General IT_BEA_noTag.zh.cln"
dict_file = "MicrosoftTermCollection_en-US_zh-CN.zh"
counter_file = "counter.txt"

#  创建消息队列, 最多存放消息数量
q = Queue(20)
executor = ProcessPoolExecutor(max_workers=9)

def writeTofile():
    with open(dir + counter_file, mode="w", encoding="utf8") as counterMessageHandler:
        while True:
            try:
                data = q.get(timeout=5)
                if data:
                    counterMessageHandler.write(data)
            except:
                break

def dict_word_checker(wordToBeChecked):
    counter = words_file_content.count(wordToBeChecked)
    print("process {} find {} occured {} times".format(os.getpid(), wordToBeChecked, counter))
    q.put(wordToBeChecked, counter)

with open(dir + words_file,'r',encoding="UTF8") as f_words:
    words_file_content = f_words.read()
    with open(dir + dict_file, "r", encoding= "UTF8") as f_dict:
        while True:
            dict_content = f_dict.readline()
            future = executor.submit(dict_word_checker, dict_content)
            if future.done():
                continue




