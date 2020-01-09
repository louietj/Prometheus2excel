import xlwt
import xlrd
from xlutils.copy import copy

def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i+1+1, j+1, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    style = xlwt.XFStyle()
    style.alignment.horz=0x02
    style.alignment.vert=0x01
    new_worksheet = workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    new_worksheet.write_merge(0,0,3,5,'util',style)
    new_worksheet.write_merge(0,0,6,8,'await',style)
    new_worksheet.write_merge(0,0,9,11,'rkb/s',style)
    new_worksheet.write_merge(0,0,12,14,'wkb/s',style)

def read_excel_xls(path,sheet_num):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[sheet_num])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据

def mergexls(newworksheet,a,b,c,d,value):
    style = xlwt.XFStyle()
    style.alignment.horz = 0x02
    style.alignment.vert = 0x01
    newworksheet.write_merge(a, b, c, d, value, style)

def merge(path,rowstart,rowend,colstart,colend,value):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    newworkbook=copy(workbook)
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    newworksheet = newworkbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

    for i in range(len(value)):
        mergexls(newworksheet,rowstart[i],rowend[i],colstart[i],colend[i],value[i])
    newworkbook.save(path)

def write_excel_xls_append_cpu_memory1(path, value1, value2):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows + 1  # 获取表格中已存在的数据的行数
    index = len(value1)
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(index):
        new_worksheet.write(i + rows_old, 1, str(value1[i]['1'], encoding="utf-8"))
        new_worksheet.write(i + rows_old, 3, float(value1[i]['3']))
        new_worksheet.write(i + rows_old, 4, float(value1[i]['4']))
        new_worksheet.write(i + rows_old, 5, float(value1[i]['5']))
        new_worksheet.write(i + rows_old, 6, float(value2[i]['3']))
        new_worksheet.write(i + rows_old, 7, float(value2[i]['4']))
        new_worksheet.write(i + rows_old, 8, float(value2[i]['5']))
    style = xlwt.XFStyle()
    style.alignment.horz = 0x02
    style.alignment.vert = 0x01
    # new_worksheet.write_merge(rows_old, index+1, 0, 0, 'as', style)
    new_workbook.save(path)  # 保存工作簿

def write_excel_xls_append_CPU_memory(path, value1,value2,value3,value4):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows+1  # 获取表格中已存在的数据的行数
    index=min(len(value1),len(value2),len(value3),len(value4))
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(index):
        new_worksheet.write(i+rows_old, 1, str(value1[i]['0'],encoding = "utf-8"))
        new_worksheet.write(i+rows_old, 2,str(value1[i]['2'],encoding = "utf-8"))
        new_worksheet.write(i+rows_old, 3, float(value1[i]['3']))
        new_worksheet.write(i+rows_old, 4, float(value1[i]['4']))
        new_worksheet.write(i+rows_old, 5, float(value1[i]['5']))
        new_worksheet.write(i+rows_old, 6, float(value2[i]['3']))
        new_worksheet.write(i+rows_old, 7, float(value2[i]['4']))
        new_worksheet.write(i+rows_old, 8, float(value2[i]['5']))
        new_worksheet.write(i+rows_old, 9, float(value3[i]['3']))
        new_worksheet.write(i+rows_old, 10, float(value4[i]['3']))
    style = xlwt.XFStyle()
    style.alignment.horz = 0x02
    style.alignment.vert = 0x01
    new_workbook.save(path)  # 保存工作簿

def write_excel_xls_append_IO(path, value1,value2,value3,value4):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows+1  # 获取表格中已存在的数据的行数
    index=len(value1)
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(index):
        new_worksheet.write(i+rows_old, 1, str(value1[i]['1'],encoding = "utf-8"))
        new_worksheet.write(i+rows_old, 2, str(value1[i]['0'],encoding = "utf-8"))
        new_worksheet.write(i + rows_old, 3, str(value1[i]['2']*100) + "%")
        new_worksheet.write(i+rows_old, 4, str(value1[i]['3']*100) + "%")
        new_worksheet.write(i+rows_old, 5, str(value1[i]['4']*100) + "%")
        new_worksheet.write(i+rows_old, 6, float(value2[i]['2']))
        new_worksheet.write(i+rows_old, 7, float(value2[i]['3']))
        new_worksheet.write(i+rows_old, 8, float(value2[i]['4']))
        new_worksheet.write(i+rows_old, 9, float(value3[i]['2']))
        new_worksheet.write(i+rows_old, 10, float(value3[i]['3']))
        new_worksheet.write(i+rows_old, 11, float(value3[i]['4']))
        new_worksheet.write(i+rows_old, 12, float(value4[i]['2']))
        new_worksheet.write(i+rows_old, 13, float(value4[i]['3']))
        new_worksheet.write(i+rows_old, 14, float(value4[i]['4']))
    style = xlwt.XFStyle()
    style.alignment.horz = 0x02
    style.alignment.vert = 0x01
    new_workbook.save(path)  # 保存工作簿

def write_excel_xls_append_network1(path, value1, value2,value3,value4):
    # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows + 1  # 获取表格中已存在的数据的行数
    #    if rows_old==3:
    #        rows_old=rows_old-1
    i = 0
    index = len(value1)
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(index):
        new_worksheet.write(i + rows_old, 1, str(value1[i]['1'], encoding="utf-8"))
        new_worksheet.write(i + rows_old, 3, float(value1[i]['3']))
        new_worksheet.write(i + rows_old, 4, float(value1[i]['4']))
        new_worksheet.write(i + rows_old, 5, float(value1[i]['5']))
        new_worksheet.write(i + rows_old, 6, float(value2[i]['3']))
        new_worksheet.write(i + rows_old, 7, float(value2[i]['4']))
        new_worksheet.write(i + rows_old, 8, float(value2[i]['5']))
        new_worksheet.write(i + rows_old, 9, float(value3[i]['3']))
        new_worksheet.write(i + rows_old, 10, float(value3[i]['4']))
        new_worksheet.write(i + rows_old, 11, float(value3[i]['5']))
        new_worksheet.write(i + rows_old, 12, float(value4[i]['3']))
        new_worksheet.write(i + rows_old, 13, float(value4[i]['4']))
        new_worksheet.write(i + rows_old, 14, float(value4[i]['5']))
    style = xlwt.XFStyle()
    style.alignment.horz = 0x02
    style.alignment.vert = 0x01
    # new_worksheet.write_merge(rows_old, index+1, 0, 0, 'as', style)
    new_workbook.save(path)  # 保存工作簿

def write_excel_xls_append_network(path, value1,value2,value3,value4):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows+1  # 获取表格中已存在的数据的行数
#    if rows_old==3:
#        rows_old=rows_old-1
    i=0
    index=min(len(value3),len(value1),len(value2),len(value4))
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(index):
        new_worksheet.write(i+rows_old, 1, str(value1[i]['0'],encoding = "utf-8"))
        new_worksheet.write(i+rows_old, 2,str(value1[i]['2'],encoding = "utf-8"))
        new_worksheet.write(i+rows_old, 3, float(value1[i]['3']))
        new_worksheet.write(i+rows_old, 4, float(value1[i]['4']))
        new_worksheet.write(i+rows_old, 5, float(value1[i]['5']))
        new_worksheet.write(i+rows_old, 6, float(value2[i]['3']))
        new_worksheet.write(i+rows_old, 7, float(value2[i]['4']))
        new_worksheet.write(i+rows_old, 8, float(value2[i]['5']))
        new_worksheet.write(i+rows_old, 9, float(value3[i]['3']))
        new_worksheet.write(i+rows_old, 10, float(value3[i]['4']))
        new_worksheet.write(i+rows_old, 11, float(value3[i]['5']))
        new_worksheet.write(i+rows_old, 12, float(value4[i]['3']))
        new_worksheet.write(i+rows_old, 13, float(value4[i]['4']))
        new_worksheet.write(i+rows_old, 14, float(value4[i]['5']))
    style = xlwt.XFStyle()
    style.alignment.horz = 0x02
    style.alignment.vert = 0x01
    #new_worksheet.write_merge(rows_old, index+1, 0, 0, 'as', style)
    new_workbook.save(path)  # 保存工作簿

def write_excel_xls_append_cpu_network_memory_title(path,value):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows + 1  # 获取表格中已存在的数据的行数
    index = len(value)
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(index):
        new_worksheet.write(rows_old+1, i+1, value[i])
    new_workbook.save(path)  # 保存工作簿

def read_cpu_memory_network(path,rowstart,rowend,colstart,colend,value):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    instance = worksheet.col_values(1)
    instance=worksheet.col_values(1)
    len_instance=len(instance)
    i = 4
    while i < len_instance - 1:
        if worksheet.col_values(1)[i] == '':
            rowstart.append(4)
            rowend.append(i - 1)
            colstart.append(0)
            colend.append(0)
            value.append('整体节点使用情况')
            break
        else:
            i = i + 1
    rowstart.append(i+4 )
    rowend.append(worksheet.nrows-1)
    colstart.append(0)
    colend.append(0)
    value.append('对应租户每个pod使用情况')
    i=2
    while i<len_instance-1:
        if instance[i+1]==instance[i] and instance[i]!='':
            rowstart.append(i)
            colstart.append(1)
            colend.append(1)
            value.append(instance[i])
            j=i+1
            while  j<len_instance and instance[j]==instance[i]:
                j=j+1
            rowend.append(j-1)
            i=j
        elif instance[i+1]!=instance[i]:
            i=i+1
        else:
            i=i+1

def read_io(path,rowstart,rowend,colstart,colend,value):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    instance=worksheet.col_values(1)
    len_instance=len(instance)
    i=4
    while i<len_instance-1:
        if worksheet.col_values(2)[i]=='':
            rowstart.append(4)
            rowend.append(i-1)
            colstart.append(0)
            colend.append(0)
            value.append('整体节点使用情况')
            break
        else:
            i=i+1
    rowstart.append(i+1)
    rowend.append(worksheet.nrows-1)
    colstart.append(0)
    colend.append(0)
    value.append('每个节点详细使用情况')
    i=0
    i=2
    while i<len_instance-1:
        if instance[i+1]==instance[i]:
            rowstart.append(i)
            colstart.append(1)
            colend.append(1)
            value.append(instance[i])
            j=i+1
            while  j<len_instance and instance[j]==instance[i]:
                j=j+1
            rowend.append(j-1)
            i=j
        elif instance[i+1]!=instance[i]:
            i=i+1