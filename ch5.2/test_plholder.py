import tensorflow as tf

# プレースホルダー定義 (型、shape)
# Noneを使うとそこは無制限実行時に決まる２つの要素を持つリスト無制限
a = tf.placeholder(tf.int32, [None,2])

# ベクトルを２倍にする演算を定義
two = tf.constant(2)
double_op = a * two


# セッションを開始
sess = tf.Session()

sample_list =[[1,1],[2,2],[3,3],[4,4]]
res = sess.run(double_op, feed_dict={a:sample_list})
print(res)
