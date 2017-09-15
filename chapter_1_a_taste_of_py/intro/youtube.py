import json
from urllib.request import urlopen
url = "https://gdata.youtube.com/feeds/api.standardfeeds/top_rated?alt=json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
	print(video['title']['$t'])

'''
• 第 1 行：从 Python 标准库中导入名为 json 的所有代码。
• 第 2 行：从 Python 标准 urllib 库中导入 urlopen 函数。
• 第 3 行：给变量 url 赋值一个 YouTube 地址。
• 第 4 行：连接指定地址处的 Web 服务器并请求指定的 Web 服务。
• 第 5 行：获取响应数据并赋值给变量 contents。
• 第 6 行：把 contents 解码成一个 JSON 格式的文本字符串并赋值给变量 text。
• 第 7 行：把 text 转换为 data——一个存储视频信息的 Python 数据结构。
• 第 8 行：每次获取一个视频的信息并赋值给变量 video。
• 第 8 行：使用两层 Python 字典（data['feed']['entry']）和切片操作（[0:6]）。
• 第 9 行：使用 print 函数打印出视频标题。
'''