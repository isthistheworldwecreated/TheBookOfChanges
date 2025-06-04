import _2_NumberGenerate 
import _3_GuaXiangGenerate
import _4_YanShengGuaGenerate
import _5_JieGua

def DoTheFortuneTelling(question):
    XiaGuaData, ShangGuaData, YaoWeiData = _2_NumberGenerate.generateNumbers(question)
    GuaXiangData = _3_GuaXiangGenerate.generateGuaXiang(XiaGuaData, ShangGuaData)
    FuGuaData, BianGuaData, HuGuaData = _4_YanShengGuaGenerate.GenerateYanShengGua(GuaXiangData)
    _5_JieGua.JieGua(GuaXiangData, FuGuaData, BianGuaData, HuGuaData, YaoWeiData)

if __name__== "__main__":
    import os
    os.makedirs("FortuneTelling", exist_ok=True)
    question = input("Your question please: ")
    XiaGuaData,ShangGuaData,YaoWeiData=_2_NumberGenerate.generateNumbers(question)
    GuaXiangData = _3_GuaXiangGenerate.generateGuaXiang(XiaGuaData, ShangGuaData)
    FuGuaData, BianGuaData, HuGuaData = _4_YanShengGuaGenerate.GenerateYanShengGua(GuaXiangData)
    _5_JieGua.JieGua(GuaXiangData, FuGuaData, BianGuaData, HuGuaData,YaoWeiData)

    
    #print(f"卦象:{GuaXiangData}, 下卦：{XiaGuaData}, 上卦：{ShangGuaData}, 爻位：{YaoWeiData},覆卦={FuGuaData}, 变卦={BianGuaData}, 互卦={HuGuaData}")