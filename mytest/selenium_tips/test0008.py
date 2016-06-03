#coding:utf-8
import xlwt
#新建并打开一个表格
page_1=['a','b','c','d','f']
page_2=['1','2','3','4','5']
sheet_names=['frist','second']
book=xlwt.Workbook(encoding='utf-8',style_compression=0)#配置信息可以不用细究
for n in xrange(len(sheet_names)):#遍历分页名字
    sheet_name=sheet_names[n]
    sheet=book.add_sheet(sheet_name,cell_overwrite_ok=True)#给分页添加名字，参数cell_overwrite_ok——False不可重新命名，True可以重新命名
    if n==0:
        num_1=len(page_1)
        for m in xrange(num_1):
            sheet.write(m,0,str(page_1[m]))
    else:
        num_2=len(page_2)
        for w in xrange(num_2):
            sheet.write(w,1,str(page_2[w]))
    #保存表
    book.save(r'D:\example.xls')
