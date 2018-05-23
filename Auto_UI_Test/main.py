#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:03
# @Author  : Adong_Chen
# @Email   : hicdnh@163.com

import settings
from selenium import webdriver
import cases
import time


def get_func_names(__driver):
	cases_lst = []
	for i in settings.SMOKE_TEST_CASES:
		case = getattr(cases.smoketest.SmokeTest(__driver), i)
		cases_lst.append(case)
		# print cases_lst
	return cases_lst


def get_driver():
	driver = webdriver.Chrome()
	driver.get("https://www.cnblogs.com/")
	driver.implicitly_wait(3)
	return driver


def run():
	log_file = open(settings.LOGFILE, "w+")
	for i in range(0, len(settings.SMOKE_TEST_CASES)):
		driver = get_driver()
		func_lst = get_func_names(driver)
		# print "run: " + str(case.func_name)
		r = func_lst[i]()
		temp = "Case:   " + func_lst[i].func_name + "result:   " + str(r) + "\n"
		# print case.func_name
		log_file.write(temp)
		log_file.flush()
		time.sleep(5)
	log_file.close()


if __name__ == "__main__":
	run()
	# run()

