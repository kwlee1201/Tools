# Winlogbeat

Winlogbeat is a tool that can help us to upload window logs to Elasticsearch. It's developed by Elastic company and the document can refer to [here](https://www.elastic.co/guide/en/beats/winlogbeat/current/index.html). The basic operation steps will show below.

1. Download the [winlogbeat](https://www.elastic.co/downloads/beats/winlogbeat) program.
2. Set your parameter in winlogbeat.yml. For example, you can add specified logs in winlogbeat.yml and then they will be sent to your Elasticsearch with specified index name.
3. Install winlogbeat in your cmd with `{YOUR_FOLDER_PATH}\winlogbeat.exe -e -c winlogbeat.yml`.
4. After the command is finished, your will see the winlogbeat is working in Task Manager (Ctrl+Alt+Del).

## winlogbeat.yml

<img src="./images/winlogbeat_page_1.png" width="800px" /> 
<img src="./images/winlogbeat_page_2.png" width="800px" /> 

This diagram is an example for the content of winlogbeat.yml.

- `winlogneat.registry_file`: The record for successful transmission information.
- `winlogbeat.event_logs`: The type of Logs which we wanted to upload. Here we can see there are three kinds of logs(Security, Sysmon, and PowerShell).
- `output.elasticsearch`: The output information of the elasticsearch, such as, host, port, and index.

## Reference

[1] [Elastic](https://www.elastic.co/beats/winlogbeat)

[2] [Elastic - Configure Winlogbeat](https://www.elastic.co/guide/en/beats/winlogbeat/current/configuration-winlogbeat-options.html)

[3] [3-2.監控工具之三:Elastic-winlogbeat事件稽核](https://ithelp.ithome.com.tw/articles/10191552)
