from typing import Dict
import utils

def multiplier(atk:int, lv_subability:int, char_rarity:int, ship_troop:bool, ship_attr:bool, ship_rarity:int, weak:bool, total_damage:int)->Dict[str, float]:
    min_mul_dmg:Dict[str,float]={
        "atk":0,
        "atk_buff":0,
        "mul_dmg_buff":0,
        "total_dmg":0,
        "mul_dmg":1001
    }

    for i in range(10):
        for j in range(10000):
            corr_atk:float = (i - 5) / 10
            corr_total_dmg:float = (j - 5000) / 10000 - 0.0215
            w:float = 1.5 if weak else 1

            mul_dmg_buff:float = 1
            if ship_troop:
                mul_dmg_buff +=  ship_rarity * 0.05
            if ship_attr:
                mul_dmg_buff += ship_rarity * 0.05
            if ship_rarity > 3:
                mul_dmg_buff += (ship_rarity - 3) * 0.0015
            if char_rarity > 3:
                mul_dmg_buff += (char_rarity - 3) * 0.0016

            atk_buff:float = utils.round_decimal((1 + 0.000152 * lv_subability), 4)

            mul_dmg:float = (((total_damage + corr_total_dmg) / w) * 10000) / utils.round_decimal((atk+corr_atk) * atk_buff, 0) / mul_dmg_buff

            if mul_dmg % 1 < 0.1 or mul_dmg % 1 > 0.9:
                mul_dmg = utils.round_decimal(mul_dmg) / 10000
                if min_mul_dmg["mul_dmg"] > mul_dmg:
                    min_mul_dmg["atk"] = (atk+corr_atk)
                    min_mul_dmg["atk_buff"] = atk_buff
                    min_mul_dmg["mul_dmg_buff"] = mul_dmg_buff
                    min_mul_dmg["total_dmg"] = (total_damage + corr_total_dmg)
                    min_mul_dmg.mul_dmg = mul_dmg

    return min_mul_dmg
