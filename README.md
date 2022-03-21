# alfresco-delete-old-files

Python script allows you to delete safely old files in the StartDate-EndDate range from Alfresco 4+. EndDate is calculated as today's date minus LagInDays. You can run script from cron. Old files will be moved by Alfresco CMIS API to the administrator's recycle bin. The administrator can confirm the operation in manual or automatic mode. After that the files can be removed safely from the folder e.g. /opt/alfresco-x.x.x/alf_data/contentstore/contentstore.deleted/.
