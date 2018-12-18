# -*- coding:utf-8 -*-
# author: Weixuan.Ding
# time  : 2018/10/8
from profile import help

import pytesseract
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def codeDemo(imagePath):
    '''
        indentify verify code
    '''
    im = imagePath

    tessdata_dir_config = '--tessdata-dir "E:\Tesseract-OCR\\tessdata"'
    vcode = pytesseract.image_to_string(
        im, lang='chi_sim', config=tessdata_dir_config
    )
    return vcode[:6]


def sendMessage(selectCountry, mobileNumber, sendMsg):
    driver = webdriver.Firefox()
    driver.get("http://www.afreesms.com/freesms/")

    try:
        basePath = '/html/body/div[3]/div/div/fieldset/table' +\
            '/tbody/tr[2]/td[2]/table/tbody/tr/td/form/table/tbody'

        country = driver.find_element_by_xpath(
            '{}/tr[2]/td[2]/select'.format(basePath)
        )
        country.send_keys(selectCountry)
        print('Set country success.')

        number = driver.find_element_by_xpath(
            '{}/tr[3]/td[2]/input'.format(basePath)
        )
        number.send_keys(mobileNumber)
        print('Set mobileNumber success.')

        message = driver.find_element_by_xpath(
            '{}/tr[4]/td[2]/textarea'.format(basePath)
        )
        message.send_keys(sendMsg)

        image = driver.find_element_by_id('captcha')
        driver.save_screenshot('.\screen.png')

        left = image.location['x']
        top = image.location['y']
        right = left + image.size['width']
        bottom = top + image.size['height'] - 10
        im = Image.open('.\screen.png')
        imagePath = im.crop((left, top, right, bottom))
        # imagePath.show()
        key = codeDemo(imagePath)
        print('Indentify verify code[{}] complete.'.format(key))

        indentifyCode = driver.find_element_by_xpath(
            '{}/tr[6]/td[2]/input'.format(basePath)
        )
        indentifyCode.send_keys(key)
        print('Set verify code success.')

        # import pdb;pdb.set_trace()
        submit = driver.find_element_by_id('submit')
        submit.send_keys(Keys.RETURN)
    except Exception as why:
        driver.close()
        errorMsg = ''
        if hasattr(why, 'message'):
            errorMsg = why.message
        else:
            errorMsg = why.args
        print('send failed.')
        print(errorMsg)

    print('send success.')
    driver.close()


if __name__ == '__main__':
    selectCountry = '中国'
    mobileNumber = '18419068159'
    sendMsg = '''
        测试信息：hello world.
    '''

    # 发送信息间隔时间(多久发一次，单位: 秒)
    sleepTime = 0
    # 最多发送多少次
    maxNumber = 1

    sendNumber = 0

    while sendNumber < maxNumber:
        sendMessage(selectCountry, mobileNumber, sendMsg)
        sendNumber += 1
        if sleepTime > 0:
            time.sleep(sleepTime)
    print('All message send complete.')

