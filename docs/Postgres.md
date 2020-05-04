# Postgres

This object describes Postgres container. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db** | **str** | Database name to create. | [optional] [default to 'postgres']
**user** | **str** | User to create in the container. | [optional] [default to 'postgres']
**password** | **str** | New user&#39;s password. | [optional] [default to 'password']
**queries** | **list[str]** | A list of queries to execute while setting up the container.  | [optional] 
**queries_file** | **str** | A SQL file to execute while setting up container state. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


