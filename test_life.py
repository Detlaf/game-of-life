import pytest
from conway import next_board_state

def test_dead_cells():
    init_state = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state = next_board_state(init_state)

    assert expected_next_state == actual_next_state


def test_dead_cell_come_alive():
    init_state = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state = next_board_state(init_state)

    assert expected_next_state == actual_next_state


