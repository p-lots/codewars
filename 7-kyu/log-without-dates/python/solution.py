def check_logs(log):
    # return the mininum number of days
    if not log:
        return 0
    return sum(prev >= curr for prev, curr in zip(log, log[1:])) + 1
