import tensorflow as tf

# 定数を定義
a = tf.constant(5, dtype=tf.float64, name ='5')
b = tf.constant(10, dtype=tf.float64, name ='10')
c = tf.constant(8, dtype=tf.float64, name ='8')
d = tf.constant(7, dtype=tf.float64, name ='7')

# 演算を定義
add_op = tf.add(a,b, name='add')
mul_op = tf.multiply(c,d, name ='mul')
cal_op = tf.multiply(add_op, mul_op, name ='cal')


# セッションを開始
sess = tf.InteractiveSession()
res1 = sess.run(add_op)
res2 = sess.run(mul_op)
res3 = sess.run(cal_op)
print(res1)
print(res2)
print(res3)

# tensorflowのためにグラフを出力
summary_writer = tf.summary.FileWriter('./logs',sess.graph)
summary_writer.close()
