import network
import write_excel

def print_network(namespace,start_time,end_time,step):
    total_network_book_name_xls = 'total_network.xls'
    Data_network_transmit_max=network.output_network('sum by(instance) (rate(node_network_transmit_bytes_total[1m]))', start_time, end_time, step)
    Data_network_transmit_avg=network.output_network('avg by(instance) (rate(node_network_transmit_bytes_total[1m]))', start_time, end_time, step)
    Data_network_receive_max=network.output_network('sum by(instance) (rate(node_network_receive_bytes_total[1m]))', start_time, end_time, step)
    Data_network_receive_avg=network.output_network('avg by(instance) (rate(node_network_receive_bytes_total[1m]))', start_time, end_time, step)

    value_title_network=[["instance"," ","max value","average value","min value","max value","average value","min value","max value","average value","min value","max value","average value","min value"], ]
    sheet_name_total_xls = 'prometheus整体network性能测试表'
    #print(IO.output_io('rate(node_disk_written_bytes_total{device=~"dm.*",instance="172.26.0.5:9100"}[1m])','1577154000','1577154577','30'))
    write_excel.write_excel_xls(total_network_book_name_xls, sheet_name_total_xls, value_title_network)
    write_excel.write_excel_xls_append_network1(total_network_book_name_xls, Data_network_transmit_max, Data_network_transmit_avg,Data_network_receive_max,Data_network_receive_avg)
    #write_excel.merge_worksheet_IO_title(total_IO_book_name_xls,0)
    #write_excel.read_excel_xls(total_network_book_name_xls,0)
    #write_excel.merge_worksheet_IO_title_col(total_IO_book_name_xls,0)
    #write_excel.read_excel_xls(total_IO_book_name_xls,0)

    for i in range(len(namespace)):
        str1=str(namespace[i])
        write_excel.write_excel_xls_append_cpu_network_memory_title(total_network_book_name_xls, ["namespace","pod","max value","average value","min value","max value","average value","min value","max value","average value","min value","max value","average value","min value"])
        Data_memory_pod_transmit_max=network.output_network('sum by (pod_name, namespace) (rate(container_network_transmit_bytes_total{job="kubelet", cluster="", namespace="' + str1 + '"}[1m]))', start_time, end_time, step)
        Data_memory_pod_transmit_avg=network.output_network('avg by (pod_name, namespace) (rate(container_network_transmit_bytes_total{job="kubelet", cluster="", namespace="' + str1 + '"}[1m]))', start_time, end_time, step)
        Data_memory_receive_max = network.output_network('sum by (pod_name, namespace) (rate(container_network_receive_bytes_total{job="kubelet", cluster="", namespace="' + str1 + '"}[1m]))', start_time, end_time, step)
        Data_memory_pod_receive_avg = network.output_network('avg by (pod_name, namespace) (rate(container_network_receive_bytes_total{job="kubelet", cluster="", namespace="' + str1 + '"}[1m]))', start_time, end_time, step)

    #write_excel.write_excel_xls(local_IO_book_name_xls, sheet_name_local_xls, value_title_IO)
        write_excel.write_excel_xls_append_network(total_network_book_name_xls,Data_memory_pod_transmit_max, Data_memory_pod_transmit_avg,Data_memory_receive_max,Data_memory_pod_receive_avg)

    rowstart = [1, 1,1,1, 9, 9,9,9]
    rowend = [1, 1, 1,1,9, 9,9,9]
    colstart = [3, 6,9,12, 3,6,9, 12]
    colend = [5, 8,11,14, 5,8,11, 14]
    value = ['transmit max', 'transmit avg', 'receive max','receive min','transmit max','transmit avg','receive max', 'receive min']
    write_excel.read_cpu_memory_network('total_network.xls', rowstart, rowend, colstart, colend, value)
    i = 1
    write_excel.merge('total_network.xls', rowstart, rowend, colstart, colend, value)

    #write_excel.read_excel_xls(total_network_book_name_xls,0)

#print_io('172.26.0.5:9100',1577154000,1577154577,30)