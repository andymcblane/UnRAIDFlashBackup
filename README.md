# UnRAID Flash Backup

Not a huge fan of backuping up my flash drive to the cloud unencrypted. 

Could not find a simple automated solution, so this was created. 

## Prerequisites 

* Remote Selenium Grid (see https://github.com/SeleniumHQ/docker-selenium)

## Environment Variables 

* USERNAME - UnRAID username
* PASSWORD - UnRAID password
* WEB_URL - UNRAID URL
* BACKUP_FREQUENCY_SECS - Number of seconds to sleep in between each backup. 
* HUB_URL - URL of Selenium Hub
