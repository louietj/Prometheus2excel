import IO
import write_excel

def print_io(instance,start_time,end_time,step):
    total_IO_book_name_xls = 'total_IO.xls'
    Data_IO_total_util=IO.output_io('rate(node_disk_io_time_seconds_total{device=~"sd.*"}[1m])', start_time, end_time, step)
    Data_IO_total_await=IO.output_io('rate(node_disk_read_time_seconds_total{device=~"sd.*"}[1m]) / rate(node_disk_reads_completed_total{device=~"sd.*"}[1m])', start_time, end_time, step)
    Data_IO_total_rkb=IO.output_io('rate(node_disk_read_bytes_total{device=~"sd.*"}[1m])', start_time, end_time, step)
    Data_IO_total_wkb=IO.output_io('rate(node_disk_written_bytes_total{device=~"sd.*"}[1m])', start_time, end_time, step)
    value_title_IO=[["instance","device","max_value","average_value","min_value","max_value","average_value","min_value","max_value","average_value","min_value","max_value","average_value","min_value"], ]
    sheet_name_total_xls = 'prometheus整体IO性能测试表'
    #print(IO.output_io('rate(node_disk_written_bytes_total{device=~"dm.*",instance="172.26.0.5:9100"}[1m])','1577154000','1577154577','30'))
    write_excel.write_excel_xls(total_IO_book_name_xls, sheet_name_total_xls, value_title_IO)
    write_excel.write_excel_xls_append_IO(total_IO_book_name_xls, Data_IO_total_util, Data_IO_total_await, Data_IO_total_rkb, Data_IO_total_wkb)
    #write_excel.merge_worksheet_IO_title(total_IO_book_name_xls,0)
    #write_excel.read_excel_xls(total_IO_book_name_xls,0)
    #write_excel.merge_worksheet_IO_title_col(total_IO_book_name_xls,0)
    #write_excel.read_excel_xls(total_IO_book_name_xls,0)
    i=0
    for i in range(len(instance)):
        local_IO_book_name_xls = 'local_IO.xls'
        str1 = ''.join(instance[i])
        metric_io_util='rate(node_disk_io_time_seconds_total{device=~"dm.*",instance="'+str1+'"}[1m])'
        #print(metric_io_util)
        metric_io_await='rate(node_disk_read_time_seconds_total{device=~"dm.*",instance="'+str1+'"}[1m]) / rate(node_disk_reads_completed_total{device=~"dm.*",instance="'+str1+'"}[1m])'
        metric_io_rkb='rate(node_disk_read_bytes_total{device=~"dm.*",instance="'+str1+'"}[1m])'
        metric_io_wkb='rate(node_disk_written_bytes_total{device=~"dm.*",instance="'+str1+'"}[1m])'
        Data_IO_local_util=IO.output_io(metric_io_util, start_time, end_time, step)
        Data_IO_local_await=IO.output_io(metric_io_await, start_time, end_time, step)
        Data_IO_local_rkb=IO.output_io(metric_io_rkb, start_time, end_time, step)
        Data_IO_local_wkb=IO.output_io(metric_io_wkb, start_time, end_time, step)
        sheet_name_local_xls = 'prometheus节点IO性能测试表'
        #write_excel.write_excel_xls(local_IO_book_name_xls, sheet_name_local_xls, value_title_IO)
        write_excel.write_excel_xls_append_IO(total_IO_book_name_xls, Data_IO_local_util, Data_IO_local_await,Data_IO_local_rkb, Data_IO_local_wkb)

        #write_excel.merge_worksheet_IO_title(total_IO_book_name_xls,1)
        #write_excel.merge_worksheet_IO_title_col(local_IO_book_name_xls,0)

    rowstart = [1, 1, 1, 1]
    rowend = [1, 1, 1, 1]
    colstart = [3, 6, 9, 12]
    colend = [5, 8, 11, 14]
    value = ['%util', 'await', 'rkb/s', 'wkb/s']
    write_excel.read_io('total_IO.xls', rowstart, rowend, colstart, colend, value)
    i = 1
    write_excel.merge('total_IO.xls', rowstart, rowend, colstart, colend, value)

    #write_excel.read_excel_xls(total_IO_book_name_xls,0)

#print_io('172.26.0.5:9100',1577154000,1577154577,30)