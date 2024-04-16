def modify_multiply(st, loc, num):
    st_split = st.split(' ')
    return '-'.join(st_split[loc] for _ in range(num))
