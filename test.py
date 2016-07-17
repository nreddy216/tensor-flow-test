import tensorflow as tf

# x is a placeholder - value that we will input
x = tf.placeholder(tf.float32, [None, 784])



#Variable is a modifiable tensor that lives in TF's graph of interacting operations
W = tf.Variable(tf.zeros([784, 10]))
