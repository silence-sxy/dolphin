##import random
##
##def gift_exchange(participants):
##    # 打乱参与者名单，确保配对是随机的
##    random.shuffle(participants)
##    
##    # 创建一个字典存储配对结果
##    pairs = {}
##    
##    # 将参与者两两配对
##    for i in range(len(participants)):
##        # 每个人的配对是下一个人，最后一个人的配对是第一个人
##        pairs[participants[i]] = participants[(i + 1) % len(participants)]
##    
##    # 打印配对结果
##    for giver, receiver in pairs.items():
##        print(f"{giver} -> {receiver}")
##
### 示例参与者名单
##participants = ["", "Bob", "Charlie", "David", "Eva"]
##
### 调用函数进行礼物互换配对
##gift_exchange(participants)
##

import streamlit as st
import random

# 16个名字列表
names = [
    '柏彬彬', '马凯','孙侠玲','费一帆','孙馨怡','徐梦晴','马琪','王观达','高超南','何伟','高敏',
    '崔盼玉','刘双双','高天琪','程辉','张白茹'
]

# 随机打乱名字的顺序
def shuffle_names(names):
    shuffled_names = names[:]
    random.shuffle(shuffled_names)
    return shuffled_names

# 配对并返回结果
def create_pairs(names):
    shuffled_names = shuffle_names(names)
    # 将名字分为8对，保证每个人配对一次
    pairs = [(shuffled_names[i], shuffled_names[i+1]) for i in range(0, len(shuffled_names), 2)]
    return pairs

# Streamlit 应用内容
st.title('🎄 圣诞礼物随机互换 🎁')

# 描述文字
st.markdown("""
    点击下方的按钮来随机匹配16个人的圣诞礼物。每个人会随机分配一个送礼对象，确保每个人只能送礼一次！
""")

# 创建按钮
if st.button('开始匹配'):
    pairs = create_pairs(names)
    st.subheader('配对结果：')

    # 显示每个配对
    for giver, receiver in pairs:
        st.write(f'{giver} 🎁 → {receiver}')

    st.success('配对完成！')



