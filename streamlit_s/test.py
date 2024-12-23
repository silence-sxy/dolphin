import streamlit as st

# 主标题：给字符设置颜色以及显示表情
st.title('This is a title')
st.title("chatbot :orange[聊天机器人] :smiley:")

#小标题-header
st.header('This is a header with a divider',divider='rainbow')
st.header('Streamlit is :blue[cool] :sunglasses:')

#设置网页名称和标题

st.title("chatbot :orange[聊天机器人] :smiley:")
st.header(':blue[you could ask anything here]',divider='rainbow')

# 文字显示语句
st.text('This is some text.')

# 写入/打印语句
st.write('Hello,**World** :sunglasses:')

# 对话输入指令
a = st.chat_input(placeholder="在这里进行提问")

#显示用户发送的信息
prompt = st.chat_input("Say something")

if prompt:
    st.write(f"User has sent the following prompt:{prompt}")

#多行文本输入语句
txt = st.text_area(
    "Text to analyze",
    "It was the best of times,it was the worse of times,it was the age of"
    "wisdom,it was the age of foolishness,(...)"
    )
st.write(f'you wrote {len(txt)} characters.')

#单行文本输入语句
st.text_input('you are','good')

api_key = st.text_input("Baidu API Key",type = "password")
secret_key = st.text_input("Baidu Secret Key",type="password")

#生成一个边栏
st.sidebar.title("边栏")
api_key = st.sidebar.text_input("Baidu API Key",type="password")
secret_key = st.sidebar.text_input("Baidu Secret Key",type="password")


























