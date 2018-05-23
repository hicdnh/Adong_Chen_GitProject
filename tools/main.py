# coding:utf-8
import xlwt
import xlrd
import re
import os
needed_result = [u"Average_FPS", u"Average_FPS"]
result = []
base_dir = r"C:\Users\Adong\Desktop\cache"


def get_result():
	os.chdir(r"C:\Users\Adong\Desktop\cache")
	for i in os.listdir(os.getcwd()):
		result.append(i.decode("gbk"))
		os.chdir(base_dir + "\\" + i)
		for j in os.listdir(os.getcwd()):
			result.append(j)
			os.chdir(base_dir + "\\" + i + "\\" + j)
			for name in os.listdir(os.getcwd()):
				if re.findall("QaAverage", name):
					fp = open(name, "r")
					for line in fp.readlines():
						num = line.split(": ")
						if num[0] in needed_result:
							result.append(num[1].decode("gbk"))
	return result


def write_into_xls():
	data = get_result()
	length = len(data)
	wb = xlwt.Workbook()
	sh = wb.add_sheet("result", cell_overwrite_ok=True)

	data = iter(data)
	for k in range(0, length):
		for o in range(0, 6):
			try:
				sh.write(k, o, data.next())
			except StopIteration:
				pass
	wb.save(r"C:\Users\Adong\Desktop\result.xls")


write_into_xls()
