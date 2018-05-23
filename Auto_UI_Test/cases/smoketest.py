#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:03
# @Author  : Adong_Chen
# @Email   : hicdnh@163.com


import time
from mydefs.defs import locate_to_scroll
from selenium.webdriver.common import action_chains


class SmokeTest(object):
	def __init__(self, driver):
		self.driver = driver

	def s_case001(self):
		"""
		1.打开网页
		2.移动右侧滚轮上下滑动
		3.浏览器全屏、最小化、指定大小
		"""
		self.driver.get("https://www.cnblogs.com/")
		for i in range(1, 100):
			self.driver.execute_script(locate_to_scroll(100*i))
		self.driver.execute_script(locate_to_scroll(0))
		self.driver.maximize_window()
		# self.driver.minimize_window()
		self.driver.set_window_size(800, 600)
		self.driver.close()
		return True

	def s_case002(self):
		"""
		1.打开“园子”一行内容
		2.打开一个内容， 先返回到首页后再进行下一步操作
		"""
		__lst = ["//*[@id=\"nav_menu\"]/a[1]", "//*[@id=\"nav_menu\"]/a[2]"]
		for i in range(0, 2):
			self.driver.find_element_by_xpath(__lst[i]).click()
			time.sleep(3)
			self.driver.back()
			time.sleep(3)
		self.driver.close()
		return True

	def s_case003(self):
		"""
		说明：这个用例写法正确，但是由于Chrome中的google搜索不可用，所有这里会报错；
		1.定位到“找找看”的搜索框
		2.输入“test”,执行搜索
		3.返回到首页，定位到google搜索框，搜索“test”
		4.返回到首页
		"""
		__input_box = ["//*[@id=\"zzk_q\"]", "//*[@id=\"google_search_q\"]"]
		__search_button = ["//*[@id=\"search_block\"]/div[1]/input[2]","//*[@id=\"google_search\"]/input[2]"]
		for i in range(0, 2):
			self.driver.find_element_by_xpath(__input_box[i]).send_keys("test")
			self.driver.find_element_by_xpath(__search_button[i]).click()
			time.sleep(3)
			self.driver.back()
		self.driver.close()
		return True

	def s_case004(self):
		"""
		1.进入网站后先等待4秒（等待完全加载完毕）
		2.鼠标依次悬停在网站分类下面的页签上
		"""
		try:
			self.driver.implicitly_wait(4)
			__lst = ["//*[@id=\"cate_item_108698\"]/a", "//*[@id=\"cate_item_2\"]/a"]
			for i in range(0, 2):
				_to_element = self.driver.find_element_by_xpath(__lst[i])
				action_chains.ActionChains(self.driver).move_to_element(_to_element).perform()
				time.sleep(3)
			self.driver.close()
			return True
		except:
			return False
