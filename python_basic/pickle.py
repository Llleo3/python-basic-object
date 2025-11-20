#pickle 存放数据
import pickle
# 要序列化的对象（可以是列表、字典、自定义类等）
data = {
    "name": "张三",
    "age": 25,
    "hobbies": ["跑步", "读书"]
}
def dump(x,y):
    return None
# 以二进制模式写入文件（pickle必须用二进制模式）
with open("data.pickle", "wb") as f:
    dump(data,f)  # 将对象序列化后写入文件

print("对象已保存到 data.pickle")


