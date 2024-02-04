from typing import List
import utils

def subability(atk:float, available_subability:int)->List[int]:
    subability_lv:int = available_subability * 100
    max_total_atk:float = utils.round_decimal(atk * (1 + 0.000152 * subability_lv), 0)
    top_lv:int = -1
    second_lv:int = -1

    while True:
        subability_lv-=1
        total_atk:float = utils.round_decimal(atk * (1 + 0.000152 * subability_lv), 0)
        if max_total_atk > total_atk and top_lv < 0:
            top_lv = subability_lv + 1
        if (max_total_atk - 1) > total_atk and second_lv < 0:
            second_lv = subability_lv + 1
            break

    return[top_lv, second_lv]