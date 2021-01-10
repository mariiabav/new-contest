from typing import List

import pytest

from .task import task7


class Case:
    def __init__(self, name: str, distance: int, startFuel: int, stations: List[List[int]], answer: int):
        self._name = name
        self.distance = distance
        self.startFuel = startFuel
        self.stations = stations
        self.answer = answer

    def __str__(self) -> str:
        return 'task7_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        distance=100,
        startFuel=10,
        stations=[
            [10, 60],
            [20, 30],
            [30, 30],
            [60, 40]
        ],
        answer=2,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task7(case: Case) -> None:
    answer = task7(
        distance=case.distance,
        startFuel=case.startFuel,
        stations=case.stations,
    )
    assert answer == case.answer
