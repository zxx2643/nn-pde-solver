print("line 1")
import tensorflow as tf
import horovod.tensorflow as hvd
hvd.init()
print(hvd.size())
print("line 6")
