# -*- coding:utf-8 -*-
import  tensorflow as tf
import numpy as np
#
x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

xs =tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])

#
def add_layer(inputs,in_size,out_size,activation_fouction=None):
    weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    wx_plus_b = tf.matmul(inputs,weights) + biases
    if activation_fouction==None:
        outputs = wx_plus_b
    else:
        outputs = activation_fouction(wx_plus_b)
    return outputs
h1 = add_layer(xs,1,20,activation_fouction=tf.nn.relu)
prediction = add_layer(h1,20,1,activation_fouction=None)
#
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys -prediction),reduction_indices=[1]))
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)


#train
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


for i in range(50000):
    sess.run(train_op,feed_dict={xs:x_data,ys:y_data})
    if i % 50 == 0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))

