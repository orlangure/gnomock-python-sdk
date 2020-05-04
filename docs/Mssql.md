# Mssql

This object describes Microsoft SQL Server container. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db** | **str** | Database name to create. | [optional] [default to 'mydb']
**password** | **str** | Superuser password. | [optional] [default to 'Gn0m!ck~']
**queries** | **list[str]** | A list of queries to execute while setting up the container.  | [optional] 
**queries_file** | **str** | A SQL file to execute while setting up container state. | [optional] 
**license** | **bool** | Accept or decline Microsoft SQL Server license. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


