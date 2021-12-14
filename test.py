# -*- coding: utf-8 -*-
from __future__ import absolute_import

from time.week import check_with_base_week


def test_check_with_base_week():
    data_lst = [
        ("2021.3",  "2021.2", -1),
        ("2021.03", "2021.02", -1),
        ("2021.3",  "2021.4",  1),
        ("2021.3",  "2021.44", 1),
        ("2021.23", "2021.8", -1),
        ("2021.23", "2021.1", -1),
        ("2021.23", "2021.44", 1),
        ("2021.3",  "2020.4", -1),
        ("2021.3",  "2020.44",-1),
        ("2021.3",  "2020.4", -1),
        ("2021.3",  "2022.1",  1),
        ("2021.33", "2022.1",  1),
        ("2021.33", "2022.43", 1),
        ("2021.33", "2022.03", 1),
    ]

    for base_week, week, want in data_lst:
        assert check_with_base_week(base_week, week) == want


if __name__ == "__main__":
    test_check_with_base_week()