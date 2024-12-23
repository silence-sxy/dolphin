import streamlit as st

#程序为老师参考，学生直接编程就可以
#要求老师提前安装好streamlit这个库，并尝试程序可以跑不出错

st.title("chatbot :orange[聊天机器人] :smiley:")
st.header(" :blue[_you could ask anything here_]",divider="rainbow")
st.text("使用文心一言模型-提问内容不限")

prompt=st.chat_input("在这里提问")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


st.text_area("安全提示","请确保您的问题合法、合规且合理，不涉及违法、违规、敏感或攻击性内容。尊重他人，保护隐私。违反规定者，我们将采取必要措施处理。感谢理解与合作，期待您提出有价值的问题。")



st.sidebar.title("边栏")
api_key = st.sidebar.text_input("Baidu API Key", type="password")
secret_key = st.sidebar.text_input("Baidu Secret Key", type="password")

result = st.sidebar.button("提交",type="primary")
st.write(result)
if result:
    st.sidebar.write('已提交')
else:
    st.sidebar.write('请填写APIkey')


st.sidebar.link_button("go get API","https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application")

select = st.sidebar.radio("你觉得回答有用吗？",["有用","无用","有点用"],captions = ["值得鼓励","需要提升","继续努力"])
st.sidebar.write("you selected:",select)

st.snow()

