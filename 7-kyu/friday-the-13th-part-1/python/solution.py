def kill_count(counselors, jason):
    return [counselor[0] for counselor in counselors if counselor[1] < jason]
