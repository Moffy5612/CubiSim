MUL_SUBABILITY1:float = 0.000152
MUL_SUBABILITY2:float = 0.000273

def multiplier(atk:int, lv_subability1:int, lv_subability2:int, char_rarity:int, ship_troop:bool, ship_attr:bool, ship_rarity:int, weak:bool, total_dmg:int) -> str:
    min_mul_dmg:dict[str, float] = {
      "atk":0,
      "atk_buff":0,
      "mul_dmg_buff":0,
      "total_dmg":0,
      "mul_dmg":1001
    }

    w:float = 1.5 if weak else 1

    mul_dmg_buff:float = 1
    if ship_troop:
        mul_dmg_buff = mul_dmg_buff + ship_rarity * 0.05
    if ship_attr:
        mul_dmg_buff = mul_dmg_buff + ship_rarity * 0.05
    if ship_rarity > 3:
        mul_dmg_buff = mul_dmg_buff + (ship_rarity - 3) * 0.0015
    if char_rarity > 2:
        mul_dmg_buff = mul_dmg_buff + (char_rarity - 2) * 0.0011
    
    atk_buff:float = round(1 + MUL_SUBABILITY1 * lv_subability1 + MUL_SUBABILITY2 * lv_subability2)

    min_mul_dmg["atk_buff"] = atk_buff
    min_mul_dmg["mul_dmg_buff"] = mul_dmg_buff

    for i in range(10):
        for j in range(100):
            corr_atk:float = (i - 5) / 10
            corr_total_dmg:float = (j - 50) / 100

            mul_dmg:float = ((total_dmg + corr_total_dmg) * 10000 / w) / (round((atk + corr_atk) * atk_buff)) / mul_dmg_buff

            if abs(mul_dmg % 1 - 0.5) < 0.1:
                mul_dmg = round(mul_dmg) / 10000
                if min_mul_dmg["mul_dmg"] > mul_dmg:
                    min_mul_dmg["atk"] = atk + corr_atk
                    min_mul_dmg["total_dmg"] = total_dmg + corr_total_dmg
                    min_mul_dmg["mul_dmg"] = mul_dmg

    out:str = "```\n"
    out = out + "基礎ATK : " + str(min_mul_dmg["atk"]) + "\n"
    out = out + "ATKバフ : " + str(min_mul_dmg["atk_buff"]) + "\n"
    out = out + "ダメージ倍率バフ : " + str(min_mul_dmg["mul_dmg_buff"]) + "\n"
    out = out + "与えたダメージ : " + str(min_mul_dmg["total_dmg"]) + "\n"
    out = out + "のとき、\n"
    out = out + "\n基礎ダメージ倍率 : " + str(min_mul_dmg["mul_dmg"]) + "\n"
    out = out + "です。\n ```"

    return out
                    
