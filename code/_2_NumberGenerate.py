import random
import time


def generateNumbers(question):
    timeString = time.asctime()
    #question = input("Your question please: ")

    questionTransformSeed = timeString + question
    random.seed(questionTransformSeed)
    firstNumber = random.randint(100, 999)
    secondNumber = random.randint(100, 999)
    thirdNumber = random.randint(100, 999)

    XiaGuaData = firstNumber%8
    ShangGuaData = secondNumber%8
    YaoWeiData = thirdNumber%6

    if XiaGuaData == 0:
        XiaGuaData = 8
    if ShangGuaData == 0:
        ShangGuaData = 8
    if YaoWeiData == 0:
        YaoWeiData = 6
    return XiaGuaData, ShangGuaData, YaoWeiData