import sys
sys.path.append('../')
from pde_utility import plot_PDE_solutions, plot_fields, split_data, expand_dataset, exe_cmd, BatchData, plot_one_field_hist, plot_one_field_stat, plot_one_field,plot_PDE_solutions_new
import tensorflow as tf
import numpy as np


class BatchData(tf.keras.utils.Sequence):
    """Produces a sequence of the data with labels."""
    """Borrowed from: class MNISTSequence(tf.keras.utils.Sequence) """

    def __init__(self, data, batch_size=128):
        """Initializes the sequence.

    Args:
      data: Tuple of numpy `array` instances, the first representing images and
            the second labels.
      batch_size: Integer, number of elements in each training batch.
    """
        self.features, self.labels = data
        # self.features, self.labels = BatchData.__preprocessing(images, labels)
        self.batch_size = batch_size

    def __len__(self):
        return int(tf.math.ceil(len(self.features) / self.batch_size))  # contains batches less than the size of batch_size
        # return int(len(self.features) / self.batch_size) # all batches are equal-sized.

    def __getitem__(self, idx):
        batch_x = self.features[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.labels[idx * self.batch_size:(idx + 1) * self.batch_size]
        return batch_x, batch_y

if __name__ == '__main__':
    tot_img = 7
    features = np.random.rand(1000,16,16,3)
    labels = np.random.rand(1000,16,16,1)
    dataset2 = tf.data.Dataset.from_tensor_slices( (tf.convert_to_tensor(features, dtype=tf.float32), tf.convert_to_tensor(labels, dtype=tf.float32)) )

    batch_size = 32
    batched_dataset2 = dataset2.batch(batch_size)
    print(dataset2, batched_dataset2)

    the_feature, the_label = expand_dataset(features, labels, times=1)
    train_dataset, train_label, val_dataset, val_label, test_dataset, test_label = split_data(the_feature, the_label, batch_size, split_ratio=['0.8', '0.1', '0.1'])
    # self.train_dataset, self.train_label, self.val_dataset, self.val_label, self.test_dataset, self.test_label = split_data(the_feature, the_label, split_ratio=['0.1', '0.1', '0.8'])
    train_seq = BatchData(data=(train_dataset, train_label), batch_size=batch_size)
    val_seq   = BatchData(data=(val_dataset,   val_label),   batch_size=batch_size)
    test_seq  = BatchData(data=(test_dataset,  test_label),  batch_size=batch_size)
    print('len of features: ', np.shape(the_feature), 
          'len of training data: ', np.shape(train_dataset), 
          'len of test data: ', np.shape(test_dataset), 
          'batch size: ', batch_size, 
          'total train batches: ', len(train_seq),
          'total val batches: ', len(val_seq),
          'total test batches: ', len(test_seq),
          )
    for b0 in batched_dataset2.prefetch(1):
        print(b0)
