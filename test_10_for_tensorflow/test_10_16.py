# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/16 15:21
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm

# import tensorflow as tf
# import numpy as np
#
# #create data
# x_data = np.random.rand(100).astype(np.float32)
# # print(x_data)
# # print('#######################################')
# y_data = x_data*0.1 + 0.3
#
# #create tensorflow structure start
# Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
# # print(Weights)
# # print('...............................................')
# biases = tf.Variable(tf.zeros([1]))
# # print(biases)
#
# #预 测 值 Y
# y = Weights*x_data + biases
# #预测差别
# loss = tf.reduce_mean(tf.square(y-y_data))
# #优化器
# optimizer = tf.train.GradientDescentOptimizer(0.5)
# #减少误差
# train = optimizer.minimize(loss)
# #初始化结构
# init = tf.initialize_all_variables()
#
# #create tensorflow structure end
# #神经网络的 指针？
# sess = tf.Session()
# sess.run(init)          #Very important
#
# for step in range(201):
#     sess.run(train)
#     if step % 20 == 0:
#         print(step,sess.run(Weights),sess.run(biases))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''              session with double method             '''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import tensorflow as tf
#
# matrix1 = tf.constant([[3,3]])
# matrix2 = tf.constant([[2],[2]])
#
# product = tf.matmul(matrix1,matrix2)
#
# #method 1
# # sess = tf.Session()
# # result = sess.run(product)
# #
# # print(result)
# # sess.close()
#
# #method 2
# with tf.Session() as sess:
#     result2 = sess.run(product)
#     print(result2)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''              variable 变量     '''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import tensorflow as tf
#
# state = tf.Variable(0,name='counter')
# # print(state.name)
# #常量
# one = tf.constant(1)
#
# new_value = tf.add(state,one)
# #将new_value的值  加载到state中，下一次生效
# update = tf.assign(state,new_value)
# # 初始哈 所有变量  ，然后用session.run激活
# init = tf.initialize_all_variables()    #must have if define variable
#
# with tf.Session() as sess:
#     sess.run(init)
#     for _ in range(3):
#         sess.run(update)
#         print(state)
#         print('===============')
#         print(sess.run(state))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''              placeholder 传入     '''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import tensorflow as tf
#
# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
#
# output = tf.multiply(input1,input2)
#
# with tf.Session() as sess:
#     print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))
#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''              激励函数                           '''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import tensorflow as tf
import numpy as np

def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size])+0.1)
    Wx_plus_b = tf.matmul(inputs,Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])
l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)
prediction = add_layer(l1,10,1,activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                     reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(100000000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i % 5000 == 0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))













