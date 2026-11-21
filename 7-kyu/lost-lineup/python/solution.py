def find_lineup(distances):
    sorted_dists = [(idx, dist) for idx, dist in sorted(enumerate(distances, 1), key=lambda pair: pair[1])]
    original_order = [i for i, _ in sorted_dists]
    final_dists = [d for _, d in sorted_dists]
    return original_order \
        if all(lhs == rhs for lhs, rhs in zip(range(len(distances)), final_dists)) \
        else []
