#!/usr/bin/env python
import os
import re
from datetime import datetime

def main():
    print 'Running speed test now...'
    os.system('speedtest --simple > result')
    f = open('result', 'r')
    text = f.read()
    os.system('rm result')

    print 'Speed Test Complete...'

    sort_result(text)

def sort_result(input_text):
    get_ping = re.search(r'Ping:\s(\d+.\d+)\sms', input_text)
    ping = get_ping.group(1)

    get_download = re.search(r'Download:\s(\d+.\d+)\sMbit\/s', input_text)
    download = get_download.group(1)

    get_upload = re.search(r'Upload:\s(\d+.\d+)\sMbit\/s', input_text)
    upload = get_upload.group(1)

    #print ping
    #print download
    #print upload

    write_file(ping, download, upload)

def write_file(ping_time, download_speed, upload_speed):
    result_time = str(datetime.now())
    out_f = open('results.csv', 'a')
    formated_text = result_time + ',' + ping_time + ',' + download_speed + ',' + upload_speed + '\n'
    out_f.write(formated_text)
    out_f.close()
    print 'Thank You!'
    print '*' * 12
    print 'Your results are as follows!'
    print 'Ping: %s ms' % ping_time
    print 'Download: %s Mbit/s' % download_speed
    print 'Upload: %s Mbit/s' % upload_speed
    print 'Your data has been written to result.csv'


if __name__ == '__main__':
    main()
