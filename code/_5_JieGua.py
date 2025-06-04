ZuiZhongGua = {
    "menu": ("次序","卦名","卦辞","初爻辞","二爻辞","三爻辞","四爻辞","五爻辞","上爻辞","象","文言","other"),
    "111111": (1,"乾卦","乾,元亨利贞","初九：潜龙勿用。","九二：见龙在田，利见大人。","九三：君子终日乾乾，夕惕若厉，无敢尚词。","九四：或跃在渊，无咎。","九五：飞龙在天，利见大人。","上九：亢龙有悔。","象曰：天行健，君子以自强不息。","文言曰：元亨利贞。", ""),
    "000000": (2,"坤卦","坤,元亨,利牝马之贞。君子有攸往，先迷后得主。利西南得朋，东北丧朋。安贞吉","初六：履霜，坚冰至。","六二：直方大，不习,无不利。","六三：含章可贞，或从王事，无成有终。","六四：括囊，无咎。","六五：黄裳，元吉。","上六：龙战于野，其血玄黄。","象曰：地势坤，君子以厚德载物。","文言曰：元亨利贞。", ""),
    "100010": (3,"屯卦","屯,元亨利贞。勿用有攸往，利建侯。","初九：磐桓，利居贞，利建侯。","六二：屯如邅如，乘马班如。匪寇婚媾，女子贞不字，十年乃字","六三：既鹿无虞，惟入于林中，君子几，不如舍，往吝。","六四：乘马班如，求婚媾，往吉，无不利。","九五：屯其膏，小贞吉，大贞凶。","上六：乘马班如，泣血涟如。","象曰：。","文言曰：。", ""),
    "010001": (4,"蒙卦" ,),
    "111010": (5,"需卦"),
    "010111": (6,"讼卦"),
    "010000": (7,"师卦"),

    "default": ("未找到该卦信息",),
}


def JieGua(GuaXiangData,FuGuaData,BianGuaData,HuGuaData,YaoWeiData):
    if GuaXiangData in ZuiZhongGua:
        print(f"卦象：{ZuiZhongGua.get(GuaXiangData, ZuiZhongGua["default"])}")
        DrawTheGua(GuaXiangData)
    else:
        print (f"卦象{ZuiZhongGua.get(GuaXiangData, ZuiZhongGua["default"])}")
        DrawTheGua(GuaXiangData)
    
    if FuGuaData in ZuiZhongGua:
        print(f"覆卦：{ZuiZhongGua.get(FuGuaData, ZuiZhongGua["default"])}")
        DrawTheGua(FuGuaData)
    else:
        print(f"覆卦：{ZuiZhongGua.get(FuGuaData, ZuiZhongGua["default"])}")
        DrawTheGua(FuGuaData)
    
    if BianGuaData in ZuiZhongGua:
        print(f"变卦：{ZuiZhongGua.get(BianGuaData, ZuiZhongGua["default"])}")
        DrawTheGua(BianGuaData)
    else:
        print(f"变卦：{ZuiZhongGua.get(BianGuaData, ZuiZhongGua["default"])}")
        DrawTheGua(BianGuaData)
    
    if HuGuaData in ZuiZhongGua:
        print(f"互卦：{ZuiZhongGua.get(HuGuaData, ZuiZhongGua["default"])}")
        DrawTheGua(HuGuaData)
    else:
        print(f"互卦：{ZuiZhongGua.get(HuGuaData, ZuiZhongGua["default"])}")
        DrawTheGua(HuGuaData)

    return None

def DrawTheGua(GuaData):
    print("Drawing the Gua...")
    for i in range(5, -1, -1):  # Loop from 5 to 0 (5 lines)
        if GuaData[i] == '1':
            print("—————", end='\n')  # Yang line
        else:
            print("—— ——", end='\n')  # Yin line
    print()  # New line after drawing the Gua