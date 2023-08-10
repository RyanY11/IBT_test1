

import streamlit as st
import pandas as pd

# 内容定义
def idea():
    st.header('本周的重点')
    text1 = '''
    1……  

    2…… 

    3……  
    '''
    st.markdown(text1)

    if st.button('OK，让我们开始吧'):
    
        st.session_state['q1'] = True
        return True
    # else:
    #     return False
    
def observ():
    # with st.form('form1'):
    #     st.header('目标行为/观测点')
    #     st.info('我准备好了重点观察孩子的以下行为表现：')
    #     text2 = '''
    #     观测点1：…… 
        
    #     观测点2：……
    #     '''
    #     st.markdown(text2)
    #     q = st.form_submit_button('明白')
        # if q:
            # st.write('ok')
            # return True

    st.header('目标行为/观测点')
    st.info('我准备好了重点观察孩子的以下行为表现：')
    text2 = '''
    观测点1：…… 
    
    观测点2：……
    '''
    st.markdown(text2)
    if st.button('明白'):
    
        # st.write('ok')
        return True

def tips():
    # with st.form('form2'):
        st.header('对于这些观测点，我们准备了一些技巧')
        st.info('按您的偏好勾选上本周将会选用的技巧吧：')
        c1 = st.checkbox('技巧1')
        c2 = st.checkbox('技巧2')
        c3 = st.checkbox('技巧3')
        
        # q = st.form_submit_button('我选好了')
        q = st.button('我选好了')
        if q:
            # st.write('ok')
            return True

def fin():
    st.header('明白了！')
    st.info('本周我将进行观察，并注意使用这些技巧')
    q = st.button('达成一致，这就开始吧！')
    if q:
        st.info('本周简报到此结束，可以截图保存，我们周后见~')
        return True

if 'q1' not in st.session_state:
    st.session_state['q1'] = None
if 'q2' not in st.session_state:
    st.session_state['q2'] = False
if 'q3' not in st.session_state:
    st.session_state['q3'] = False
if 'q4' not in st.session_state:
    st.session_state['q4'] = False


# 页面绘制
st.title('一周的开始')
st.info('元气满满，新的一周！')
st.write(' ')

print('q1: '+str(st.session_state['q1']))
if st.session_state['q1'] != False:
    # st.session_state['q1'] = idea()
    idea()
    print(st.session_state['q1'])
    if st.session_state['q1'] == True:
        st.session_state['q2'] = True
print('q2: '+str(st.session_state['q2']))
if st.session_state['q2'] != False:
    st.session_state['q2'] = observ()
    if st.session_state['q2'] == True:
        st.session_state['q3'] = True
print('q3: '+str(st.session_state['q3']))
if st.session_state['q3'] != False:
    st.session_state['q3'] = tips()
    if st.session_state['q3'] == True:
        st.session_state['q4'] = True
if st.session_state['q4'] != False:
    st.session_state['q4'] = fin()
    
        

# if q1 == True:
#     st.header('目标行为/观测点')
#     st.info('我准备好了重点观察孩子的以下行为表现：')
#     text2 = '''
#     观测点1：…… 
    
#     观测点2：……
#     '''
#     st.markdown(text2)
#     q2 = st.button('明白')
    
# else:
#     q2 = False

# print(q2)

# if q2 == True:
#     st.header('对于这些观测点，我们准备了一些技巧')
#     st.info('按您的偏好勾选上本周将会选用的技巧吧：')
#     c1 = st.checkbox('技巧1')
#     c2 = st.checkbox('技巧2')
#     c3 = st.checkbox('技巧3')
# else:
#     c1 = False
#     c2 = False
#     c3 = False

# if c1 != False or c2 != False or c3 != False:
#     st.header('明白了！')
#     st.info('本周我将进行观察，并注意使用这些技巧')
#     st.button('达成一致，这就开始吧！')



# flag = False
# if q1 == True:
#     q2 = observ()
#     flag = True
    
# if flag == True:
#     flag = False
#     if q2 == True:
#         q3 = tips()
#         flag = True
    
# if flag == True:
#     flag = False
#     if q3 == True:
    
#         st.header('明白了！')
#         st.info('本周我将进行观察，并注意使用这些技巧')
#         st.button('达成一致，这就开始吧！')