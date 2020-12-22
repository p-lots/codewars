def cat_mouse(x):
    c_idx = x.index('C')
    m_idx = x.index('m')
    return 'Caught!' if abs(c_idx - m_idx) <= 4 else 'Escaped!'
