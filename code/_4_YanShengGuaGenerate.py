
def GenerateYanShengGua(GuaXiangData):

    FuGuaData = GuaXiangData[::-1]  
    BianGuaData = GuaXiangData.replace('0', 'x').replace('1', '0').replace('x', '1')
    #ShangHuGuaData = GuaXiangData[1:4]
    #XiaHuGuaData = GuaXiangData[2:5]
    HuGuaData = GuaXiangData[1:4] + GuaXiangData[2:5]
    #print(f"上互卦：{GuaXiangData[1:4]}, 下互卦：{GuaXiangData[2:5]}")
    for i in range(0, len(GuaXiangData)):
        print(f"爻位{i+1}：{GuaXiangData[i]}")
    return FuGuaData, BianGuaData, HuGuaData