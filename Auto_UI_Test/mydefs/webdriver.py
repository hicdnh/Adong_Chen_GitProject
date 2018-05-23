#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 14:00
# @Author  : Adong_Chen
# @Email   : hicdnh@163.com
from selenium.webdriver.chrome import webdriver as chrome
from selenium.webdriver.remote import webdriver


class Driver(webdriver.WebDriver, chrome):
	def __init__(self):
		webdriver.WebDriver.__init__(self)

	@staticmethod
	def locate_to_scroll(fos_arg):
		webdriver.WebDriver.execute_script("var q=document.documentElement.scrollTop=" + str(fos_arg))
		# 这个地方有点问题，暂时没有做处理
	# driver.execute_script(focus_on_scroll)
	# 0:最顶端，10000：对底端，中间位置根据需要填写
