# -*- coding: utf-8 -*-

def check_with_base_week(base_week, week):
    """
    :param week: "2021.34","2021.9"...
    :param base_week: like week
    :return: -1 less
             0  equal
             1 bigger
    """
    week_lst = [int(t) for t in week.split('.')]
    base_week_lst = [int(t) for t in base_week.split('.')]
    if len(week_lst) != len(base_week_lst):
        raise Exception("week format error!")
    for i in range(len(base_week_lst)):
        if week_lst[i] > base_week_lst[i]:
            return 1
        elif week_lst[i] < base_week_lst[i]:
            return -1
    return 0
