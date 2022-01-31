# alfresco-delete-old-files

Python script allows you to safely delete old files in the starttime-endtime range from Alfresco 4+. Endtime is calculated as today's date minus lagindays. You can run script from cron. Old files will be moved by Alfresco CMIS API to the administrator's recycle bin. The administrator in manual or automatic mode can confirm the operation. After that the files can be safely removed from the folder e.g. /opt/alfresco-x.x.x/alf_data/contentstore/contentstore.deleted/.
