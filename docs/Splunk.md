# Splunk

This object describes Splunk container. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**list[SplunkValues]**](SplunkValues.md) | A list of events to ingest into the container. | [optional] 
**values_file** | **str** | File name with events to ingest into Splunk. Use JSON Lines format (every event is a separate JSON object), each new event starts from a new line.  | [optional] 
**accept_license** | **bool** | Accept or decline Splunk license. | 
**admin_password** | **str** | Set a password for &#x60;admin&#x60; user. | 
**version** | **str** | Splunk version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


