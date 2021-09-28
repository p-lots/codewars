def shifter(st): 
    SHIFTER_CHARS = 'HINOSXZMW'
    st_split = set(st.split())
    return sum(1 for word in st_split if all(ch in SHIFTER_CHARS for ch in word))
