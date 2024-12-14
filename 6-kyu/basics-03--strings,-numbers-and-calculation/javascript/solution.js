const calculateString = st => Math.round(eval(st.replace(/[^\d\.\+\-\*\/]/g, ""))).toString();
