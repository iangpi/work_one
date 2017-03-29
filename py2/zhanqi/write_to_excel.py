#coding:utf-8
import xlrd
import xlwt
def myexcel():
    #创建一个新的工作薄
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    #添加一个sheet，命名为first，cell_overwrite_ok，表示可不可以重复写入值。就是当前单元格非空，要覆盖写入
    names=['1','2','3']
    for n in xrange(len(names)):
        sheet=book.add_sheet(names[n],cell_overwrite_ok=True)
        #开始往里面写值
        sheet.write(0,0,'yes')

    book.save(r'd:\first.xls')
myexcel()

