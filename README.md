# ChatGPT-HTTPAPI
基于acheong08/ChatGPT的revChatGPT.V1和Flask的ChatGPT的http json api  
这是一个本人自用QQ机器人的的ChatGPT聊天接口，现已开源  
当然，本程序只是一个接口，你需要通过本程序的接口进行开发  
你可以随意的修改代码实现你想要的功能  
如果这个接口对你有帮助的话，不要忘记点个star哦🌹  
本程序有效性跟随 https://github.com/acheong08/ChatGPT 
如果你发现了本程序失效了可尝试更新revChatGPT 

python小白，如果写的太烂，勿喷😅


# 需要安装的python库
```python
pip install --upgrade revChatGPT
```

```python
pip install Flask
```

# 运行

```python
python main.py
```

# 配置文件
```json
{
    "auth": {
        "access_token": ""
    },
    "port": 8080,
    "path": "/"
}
```
或者
```json
{
    "auth": {
        "email": "email",
        "password": "your password"
    },
    "port": 8080,
    "path": "/"
}
```
auth中填入token或者账号密码（推荐token）  
port为http端口  
path为请求路径 

# 请求方式  
POST请求 `0.0.0.0:8080/`  
Body传入4个长度的数组

`["讲个笑话","7cdf5d80-68b2-49ca-b43f-f29139f927b2","4dc1433b-ce65-4101-9d67-a23a1ec361dc","getSeesions"]`  

第一个为对话内容  
第二个为会话ID  
第三个为父ID  
第四个为随意内容，为getSeesions时，将获取新的会话id  


# 示例请求结果  
```json
{
    "code": 200,
    "data": {
        "message": "Hello! How can I assist you today?",
        "conversation_id": "65051b21-87b4-42f2-8f5f-6d552c2c266a",
        "parent_id": "10fa7bc5-4499-4016-b97b-e95b5ff48659",
        "model": "text-davinci-002-render-sha",
        "finish_details": "stop",
        "end_turn": true,
        "recipient": "all"
    },
    "err": "null"
}
```









