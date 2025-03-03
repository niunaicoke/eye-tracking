from collections import Counter


def compute_transition_entropy(transitions):
    """
    计算过渡熵（H_t）
    :param transitions: List，每个元素是 (from_AOI, to_AOI) 形式的转移
    :return: H_t 值
    """
    transition_counts = Counter(transitions)  # 统计每个转移的次数
    total_transitions = sum(transition_counts.values())  # 总转移次数

    # 计算转移概率
    p_ij = {k: v / total_transitions for k, v in transition_counts.items()}

    # 避免 log2(0) 计算错误
    p_values = np.array(list(p_ij.values()))
    p_values = p_values[p_values > 0]

    # Shannon 熵计算
    H_t = -np.sum(p_values * np.log2(p_values))
    return H_t


# 示例数据：模拟用户的视线转移序列
fixation_sequence = ["Guide", "OR", "Guide", "Progbars", "Guide", "OR", "Combined total screen", "Guide"]
transitions = list(zip(fixation_sequence[:-1], fixation_sequence[1:]))  # 生成 (from, to) 形式的转移对

H_t = compute_transition_entropy(transitions)
print(f"过渡熵 H_t: {H_t:.4f} bits")
