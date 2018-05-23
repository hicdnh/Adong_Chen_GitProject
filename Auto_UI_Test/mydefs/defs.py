#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Adong_Chen
# @Email   : hicdnh@163.com


def locate_to_scroll(fos_arg):
	return "var q=document.documentElement.scrollTop=" + str(fos_arg)
	# driver.execute_script(focus_on_scroll)
	# 0:最顶端，10000：对底端，中间位置根据需要填写


