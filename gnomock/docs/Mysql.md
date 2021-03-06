# Mysql

This object describes MySQL container. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db** | **str** | Database name to create. | [optional] [default to 'mydb']
**user** | **str** | User to create in the container. | [optional] [default to 'gnomock']
**password** | **str** | New user&#39;s password. | [optional] [default to 'gnomick']
**queries** | **list[str]** | A list of queries to execute while setting up the container.  | [optional] 
**queries_file** | **str** | A SQL file to execute while setting up container state. | [optional] 
**version** | **str** | Docker image tag (version) | [optional] [default to 'latest']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


