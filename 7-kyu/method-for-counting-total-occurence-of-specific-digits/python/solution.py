class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        ret = []
        int_str_list = [list(str(i)) for i in integers_list]
        dig_str_list = [str(dig) for dig in digits_list]
        for dig_str in dig_str_list:
            cnt = (int(dig_str), 0)
            for integer in int_str_list:
                cnt = (cnt[0], cnt[1] + integer.count(dig_str))
            ret.append(cnt)
        return ret
