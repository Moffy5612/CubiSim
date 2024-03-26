MUL_SUBABILITY1:float = 0.000152
MUL_SUBABILITY2:float = 0.000273

def cul_dmg(atk:int, lv_subability1:int, lv_subability2:int, atk_buff:float, mul_dmg:float, ship_troop:float, ship_attr:float, char_rarity:int, ship_rarity:int, mul_dmg_buff:float, weak:bool)->str:
    w:float = 1.5 if weak else 1

    if ship_troop:
        mul_dmg_buff = mul_dmg_buff + ship_rarity * 0.05
    if ship_attr:
        mul_dmg_buff = mul_dmg_buff + ship_rarity * 0.05
    if ship_rarity > 3:
        mul_dmg_buff = mul_dmg_buff + (ship_rarity - 3) * 0.0015
    if char_rarity > 2:
        mul_dmg_buff = mul_dmg_buff + (char_rarity - 2) * 0.0011
    
    atk_buff = atk_buff + round(1 + MUL_SUBABILITY1 * lv_subability1 + MUL_SUBABILITY2 * lv_subability2)

    total_dmg:float = round(atk * atk_buff) * mul_dmg * mul_dmg_buff * weak

    out:str = "```\n"
    out = out + "基礎ATK : " + str(atk) + "\n"
    out = out + "ATKバフ : " + str(atk_buff) + "\n"
    out = out + "基礎ダメージ倍率 : " + str(mul_dmg) + "\n"
    out = out + "ダメージ倍率バフ : " + str(mul_dmg_buff) + "\n"
    out = out + "弱点倍率 : " + str(w) + "\n"
    out = out + "のとき、\n"
    out = out + "\n与えるダメージ : " + str(total_dmg) + "\n"
    out = out + "です。\n ```"

    return out