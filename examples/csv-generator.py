import csv

if __name__ == '__main__':
    csvData = []
    csvData.append(['#profile name', 'device name', 'app ids (| separated)', 'friendly name', 'description', 'tags (| separated)', 'status', 'period (in seconds)', 'customIds (| separated)', 'timezone', 'location annotation is enabled', 'meta annotation is enabled', 'location'])

    for i in range(1, 1001):        
        csvData.append(['Logika26Gw','Logika26Gw.{}'.format(i),'_app_500665860676036489','','','test|csv','enabled',0,'sn=SN-LK-00{}'.format(i)])

    with open('new_device.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)

    csvFile.close()
