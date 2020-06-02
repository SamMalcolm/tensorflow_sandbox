import os
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 

#os.environ['TF_CPP_MIN_LOG_LEVEL'] = 2

X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")

addition = tf.add(X,Y,name="addition")

with tf.Session() as session:
	result = session.run(addition, feed_dict = {X: [1], Y:[4]})
	print(result)