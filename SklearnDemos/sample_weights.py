"""
根据labels序列进行统计，生成对应的sample权重
或者根据指定的权重字典，生成对应的sample权重
"""

import numpy as np


def sample_weights_cal(labels, flag=0, class_weights=None):
    """
    :param labels: 样本labels
    :param flag: 0-返回权重字典，1-返回labels同维的权重序列
    :return: 权重字典或权重序列
    """
    try:
        labels = np.array(labels)
    except TypeError:
        print("输入格式错误")
    assert labels.ndim == 1

    labels_set = set(labels)
    labels_value = list(labels_set)

    labels_count = np.array([(labels==l).sum() for l in labels_value])
    sample_ratio = labels_count.prod()/labels_count

    sample_ratio_std = sample_ratio / sample_ratio.sum()

    sample_weights_dict = {i: round(j, 4) for i, j in zip(labels_value, sample_ratio_std)}

    if not class_weights:
        if flag == 0:
            return sample_weights_dict
        else:
            sample_weights_info = np.zeros(shape=labels.shape)
            for i in range(sample_weights_info.shape[0]):
                sample_weights_info[i] = sample_weights_dict.get(labels[i])
            return sample_weights_info

    else:
        assert isinstance(class_weights, dict)    # 必须为字典
        assert flag==1   # 必须返回序列
        assert labels_set == set(class_weights.keys())
        class_weights_sum = np.array(list(class_weights.values())).sum()
        print(class_weights_sum)
        for key, value in class_weights.items():
            class_weights[key] = value/class_weights_sum

        sample_weights_info = np.zeros(shape=labels.shape)
        for i in range(sample_weights_info.shape[0]):
            sample_weights_info[i] = class_weights.get(labels[i])
        return sample_weights_info


if __name__ == '__main__':
    y = [1, 2, 1, 2, 3, 4]
    result= sample_weights_cal(y, flag=1, class_weights={1:0.1,2:0.1,3:0.4,4:0.4})
    print(result)