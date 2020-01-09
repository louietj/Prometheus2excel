import cpu
import write_excel

def print_cpu(namespace,start_time,end_time,step):
    total_CPU_book_name_xls = 'total_cpu.xls'
    Data_CPU_total_max=cpu.output_io('sum by(instance) (rate(node_cpu_seconds_total{mode!="idle"}[2m])) * 100', start_time, end_time, step)
    Data_IO_total_avg=cpu.output_io('avg by(instance) (rate(node_cpu_seconds_total{mode!="idle"}[2m])) * 100', start_time, end_time, step)

    value_title_IO=[["instance"," ","max value","average value","min value","max value","average value","min value"], ]
    sheet_name_total_xls = 'prometheus整体cpu性能测试表'
    write_excel.write_excel_xls(total_CPU_book_name_xls, sheet_name_total_xls, value_title_IO)
    write_excel.write_excel_xls_append_cpu_memory1(total_CPU_book_name_xls, Data_CPU_total_max, Data_IO_total_avg)
    #write_excel.read_excel_xls(total_CPU_book_name_xls,0)


    for i in range(len(namespace)):
        str1=str(namespace[i])

        write_excel.write_excel_xls_append_cpu_network_memory_title(total_CPU_book_name_xls, ["namespace","pod","max value","average value","min value","max value","average value","min value"])
        Data_CPU_pod_max=cpu.output_io('sum(namespace_pod_name_container_name:container_cpu_usage_seconds_total:sum_rate{container_name !="POD",namespace="' + str1 + '"}) by (container_name,  pod_name, namespace)', start_time, end_time, step)
        Data_CPU_pod_avg=cpu.output_io('avg(namespace_pod_name_container_name:container_cpu_usage_seconds_total:sum_rate{container_name !="POD", namespace="' + str1 + '"}) by (container_name,  pod_name, namespace)', start_time, end_time, step)
        Data_CPU_pod_request = cpu.output_io('sum(kube_pod_container_resource_requests_cpu_cores{namespace="' + str1 + '"}) by (container, pod, namespace)', start_time, end_time, step)
        Data_CPU_pod_limit = cpu.output_io('sum(kube_pod_container_resource_limits_cpu_cores{namespace="' + str1 + '"}) by (container, pod, namespace)', start_time, end_time, step)

        write_excel.write_excel_xls_append_CPU_memory(total_CPU_book_name_xls,Data_CPU_pod_max, Data_CPU_pod_avg,Data_CPU_pod_request,Data_CPU_pod_limit)

    rowstart = [1, 1, 9, 9,9,9]
    rowend = [1, 1, 9, 9,9,9]
    colstart = [3, 6, 3,6,9, 10]
    colend = [5, 8, 5,8,9, 10]
    value = ['max', 'avg', 'max','avg','pod request', 'pod limit']
    write_excel.read_cpu_memory_network('total_cpu.xls', rowstart, rowend, colstart, colend, value)
    i = 1
    write_excel.merge('total_cpu.xls', rowstart, rowend, colstart, colend, value)

    #write_excel.read_excel_xls(total_CPU_book_name_xls,0)

