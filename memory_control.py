import memory
import write_excel

def print_memory(namespace,start_time,end_time,step):
    total_memory_book_name_xls = 'total_memory.xls'
    Data_memory_total_max=memory.output_memory('(max_over_time(node_memory_MemTotal_bytes[1m]) - min_over_time(node_memory_MemFree_bytes[1m]) - min_over_time(node_memory_Cached_bytes[1m])) / (1024 * 1024 * 1024)', start_time, end_time, step)
    Data_memory_total_avg=memory.output_memory('(avg_over_time(node_memory_MemTotal_bytes[1m]) - avg_over_time(node_memory_MemFree_bytes[1m]) - avg_over_time(node_memory_Cached_bytes[1m])) / (1024 * 1024 * 1024)', start_time, end_time, step)

    value_title_memory=[["instance"," ","max value","average value","min value","max value","average value","min value"], ]
    sheet_name_total_xls = 'prometheus整体Memory性能测试表'
    #print(IO.output_io('rate(node_disk_written_bytes_total{device=~"dm.*",instance="172.26.0.5:9100"}[1m])','1577154000','1577154577','30'))
    write_excel.write_excel_xls(total_memory_book_name_xls, sheet_name_total_xls, value_title_memory)
    write_excel.write_excel_xls_append_cpu_memory1(total_memory_book_name_xls, Data_memory_total_max, Data_memory_total_avg)
    #write_excel.merge_worksheet_IO_title(total_IO_book_name_xls,0)
    #write_excel.read_excel_xls(total_memory_book_name_xls,0)
    #write_excel.merge_worksheet_IO_title_col(total_IO_book_name_xls,0)
    #write_excel.read_excel_xls(total_IO_book_name_xls,0)

    for i in range(len(namespace)):
        str1=str(namespace[i])
        write_excel.write_excel_xls_append_cpu_network_memory_title(total_memory_book_name_xls, ["namespace","pod","max value","average value","min value","max value","average value","min value"])
        Data_memory_pod_max=memory.output_memory('max_over_time(container_memory_usage_bytes{job="kubelet", cluster="", namespace="' + str1 + '",container_name!="POD",service="prometheus-operator-kubelet"}[2m])/(1024*1024*1024)', start_time, end_time, step)
        Data_memory_pod_avg=memory.output_memory('avg_over_time(container_memory_usage_bytes{job="kubelet", cluster="", namespace="' + str1 + '", container_name!="POD",service="prometheus-operator-kubelet"}[2m])/(1024*1024*1024)', start_time, end_time, step)
        Data_memory_pod_request = memory.output_memory('sum(kube_pod_container_resource_requests_memory_bytes{namespace="' + str1 + '"}) by (container,pod,namespace)/(1024*1024*1024)', start_time, end_time, step)
        Data_memory_pod_limit = memory.output_memory('sum(kube_pod_container_resource_limits_memory_bytes{namespace="' + str1 + '"}) by (container,pod,namespace)/(1024*1024*1024)', start_time, end_time, step)

    #write_excel.write_excel_xls(local_IO_book_name_xls, sheet_name_local_xls, value_title_IO)
        write_excel.write_excel_xls_append_CPU_memory(total_memory_book_name_xls,Data_memory_pod_max, Data_memory_pod_avg,Data_memory_pod_request,Data_memory_pod_limit)

    rowstart = [1, 1, 9, 9,9,9]
    rowend = [1, 1, 9, 9,9,9]
    colstart = [3, 6, 3,6,9, 10]
    colend = [5, 8, 5,8,9, 10]
    value = ['max', 'avg', 'max','avg','pod request', 'pod limit']
    write_excel.read_cpu_memory_network('total_memory.xls', rowstart, rowend, colstart, colend, value)
    i = 1
    write_excel.merge('total_memory.xls', rowstart, rowend, colstart, colend, value)

    #write_excel.read_excel_xls(total_memory_book_name_xls,0)

#print_io('172.26.0.5:9100',1577154000,1577154577,30)