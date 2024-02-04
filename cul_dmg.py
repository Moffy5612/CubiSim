from typing import Dict
import utils

def cul_dmg(atk:float, lv_subability:int, atk_buff:float, mul_dmg:float, char_rarity:int, ship_troop:bool, ship_attr:bool, ship_rarity:int, mul_dmg_buff:float, weak:bool)->Dict[str, float]:
    atk_buff+=1
    mul_dmg_buff+=1

    w:float = 1.5 if weak else 1

    if ship_troop:
        mul_dmg_buff +=  ship_rarity * 0.05
    if ship_attr:
        mul_dmg_buff += ship_rarity * 0.05
    if ship_rarity > 3:
        mul_dmg_buff += (ship_rarity - 3) * 0.0015
    if char_rarity > 3:
        mul_dmg_buff += (char_rarity - 3) * 0.0016

    atk_buff += utils.round_decimal((0.000152 * lv_subability), 4)

    total_dmg:float = utils.round_decimal((utils.round_decimal(atk * atk_buff, 0) * utils.round_decimal(mul_dmg * mul_dmg_buff, 4) * w + 0.0215), 2)

    return {
        "atk" : atk,
        "atk_buff" : atk_buff,
        "mul_dmg" : mul_dmg,
        "mul_dmg_buff" : mul_dmg_buff,
        "weak" : w,
        "total_damage" : total_dmg
    }