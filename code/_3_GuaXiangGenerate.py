XianTianBaGua = {
    1: ("乾","111"),
    2: ("兑","110"),
    3: ("离","101"),
    4: ("震","100"),
    5: ("巽","011"),
    6: ("坎","010"),
    7: ("艮","001"),
    8: ("坤","000"),
}





def generateGuaXiang(XiaGuaData, ShangGuaData): 
    """
    Generate the Gua Xiang based on the given data.
    
    Parameters:
    XiaGuaData (int): The lower trigram data (1-8).
    ShangGuaData (int): The upper trigram data (1-8).
    
    Returns:
    str: The Gua Xiang in a formatted string.
    """
    xiaGua = XianTianBaGua[XiaGuaData][0]
    shangGua = XianTianBaGua[ShangGuaData][0]
    GuaXiangData = XianTianBaGua[XiaGuaData][1]+ XianTianBaGua[ShangGuaData][1]
    return GuaXiangData