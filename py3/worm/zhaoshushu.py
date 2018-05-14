import xlrd
import xlwt
import os
import xdrlib,sys  
import xlwt  

laiyuan_path=os.path.abspath(r"D:\zhaoshushu\laiyuan.xlsx")
quxiang_path=os.path.abspath(r"D:\zhaoshushu\quxiang.xlsx")

data = xlrd.open_workbook(laiyuan_path) 

table = data.sheets()[0]             #通过索引顺序获取  
#table = data.sheet_by_index(0)       #通过索引顺序获取  

nrows = table.nrows  
ncols = table.ncols  

#下面开始采集数据，
res1=[]
for i in range(nrows):
	res1.append(table.row_values(i))
#print (res1)
data2=xlrd.open_workbook(quxiang_path)
table2=data2.sheets()[0]
nrows2=table2.nrows
ncols2=table2.nrows

res2=[]
for ii in range(nrows2):
	res2.append(table2.row_values(ii))
#print (res2)
'''
table3=data2.sheets()[1]
nrows3=table3.nrows
ncols3=table3.nrows
res3=[]
for iii in range(nrows3):
	res3.append(table3.row_values(iii))

table4=data2.sheets()[2]
nrows4=table4.nrows
ncols4=table4.nrows
res4=[]
for iiii in range(nrows4):
	res4.append(table4.row_values(iiii))
'''
#下面开始筛选数据放入新的list
sheet1_fin_res=[]
for i in res2:
	if i in res1:
		sheet1_fin_res.append(i)
print ('sheet1_fin_res:',sheet1_fin_res)
'''
sheet2_fin_res=[]
for i in res3:
	if i in res1:
		sheet2_fin_res.append(i)
print ('sheet2_fin_res:',sheet2_fin_res)

sheet3_fin_res=[]
for i in res4:
	if i in res1:
		sheet3_fin_res.append(i)
print ('sheet3_fin_res:',sheet3_fin_res)
'''
#下面开始写入
f1 = xlwt.Workbook() #创建工作簿
sheet1 = f1.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
#l_=[1,2,3,4,5]
#for i in range(len(l_)):
n=0
for i in range(len(sheet1_fin_res)):
	sheet1.write(n,0,i+1)#表格的第一行开始写。第一列，第二列。。。。 
	n=n+1
	#print (n)
f1.save('text.xlsx')#保存文件