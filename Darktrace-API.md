# DARKTRACE THREAT VISUALIZER API

# GUIDE

## Darktrace Threat Visualizer 6.

###### Last Updated: January 9 2024


### DARKTRACE THREAT VISUALIZER API GUIDE

#### Darktrace Threat Visualizer 6.

##### Getting Started with the API

##### API Authentication

##### Code Examples - API Signature Generation

##### Code Examples - API GET Requests

##### Code Examples - API POST Requests

##### Minimum Required Permissions for API Endpoints

##### /advancedsearch/api/search

##### /advancedsearch/api/search Response Schema

##### /advancedsearch/api/analyze

##### /advancedsearch/api/analyze Response Schema

##### /advancedsearch/api/graph

##### /advancedsearch/api/graph Response Schema

##### /agemail/api/ep/api/v1.0/*

##### /aianalyst/incidentevents

##### /aianalyst/incidentevents Response Schema

##### /aianalyst/groups

##### /aianalyst/groups Response Schema

##### /aianalyst/acknowledge and /unacknowledge

##### /aianalyst/pin and /unpin

##### /aianalyst/incident/comments

##### /aianalyst/incident/comments Response Schema

##### /aianalyst/stats

##### 6

##### 8

##### 10

##### 11

##### 13

##### 16

##### 19

##### 24

##### 27

##### 31

##### 39

##### 43

##### 47

##### 49

##### 54

##### 65

##### 70

##### 74

##### 75

##### 76

##### 78

##### 79


##### /aianalyst/stats Response Schema

##### /aianalyst/investigations

##### /aianalyst/investigations Response Schema

##### /aianalyst/incidents (deprecated)

##### /aianalyst/incidents Response Schema (deprecated)

##### /antigena

##### /antigena Response Schema

##### /antigena/manual

##### /antigena/summary

##### /antigena/summary Response Schema

##### /components

##### /components Response Schema

##### /cves

##### /cves Response Schema

##### /details

##### /details Response Schema

##### /deviceinfo

##### /deviceinfo Response Schema

##### /devices

##### /devices Response Schema

##### /devicesearch

##### /devicesearch Response Schema

##### /devicesummary

##### /devicesummary Response Schema

##### 82

##### 86

##### 89

##### 91

##### 96

##### 106

##### 112

##### 122

##### 124

##### 126

##### 127

##### 130

##### 133

##### 135

##### 137

##### 140

##### 166

##### 169

##### 183

##### 186

##### 196

##### 199

##### 204

##### 207


##### /endpointdetails

##### /endpointdetails Response Schema

##### /enums

##### /enums Response Schema

##### /filtertypes

##### /filtertypes Response Schema

##### /intelfeed

##### /intelfeed Response Schema

##### /mbcomments

##### /mbcomments Response Schema

##### /metricdata

##### /metricdata Response Schema

##### /metrics

##### /metrics Response Schema

##### /models

##### /models Response Schema

##### /modelbreaches

##### /modelbreaches Response Schema

##### /modelbreaches/[pbid]/comments

##### /modelbreaches/[pbid]/comments Response Schema

##### /modelbreaches/[pbid]/acknowledge and /unacknowledge

##### /network

##### /network Response Schema

##### /pcaps

##### 212

##### 214

##### 221

##### 222

##### 225

##### 227

##### 228

##### 230

##### 232

##### 234

##### 235

##### 237

##### 240

##### 242

##### 243

##### 246

##### 253

##### 258

##### 303

##### 304

##### 305

##### 306

##### 311

##### 342


##### /pcaps Response Schema

##### /similardevices

##### /similardevices Response Schema

##### /subnets

##### /subnets Response Schema

##### /status

##### /status Response Schema

##### /summarystatistics

##### /summarystatistics Response Schema

##### /tags

##### /tags Response Schema

##### /tags/entities

##### /tags/[tid]/entities

##### /tags/entities and /tags/[tid]/entities Response Schema

##### Appendix: Darktrace Threat Visualizer API Guide Changelog

##### 345

##### 347

##### 349

##### 353

##### 355

##### 357

##### 361

##### 399

##### 402

##### 408

##### 410

##### 411

##### 413

##### 416

##### 421


## GETTING STARTED WITH THE API

The Darktrace API provides a method of accessing additional information about a particular alert or device in the Darktrace

system. The API uses HTTP GET requests to return formatted JSON data containing the requested information and HTTP

POST or DELETE requests to configure the system. The API can be an incredibly useful tool to integrate Darktrace with

third-party SIEM or SOC environments, or perform bulk actions on devices and model breaches.

Requests are made in the format:

```
'https://[appliance-IP]/[endpoint]' -H "DTAPI-Token: [token]" -H "DTAPI-Date: [date]" -H
"DTAPI-Signature: [signature]"
```
_Pseudocode example_

The required headers are composed of a date-time within 30 minutes of the instance server time (DTAPI-Date), a public

token collected from user account settings or the Threat Visualizer System Config page (DTAPI-Token), and a HMAC-

SHA1 hash (DTAPI-Signature) of the public and private tokens, the date-time and the specific API endpoint and request

parameters.

#### Acquiring the API Token Pair

Before any data can be queried, an API token pair is needed for each Master instance.

As of Darktrace Threat Visualizer 5.1, API tokens can be generated on a per-user basis. Global tokens generated before 5.

will continue to work and be available for generation from the System Config page.

###### Per-user Token

To create a per-user token, the user must first be granted permission to access the API. API tokens can only be created by

local users - those created within the Threat Visualizer - and are not available to users created via LDAP or SAML SSO.

1. On the Threat Visualizer of the instance you wish to request data from, navigate to the Permissions Admin page
    (Main Menu > Admin) as a user who can modify the user intended for API access. Select the “Created
    Accounts” tab.
2. Locate the user and click the pen icon to edit. On the Flags step, turn on “API Access”. Save the changes.
3. As the user intended for API access, access the Threat Visualizer or Platform Accounts Console ( _formerly SaaS_
    _Console_ ). If already logged in, a logout/login is recommended to refresh the permissions. Navigate to Account
    Settings from the main menu.

```
Locate the ‘API Access’ button and click it.
```
4. In the popup, click ‘New’. Two values will be displayed, a Public and Private token, the Private token will not be
    displayed again.

```
Both Tokens are required to generate the DT-API Signature value, which must be passed with every API
request made to the appliance, so make sure you record them securely.
```
The API endpoints accessible by user tokens are restricted to those the user can access in the Threat Visualizer user

interface. Please see _Minimum Required Permissions for API Endpoints_ for more information.


###### Global Token

Creating a global API token requires access to the Darktrace Threat Visualizer interface and a user account with appropriate

permissions to access and modify the System Config page.

Actions by the global API token will be assigned to the DTAPI_[token] user, where [token] represents the public token

of the pair generated below.

1. Navigate to the System Config page on the Threat Visualizer of the instance you wish to request data from.
    Select “Settings” from the left-hand menu.
2. Locate the ‘API Token’ subsection and click ‘New’.
3. Two values will be displayed, a Public and Private token, the Private token will not be displayed again.

Both Tokens are required to generate the DT-API Signature value, which must be passed with every API request made

to the appliance, so make sure you record them securely.


## API AUTHENTICATION

#### Building an API request

API Authentication requires the API request to be constructed in advance as the specific request with its parameters is

used to generate the authentication value [signature]. In this example, the following GET request is used to retrieve

model breaches from an instance within a given timeframe.

```
https://<appliance-ip>/modelbreaches?starttime=[START_TIMESTAMP]&endtime=[END_TIMESTAMP]
```
Where:

- [START_TIMESTAMP]= UNIX timestamp in milliseconds (verify 13 digits)
- [END_TIMESTAMP]= UNIX timestamp in milliseconds (verify 13 digits)

#### Required Headers

Every API query requires three header values for authentication:

DTAPI-Token: [public-token] is the public token obtained when creating the API token pair.

DTAPI-Date: [date] is the current date and time, which must be within 30 minutes of the Darktrace system time (UTC).

Any of the following formats are acceptable.

- YYYYMMDDTHHIISS, i.e. 20230101T
- YYYY-MM-DDTHH:ii:ss, i.e. 2023-01-01T12:00:
- YYYY-MM-DD HH:ii:ss, i.e. 2023-01-01 12:00:
- Mon, 01 Jan 2023 12:00:
- Mon, 01 Jan 2023 12:00:00 [GMT/UTC]
- Mon Jan 1 12:00:00 2023

DTAPI-Signature: [signature] is determined by computing the HMAC-SHA1 construct of a specific string. This string is

composed of the API query string created above, the private API token, the public API token and the current date in any of

the formats above, each separated by a newline character.

#### Generating the Signature

The [signature] value is calculated using an implementation of the following method. Note the \n newline characters

between the request, API token and timestamp in the 2nd parameter passed to the function:

```
hmac-sha1("[private-token]","[api-request]\n[public-token]\n[date]");
```
```
hmac-sha1("7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb","/modelbreaches?
starttime=1701388800000&endtime=1704070800000\n118v8jecrbrtkucou5a34hsbzounohx6jce61dwy\n
101T120000");
```
_Pseudocode example_

The above function outputs f19ae16721cc0e020ad12ec372cb15fa93bf3626, the [signature] value, using the

following example values.


```
[api-request]: /modelbreaches?starttime=1701388800000&endtime=
[public-token]: 118v8jecrbrtkucou5a34hsbzounohx6jce61dwy
[private-token]: 7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb
[date]: 20230101T
```
Examples of signature generation in Python3 and Bash are provided in _Code Examples - API Signature Generation_.

Important Notes:

- Only the endpoint request is used to generate the signature, the IP address or hostname of the instance should
    not be included.
- The time value used for the signature generation and for the request must be consistent.
- For POST requests, add each post parameter into the query string as
    /postendpoint?param1=value&param2=value or
    /postendpoint?{"param1":"value","param2":"value"} to generate the signature value, where param
    and param2 are the data fields to be edited.

#### Making the API Query

Once the [signature] value is generated, all headers are now ready for authentication. The API call can now be made in

the following format:

```
'https://[appliance-IP]/[request]' -H "DTAPI-Token: [public-token]" -H "DTAPI-Date: [date]"
-H "DTAPI-Signature: [signature]"
```
_Pseudocode example_

For example:

```
curl -k 'https://192.168.0.1/modelbreaches?starttime=1701388800000&endtime=1704070800000' -H
"DTAPI-Token: 118v8jecrbrtkucou5a34hsbzounohx6jce61dwy" -H "DTAPI-Date: 20230101T120000" -H
"DTAPI-Signature: f19ae16721cc0e020ad12ec372cb15fa93bf3626"
```

## CODE EXAMPLES - API SIGNATURE GENERATION

Below are examples of the [signature] generation in Python3 and Bash using the sample parameters provided.

More code examples in other languages, along with full authentication and connection scripts where available, may be

requested from Darktrace support.

```
COMPONENT VALUE
```
```
Request /modelbreaches?starttime=1701388800000&endtime=
```
```
Public Token 118v8jecrbrtkucou5a34hsbzounohx6jce61dwy
```
```
Private Token 7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb
```
```
Date 20230101T
```
```
Expected Output f19ae16721cc0e020ad12ec372cb15fa93bf
```
Ensure that the library or method used for signature generation uses the correct encoding for your environment, to prevent

signature generation errors.

**Python**

```
import hmac
import hashlib
sig = hmac.new('7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb'.encode('ASCII'),('/modelbreaches?
starttime=1701388800000&endtime=1704070800000' +'\n'+
'118v8jecrbrtkucou5a34hsbzounohx6jce61dwy' +'\n'+ '20230101T120000').encode('ASCII'),
hashlib.sha1).hexdigest()
print(sig)
```
**Bash**

This example uses the current time to generate the signature value. To recreate the example value above, replace the

```
date function with 20230101T
```
```
#!/bin/bash
```
```
time=$( date -u +"%Y-%m-%d %T" ) #Adjust if required for time zone
privatetoken=7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb
publictoken=118v8jecrbrtkucou5a34hsbzounohx6jce61dwy
request="/modelbreaches?starttime=1701388800000&endtime=1704070800000"
```
```
authSig=$(printf '%s\n' "$request" "$publictoken" "$time")
hmac="$(echo -n "$authSig" | openssl dgst -sha1 -hex -hmac "$privatetoken" -binary | xxd -
p )"
echo $hmac
```

## CODE EXAMPLES - API GET REQUESTS

The following are simple examples of GET requests in shell script (Bash).

More code examples in other languages, along with full authentication and connection scripts where available, may be

requested from Darktrace support.

###### 1. Retrieve Basic Instance Health Info

```
#!/bin/bash
```
```
time=$( date -u +"%Y-%m-%d %T" ) #Adjust if required for time zone
privatetoken=7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb
publictoken=118v8jecrbrtkucou5a34hsbzounohx6jce61dwy
```
```
host="https://example.darktrace.com"
```
```
request="/status?fast=true&includechildren=false"
```
```
authSig=$(printf '%s\n' "$request" "$publictoken" "$time")
hmac="$(echo -n "$authSig" | openssl dgst -sha1 -hex -hmac "$privatetoken" -binary | xxd -
p )"
```
```
curl -k "$host$request" -H "DTAPI-Token: $publictoken" -H "DTAPI-Date: $time" -H "DTAPI-
Signature: $hmac"
```
###### Expected Response

```
{
"excessTraffic": false,
"time": "2021-04-01 13:30",
"installed": "2018-10-22",
"mobileAppConfigured": true,
"version": "5.1.0 (d80d42)",
"ipAddress": "10.1.2.3",
"modelsUpdated": "2021-03-26 11:20:48",
"modelPackageVersion": "4.0-8515~20210322143408~g300d5d",
"bundleVersion": "50018",
"bundleDate": "2021-03-24 18:33:59",
"bundleInstalledDate": "2021-03-24 20:20:33",
"hostname": "example",
"inoculation": false,
"applianceOSCode": "x",
"license": "2024-12-30 00:00:00",
...
```

###### 2. Get Advanced Search Results of DNS Requests

Advanced Search queries are base64 encoded JSON, which is reflected in the example below.

```
#!/bin/bash
```
```
time=$( date -u +"%Y-%m-%d %T" ) #Adjust if required for time zone
privatetoken=7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb
publictoken=118v8jecrbrtkucou5a34hsbzounohx6jce61dwy
```
```
host="https://example.darktrace.com"
endpoint="/advancedsearch/api/search/"
```
```
raw_request='{"search":"@type:dns","fields":[],"offset":0,"timeframe":"43200","time":
{"user_interval":0}}';
request=$(echo $raw_request | base64)
```
```
authSig=$(printf '%s\n' "$endpoint$request" "$publictoken" "$time")
hmac="$(echo -n "$authSig" | openssl dgst -sha1 -hex -hmac "$privatetoken" -binary | xxd -
p )"
```
```
curl -k "$host$endpoint$request" -H "DTAPI-Token: $publictoken" -H "DTAPI-Date: $time" -H
"DTAPI-Signature: $hmac"
```
###### Expected Response

```
{
"took": 0,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
...
```

## CODE EXAMPLES - API POST REQUESTS

The following are simple examples of POST requests using shell script (Bash).

More code examples in other languages, along with full authentication and connection scripts where available, may be

requested from Darktrace support.

#### 1. Update the Label on a Device

This example uses a POST request with parameters.

```
#!/bin/bash
```
```
time=$( date -u +"%Y-%m-%d %T" )
privatetoken=7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb
publictoken=118v8jecrbrtkucou5a34hsbzounohx6jce61dwy
```
```
host="https://example.darktrace.com"
```
```
endpoint="/devices"
request='did=101&label=Test'
```
```
authSig=$(printf '%s\n' "$endpoint?$request" "$publictoken" "$time")
hmac="$(echo -n "$authSig" | openssl dgst -sha1 -hex -hmac "$privatetoken" -binary | xxd -
p )"
```
```
curl -k -X POST "$host$endpoint" -H "DTAPI-Token: $publictoken" -H "DTAPI-Date: $time" -H
"DTAPI-Signature: $hmac" --data "$request"
```
###### Expected Response

```
{
"response": "SUCCESS",
"device": {
"did": 101,
"ip": "10.15.12.201",
"ips": [
{
"ip": "10.15.12.201",
"timems": 1617278400000,
"time": "2021-04-01 12:00:00",
"sid": 12
}
],
"sid": 12,
"firstSeen": 1605794873000,
"lastSeen": 1617279920000,
"devicelabel": "Test",
"typename": "server",
"typelabel": "Server"
}
}
```

#### 2. Create A New Tag

This example uses a POST request with a JSON body.

```
#!/bin/bash
```
```
time=$( date -u +"%Y-%m-%d %T" )
privatetoken=7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb
publictoken=118v8jecrbrtkucou5a34hsbzounohx6jce61dwy
```
```
host="https://example.darktrace.com"
```
```
endpoint="/tags"
request='{"name":"Example Tag","data":
{"auto":false,"visibility":"Public","description":"Test","color":200}}'
```
```
authSig=$(printf '%s\n' "$endpoint?$request" "$publictoken" "$time")
hmac="$(echo -n "$authSig" | openssl dgst -sha1 -hex -hmac "$privatetoken" -binary | xxd -
p )"
```
```
curl -k -X POST "$host$endpoint" -H "DTAPI-Token: $publictoken" -H "DTAPI-Date: $time" -H
"DTAPI-Signature: $hmac" --data "$request" -H "Content-Type: application/json"
```
###### Expected Response

```
{
"tid": 143,
"expiry": 0,
"thid": 143,
"name": "Example Tag",
"restricted": false,
"data": {
"auto": false,
"color": 200,
"description": "Test",
"visibility": "Public"
},
"isReferenced": false
}
```
If the response "INPUT ERROR" is returned, ensure a tag with the same name does not already exist.


#### 3. Create a Comment on a Model Breach

This example uses a POST request with a JSON body.

```
#!/bin/bash
```
```
time=$( date -u +"%Y-%m-%d %T" ) #Adjust if required for time zone
privatetoken=7chbwad4hl4n5ok69e2edrs2ogpiqy8ldd5oozdb
publictoken=118v8jecrbrtkucou5a34hsbzounohx6jce61dwy
```
```
host="https://example.darktrace.com"
```
```
endpoint="/modelbreaches/101/comments"
request='{"message":"Test Comment"}'
```
```
authSig=$(printf '%s\n' "$endpoint?$request" "$publictoken" "$time")
hmac="$(echo -n "$authSig" | openssl dgst -sha1 -hex -hmac "$privatetoken" -binary | xxd -
p )"
```
```
curl -k -X POST "$host$endpoint" -H "DTAPI-Token: $publictoken" -H "DTAPI-Date: $time" -H
"DTAPI-Signature: $hmac" --data "$request" -H "Content-Type: application/json"
```
###### Expected Response

```
{
"response": "SUCCESS"
}
```

## MINIMUM REQUIRED PERMISSIONS FOR API

## ENDPOINTS

From Darktrace Threat Visualizer 5.1 and above, API tokens can be generated on a per-user basis. User tokens are subject to

the network restrictions and permission restrictions on their associated user. The following permissions are the minimum

that must be assigned to the associated user to access the endpoint.

The global API token generated on the System Config page is not subject to these restrictions.

```
ENDPOINT GET POST/ DELETE
```
```
/advancedsearch/api/search Unrestricted Devices and Advanced Search
```
```
Unrestricted Devices and Advanced
Search
```
```
/advancedsearch/api/analyze Unrestricted Devices and Advanced Search N/A
```
```
/advancedsearch/api/graph Unrestricted Devices and Advanced Search N/A
```
```
/aianalyst/acknowledge N/A Acknowledge Breaches
```
```
/aianalyst/unacknowledge N/A Acknowledge Breaches
```
```
/aianalyst/groups
```
```
Unrestricted Devices¹ and any of : Visualizer/
Platform Accounts Console
N/A
```
```
/aianalyst/incidents
Unrestricted Devices¹ and any of : Visualizer/
Platform Accounts Console
```
```
N/A
```
```
/aianalyst/incidentevents
Unrestricted Devices¹ and any of : Visualizer/
Platform Accounts Console
```
```
N/A
```
```
/aianalyst/incident/comments
Unrestricted Devices¹ and any of : Visualizer/
Platform Accounts Console
```
```
Discuss Breaches
```
```
/aianalyst/investigations N/A Create AI Analyst Investigations
```
```
/aianalyst/stats
Unrestricted Devices¹ and any of : Visualizer/
Platform Accounts Console
N/A
```
```
/aianalyst/pin N/A
Any of : Visualizer/Platform Accounts
Console
```
```
/aianalyst/unpin N/A
```
```
Any of : Visualizer/Platform Accounts
Console
```
```
/antigena Unrestricted Devices¹ and Visualizer
```
```
Darktrace RESPOND (formerly
Antigena ), Unrestricted Devices¹,
Visualizer
```
```
/antigena/manual N/A
```
```
Darktrace RESPOND (formerly
Antigena ), Unrestricted Devices¹,
Visualizer
```
```
/antigena/summary Unrestricted Devices¹ and Visualizer N/A
```
```
/components
Any of : Visualizer/Platform Accounts Console/
View Models/Edit Models
N/A
```
```
/cves² Visualizer N/A
```
```
/details
```
```
Unrestricted Devices¹ and any of : Visualizer/
Platform Accounts Console
N/A
```
```
/deviceinfo Unrestricted Devices¹ and Visualizer N/A
```

```
ENDPOINT GET POST/ DELETE
```
```
/devices
```
```
Unrestricted Devices¹ and any of : Visualizer/
Platform Accounts Console/View Models/Edit
Models/Device Admin
```
```
Device Admin and Unrestricted
Devices
```
```
/devicesummary
```
```
Unrestricted Devices¹ and any of : Visualizer/
Platform Accounts Console/View Models/Edit
Models/Device Admin
```
```
N/A
```
```
/devicesearch Visualizer and Unrestricted Devices N/A
```
```
/endpointdetails Unrestricted Devices¹ and Visualizer N/A
```
```
/enums
```
```
Any of : Visualizer/Platform Accounts Console/
View Models/Edit Models
N/A
```
```
/filtertypes
```
```
Any of : Visualizer/Platform Accounts Console/
View Models/Edit Models
N/A
```
```
/intelfeed Edit Domains Edit Domains
```
```
/mbcomments Visualizer N/A
```
```
/metricdata Visualizer N/A
```
```
/metrics
```
```
Any of : Visualizer/Platform Accounts Console/
View Models/Edit Models
N/A
```
```
/models
Any of : Visualizer/Platform Accounts Console/
View Models/Edit Models
```
```
N/A
```
```
/modelbreaches
```
```
Unrestricted Devices¹ and any of : Visualizer/
Platform Accounts Console/View Models/Edit
Models
```
```
N/A
```
```
/modelbreaches/[pbid]/comments Visualizer/Platform Accounts Console Discuss Breaches
```
```
/modelbreaches/[pbid]/acknowledge N/A Acknowledge Breaches
```
```
/modelbreaches/[pbid]/unacknowledge N/A Acknowledge Breaches
```
```
/network Unrestricted Devices¹ and Visualizer N/A
```
```
/pcaps Create PCAPs Create PCAPs
```
```
/pcaps/[filename] Create PCAPs and Download PCAPs N/A
```
```
/similardevices Visualizer N/A
```
```
/subnets
Any of : Visualizer/Platform Accounts Console/
Subnet Admin
```
```
Subnet Admin
```
```
/status Status N/A
```
```
/summarystatistics Visualizer N/A
```
```
/tags
Any of : Visualizer/Platform Accounts Console/
View Models/Edit Models/Device Admin
```
```
Edit Tags³
```
```
/tags/entities
Any of : Visualizer/Platform Accounts Console/
View Models/Edit Models/Device Admin
Edit Tags³
```
```
/tags/[tid]/entities
```
```
Any of : Visualizer/Platform Accounts Console/
View Models/Edit Models/Device Admin
Edit Tags³
```
¹ Without this permission, data will be returned in anonymized format.

² Only valid in Darktrace/OT environments.


³ This permission is required from Darktrace Threat Visualizer 5.2 and above. On upgrade to 5.2, users who possess

“Visualizer” or “Platform Accounts Console” will be granted this permission automatically.

The Visualizer or Platform Accounts Console permissions are required to initially generate and retrieve the public/private

token pair for the user but can be revoked after this action has been performed if no longer required.

###### Darktrace/Email API Endpoints

The relevant permissions for Darktrace/Email endpoints are included in the API documentation, available at

```
https://[instance]/agemail/api/api-docs. These permissions are repeated below for reference.
```
All endpoints require the Email Logs permission at a minimum.

```
ENDPOINT GET POST
```
```
/v1.0/admin/decode_link Email logs N/A
```
```
/v1.0/dash/action_summary Email logs N/A
```
```
/v1.0/dash/dash_stats Email logs N/A
```
```
/v1.0/dash/data_loss Email logs N/A
```
```
/v1.0/dash/user_anomaly Email logs N/A
```
```
/v1.0/emails/{uuid}/action N/A Email logs, Manual Action or Restricted Manual Action¹
```
```
/v1.0/emails/{uuid} Email logs N/A
```
```
/v1.0/emails/{uuid}/download Email logs,Download Email N/A
```
```
/v1.0/emails/search N/A Email logs
```
```
/v1.0/resources/actions Email logs N/A
```
```
/v1.0/resources/tags Email logs N/A
```
```
/v1.0/resources/filters Email logs N/A
```
```
/v1.0/system/audit/eventTypes Email logs, Audit Log (Darktrace/Email) N/A
```
```
/v1.0/system/audit/events Email logs, Audit Log (Darktrace/Email) N/A
```
¹ If Restricted Manual Action is possessed, users can only release emails to the original recipient.


## /ADVANCEDSEARCH/API/SEARCH

The /advancedsearch endpoint allows Advanced Search data to be queried and exported in JSON format from the

Darktrace instance programmatically. Advanced Search queries are Base64 encoded strings, composed of the query

search terms. There are three extensions available:

- /advancedsearch/api/search
- /advancedsearch/api/analyze
- /advancedsearch/api/graph

The search extension provides the standard Advanced Search query functionality - see graph or analyze for more

details on other extensions.

To familiarize yourself with what a query might look like, make a basic query in the Threat Visualizer version of Advanced

Search and look at the URL - it will appear as a string of random characters. Copy the string of random characters found

after the # in the URL. From the Threat Visualizer homepage, select Utilities from the main menu and then Base

Converter. Paste the string into the pop-up and click ‘Decode’ - you can now see what an Advanced Search query is

composed of.

For example, making a query in the Threat Visualizer Advanced Search for @type:"ssl" AND @fields.dest_port:"443"

over the last 15 minutes will produce the URL:

```
https://[instance]/advancedsearch/
#eyJzZWFyY2giOiIgQHR5cGU6XCJzc2xcIiBBTkQgQGZpZWxkcy5kZXN0X3BvcnQ6XCI0NDNcIiIsImZpZWxkcyI6W10sI
m9mZnNldCI6MCwidGltZWZyYW1lIjoiOTAwIiwiZ3JhcGhtb2RlIjoiY291bnQiLCJ0aW1lIjp7InVzZXJfaW50ZXJ2YWw
iOjB9LCJtb2RlIjoiIiwiYW5hbHl6ZV9maWVsZCI6IiJ
```
Pasting the part after the # into the Base64 converter and clicking ‘Decode’ will produce:

```
{"search":" @type:\"ssl\" AND @fields.dest_port:\"443\"","fields":[],"offset":
0,"timeframe":"900","graphmode":"count","time":{"user_interval":
0},"mode":"","analyze_field":""}
```
This is the basic structure of an Advanced Search query. Some of the parameters included in this request are not necessary

when accessing Advanced Search programmatically. Please see the notes section for more details.

###### Request Type(s)

```
[GET] [POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
from string Start time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
to string End time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
interval numeric A time interval in seconds from the current time over which to return results.
```
```
search string Optional Advanced Search search query to make. Ensure all double quotes are escaped.
```
```
analyze_field string The field to return aggregate stats for. Only used when making queries to the /graph/mean extension
```

```
PARAMETER TYPE DESCRIPTION
```
```
offset numeric An offset for the results returned.
```
###### Notes

- Double quotes used in the search string must be escaped with a backslash before encoding. For example,
    "search":" @type:\"ssl\" AND @fields.dest_port:\"443\"".
- The query timeframe can either take a starttime/endtime or to/from value, or a timeframe interval of
    seconds since the current time.

```
◦ If starttime/endtime or to/from is used, the timeframe value must be set to "custom". Time
parameters must always be specified in pairs.
```
```
◦ If using interval, the time: {} object can be omitted from the query. It is important to note that
the query response will not be the same every time as the interval time value is relative.
```
- By default, this endpoint will return 50 records at a time. The size parameter can be used to return up to
    10,000 results. Returned data can be paginated by limiting the size value and making multiple requests,
    incrementing the offset value by the size value each time (e.g., size=100, multiple queries for
       offset=0, offset=100, offset=200).
- The empty fields array is required but the values contained within it do not change the API response. All
    fields will be returned when accessing advanced search programmatically.
- The parameters graphmode and mode appear in Advanced Search queries made in the Threat Visualizer.
    They are not required when accessing Advanced Search programmatically.
- The analyze_field parameter is only required when making queries to the
    /advancedsearch/api/graph/mean endpoint.
- As of Darktrace 6.1, it is possible to use POST requests to make more complex queries. In this scenario, a POST
    request is made to /advancedsearch/api/search with the body `{“hash”:“[base64 encoded string]”}.

```
Please see example three below for more information.
```

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET HTTP/HTTPS unidirectional traffic seen over the last 12 hours:

```
https://[instance]/advancedsearch/api/search/
eyJzZWFyY2giOiJAdHlwZTpjb25uIEFORCBAZmllbGRzLnByb3RvOnRjcCBBTkQgTk9UIEBmaWVsZHMuY29ubl9z
dGF0ZTpcIlMwXCIgQU5EIE5PVCBAZmllbGRzLmNvbm5fc3RhdGU6XCJSRUpcIiBBTkQgKEBmaWVsZHMub3JpZ19w
a3RzOjAgT1IgQGZpZWxkcy5yZXNwX3BrdHM6MCkgQU5EIChAZmllbGRzLmRlc3RfcG9ydDpcIjQ0M1wiIE9SIEBm
aWVsZHMuZGVzdF9wb3J0OlwiODBcIikiLCJmaWVsZHMiOltdLCJvZmZzZXQiOjAsInRpbWVmcmFtZSI6IjQzMjAw
IiwidGltZSI6eyJ1c2VyX2ludGVydmFsIjowfX0=
```
```
Where the string
```
```
{"search":"@type:conn AND @fields.proto:tcp AND NOT @fields.conn_state:\"S0\" AND NOT
@fields.conn_state:\"REJ\" AND (@fields.orig_pkts:0 OR @fields.resp_pkts:0) AND
(@fields.dest_port:\"443\" OR @fields.dest_port:\"80\")","fields":[],"offset":
0,"timeframe":"43200","time":{"user_interval":0}}
```
```
has been Base64 encoded to
```
```
eyJzZWFyY2giOiJAdHlwZTpjb25uIEFORCBAZmllbGRzLnByb3RvOnRjcCBBTkQgTk9UIEBmaWVsZHMuY29ubl9z
dGF0ZTpcIlMwXCIgQU5EIE5PVCBAZmllbGRzLmNvbm5fc3RhdGU6XCJSRUpcIiBBTkQgKEBmaWVsZHMub3JpZ19w
a3RzOjAgT1IgQGZpZWxkcy5yZXNwX3BrdHM6MCkgQU5EIChAZmllbGRzLmRlc3RfcG9ydDpcIjQ0M1wiIE9SIEBm
aWVsZHMuZGVzdF9wb3J0OlwiODBcIikiLCJmaWVsZHMiOltdLCJvZmZzZXQiOjAsInRpbWVmcmFtZSI6IjQzMjAw
IiwidGltZSI6eyJ1c2VyX2ludGVydmFsIjowfX0=
```
2. GET all identified files between 8am and 10am on February 1st 2020 with a computed SHA-1 hash:

```
https://[instance]/advancedsearch/api/search/
eyJzZWFyY2giOiJAdHlwZTpmaWxlc19pZGVudGlmaWVkIEFORCBfZXhpc3RzXzpcIkBmaWVsZHMuc2hhMVwiIiwi
ZmllbGRzIjpbXSwib2Zmc2V0IjowLCJ0aW1lZnJhbWUiOiJjdXN0b20iLCJ0aW1lIjp7ImZyb20iOiIyMDIwLTAy
LTAxVDA4OjAwOjAwWiIsInRvIjoiMjAyMC0wMi0wMVQxMDowMDowMFoiLCJ1c2VyX2ludGVydmFsIjoiMCJ9fQ==
```
```
Where the string
```
```
{"search":"@type:files_identified AND _exists_:\"@fields.sha1\"","fields":[],"offset":
0,"timeframe":"custom","time":
{"from":"2020-02-01T08:00:00Z","to":"2020-02-01T10:00:00Z","user_interval":"0"}}
```
```
has been Base64 encoded to
```
```
eyJzZWFyY2giOiJAdHlwZTpmaWxlc19pZGVudGlmaWVkIEFORCBfZXhpc3RzXzpcIkBmaWVsZHMuc2hhMVwiIiwi
ZmllbGRzIjpbXSwib2Zmc2V0IjowLCJ0aW1lZnJhbWUiOiJjdXN0b20iLCJ0aW1lIjp7ImZyb20iOiIyMDIwLTAy
LTAxVDA4OjAwOjAwWiIsInRvIjoiMjAyMC0wMi0wMVQxMDowMDowMFoiLCJ1c2VyX2ludGVydmFsIjoiMCJ9fQ==
```

3. POST to retrieve any SMB1 sessions seen in the last 7 days, using the new 6.1 method:

```
https://[instance]/advancedsearch/api/search with body
{"hash":"eyJzZWFyY2giOiJAdHlwZTpzbWJfc2Vzc2lvbiBBTkQgQGZpZWxkcy5wcm90b2NvbF92ZXI6XCJzbWI
xXCIiLCJmaWVsZHMiOltdLCJvZmZzZXQiOjAsInRpbWVmcmFtZSI6IjYwNDgwMCIsInRpbWUiOnsidXNlcl9pbnR
lcnZhbCI6MH19"}
```
```
Where the string
```
```
{"search":"@type:smb_session AND @fields.protocol_ver:\"smb1\"","fields":[],"offset":
0,"timeframe":"604800","time":{"user_interval":0}}
```
```
has been Base64 encoded to
```
```
eyJzZWFyY2giOiJAdHlwZTpzbWJfc2Vzc2lvbiBBTkQgQGZpZWxkcy5wcm90b2NvbF92ZXI6XCJzbWIxXCIiLCJm
aWVsZHMiOltdLCJvZmZzZXQiOjAsInRpbWVmcmFtZSI6IjYwNDgwMCIsInRpbWUiOnsidXNlcl9pbnRlcnZhbCI6
MH19
```

###### Example Response

_Request:_

```
/advancedsearch/api/search/
eyJzZWFyY2giOiJAdHlwZTpjb25uIEFORCBAZmllbGRzLnByb3RvOnRjcCBBTkQgTk9UIEBmaWVsZHMuY29ubl9zdGF0ZT
pcIlMwXCIgQU5EIE5PVCBAZmllbGRzLmNvbm5fc3RhdGU6XCJSRUpcIiBBTkQgKEBmaWVsZHMub3JpZ19wa3RzOjAgT1Ig
QGZpZWxkcy5yZXNwX3BrdHM6MCkgQU5EIChAZmllbGRzLmRlc3RfcG9ydDpcIjQ0M1wiIE9SIEBmaWVsZHMuZGVzdF9wb3
J0OlwiODBcIikiLCJmaWVsZHMiOltdLCJvZmZzZXQiOjAsInRpbWVmcmFtZSI6IjQzMjAwIiwidGltZSI6eyJ1c2VyX2lu
dGVydmFsIjowfX0=
```
```
{
"took": 17,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 6900,
"max_score": null,
"hits": [
{
"_index": "logstash-dt-01-01-2020.02.24",
"_type": "doc",
"_id": "AXB4bgyXFqFpgk38klzi",
"_score": null,
"_source": {
"@fields": {
"orig_pkts": 2,
...
},
"@type": "conn",
"@timestamp": "2020-02-24T18:20:31",
"@message":
"1582568431.7656\tCNbx1P3gEMU3dZqS00\t10.0.56.12\t50518\t192.168.120.39\t443\ttcp\t-
\t2\t64\tOriginator SYN + FIN\tSH\ttrue\t0\t0\t1582568431.7656\t0\t104\tF\ttrue\t0"
},
"sort": [
1582568431000
]
},
...
}
]
},
"darktraceChildError": "",
"kibana": {
"index": [
"logstash-darktrace-2020.02.24"
],
"per_page": 50,
"time": {
"from": "2020-02-24T06:27:23.209Z",
"to": "2020-02-24T18:27:23.209Z"
},
"default_fields": [
"@type",
"@message"
]
}
}
```
_Response is abbreviated._


## /ADVANCEDSEARCH/API/SEARCH RESPONSE

## SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
took numeric 22 The time the request took in milliseconds.
```
```
timed_out boolean FALSE Whether the response timed out.
```
```
_shards object A system field.
```
```
_shards.total numeric 2 A system field.
```
```
_shards.successful numeric 2 A system field.
```
_shards.skipped numeric (^0) A system field.
_shards.failed numeric 0 A system field.
hits object
An object encapsulating the advanced search
entries that matched the request.
hits.total numeric 13123
The total number of entries that matched the
query.
hits.max_score - null A system field.
hits.hits array An array of advanced search entries.
hits.hits._index string
logstash-
dt-01-2020.03.23
The index the entry was returned from.
hits.hits._type string doc A system field.
hits.hits._id string K18S2Iqiu7Wz1jaN The unique id for the entry in the database.
hits.hits._score - null A system field.
hits.hits._source object An object describing the entry.
hits.hits._source.@fields object
An object containing all the relevant fields for the
protocol. A list of fields that may be returned for
each protocol can be found at [].
hits.hits._source.@type string conn The protocol or entry type.
hits.hits._source.@timestamp string 2020-03-23T11:59:09
A timestamp for the insertion of the entry into
advanced search logs.
hits.hits._source.@message string
1584964749.0817
CT6zqD1olMlncAp00
104.20.203.23 54250
172.217.169.36443
tcp - 2  64
Midstream traffic
OTH true 0 0
1584964749.0817 0
104 A true 0
A unique string constructed from field values for
the entry.
hits.hits.sort array 1586937600000
A simplified timestamp for the record for sorting
purposes.
darktraceChildError string Factory Probe 1 The name of a probe which did not respond to
the request.
kibana object Details about the advanced search logs.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

kibana.index array A system field.

kibana.per_page numeric 50

```
The number of results returned in the page. If the
size value is changed, will continue to return a
value of 50.
```
kibana.time object The time window specified in the request.

kibana.time.from string
2020-03-23T00:09:24
.980Z

```
The start of the time window specified in the
request.
```
kibana.time.to string
2020-03-23T12:09:24
.980Z

```
The end of the time window specified in the
request.
```
kibana.default_fields array “@type” Default fields always returned at the highest
level.


###### Example Response

_Request:_

```
/advancedsearch/api/search/
eyJzZWFyY2giOiJAdHlwZTpjb25uIEFORCBAZmllbGRzLnByb3RvOnRjcCBBTkQgTk9UIEBmaWVsZHMuY29ubl9zdGF0ZT
pcIlMwXCIgQU5EIE5PVCBAZmllbGRzLmNvbm5fc3RhdGU6XCJSRUpcIiBBTkQgKEBmaWVsZHMub3JpZ19wa3RzOjAgT1Ig
QGZpZWxkcy5yZXNwX3BrdHM6MCkgQU5EIChAZmllbGRzLmRlc3RfcG9ydDpcIjQ0M1wiIE9SIEBmaWVsZHMuZGVzdF9wb3
J0OlwiODBcIikiLCJmaWVsZHMiOltdLCJvZmZzZXQiOjAsInRpbWVmcmFtZSI6IjQzMjAwIiwidGltZSI6eyJ1c2VyX2lu
dGVydmFsIjowfX0=
```
```
{
"took": 17,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 6900,
"max_score": null,
"hits": [
{
"_index": "logstash-dt-01-01-2020.02.24",
"_type": "doc",
"_id": "AXB4bgyXFqFpgk38klzi",
"_score": null,
"_source": {
"@fields": {
"orig_pkts": 2,
...
},
"@type": "conn",
"@timestamp": "2020-02-24T18:20:31",
"@message":
"1582568431.7656\tCNbx1P3gEMU3dZqS00\t10.0.56.12\t50518\t192.168.120.39\t443\ttcp\t-
\t2\t64\tOriginator SYN + FIN\tSH\ttrue\t0\t0\t1582568431.7656\t0\t104\tF\ttrue\t0"
},
"sort": [
1582568431000
]
},
...
}
]
},
"darktraceChildError": "",
"kibana": {
"index": [
"logstash-darktrace-2020.02.24"
],
"per_page": 50,
"time": {
"from": "2020-02-24T06:27:23.209Z",
"to": "2020-02-24T18:27:23.209Z"
},
"default_fields": [
"@type",
"@message"
]
}
}
```
_Response is abbreviated._


## /ADVANCEDSEARCH/API/ANALYZE

The /advancedsearch endpoint allows Advanced Search data to be queried and exported in JSON format from the

Darktrace instance programmatically. Advanced Search queries are Base64 encoded strings, composed of the query

search terms.

The analyze extension can produce a trend, score, terms or mean (“stats” in the User Interface) analysis on a

specific field. It requires a Base64 encoded query string as created in /advancedsearch/api/search as part of the

request.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
from string Start time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
to string End time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
interval numeric A time interval in seconds from the current time over which to return results.
```
```
search string Optional Advanced Search search query to make. Ensure all double quotes are escaped.
```
###### Notes

- Double quotes used in the search string must be escaped with a backslash before encoding. For example,
    "search":" @type:\"ssl\" AND @fields.dest_port:\"443\"".
- The query timeframe can either take a starttime/endtime or to/from value, or a timeframe interval of
    seconds since the current time.

```
◦ If starttime/endtime or to/from is used, the timeframe value must be set to "custom". Time
parameters must always be specified in pairs.
```
```
◦ If using interval, the time: {} object can be omitted from the query. It is important to note that
the query response will not be the same every time as the interval time value is relative.
```
- The parameters graphmode and mode appear in Advanced Search queries made in the Threat Visualizer.
    They are not required when accessing Advanced Search programmatically.
- The empty fields array is required but the values contained within it do not change the API response.


###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET the most used terms for @fields.dest_port between 2020-02-20 17:00:00 and 2020-02-20 17:15:00
    for the query @type:"dns" AND @fields.proto:"udp":

```
https://[instance]/advancedsearch/api/analyze/@fields.dest_port/terms/
eyJzZWFyY2giOiIgQHR5cGU6XCJkbnNcIiBBTkQgQGZpZWxkcy5wcm90bzpcInVkcFwiIiwiZmllbGRzIjpbXSwi
b2Zmc2V0IjowLCJ0aW1lZnJhbWUiOiJjdXN0b20iLCJ0aW1lIjp7ImZyb20iOiIyMDIwLTAyLTIwVDE3OjAwOjAw
WiIsInRvIjoiMjAyMC0wMi0yMFQxNzoxNTowMFoiLCJ1c2VyX2ludGVydmFsIjoiMCJ9fQ==
```
```
Where the string
```
```
{"search":" @type:\"dns\" AND @fields.proto:\"udp\"","fields":[],"offset":
0,"timeframe":"custom","time":
{"from":"2020-02-20T17:00:00Z","to":"2020-02-20T17:15:00Z","user_interval":"0"}}
```
```
has been Base64 encoded to
```
```
eyJzZWFyY2giOiIgQHR5cGU6XCJkbnNcIiBBTkQgQGZpZWxkcy5wcm90bzpcInVkcFwiIiwiZmllbGRzIjpbXSwi
b2Zmc2V0IjowLCJ0aW1lZnJhbWUiOiJjdXN0b20iLCJ0aW1lIjp7ImZyb20iOiIyMDIwLTAyLTIwVDE3OjAwOjAw
WiIsInRvIjoiMjAyMC0wMi0yMFQxNzoxNTowMFoiLCJ1c2VyX2ludGVydmFsIjoiMCJ9fQ==
```
2. GET the Office 365 users (@fields.saas_credential) with the most frequent failed logins
    (@type:office365 AND @fields.saas_event:"UserLoginFailed") over the last 7 days:

```
https://[instance]/advancedsearch/api/analyze/@fields.saas_credential/score/
eyJzZWFyY2giOiJAdHlwZTpvZmZpY2UzNjUgQU5EIEBmaWVsZHMuc2Fhc19ldmVudDpcIlVzZXJMb2dpbkZhaWxl
ZFwiIiwiZmllbGRzIjpbXSwib2Zmc2V0IjowLCJ0aW1lZnJhbWUiOiI2MDQ4MDAifQ==
```
```
Where the string
```
```
{"search":"@type:office365 AND @fields.saas_event:\"UserLoginFailed\"","fields":
[],"offset":0,"timeframe":"604800"}
```
```
has been Base64 encoded to
```
```
eyJzZWFyY2giOiJAdHlwZTpvZmZpY2UzNjUgQU5EIEBmaWVsZHMuc2Fhc19ldmVudDpcIlVzZXJMb2dpbkZhaWxl
ZFwiIiwiZmllbGRzIjpbXSwib2Zmc2V0IjowLCJ0aW1lZnJhbWUiOiI2MDQ4MDAifQ==
```

3. GET stats about the volume of bytes transferred from 192.168.120.39 to 10.0.56.12 on 2nd February 2020:

```
https://[instance]/advancedsearch/api/analyze/@fields.orig_bytes/mean/
eyJzZWFyY2giOiIgQGZpZWxkcy5kZXN0X2lwOlwiMTAuMC41Ni4xMlwiIEFORCBAZmllbGRzLnNvdXJjZV9pcDpc
IjE5Mi4xNjguMTIwLjM5XCIgQU5EIEB0eXBlOlwiY29ublwiIiwiZmllbGRzIjpbXSwib2Zmc2V0IjowLCJ0aW1l
ZnJhbWUiOiJjdXN0b20iLCJ0aW1lIjp7ImZyb20iOiIyMDIwLTAyLTAyVDAwOjAwOjAwWiIsInRvIjoiMjAyMC0w
Mi0wMlQyMzo1OTo1OVoiLCJ1c2VyX2ludGVydmFsIjowfX0=
```
```
Where the string
```
```
{"search":" @fields.dest_ip:\"10.0.56.12\" AND @fields.source_ip:\"192.168.120.39\" AND
@type:\"conn\"","fields":[],"offset":0,"timeframe":"custom","time":
{"from":"2020-02-02T00:00:00Z","to":"2020-02-02T23:59:59Z","user_interval":0}}
```
```
has been Base64 encoded to
```
```
eyJzZWFyY2giOiIgQGZpZWxkcy5kZXN0X2lwOlwiMTAuMC41Ni4xMlwiIEFORCBAZmllbGRzLnNvdXJjZV9pcDpc
IjE5Mi4xNjguMTIwLjM5XCIgQU5EIEB0eXBlOlwiY29ublwiIiwiZmllbGRzIjpbXSwib2Zmc2V0IjowLCJ0aW1l
ZnJhbWUiOiJjdXN0b20iLCJ0aW1lIjp7ImZyb20iOiIyMDIwLTAyLTAyVDAwOjAwOjAwWiIsInRvIjoiMjAyMC0w
Mi0wMlQyMzo1OTo1OVoiLCJ1c2VyX2ludGVydmFsIjowfX0=
```

###### Example Response

_Request:_

```
/advancedsearch/api/analyze/@fields.dest_port/terms/
eyJzZWFyY2giOiIgQHR5cGU6XCJkbnNcIiBBTkQgQGZpZWxkcy5wcm90bzpcInVkcFwiIiwiZmllbGRzIjpbXSwib2Zmc2
V0IjowLCJ0aW1lZnJhbWUiOiJjdXN0b20iLCJ0aW1lIjp7ImZyb20iOiIyMDIwLTAyLTIwVDE3OjAwOjAwWiIsInRvIjoi
MjAyMC0wMi0yMFQxNzoxNTowMFoiLCJ1c2VyX2ludGVydmFsIjoiMCJ9fQ==
```
```
{
"took": 0,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 8001,
"max_score": 0,
"hits": []
},
"aggregations": {
"terms": {
"doc_count_error_upper_bound": 0,
"sum_other_doc_count": 0,
"buckets": [
{
"key": 53,
"doc_count": 6574
},
{
"key": 5353,
"doc_count": 1427
}
]
}
},
"darktraceChildError": "",
"kibana": {
"index": "logstash-darktrace-2020.02.20",
"per_page": 50,
"time": {
"from": "2020-02-20T17:00:00.000Z",
"to": "2020-02-20T17:15:00.000Z"
}
}
}
```

## /ADVANCEDSEARCH/API/ANALYZE RESPONSE

## SCHEMA

#### Response Schema - /mean

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
took numeric (^406) The time the request took in milliseconds.
timed_out boolean FALSE Whether the response timed out.
_shards object A system field.
_shards.total numeric 2 A system field.
_shards.successful numeric 2 A system field.
_shards.skipped numeric (^0) A system field.
_shards.failed numeric 0 A system field.
hits object
An object encapsulating the advanced search
entries that matched the request.
hits.total numeric 20573
The total number of entries that matched the
query.
hits.max_score numeric 0 A system field.
hits.hits array An array of advanced search entries.
aggregations object
Aggregated values to use in graphical
operations.
aggregations.stats object An object describing statistical analysis on the
results within that interval.
aggregations.stats.count numeric 10355
The number of results contained within the
grouped interval.
aggregations.stats.min numeric 0 For the field specified when making the request,
the minimum value observed within the interval.
aggregations.stats.max numeric 14651
For the field specified when making the request,
the maximum value observed within the interval.
aggregations.stats.avg numeric 310.263351 For the field specified when making the request,
the average value observed within the interval.
aggregations.stats.sum numeric 3212777
For the field specified when making the request,
the sum of all values observed within the interval.
darktraceChildError string FactoryProbe_1 The name of a probe which did not respond to
the request.
kibana object Details about the advanced search logs.
kibana.index string
logstash-
darktrace-2020.03.0
2
A system field.
kibana.per_page numeric 50
The number of results returned in the page. If the
size value is changed, will continue to return a
value of 50.
kibana.time object The time window which the data is grouped into.


```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
kibana.time.from string
2020-03-02T00:00:00
.000Z
```
```
The start of the time window specified in the
request.
```
```
kibana.time.to string
2020-03-02T23:59:59
.000Z
```
```
The end of the time window specified in the
request.
```
###### Example Response

```
{
"took": 0,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 25,
"max_score": 0,
"hits": []
},
"aggregations": {
"stats": {
"count": 25,
"min": 97,
"max": 308,
"avg": 195.36,
"sum": 4884
}
},
"kibana": {
"index": "logstash-darktrace-2020.04.17",
"per_page": 50,
"time": {
"from": "2020-04-17T17:27:43.806Z",
"to": "2020-04-17T18:27:43.806Z"
}
}
}
```

#### Response Schema - /terms

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
took numeric 171 The time the request took in milliseconds.
```
```
timed_out boolean FALSE Whether the response timed out.
```
```
_shards object A system field.
```
```
_shards.total numeric 4 A system field.
```
```
_shards.successful numeric 4 A system field.
```
```
_shards.skipped numeric 0 A system field.
```
```
_shards.failed numeric 0 A system field.
```
```
hits object An object encapsulating the advanced search
entries that matched the request.
```
```
hits.total numeric 5
The total number of entries that matched the
query.
```
hits.max_score numeric (^0) A system field.
hits.hits array An array of advanced search entries.
aggregations object
An array of aggregated data about the field
queried upon.
aggregations.terms object
An array of aggregated data from the terms
analysis performed.
aggregations.terms.doc_count_error_upp
er_bound
numeric 0 A system field.
aggregations.terms.sum_other_doc_count numeric 0 A system field.
aggregations.terms.buckets array
An array of values for the field which was
analyzed.
aggregations.terms.buckets.key string
grayson.stone@holdi
ngsinc.com
A field value.
aggregations.terms.buckets.doc_count numeric 3
The number of times the value appeared in the
specified field.
darktraceChildError string FactoryProbe_1
The name of a probe which did not respond to
the request.
kibana object Details about the advanced search logs.
kibana.index string
logstash-
darktrace-2020.03.2
3
A system field.
kibana.per_page numeric 50
The number of results returned in the page. If the
size value is changed, will continue to return a
value of 50.
kibana.time object The time window specified in the request.
kibana.time.from string
2020-03-16T16:34:45
.211Z
The start of the time window specified in the
request.
kibana.time.to string
2020-03-23T16:34:45
.211Z
The end of the time window specified in the
request.


###### Example Response

```
{
"took": 0,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 8001,
"max_score": 0,
"hits": []
},
"aggregations": {
"terms": {
"doc_count_error_upper_bound": 0,
"sum_other_doc_count": 0,
"buckets": [
{
"key": 53,
"doc_count": 6574
},
...
]
}
},
"darktraceChildError": "",
"kibana": {
"index": "logstash-darktrace-2020.02.20",
"per_page": 50,
"time": {
"from": "2020-02-20T17:00:00.000Z",
"to": "2020-02-20T17:15:00.000Z"
}
}
}
```
_Response is abbreviated._


#### Response Schema - /trend

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
took numeric 83 The time the request took in milliseconds.
```
```
timed_out boolean FALSE Whether the response timed out.
```
```
_shards object A system field.
```
```
_shards.total numeric 2 A system field.
```
```
_shards.successful numeric 2 A system field.
```
```
_shards.skipped numeric 0 A system field.
```
```
_shards.failed numeric 0 A system field.
```
```
hits object An object encapsulating the advanced search
entries that matched the request.
```
```
hits.total numeric 20573
The total number of entries that matched the
query.
```
```
hits.max_score NoneTypenull A system field.
```
```
hits.hits array An array of advanced search entries.
```
```
hits.hits.id string SF The value of the specified field.
```
```
hits.hits.count numeric 6868
The amount of times that value appeared in the
entries that matched the query parameters.
```
```
hits.hits.start numeric 2707 A system field.
```
```
hits.hits.trend numeric 41.61 The increase or decrease of that value’s
occurrence over the time window specified.
```
```
hits.count numeric 10000 The total number of entries analyzed.
```
```
darktraceChildError string FactoryProbe_1
The name of a probe which did not respond to
the request.
```
```
kibana object Details about the advanced search logs.
```
```
kibana.index array
```
```
logstash-
darktrace-2020.03.0
2
```
```
A system field.
```
```
kibana.per_page numeric 50
```
```
The number of results returned in the page. If the
size value is changed, will continue to return a
value of 50.
```
```
kibana.time object The time window specified in the request.
```
```
kibana.time.from string
2020-03-02T00:00:00
.000Z
```
```
The start of the time window specified in the
request.
```
```
kibana.time.to string
2020-03-02T23:59:59
.000Z
```
```
The end of the time window specified in the
request.
```

###### Example Response

```
{
"took": 0,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 26,
"max_score": null,
"hits": [
{
"id": "SearchAlert",
"count": 3,
"start": 3,
"trend": 0
},
...
],
"count": 26
},
"kibana": {
"index": [
"logstash-darktrace-2020.04.17"
],
"per_page": 50,
"time": {
"from": "2020-04-17T17:24:50.759Z",
"to": "2020-04-17T18:24:50.759Z"
}
}
}
```
_Response is abbreviated._


#### Response Schema - /score

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
took numeric 25 The time the request took in milliseconds.
```
```
timed_out boolean FALSE Whether the response timed out.
```
```
_shards object A system field.
```
```
_shards.total numeric 2 A system field.
```
```
_shards.successful numeric 2 A system field.
```
```
_shards.skipped numeric 0 A system field.
```
```
_shards.failed numeric 0 A system field.
```
```
hits object An object encapsulating the advanced search
entries that matched the request.
```
```
hits.total numeric 52
The total number of entries that matched the
query.
```
```
hits.max_score NoneTypenull A system field.
```
```
hits.hits array An array of advanced search entries.
```
```
hits.hits.id string
benjamin.ash@holdin
gsinc.com
For the field specified in the request, the value.
```
```
hits.hits.count numeric 19
The frequency that that value appeared within
the entries that matched the parameters.
```
```
hits.count numeric 52
The total number of entries that matched the
query.
```
```
darktraceChildError string FactoryProbe_1
The name of a probe which did not respond to
the request.
```
```
kibana object Details about the advanced search logs.
```
```
kibana.index array
```
```
logstash-
darktrace-2020.03.2
3
```
```
A system field.
```
```
kibana.per_page numeric 50
```
```
The number of results returned in the page. If the
size value is changed, will continue to return a
value of 50.
```
```
kibana.time object The time window specified in the request.
```
```
kibana.time.from string
2020-03-16T16:33:00
.615Z
```
```
The start of the time window specified in the
request.
```
```
kibana.time.to string
2020-03-23T16:33:00
.615Z
```
```
The end of the time window specified in the
request.
```

###### Example Response

```
"took": 0,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 26,
"max_score": null,
"hits": [
{
"id": "Saas::Misc",
"count": 23
},
{
"id": "Saas::Login",
"count": 3
}
],
"count": 26
},
"kibana": {
"index": [
"logstash-darktrace-2020.04.17"
],
"per_page": 50,
"time": {
"from": "2020-04-17T17:26:24.603Z",
"to": "2020-04-17T18:26:24.603Z"
}
}
}
```

## /ADVANCEDSEARCH/API/GRAPH

The /advancedsearch endpoint allows Advanced Search data to be queried and exported in JSON format from the

Darktrace instance programmatically. Advanced Search queries are Base64 encoded strings, composed of the query

search terms.

The graph extension returns data to create a timeseries graph of results, it can produce a count or mean graph. It

requires a Base64 encoded query string as created in _/advancedsearch/api/search_ as part of the request. When making a

request to mean, a field must also be supplied to aggregate upon.

A request to the graph extension requires a graph interval. The graph interval is the time window that results will be

grouped into for each ‘bar’ of the graph. It takes a value in milliseconds (seconds * 1000). The larger the value, the faster the

query will be returned. Queries over a large timeframe with a low graph interval value will use significant resources and are

strongly discouraged. At a minimum, the following values should be used:

```
QUERY TIMEFRAME MINIMUM GRAPH INTERVAL
```
```
15m 10000 (10s)
```
```
60m 30000 (30s)
```
```
4h 60000 (1m)
```
```
12h 300000 (10m)
```
```
24h 300000 (10m)
```
```
48h 1800000 (30m)
```
```
7d 3600000 (1h)
```
###### Correction

A previous version of this content incorrectly stated that data for the entire timeframe is returned by default. In actuality,

data is returned in 24 hour blocks, split at 00:00.

Please refer to the note on pagination below for information on how to request additional 24hr blocks.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
from string Start time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
to string End time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
interval numeric A time interval in seconds from the current time over which to return results.
```
```
size numeric The number of results to return, default is 50 if unspecified. Maximum is 10,000
```
```
search string Optional Advanced Search search query to make. Ensure all double quotes are escaped.
```
```
analyze_field string The field to return aggregate stats for. Only used when making queries to the /graph/mean extension
```

###### Notes

- Double quotes used in the search string must be escaped with a backslash before encoding. For example,
    "search":" @type:\"ssl\" AND @fields.dest_port:\"443\"".
- The query timeframe can either take a starttime/endtime or to/from value, or a timeframe interval of
    seconds since the current time.

```
◦ If starttime/endtime or to/from is used, the timeframe value must be set to "custom". Time
parameters must always be specified in pairs.
```
```
◦ If using interval, the time: {} object can be omitted from the query. It is important to note that
the query response will not be the same every time as the interval time value is relative.
```
- Data is returned in 24hr blocks, split at 00:00 - queries which stretch across midnight must be paginated to
    return additional days.

```
Pagination takes the form of an incremented, numeric extension (e.g. /1). Each increment goes further back in
time by 24hrs. The "next": 1 value in the response indicates if there are further pages.
```
- The analyze_field parameter is required when making queries to the mean extension. It must be provided
    in the Base64 encoded string.
- The graphmode parameter appears in Advanced Search queries made in the Threat Visualizer. When
    accessing Advanced Search programmatically, the type of data returned is controlled by the extension used -
       /advancedsearch/graph/count or /advancedsearch/graph/mean - rather than the graphmode field.
- The parameter "mode": appears in Advanced Search queries made in the Threat Visualizer. It is not required
    when accessing Advanced Search programmatically.
- The empty fields array is required but the values contained within it do not change the API response.


###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET the number of SSH connections (in half-hour segments) between 192.168.120.39 and 10.0.56.12 in the last
    48 hours:

```
https://[instance]/advancedsearch/api/graph/count/1800000/
eyJzZWFyY2giOiJAdHlwZTpzc2ggQU5EICgoQGZpZWxkcy5kZXN0X2lwOlwiMTAuMC41Ni4xMlwiIEFORCBAZmll
bGRzLnNvdXJjZV9pcDpcIjE5Mi4xNjguMTIwLjM5XCIpIE9SIChAZmllbGRzLnNvdXJjZV9pcDpcIjEwLjAuNTYu
MTJcIiBBTkQgQGZpZWxkcy5kZXN0X2lwOlwiMTkyLjE2OC4xMjAuMzlcIikpIiwiZmllbGRzIjpbXSwib2Zmc2V0
IjowLCJ0aW1lZnJhbWUiOiIxNzI4MDAiLCJ0aW1lIjp7InVzZXJfaW50ZXJ2YWwiOjB9fQ==
```
```
Where the string
```
```
{"search":"@type:ssh AND ((@fields.dest_ip:\"10.0.56.12\" AND @fields.source_ip:
\"192.168.120.39\") OR (@fields.source_ip:\"10.0.56.12\" AND @fields.dest_ip:
\"192.168.120.39\"))","fields":[],"offset":0,"timeframe":"172800","time":
{"user_interval":0}}
```
```
has been Base64 encoded to
```
```
eyJzZWFyY2giOiJAdHlwZTpzc2ggQU5EICgoQGZpZWxkcy5kZXN0X2lwOlwiMTAuMC41Ni4xMlwiIEFORCBAZmll
bGRzLnNvdXJjZV9pcDpcIjE5Mi4xNjguMTIwLjM5XCIpIE9SIChAZmllbGRzLnNvdXJjZV9pcDpcIjEwLjAuNTYu
MTJcIiBBTkQgQGZpZWxkcy5kZXN0X2lwOlwiMTkyLjE2OC4xMjAuMzlcIikpIiwiZmllbGRzIjpbXSwib2Zmc2V0
IjowLCJ0aW1lZnJhbWUiOiIxNzI4MDAiLCJ0aW1lIjp7InVzZXJfaW50ZXJ2YWwiOjB9fQ==
```
2. GET the average data transfer (volume of bytes) transferred from 192.168.120.39 to 10.0.56.12 on 2nd February
    2020:

```
https://[instance]/advancedsearch/api/graph/mean/30000/
eyJzZWFyY2giOiIgQGZpZWxkcy5kZXN0X2lwOlwiMTAuMC41Ni4xMlwiIEFORCBAZmllbGRzLnNvdXJjZV9pcDpc
IjE5Mi4xNjguMTIwLjM5XCIgQU5EIEB0eXBlOlwiY29ublwiIiwiZmllbGRzIjpbXSwib2Zmc2V0IjowLCJ0aW1l
ZnJhbWUiOiJjdXN0b20iLCJ0aW1lIjp7ImZyb20iOiIyMDIwLTAyLTAyVDAwOjAwOjAwWiIsInRvIjoiMjAyMC0w
Mi0wMlQyMzo1OTo1OVoiLCJ1c2VyX2ludGVydmFsIjowfSwiYW5hbHl6ZV9maWVsZCI6IkBmaWVsZHMub3JpZ19p
cF9ieXRlcyJ9
```
```
Where the string
```
```
{"search":" @fields.dest_ip:\"10.0.56.12\" AND @fields.source_ip:\"192.168.120.39\" AND
@type:\"conn\"","fields":[],"offset":0,"timeframe":"custom","time":
{"from":"2020-02-02T00:00:00Z","to":"2020-02-02T23:59:59Z","user_interval":
0},"analyze_field":"@fields.orig_ip_bytes"}
```
```
has been Base64 encoded to
```
```
eyJzZWFyY2giOiIgQGZpZWxkcy5kZXN0X2lwOlwiMTAuMC41Ni4xMlwiIEFORCBAZmllbGRzLnNvdXJjZV9pcDpc
IjE5Mi4xNjguMTIwLjM5XCIgQU5EIEB0eXBlOlwiY29ublwiIiwiZmllbGRzIjpbXSwib2Zmc2V0IjowLCJ0aW1l
ZnJhbWUiOiJjdXN0b20iLCJ0aW1lIjp7ImZyb20iOiIyMDIwLTAyLTAyVDAwOjAwOjAwWiIsInRvIjoiMjAyMC0w
Mi0wMlQyMzo1OTo1OVoiLCJ1c2VyX2ludGVydmFsIjowfSwiYW5hbHl6ZV9maWVsZCI6IkBmaWVsZHMub3JpZ19p
cF9ieXRlcyJ9
```

###### Example Response

_Request:_

```
/advancedsearch/api/graph/count/10000/
eyJzZWFyY2giOiJAdHlwZTpjb25uIEFORCBAZmllbGRzLnByb3RvOnRjcCBBTkQgTk9UIEBmaWVsZHMuY29ubl9zdGF0ZT
pcIlMwXCIgQU5EIE5PVCBAZmllbGRzLmNvbm5fc3RhdGU6XCJSRUpcIiBBTkQgKEBmaWVsZHMub3JpZ19wa3RzOjAgT1Ig
QGZpZWxkcy5yZXNwX3BrdHM6MCkgQU5EIChAZmllbGRzLmRlc3RfcG9ydDpcIjQ0M1wiIE9SIEBmaWVsZHMuZGVzdF9wb3
J0OlwiODBcIikiLCJmaWVsZHMiOltdLCJvZmZzZXQiOjAsInRpbWVmcmFtZSI6IjQzMjAwIiwidGltZSI6eyJ1c2VyX2lu
dGVydmFsIjowfX0=
```
```
{
"took": 1,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 217,
"max_score": 0,
"hits": []
},
"aggregations": {
"count": {
"buckets": [
{
"key": 1582536600000,
"doc_count": 17
}
...
]
}
},
"darktraceChildError": "",
"kibana": {
"index": [
"logstash-darktrace-2020.02.24",
"logstash-darktrace-2020.02.23",
"logstash-darktrace-2020.02.22"
],
"per_page": 50,
"next": 1
}
```
_Response is abbreviated._


## /ADVANCEDSEARCH/API/GRAPH RESPONSE

## SCHEMA

###### Response Schema - /graph/mean

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
took numeric 8 The time the request took in milliseconds.
```
```
timed_out boolean FALSE Whether the response timed out.
```
```
_shards object A system field.
```
```
_shards.total numeric 2 A system field.
```
_shards.successful numeric (^2) A system field.
_shards.skipped numeric 0 A system field.
_shards.failed numeric 0 A system field.
hits object An object encapsulating the advanced search
entries that matched the request.
hits.total numeric 20573
The total number of entries that matched the
query.
hits.max_score numeric (^0) A system field.
hits.hits array An array of advanced search entries.
aggregations object
Aggregated values to use in graphical
operations.
aggregations.mean object
An object containing time series data for a mean
graph.
aggregations.mean.buckets array
An array of grouped data which can be
represented as time series data.
aggregations.mean.buckets.key_as_strin
g
string
2020-03-02T00:00:00
.000Z
The timestamp for the grouped data interval in
readable format.
aggregations.mean.buckets.key numeric 1586937600000
The timestamp for the grouped data interval in
epoch time.
aggregations.mean.buckets.doc_count numeric 131
The number of results contained within the
grouped interval.
aggregations.mean.buckets.mean_stats object
An object describing statistical analysis on the
results within that interval.
aggregations.mean.buckets.mean_stats.c
ount
numeric 131
The number of results contained within the
grouped interval.
aggregations.mean.buckets.mean_stats.m
in
numeric 0
For the field specified when making the request,
the minimum value observed within the interval.
aggregations.mean.buckets.mean_stats.m
ax
numeric 2448
For the field specified when making the request,
the maximum value observed within the interval.
aggregations.mean.buckets.mean_stats.a
vg
numeric 219.6946565
For the field specified when making the request,
the average value observed within the interval.
aggregations.mean.buckets.mean_stats.s
um
numeric 28780
For the field specified when making the request,
the sum of all values observed within the interval.


```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
darktraceChildError string FactoryProbe_1
The name of a probe which did not respond to
the request.
```
```
kibana object Details about the advanced search logs.
```
```
kibana.index array
```
```
logstash-
darktrace-2020.03.0
2
```
```
A system field.
```
```
kibana.per_page numeric 50
```
```
The number of results returned in the page. If the
size value is changed, will continue to return a
value of 50.
```
###### Example Response

```
{
"took": 0,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 22,
"max_score": 0,
"hits": []
},
"aggregations": {
"mean": {
"buckets": [
{
"key_as_string": "2020-04-17T18:02:30.000Z",
"key": 1587146550000,
"doc_count": 1,
"mean_stats": {
"count": 1,
"min": 144,
"max": 144,
"avg": 144,
"sum": 144
}
},
...
]
}
},
"kibana": {
"index": [
"logstash-darktrace-2020.04.17"
],
"per_page": 50
}
}
```
_Response is abbreviated._


#### Response Schema - /graph/count

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
took numeric 2 The time the request took in milliseconds.
```
```
timed_out boolean FALSE Whether the response timed out.
```
```
_shards object A system field.
```
```
_shards.total numeric 2 A system field.
```
```
_shards.successful numeric 2 A system field.
```
```
_shards.skipped numeric 0 A system field.
```
```
_shards.failed numeric 0 A system field.
```
```
hits object An object encapsulating the advanced search
entries that matched the request.
```
```
hits.total numeric 8921
The total number of entries that matched the
query.
```
hits.max_score numeric (^0) A system field.
hits.hits array An array of advanced search entries.
aggregations object
Aggregated values to use in graphical
operations.
aggregations.count object
An object containing time series data for a count
graph.
aggregations.count.buckets array
An array of grouped data which can be
represented as time series data.
aggregations.count.buckets.key numeric 1586937600000
The timestamp for the grouped data interval in
epoch time.
aggregations.count.buckets.doc_count numeric 39
The number of results contained within the
grouped interval.
darktraceChildError string FactoryProbe_1
The name of a probe which did not respond to
the request.
kibana object Details about the advanced search logs.
kibana.index array
logstash-
darktrace-2020.03.2
3
A system field.
kibana.per_page numeric 50
The number of results returned in the page. If the
size value is changed, will continue to return a
value of 50.


###### Example Response

```
{
"took": 1,
"timed_out": false,
"_shards": {
"total": 2,
"successful": 2,
"skipped": 0,
"failed": 0
},
"hits": {
"total": 217,
"max_score": 0,
"hits": []
},
"aggregations": {
"count": {
"buckets": [
{
"key": 1582536600000,
"doc_count": 17
}
...
]
}
},
"darktraceChildError": "",
"kibana": {
"index": [
"logstash-darktrace-2020.02.24",
"logstash-darktrace-2020.02.23",
"logstash-darktrace-2020.02.22"
],
"per_page": 50,
"next": 1
}
```
_Response is abbreviated._


## /AGEMAIL/API/EP/API/V1.0/*

#### Darktrace/Email API

From April 2023, Darktrace/Email now offers a selection of API endpoints. These endpoints are located at

```
https://[instance]/agemail/api/ep/api/v1.0/* ¹. Endpoints are accessed through the standard Darktrace Threat
```
Visualizer API token workflow with the relevant Darktrace/Email permissions.

The Darktrace/Email API offers Open API compliant API documentation, available at

```
https://[instance]/agemail/api/api-docs. For full example queries, parameters, responses and schemas, please
```
refer to this resource.

¹ [instance] may be replaced with the instance IP or FQDN - for example, https://10.0.0.1 or

```
https://euw1-1234-01.cloud.darktrace.com
```
###### Endpoints

The list of available API endpoints at the time of writing is provided here for reference, but this is subject to change.

```
TYPE REQUEST TYPE(S) ENDPOINT
```
```
v1.0 GET /v1.0/admin/decode_link
```
```
v1.0 GET /v1.0/dash/action_summary
```
```
v1.0 GET /v1.0/dash/dash_stats
```
```
v1.0 GET /v1.0/dash/data_loss
```
```
v1.0 GET /v1.0/dash/user_anomaly
```
```
v1.0 POST /v1.0/emails/{uuid}/action
```
```
v1.0 GET /v1.0/emails/{uuid}
```
```
v1.0 GET /v1.0/emails/{uuid}/download
```
```
v1.0 POST /v1.0/emails/search
```
```
v1.0 GET /v1.0/resources/tags
```
```
v1.0 GET /v1.0/resources/actions
```
```
v1.0 GET /v1.0/resources/filters
```
```
v1.0 GET /v1.0/system/audit/eventTypes
```
```
v1.0 GET /v1.0/system/audit/events
```
###### Example Usage

```
https://[instance]/agemail/api/ep/api/v1.0/dash/user_anomaly?limit=2&days=28
```

###### Example Response

```
{
"sofia.martinez@holdingsinc.com": {
"n_emails": 21,
"total_emails": 1106,
"n_last_period": 71,
"n_last_week": 71,
"percentage": 29,
"n_links": 0,
"n_attachments": 0
},
"grayson.stone@holdingsinc.com": {
"n_emails": 1,
"total_emails": 32,
"n_last_period": 0,
"n_last_week": 0,
"percentage": 0,
"n_links": 0,
"n_attachments": 0
}
}
```

## /AIANALYST/INCIDENTEVENTS

The /aianalyst/incidentevents endpoint provides access to AI Analyst events - a group of anomalies or network

activity investigated by Cyber AI Analyst.

The Darktrace Cyber AI Analyst investigates, analyzes and reports upon threats seen within your Darktrace environment; as

a starting point, it reviews and investigates all model breaches that occur on the system. If anomalies or patterns of activity

are identified during this analysis process, an event is created.

Darktrace Threat Visualizer 5.2 introduces a significant development in the way AI Analyst incidents are constructed. New,

‘open’ incidents are created by a meta-analysis of the devices, endpoints and activity involved in each event. Events with

linking factors are then joined together persistently to create incidents encompassing a much wider scope of time and

activity.

AI Analyst incidents in the Threat Visualizer UI are comprised of one or more events, where an event is a tab within each

incident. The /aianalyst/incidentevents endpoint returned detailed information about each of these events.

###### Constructing Incidents from Incident Events

To build incidents from incident events, the simplest method is to use the /aianalyst/groups endpoint to retrieve a

mapping of incident events to incidents, then retrieving further details about those events from this endpoint

(/aianalyst/incidentevents).

Incident events retrieved from /aianalyst/incidentevents do still contain mapping information that allow incidents to

be reconstructed:

- The field currentGroup contains the groupid that corresponds to the overall incident.
- The field groupPreviousGroups contains the previous groupids of incidents the event was part of, if the
    incident was subsequently merged into another.

```
Please refer to “Incidents within Incidents” in /aianalyst/groups for more information on merged incidents.
```
###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
includeacknowledged boolean Include acknowledged events in the data.
```
```
includeallpinned boolean
True by default. Controls whether pinned events are returned alongside those from the
timeframe specified.
```
```
includeonlypinned boolean False by default. Used to only return pinned incident events.
```
```
includeincidenteventurl boolean
Controls whether links to events are included in the response - requires the FQDN value to be
set and valid for the queried instance.
```
```
locale string
```
```
The language for returned strings. Currently supported are de_DE (German), en_GB
(English UK), en_US (English US), es_ES (Spanish ES), es_419 (Spanish LATAM), fr_FR
(French), it_IT (Italian), ja_JP (Japanese), ko_KR (Korean) , pt_BR (Portuguese BR),
zh_Hans (Chinese (Simplified)), zh_Hant (Chinese (Traditional))
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
groupcompliance boolean
```

```
PARAMETER TYPE DESCRIPTION
```
```
Return only events that are part of incidents which have the “compliance” behavior category.
Multiple category parameters can be specified.
```
```
groupsuspicious boolean
Return only events that are part of incidents which have the “suspicious” behavior category.
Multiple category parameters can be specified.
```
```
groupcritical boolean
Return only events that are part of incidents which have the “critical” behavior category.
Multiple category parameters can be specified.
```
```
maxscore numeric
```
```
The maximum score an event can possess and still be returned. Accepts values between 0
and 100.
```
```
minscore numeric
```
```
The minimum score an event can possess and still be returned. Accepts values between 0
and 100.
```
```
maxgroupscore numeric
Restrict returned events by the maximum incident score for the incident it is associated with.
Accepts values between 0 and 100.
```
```
mingroupscore numeric
Restrict returned events by the minimum incident score for the incident it is associated with.
Accepts values between 0 and 100.
```
```
did numeric
Identification number of a device modeled in the Darktrace system to include incident events
for.
```
```
excludedid numeric
Identification number of a device modeled in the Darktrace system to remove incident events
for.
```
```
sid numeric
```
```
Identification number of a subnet modeled in the Darktrace system to include incident events
for.
```
```
excludesid numeric
```
```
Identification number of a subnet modeled in the Darktrace system to remove incident events
for.
```
```
master numeric
```
```
Identification number of a master instance under a Unified View to include incident events for.
Only relevant in Unified View environments.
```
```
saasonly boolean Restricts returned events to only those that contain SaaS activity.
```
```
groupid string
```
```
A unique identifier of an AI Analyst incident. If specified, overrides all other filter parameters
specified (exception uuid, which takes priority) and only returns events associated with the
specified incidents.
```
```
uuid string
A unique identified of an AI Analyst incident event. If specified, overrides all other filter
parameters specified and only returns the chosen events.
```
###### Notes

- A time window for the returned events can be specified using starttime/endtime and unix time in
    milliseconds.

```
◦ Where only endtime is set,starttime will default to 1 week before endtime. Where only
starttime is set, endtime will default to the current time.
```
```
◦ If no time parameters are specified, events from the last seven days (and pinned events, if applicable)
will be returned.
```
- Events that are pinned or part of pinned incidents will always be returned, regardless of the time period
    specified. This can be prevented with includeallpinned=false

```
The includeonlypinned parameter can be used to only return events that have been pinned.
```
- Where locale is not specified or not supported in the current software version, strings will default to en_GB.

```
◦ Where the specified locale uses non-ascii characters, these will be returned in unicode format and
must be parsed.
```

- The uuid of an event can be found in the id field of the JSON response.
- For scoring parameters minscore and maxscore, note that incident scores may change (increase) over time
    as new events are added with more severe behavior.
- The parameter uuid takes priority over all filters. The parameter groupid takes priority over all filters _other_
    _than_ uuid.

```
◦ A uuid value can be found in the field id, or in the field uuid in the incidentEvents array of an
incident event retrieved from the /aianalyst/groups endpoint.
```
```
◦ A groupid value can be found in the field currentGroup, or in the id field of an incident event
retrieved from the /aianalyst/groups endpoint.
```
- As of Darktrace 6.1, incident events may contain a sender value, indicating the event activity is sourced from
    Darktrace/Email. For these events, the breachDevices array will be returned empty.

_Please see the response schema for a full breakdown of the_ details _array._

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET details of the AI Analyst event uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633:

```
https://[instance]/aianalyst/incidentevents?uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633
```
2. GET details of all AI Analyst events for the incident groupid=g04a3f36e-4u8w-v9dh-x6lb-894778cf9633 in
    French:

```
https://[instance]/aianalyst/incidentevents?groupid=g04a3f36e-4u8w-v9dh-
x6lb-894778cf9633&locale=fr_FR
```
3. GET all AI Analyst events for the device with did=100 - including acknowledged events - for the 7 day period
    from 1st to 7th March 2022:

```
https://[instance]/aianalyst/incidents?
starttime=1646092800000&endtime=1646611200000&includeacknowledged=true&did=100&includeal
lpinned=false
```
4. GET AI Analyst events for SaaS activity that are part of critical incidents with a score >90 in the last 7 days:

```
https://[instance]/aianalyst/incidentevents?
mingroupscore=90&groupcritical=true&saasonly=true
```

###### Example Response

_Request: /aianalyst/incidentevents?uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633&locale=en_US_

```
[
{
"summariser": "AdminConnSummary",
"mitreTactics": [
"lateral-movement"
],
"acknowledged": false,
"pinned": true,
"createdAt": 1628002089240,
"attackPhases": [
5
],
"title": "Extensive Unusual SSH Connections",
"id": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"children": [
"04a3f36e-4u8w-v9dh-x6lb-894778cf9633"
],
"category": "critical",
"currentGroup": "g04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"groupCategory": "critical",
"groupScore": "72.9174234",
"groupPreviousGroups": null,
"activityId": "da39a3ee",
"groupingIds": [
"268d2b8c"
],
"groupByActivity": false,
"userTriggered": false,
"externalTriggered": false,
"aiaScore": 98,
"summary": "The device 10.1.2.3 was observed making unusual internal SSH connections to
a wide range of devices...",
"periods": [
{
"start": 1627985298683,
"end": 1628000141220
}
],
"breachDevices": [
{
"identifier": null,
"hostname": null,
"ip": "10.1.2.3",
"mac": null,
"subnet": "VPN",
"did": 10,
"sid": 12
}
],
"relatedBreaches": [
{
"modelName": "Unusual Activity / Unusual Activity from Re-Activated Device",
"pbid": 1234,
"threatScore": 37,
"timestamp": 1627997157000
}
],
"details": [
[
{
"header": "Breaching Device",
"contents": [
```
_continued..._


```
{
"key": null,
"type": "device",
"values": [
{
"identifier": null,
"hostname": null,
"ip": "10.1.2.3",
"mac": null,
"subnet": "VPN",
"did": 10,
"sid": 12
}
]
}
]
}
],
[
{
"header": "SSH Activity",
"contents": [
{
"key": "Time",
"type": "timestampRange",
"values": [
{
"start": 1627985298683,
"end": 1628000141220
}
]
},
...
] } ] ] } ]
```
_Response is abbreviated._


## /AIANALYST/INCIDENTEVENTS RESPONSE SCHEMA

#### /incidents and /incidentevents

Prior to v5.2, incident events were retrieved from /aianalyst/incidents and constructed around devices or activity

using the fields activityID, groupingID and groupByActivity. From v5.2, a new methodology is used to construct

AI Analyst incidents, utilizing linking factors to create persistent incident groupings. v5.2 incident events are constructed

using currentGroup and groupPreviousGroups and can be requested from /aianalyst/incidentevents.

Additional fields are also added (groupScore, category, groupCategory) which are only relevant to incidents

constructed using the v5.2 method.

_Incident events created prior to v5.2 will not contain values for_ currentGroup _and_ groupPreviousGroups_._

For more information on how to construct AI Analyst incidents from API responses, please see _/aianalyst/groups_ and

_/aianalyst/incidentevents_.

###### Understanding the details array

The details array and sub-arrays contain all contextual information and analysis output regarding the event. The outer array

groups sections of information together which are related, and the inner array groups together subsections that make up

that section. Each subsection has a header and one or more objects (in the contents array) containing relevant information

- subsections are interrelated and should not be moved outside their parent section.

For example, an event concerns a suspicious SaaS activity. The details array contains two sub-arrays (sections), the first

section concerns the SaaS account itself and contains only one subsection, the second section concerns the activity itself

and contains three subsections. This would be structured as follows:

```
"details": [
[ // Section 1
{
"header": "SaaS User Details", // Subsection 1.1
"contents": [ // Information relevant to Subsection 1.1
...
]
}
], // End of Section 1
[ // Section 2
{
"header": "Agent Carrying out Suspicious Activity", // Subsection 2.1
"contents": [ // Information relevant to Subsection 2.1
...
]
},
{
"header": "Summary of Activity", // Subsection 2.2
"contents": [ // Information relevant to Subsection 2.2
...
]
},
{
"header": "Activity Details", // Subsection 2.3
"contents": [ // Information relevant to Subsection 2.3
...
]
}
]
], // End of Section 2
```
It is important to preserve the sectioning of information as it directly relates to one another, particularly where multiple

actors or connections appear within the event. For example, if an event contained two connections - one with data transfer


and one without - it is essential that the subsection concerning the data that was transferred stays with the information

about the connection it was transferred over.

###### The summariser / summarizer Field

The Darktrace AI Analyst operates a hypothesis- based analysis approach, where activity is evaluated against a number of

possible, relevant hypotheses and a determination is taken of which (if any) hold based upon the evidence gathered and

investigations performed. These hypotheses are represented by “summarizers” – grouped investigative steps, analysis

approaches, or classifiers – which each try to locate activity or indicators relevant to their field of investigation.

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
summariser string AdminConnSummary
```
```
In this case, the system name for the summarizer
which identified the activity AI Analyst chose to
surface to the end user. See above for more
details.
```
```
mitreTactics array lateral-movement
An array of MITRE ATT&CK Framework tactics
that have been mapped to this event.
```
```
acknowledged boolean FALSE Whether the event has been acknowledged.
```
```
pinned boolean TRUE
```
```
Whether the event, or an incident that the event
is associated with, is pinned within the Threat
Visualizer user interface. Pinned events will
always return regardless of the timeframe
specified.
```
createdAt numeric (^1702392635000) Timestamp for event creation in epoch time.
attackPhases array 5
Of the six attack phases, which phases are
applicable to the activity.
title string
Extensive Unusual
SSH Connections A title describing the activity that occurred.
id string
04a3f36e-4u8w-v9dh-
x6lb-894778cf9633
A unique identifier that can be used to request
this AI Analyst event.
children array
04a3f36e-4u8w-v9dh-
x6lb-894778cf9633
A unique identifier that can be used to request
this AI Analyst event. This array will only contain
one entry as of v5.2 and above.
category string critical
The behavior category associated with the
incident event. Relevant for v5.2+ incident
construction only.
currentGroup string
g04a3f36e-4u8w-
v9dh-
x6lb-894778cf9633
The UUID of the current incident this event
belongs to. Used for v5.2+ incident construction.
groupCategory string critical
The behavior category associated with the
incident overall. Relevant for v5.2+ incident
construction only.
groupScore numeric 72.9174234
The current overall score of the incident this
event is part of. Relevant for v5.2+ incident
construction only.
groupPreviousGroups NoneTypenull
If the incident event was part of an incident which
was later merged with another, the UUIDs of the
incidents before they were merged. Used for
v5.2+ incident construction.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

activityId string da39a3ee

```
Used by pre-v5.2 legacy incident construction.
An identifier for the specific activity detected by
AI Analyst. If groupByActivity=true, this
field should be used to group events together
into an incident.
```
groupingIds array 268d2b8c

```
Used by pre-v5.2 legacy incident construction.
Each entry in the groupingIDs array refers to
a device that triggered the activity detection. In
single events, should only contain one ID. If
groupByActivity=false, this field should be
used to group events together into an incident.
```
groupByActivity boolean FALSE

```
Used by pre-v5.2 legacy incident construction.
Indicates whether the event should be
aggregated by activity or by device to create an
incident. When true, the event should be
aggregated by activityID, and when false,
aggregated by groupingID(s).
```
userTriggered boolean FALSE
Whether the event was created as a result of a
user-triggered AI Analyst investigation.

externalTriggered boolean FALSE
Whether the event was created as a result of an
externally triggered AI Analyst investigation.

aiaScore numeric 98
The anomalousness of the event as classified by
AI Analyst - out of 100.

summary string

```
The device 10.1.2.3
was observed making
unusual internal
SSH
connections to a
wide range of
devices...
```
```
A textual summary of the suspicious activity.
```
periods array

```
An array of one or more periods of time where
anomalous activity occurred that AI Analyst
investigated.
```
periods.start numeric 1702392635000 A timestamp for the start of the activity period in
epoch time.

periods.end numeric 1702392719930
A timestamp for the end of the activity period in
epoch time.

sender string example@example.com

```
If the incident event is created from Darktrace/
Email activity, this field will be populated with an
email address representing the sender of the
anomalous email or email campaign
investigated. Otherwise, null.
```
breachDevices array

```
An array of devices involved in the related model
breach(es). For incident events created from
Darktrace/Email activity, this array is empty.
```
breachDevices.identifier string
ws192.holdingsinc.c
om

```
An identifier for the device used when
constructing summaries or reports. May be the
device label, hostname or IP, depending on
availability.
```
breachDevices.hostname string
ws192.holdingsinc.c
om

```
The hostname associated with the device, if
available.
```
breachDevices.ip string 10.1.2.3 The IP associated with the device.

breachDevices.mac string The MAC address associated with the device.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

breachDevices.subnet string VPN
The subnet label for the corresponding subnet, if
available.

breachDevices.did numeric 10

```
The unique “device id” identifier for the device
that triggered the breach. This field is used to
group events into device-based incidents within
the Threat Visualizer.
```
breachDevices.sid numeric 12
The subnet id for the subnet the device is
currently located in.

relatedBreaches array
An array of model breaches related to the activity
investigated by AI analyst.

relatedBreaches.modelName string

```
Unusual Activity /
Unusual Activity
from Re-Activated
Device
```
```
The name of the model that breached.
```
relatedBreaches.pbid numeric 1234
The “policy breach ID” unique identifier of the
model breach.

relatedBreaches.threatScore numeric 37 The breach score of the associated model
breach - out of 100.

relatedBreaches.timestamp numeric 1628002089240
The timestamp at which the model breach
occurred in epoch time.

details array

```
An array of multiple sections (sub-arrays) of
event information. Please see Understanding the
details array” above. ”
```
details.header string First Hop
A short title describing the section of
information.

details.contents array

```
An array of multiple objects describing relevant
information for this subsection, such as involved
devices, relevant external hosts, ports used and
anomaly scorings.
```
details.contents.key device Assigns meaning to the values in the values
field - a short description of the data.

details.contents.type string Source device
The type of information contained within the
object. A full list of examples is available.

details.contents.values array

```
One or more values that relate to the key. For
example, a series of ports or hostnames. Full
examples of all data types are available.
```

###### Example Response

```
[
{
"summariser": "AdminConnSummary",
"mitreTactics": [
"lateral-movement"
],
"acknowledged": false,
"pinned": true,
"createdAt": 1628002089240,
"attackPhases": [
5
],
"title": "Extensive Unusual SSH Connections",
"id": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"children": [
"04a3f36e-4u8w-v9dh-x6lb-894778cf9633"
],
"category": "critical",
"currentGroup": "g04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"groupCategory": "critical",
"groupScore": "72.9174234",
"groupPreviousGroups": null,
"activityId": "da39a3ee",
"groupingIds": [
"268d2b8c"
],
"groupByActivity": false,
"userTriggered": false,
"externalTriggered": false,
"aiaScore": 98,
"summary": "The device 10.1.2.3 was observed making unusual internal SSH connections to
a wide range of devices.\n\nThough this behaviour could be the result of legitimate remote
access or administration, it could also be a sign of attempted lateral movement by a
compromised machine.\n\nConsequently, if this activity was not expected, the security team
may wish to investigate further.",
"periods": [
{
"start": 1627985298683,
"end": 1628000141220
}
],
"sender": null,
"breachDevices": [
{
"identifier": null,
"hostname": null,
"ip": "10.1.2.3",
"mac": null,
"subnet": "VPN",
"did": 10,
"sid": 12
}
],
"relatedBreaches": [
{
"modelName": "Unusual Activity / Unusual Activity from Re-Activated Device",
"pbid": 1234,
"threatScore": 37,
"timestamp": 1627997157000
}
],
"details": [
[
{
"header": "Breaching Device",
```
_continued..._


```
"contents": [
{
"key": null,
"type": "device",
"values": [
{
"identifier": null,
"hostname": null,
"ip": "10.1.2.3",
"mac": null,
"subnet": "VPN",
"did": 10,
"sid": 12
}
]
}
]
}
],
[
{
"header": "SSH Activity",
"contents": [
{
"key": "Time",
"type": "timestampRange",
"values": [
{
"start": 1627985298683,
"end": 1628000141220
}
]
},
{
"key": "Number of unique IPs",
"type": "integer",
"values": [
16
]
},
{
"key": "Targeted IP ranges include",
"type": "device",
"values": [
{
"identifier": null,
"hostname": null,
"ip": "10.11.12.0/24",
"mac": null,
"subnet": null,
"did": null,
"sid": null
},
{
"identifier": null,
"hostname": null,
"ip": "10.11.13.0/24",
"mac": null,
"subnet": null,
"did": null,
"sid": null
},
{
```
_continued..._


```
"identifier": null,
"hostname": null,
"ip": "10.11.14.0/24",
"mac": null,
"subnet": null,
"did": null,
"sid": null
}
]
},
{
"key": "Destination port",
"type": "integer",
"values": [
22
]
},
{
"key": "Connection count",
"type": "integer",
"values": [
40
]
},
{
"key": "Percentage successful",
"type": "percentage",
"values": [
100
] } ] } ] ] } ]
```
_Response is abbreviated._

#### Response Schema - Cross-Network Event

_Cross-Network events are deprecated as of v5.2_

#### Example details entries

###### "type": "string"

```
{
"type": "string",
"key": "Application protocol",
"values": [
"SSH"
]
}
```

###### "type": "device"

```
{
"type": "device",
"key": "Source device",
"values": [
{
"sid": 12,
"mac": "93:gb:28:g1:fc:g1",
"ip": "10.140.15.33",
"identifier": "Workstation 12",
"did": 57,
"hostname": null,
"subnet": null
}
]
}
```
###### "type": "externalHost"

```
{
"type": "externalHost",
"key": "Endpoint",
"values": [
{
"ip": null,
"hostname": "stackoverflow.com"
}
]
}
```
###### "type": "timestamp"

```
{
"type": "timestamp",
"key": "Hostname first observed",
"values": [
1593646723036
],
},
```
###### "type": "duration"

```
{
"type": "duration",
"key": "Median beacon period",
"values": [
30
]
}
```

###### "type": "integer"

```
{
"type": "integer",
"key": "Destination port",
"values": [
22
]
}
```
###### "type": "float"

```
{
"type": "float",
"key": "Latitude",
"values": [
12.46
]
}
```
###### "type": "percentage"

```
{
"type": "percentage",
"key": "Hostname rarity",
"values": [
100
]
}
```
###### "type": "dataVolume"

```
{
"type": "dataVolume",
"key": "Total data in",
"values": [
142271
]
}
```

###### "type": "ratio"

```
{
"type": "ratio",
"key": "Validation Statuses",
"values": [
{
"percentage": 50
"value": "ok",
},
{
"percentage": 50
"value": "Unknown",
}
]
}
```
###### "type": "timestampRange"

```
{
"type": "timestampRange",
"key": "Time",
"values": [
{
"start": 1579710063121,
"end": 1579711920166
}
]
}
```
###### "type": "integerRange"

```
{
"type": "integerRange",
"key": "Range of connections per hour",
"values": [
{
"start": 1
"end": 6,
}
]
}
```
###### "type": "durationRange"

```
{
"type": "durationRange",
"key": "Range of periods",
"values": [
{
"start": 30
"end": 79,
}
]
}
```

###### "type":

###### "dataVolumeRange"

```
{
"type": "dataVolumeRange",
"key": "Range of data volumes sent per external connection",
"values": [
{
"start": 717
"end": 944,
}
]
}
```
###### "type":

###### "percentageRange"

```
{
"type": "percentageRange",
"key": "Rarity of all endpoints",
"values": [
{
"start": 100
"end": 100,
}
]
}
```
###### "type": "stringRange"

```
{
"type": "stringRange",
"key": "Days of activity",
"values": [
{
"start": "Wednesday"
"end": "Sunday",
}
]
}
```

## /AIANALYST/GROUPS

The Darktrace Cyber AI Analyst investigates, analyzes and reports upon threats seen within your Darktrace environment; as

a starting point, it reviews and investigates all model breaches that occur on the system. If anomalies or patterns of activity

are identified during this analysis process, an event is created.

Darktrace Threat Visualizer 5.2 introduces a significant development in the way AI Analyst incidents are constructed. New,

‘open’ incidents are created by a meta-analysis of the devices, endpoints and activity involved in each event. Events with

linking factors are then joined together persistently to create incidents encompassing a much wider scope of time and

activity.

AI Analyst incidents in the Threat Visualizer UI are comprised of one or more events, where an event is a tab within each

incident. The /aianalyst/groups endpoint returns incidents as groups and lists the events that comprise those groups.

It is useful for understanding the current active incidents in the environment and how data retrieved from the

```
/aianalyst/incidentevents endpoint fits together.
```
#### Incidents within Incidents

Over time, incidents can become merged with one another. This happens when two sets of disparate activity are suddenly

linked by shared factors.

In a simple example, a credential (user1) is seen in event A under incident 1. Incident 2 has an event (event B) for port

scanning and is separate. Both incident 1 and incident 2 are returned as separate entries from the /aianalyst/groups

endpoint.

The device performing port scanning in incident 2 then performs unusual administrative connections and an event is

created (event C). Around the time of those connections, the same credential (user1) is seen in use on the device and is

included in the event. This event links both incident 1 and incident 2 together, and incident 2 is merged into incident 1.

Now, the /aianalyst/groups endpoint returns one incident - incident 1 - with events A, B and C. The id of incident 2

can now be found in the previousIds field to indicate it was merged into incident 1.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
includeacknowledged boolean Include acknowledged incidents in the data. False by default.
```
```
includeallpinned boolean
True by default. Controls whether pinned incidents are returned alongside those from the
timeframe specified.
```
```
includeonlypinned boolean False by default. Used to only return pinned incidents.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
locale string
```
```
The language for returned strings. Currently supported are de_DE (German), en_GB (English UK),
en_US (English US), es_ES (Spanish ES), es_419 (Spanish LATAM), fr_FR (French), it_IT
(Italian), ja_JP (Japanese), ko_KR (Korean) , pt_BR (Portuguese BR), zh_Hans (Chinese
(Simplified)), zh_Hant (Chinese (Traditional))
```
```
includegroupurl boolean
Controls whether links to the incident in the Threat Visualizer are included in the response -
requires the FQDN value to be set and valid for the queried instance. Defaults to false.
```
```
compliance boolean
Return incidents which have the “compliance” behavior category. Multiple category parameters
can be specified.
```

```
PARAMETER TYPE DESCRIPTION
```
```
suspicious boolean
Return only incidents which have the “suspicious” behavior category. Multiple category parameters
can be specified.
```
```
critical boolean
```
```
Return only incidents which have the “critical” behavior category. Multiple category parameters can
be specified.
```
```
did numeric Identification number of a device modeled in the Darktrace system to include incidents for.
```
```
excludedid numeric Identification number of a device modeled in the Darktrace system to remove incidents for.
```
```
sid numeric Identification number of a subnet modeled in the Darktrace system to include incidents for.
```
```
master numeric
```
```
Identification number of a master instance under a Unified View to include incidents for. Only
relevant in Unified View environments.
```
```
excludesid numeric Identification number of a subnet modeled in the Darktrace system to remove incidents for.
```
```
saasonly boolean Restricts returned incidents to only those that contain a minimum of one SaaS incident event.
```
```
maxscore numeric
```
```
The maximum score an incident can possess and still be returned. Replicates the slider filter on the
Threat Tray. Accepts values between 0 and 100.
```
```
minscore numeric
```
```
The minimum score an incident can possess and still be returned. Replicates the slider filter on the
Threat Tray. Accepts values between 0 and 100.
```
```
groupid string
A unique identifier of an AI Analyst incident. If specified, overrides all other filter parameters
specified and only returns the specified incidents.
```
```
uuid string
```
```
A unique identified of an AI Analyst incident event. If specified, overrides all other filter parameters
(exception groupID, which takes priority) specified and only returns incidents containing the
specified ids.
```
###### Notes

- A time window for the returned events can be specified using starttime/endtime and unix time in
    milliseconds.

```
◦ Where only endtime is set,starttime will default to 1 week before endtime. Where only
starttime is set, endtime will default to the current time.
```
```
◦ If no time parameters are specified, events from the last seven days (and pinned events, if applicable)
will be returned.
```
- For sid and did filters:

```
◦ If sid and did are used, a minimum of one event in an incident group must include the specified
device or device in the specified subnet for the incident to be included.
```
```
◦ If excludesid and excludedid are used, no event in an incident group can include the specified
device or devices in the specified subnet for the incident to be included.
```
- Incidents that are pinned or contain pinned events will always be returned, regardless of the time period
    specified. This can be prevented with includeallpinned=false.

```
The includeonlypinned parameter can be used to only return incidents that have been pinned.
```
- Links back to the Threat Visualizer can be included in the response with includegroupurl=true.
- Where locale is not specified or not supported in the current software version, strings will default to en_GB.

```
◦ Where the specified locale uses non-ascii characters, these will be returned in unicode format and
must be parsed.
```

- For scoring parameters minscore and maxscore, note that incident scores may change (increase) over time
    as new events are added with more severe behavior.
- The parameter groupid takes priority over all filters. The parameter uuid takes priority over all filters _other_
    _than_ groupid.

```
◦ A groupid value can be found in the field id, or in the currentGroup field of an incident event
retrieved from the /aianalyst/incidentevents endpoint.
```
```
◦ A uuid value can be found in the field uuid in the incidentEvents array, or in the id field of an
incident event retrieved from the /aianalyst/incidentevents endpoint.
```
- As of Darktrace 6.1, incident events in the incidentEvents array may contain a sender value instead of a
    triggerDid, where the event activity is sourced from Darktrace/Email.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all critical AI Analyst incidents for the 7 day period from 1st to 7th March 2022:

```
https://[instance]/aianalyst/groups?
starttime=1646092800000&endtime=1646611200000&includeallpinned=false&critical=true
```
2. GET details of an AI Analyst incident with groupid=g04a3f36e-4u8w-v9dh-x6lb-894778cf9633 in French:

```
https://[instance]/aianalyst/groups?groupid=g04a3f36e-4u8w-v9dh-
x6lb-894778cf9633&locale=fr_FR
```
3. GET details of suspicious SaaS incidents with a minimum score of 70 in the last 7 days:

```
https://[instance]/aianalyst/groups?suspicious=true&saasonly=true&minscore=70
```

###### Example Response

_Request: /aianalyst/groups?groupid=g04a3f36e-4u8w-v9dh-x6lb-894778cf9633&locale=en_US_

```
[
{
"id": "g04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"active": true,
"acknowledged": false,
"pinned": false,
"userTriggered": false,
"externalTriggered": false,
"previousIds": [
"gc6e8baed-0729-437d-9268-e68d696491c1"
],
"incidentEvents": [
{
"uuid": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"start": 1702392635000,
"title": "Unusual Internal Upload",
"triggerDid": 1044,
"sender": null,
"visible": true,
"acknowledged" : false
},
...
],
"mitreTactics": [
"collection",
"exfiltration",
"lateral-movement"
],
"devices": [
1044,
1155,
...
],
"initialDevices": [
1044
],
"category": "critical",
"groupScore": 99.93292997390672,
"start": 1702392635000,
"end": 1702392719930,
"edges": [
{
"isAction": false,
"source": {
"nodeType": "device",
"value": 13255
},
"target": {
"nodeType": "device",
"value": "1317"
},
"start": null,
"incidentEvent": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"description": Internal Upload,
"details": [
{
"key": null,
"type": "dataVolume",
"values": [
3274396882
]
```
_continued..._


```
}
]
},
...
]
}
]
```
_Response is abbreviated._


## /AIANALYST/GROUPS RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
id string
```
```
g04a3f36e-4u8w-
v9dh-
x6lb-894778cf9633
```
```
A unique id of the incident. Can be used as a
value for the groupid parameter or to link to
the incident in the Threat Visualizer user
interface.
```
```
active boolean TRUE
```
```
acknowledged boolean FALSE Whether the incident has been acknowledged.
```
```
pinned boolean FALSE Whether the incident is pinned.
```
```
userTriggered boolean FALSE
Whether any of the events in the incident were
created due to a user-triggered investigation.
```
```
externalTriggered boolean FALSE
```
```
Whether any of the events in the incident were
created due to an externally-triggered
(telemetry) investigation.
```
```
previousIds array
gc6e8baed-0729-437d
-9268-e68d696491c1
g927442d7-c2f7-4ceb-9fa2-398169bb9bcf
```
```
incidentEvents array
```
```
An array of the events that make up this incident.
More detailed information can be retrieved from
/incidentevents using the uuid values provided
here.
```
```
incidentEvents.uuid string
04a3f36e-4u8w-v9dh-
x6lb-894778cf9633
```
```
A unique id of the incident. Can be used as a
value for the groupid parameter or to link to
the incident in the Threat Visualizer user
interface.
```
```
incidentEvents.start numeric 1702392635000
The start time of the activity covered by the
event.
```
```
incidentEvents.title string
Unusual Internal
Upload The title of the event.
```
```
incidentEvents.triggerDid numeric 1044
```
```
The unique device id of the device that triggered
the AI Analyst investigation that produced the
incident event. If the incident event is created
from Darktrace/Email activity, this field will not be
populated.
```
```
incidentEvents.sender string example@example.com
```
```
If the incident event is created from Darktrace/
Email activity, this field will be populated with an
email address representing the sender of the
anomalous email or email campaign
investigated.
```
```
incidentEvents.visible boolean TRUE A system field.
```
```
incidentEvents.acknowledged boolean TRUE
Whether the specific incident event has been
acknowledged.
```
```
mitreTactics array collection
```
```
An array of MITRE ATT&CK Framework tactics
that have been mapped to events contained
within this incident.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

devices array

```
1044, 1155, 1283,
1317, 1451, 1514,
1620, 1709, 1817,
1906, 2028,
2146
```
```
An array of unique device ids of devices that
triggered the AI Analyst investigations for events
contained within this incident.
```
initialDevices array 1044
The device(s) that initially triggered the first
event under this incident.

category string critical The overall behavior category of the incident.

groupScore float 99.93292997 The overall incident score of the incident.

start numeric 1702392635000
The start time of all activity covered by the
incident events.

end numeric 1702392719930
The end time of all activity covered by the
incident events.

edges array

```
An array describing the links between events
under this incident. This array is intended for use
by the Threat Visualizer system.
```
edges.isAction boolean FALSE A system field.

edges.source object
An object describing the source of a pair of
linking factors.

edges.source.nodeType string device
The type of linking factor that linked the activity
or information together.

edges.source.value numeric 1044
A value that represents the linking factor. Here, a
unique device id.

edges.target object
An object describing the target of a pair of linking
factors.

edges.target.nodeType string internalIp
The type of linking factor that linked the activity
or information together.

edges.target.value string 10.1.1.2
A value that represents the linking factor. Here,
an IP that corresponds to the unique device ID.

edges.start numeric
For time-based linked factors, a start time for the
link.

edges.incidentEvent string

```
04a3f36e-4u8w-v9dh-
x6lb-894778cf9633
The incident event these linking factors relate to.
```
edges.description string Internal Upload If applicable, a description of the linking factor.

edges.details array Additional details about the linking factor, if
applicable.


###### Example Response

```
[
{
"id": "g04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"active": true,
"acknowledged": false,
"pinned": false,
"userTriggered": false,
"externalTriggered": false,
"previousIds": [
"gc6e8baed-0729-437d-9268-e68d696491c1"
],
"incidentEvents": [
{
"uuid": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"start": 1702392635000,
"title": "Unusual Internal Upload",
"triggerDid": 1044,
"sender": null,
"visible": true,
"acknowledged" : false
},
...
],
"mitreTactics": [
"collection",
"exfiltration",
"lateral-movement"
],
"devices": [
1044,
1155,
...
],
"initialDevices": [
1044
],
"category": "critical",
"groupScore": 99.93292997390672,
"start": 1702392635000,
"end": 1702392719930,
"edges": [
{
"isAction": false,
"source": {
"nodeType": "device",
"value": 13255
},
"target": {
"nodeType": "device",
"value": "1317"
},
"start": null,
"incidentEvent": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"description": Internal Upload,
"details": [
{
"key": null,
"type": "dataVolume",
"values": [
3274396882
]
```
_continued..._


}
]
},
...
]
}
]


## /AIANALYST/ACKNOWLEDGE AND /

## UNACKNOWLEDGE

The /acknowledge and /unacknowledge extensions of the /aianalyst endpoint allow for AI Analyst events to be

acknowledged or unacknowledged programmatically, given a uuid value. This can be very useful when integrating

Darktrace with other SOC or ticket-management tools.

```
POST requests to these endpoints must be made with parameters. JSON is not supported.
```
###### Request Type(s)

```
[POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
uuid string A unique identifier for an AI Analyst event. Takes multiple values comma-separated.
```
###### Notes

- A uuid is a unique identifier of an incident event, it can be found in:

```
◦ The id field of an incident retrieved from /aianalyst/incidentevents
```
```
◦ The uuid field inside the incidentEvents array of an incident event retrieved from the
/aianalyst/groups endpoint.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. POST to acknowledge an AI Analyst incident event with uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633:

```
https://[instance]/aianalyst/acknowledge with body uuid=04a3f36e-4u8w-v9dh-
x6lb-894778cf9633
```
2. POST to unacknowledge an AI Analyst event with uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633:

```
https://[instance]/aianalyst/unacknowledge with body uuid=04a3f36e-4u8w-v9dh-
x6lb-894778cf9633
```

## /AIANALYST/PIN AND /UNPIN

The /pin and /unpin extensions of the /aianalyst endpoint allow for AI Analyst events to be pinned or unpinned

programmatically given a uuid value, ensuring they persist and are always returned when queried regardless of the time

period specified.

Pinned events are returned by /aianalyst/incidentevents, /aianalyst/groups and /aianalyst/incidents by

default, unless includeallpinned=false is included with the request.

```
POST requests to these endpoints must be made with parameters. JSON is not supported.
```
###### Request Type(s)

```
[POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
uuid string A unique identifier for an AI Analyst event. Takes multiple values comma-separated.
```
###### Notes

- A uuid is a unique identifier of an incident event, it can be found in:

```
◦ The id field of an incident retrieved from /aianalyst/incidentevents
```
```
◦ The uuid field inside the incidentEvents array of an incident event retrieved from the
/aianalyst/groups endpoint.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. POST to pin an AI Analyst incident event with uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633:

```
https://[instance]/aianalyst/pin with body uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633
```
2. POST to unpin an AI Analyst event with uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633:

```
https://[instance]/aianalyst/unpin with body uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633
```

## /AIANALYST/INCIDENT/COMMENTS

The /aianalyst/incident/comments endpoint returns current comments on an AI Analyst event. It requires the uuid

of an event to be provided.

As of Darktrace Threat Visualizer 6.0.2, it is now possible to POST comments to this endpoint. POST requests to these

endpoints must be made with JSON.

###### Request Type(s)

```
[GET] [POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
incident_id string A unique identifier for the AI Analyst event to return comments for. Only one value is supported at a time.
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
```
message string Text that should be added as a comment to the AI Analyst incident event. For POST requests only.
```
###### Notes

- An incident_id value corresponds to an event uuid, it can be found in:

```
◦ The id field of an incident retrieved from /aianalyst/incidentevents
```
```
◦ The uuid field inside the incidentEvents array of an incident event retrieved from the
/aianalyst/groups endpoint.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET comments for an AI Analyst event with incident_id=04a3f36e-4u8w-v9dh-x6lb-894778cf9633:

```
https://[instance]/aianalyst/incident/comments?incident_id=04a3f36e-4u8w-v9dh-
x6lb-894778cf9633
```
2. POST a comment to the AI Analyst event with incident_id=04a3f36e-4u8w-v9dh-x6lb-894778cf9633:

```
https://[instance]/aianalyst/incident/comments with body {"incident_id":"04a3f36e-4u8w-
v9dh-x6lb-894778cf9633","message":"Test Comment"}
```

###### Example Response

_Request: /aianalyst/incident/comments?incident_id=04a3f36e-4u8w-v9dh-x6lb-894778cf9633_

```
{
"comments": [
{
"username": "smartinez_admin",
"time": 1595501000000,
"incident_id": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"message": "Assigned to Aidan Johnston for investigation."
}
]
}
```

## /AIANALYST/INCIDENT/COMMENTS RESPONSE

## SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
comments array
An array of comments made against the incident
events.
```
```
comments.username string ecarr The user who made the comment.
```
```
comments.time numeric 1595501000000 The time the comment was posted in epoch
time.
```
```
comments.incident_id string
7d0c1dec-593e-4559-
8a71-49847c3e53f5
```
```
The unique identifier of the event against which
the comment was posted.
```
```
comments.message string
```
```
Concerning
behavior.
Investigating
possible
compromise.
```
```
The comment text.
```
###### Example Response

```
{
"comments": [
{
"username": "ecarr",
"time": 1595501000000,
"incident_id": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"message": "Concerning behavior. Investigating possible compromise."
}
]
}
```

## /AIANALYST/STATS

The /stats extension of the /aianalyst endpoint returns metadata on the investigations AI Analyst has performed and

the incidents and incident events resulting from those investigations. This data is used to populate the homepage summary

panel (refer to Understanding the Summary Panel (Customer Portal) for more information).

Darktrace Threat Visualizer 6 introduced a new iteration of the homepage summary which visualizes how vast quantities of

raw events have been distilled by Darktrace analysis, and how these events are relevant to _tactics_ under the MITRE ATT&CK

framework.

- For model breaches and raw events, this data is retrieved from the /summarystatistics endpoint with the
    mitreTactics parameter.
- For AI Analyst, this data is returned in the groupStats.mitreTactics object returned from the
    /aianalyst/stats endpoint.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
###### Notes

- The default time period for this endpoint - if no time parameters are specified - is 7 days.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET statistics about AI Analyst investigations, incidents and incident events for the last 7 days:

```
https://[instance]/aianalyst/stats
```

###### Example Response

_Request: /aianalyst/stats_

```
{
"equivalentHumanTime": 106020000,
"positiveInvestigations": 2,
"negativeInvestigations": 24,
"graphData": {
"breachTime": [
1668689043000,
1668689043000,
...
1668176785000
],
"endTime": [
1668691048000,
1668690970000,
...
1668176856000
],
"equivalentHumanTime": [
4980000,
...
4740000
],
"isPositive": [
true,
...
false
],
"aiaScore": [
0.544,
0.16,
...
null
]
},
"attackPhases": [
{
"phases": [
6
],
"count": 1
},
{
"phases": [
5
],
"count": 1
}
],
"groupStats": {
"total": 2,
"compliance": 0,
"suspicious": 2,
"critical": 0,
"mitreTactics": {
"total": {
"credential-access": 1,
"collection": 1,
"exfiltration": 1
},
"compliance": {},
"suspicious": {
```
_continued..._


```
"credential-access": 1,
"collection": 1,
"exfiltration": 1
},
"critical": {}
}
},
"metadata": {
"estimatedQueries": 0,
"estimatedQueryMs": 0,
"ratioEstimated": 0.0
}
}
```
_Response is abbreviated._


## /AIANALYST/STATS RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
equivalentHumanTime numeric 9684480000
```
```
Based upon the investigations AI Analyst
performed over the time period, the total
estimated equivalent time it would take for a
human analyst to perform the same analysis.
```
```
positiveInvestigations numeric 191
```
```
The number of AI Analyst investigations over the
time period which resulted in the creation of AI
Analyst incident events.
```
```
negativeInvestigations numeric 2583
```
```
The number of AI Analyst investigations over the
time period which did not discover activity
considered suspicious enough to result in the
creation of an AI Analyst incident event.
```
```
graphData object
```
```
An object containing metadata about each
individual AI Analyst investigations across the
time frame.
```
```
graphData.breachTime array 1668686773000 The time of each model breach that triggered
the investigation in epoch time.
```
```
graphData.endTime array 1668688968000
```
```
For each investigation, the time at which AI
Analyst completed its investigation in epoch
time.
```
```
graphData.equivalentHumanTime array 19440000
```
```
The estimated equivalent time it would take for a
human analyst to perform the same analysis as
AI Analyst for each investigation.
```
```
graphData.isPositive array FALSE
Whether each investigation resulted in the
creation of an AI Analyst incident event.
```
```
graphData.aiaScore array 0.74
```
```
The score of the associated AI Analyst incident
event for each event created. If no event was
created, may be null.
```
```
attackPhases array
```
```
An array of information about the AI Analyst
attack phases for incident events created over
the timeframe.
```
```
attackPhases.phases array 6 An example phase.
```
```
attackPhases.count numeric 124
The number of AI Analyst incident events
relevant to this phase.
```
```
groupStats object
```
```
Aggregated statistics about the grouped AI
Analyst incidents produced over the time period
```
- grouped in this case refers to groups of incident
events which have been associated into
incidents.

```
groupStats.total numeric 120
The total number of groups - AI Analyst incidents
```
- created during the time frame

```
groupStats.compliance numeric 2
```
```
The number of AI Analyst incidents categorized
as having the “compliance” threat behavior
category over the time period.
```
```
groupStats.suspicious numeric 70
```
```
The number of AI Analyst incidents categorized
as having the “suspicious” threat behavior
category over the time period.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

groupStats.critical numeric 48

```
The number of AI Analyst incidents categorized
as having the “critical” threat behavior category
over the time period.
```
groupStats.mitreTactics object

```
For the grouped AI Analyst incidents created
over the time frame, this object describes how
these incidents are mapped to MITRE ATT&CK
Framework tactics.
```
groupStats.mitreTactics.total object

```
An object describing the total number of
incidents relevant to each MITRE ATT&CK
Framework tactic, across all threat behavior
categories. If there are no incidents relevant to a
tactic, the key for that tactic will not appear. The
example provided is non-exhaustive.
```
groupStats.mitreTactics.total.discover
y numeric
5
The total number of incidents relevant to the
MITRE ATT&CK Framework tactic “discovery”.

groupStats.mitreTactics.compliance object

```
An object describing the number of incidents
categorized as “compliance” (threat behavior
category) that are relevant to each MITRE
ATT&CK Framework tactic. If there are no
incidents relevant to a tactic, the key for that
tactic will not appear. The example provided is
non-exhaustive.
```
groupStats.mitreTactics.compliance.dis
covery
numeric 2

```
The total number of “compliance” incidents
relevant to the MITRE ATT&CK Framework tactic
“discovery”.
```
groupStats.mitreTactics.suspicious object

```
An object describing the number of incidents
categorized as “suspicious” (threat behavior
category) that are relevant to each MITRE
ATT&CK Framework tactic. If there are no
incidents relevant to a tactic, the key for that
tactic will not appear. The example provided is
non-exhaustive.
```
groupStats.mitreTactics.suspicious.dis
covery
numeric 5

```
The total number of “suspicious” incidents
relevant to the MITRE ATT&CK Framework tactic
“discovery”.
```
groupStats.mitreTactics.critical object

```
An object describing the number of incidents
categorized as “critical” (threat behavior
category) that are relevant to each MITRE
ATT&CK Framework tactic. If there are no
incidents relevant to a tactic, the key for that
tactic will not appear. The example provided is
non-exhaustive.
```
groupStats.mitreTactics.critical.exfil
tration numeric
45 The total number of “critical” incidents relevant to
the MITRE ATT&CK Framework tactic “discovery”.

metadata object An object containing system information.

metadata.estimatedQueries numeric 0 A system field.

metadata.estimatedQueryMs numeric 0 A system field.

metadata.ratioEstimated numeric 0 A system field.


###### Example Response

```
{
"equivalentHumanTime": 106020000,
"positiveInvestigations": 2,
"negativeInvestigations": 24,
"graphData": {
"breachTime": [
1668689043000,
1668689043000,
...
1668176785000
],
"endTime": [
1668691048000,
1668690970000,
...
1668176856000
],
"equivalentHumanTime": [
4980000,
...
4740000
],
"isPositive": [
true,
...
false
],
"aiaScore": [
0.544,
0.16,
...
null
]
},
"attackPhases": [
{
"phases": [
6
],
"count": 1
},
{
"phases": [
5
],
"count": 1
}
],
"groupStats": {
"total": 2,
"compliance": 0,
"suspicious": 2,
"critical": 0,
"mitreTactics": {
"total": {
"credential-access": 1,
"collection": 1,
"exfiltration": 1
},
"compliance": {},
"suspicious": {
```
_continued..._


"credential-access": 1,
"collection": 1,
"exfiltration": 1
},
"critical": {}
}
},
"metadata": {
"estimatedQueries": 0,
"estimatedQueryMs": 0,
"ratioEstimated": 0.0
}
}


## /AIANALYST/INVESTIGATIONS

The /aianalyst/investigations endpoint returns manual AI Analyst investigations launched by users from the

Threat Visualizer (Customer Portal), Mobile App (Customer Portal), or via the API. It can also be used to create new manual

investigations.

Darktrace AI Analyst already investigates all relevant, non-custom model breach alerts observed on the platform. The

creation of manual investigations should therefore be limited to cases where a custom model has been defined, of where a

third-party alert is raised for a device outside Darktrace that warrants further investigation in the platform. It is highly

recommended to keep the number of triggered investigations within reasonable bounds to prevent overloading the AI

Analyst and preventing legitimate investigations from occurring. Manual investigations can also be triggered via syslog

input - please see AI Analyst Triggered Investigations (Customer Portal) for more information.

There are three states for investigations: pending, processing and finished. A pending investigation waiting for AI

Analyst to start the analysis. A processing investigation means analysis is underway and a finished investigation

means the investigation has concluded.

Whether the investigation identified activity of concern is indicated by the presence of the incidentId key and a non-

empty incidents array for the investigation. AI Analyst incident events created by manual AI Analyst investigations may

create new AI Analyst incidents, or be added to existing incidents if found to link to existing detected activity.

```
POST requests to these endpoints must be made with JSON.
```
###### Request Type(s)

```
[GET] [POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
investigateTime string The time that the investigation should focus around. Valid for POST requests only.
```
```
did numeric The device that an investigation should be created for. Valid for POST requests only.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
investigationId string Unique identifier of a specific AI Analyst manual investigation.
```
```
responseData string Limit the response to the specific top-level field(s).
```
###### Notes

- Once a Darktrace AI Analyst investigation is created, the result will not be instantaneous. Regular GET requests
    should be made to the /aianalyst/investigations endpoint - optionally with the investigationId of
    the created investigation - until the status key displays finished.

```
The investigationId is provided in the response to a valid POST request to this endpoint.
```

- Successful investigations will return an object inside the incidents array with a uuid and array of related
    model breaches in pbid format.

```
◦ To review the AI Analyst incident the event is associated with - including whether there are other events
found - query the /aianalyst/groups endpoint with the uuid value described above in the format
uuid=[uuid]. For example,
/aianalyst/groups?uuid=af763617-2626-4e4c-84fc-e03d5cd8e6c8.
```
```
◦ To review the specific incident event created by the investigation in more detail, query the
/aianalyst/incidentevents endpoint using the uuid value in the format
/aianalyst/incidentevents?uuid=[uuid]. For example,
/aianalyst/incidentevents?uuid=af763617-2626-4e4c-84fc-e03d5cd8e6c8.
```
```
◦ To review the related model breaches, the numeric values from the related array (within incidents
array objects) can be provided to the /modelbreaches endpoint in the format
/modelbreaches/[pbid] or /modebreaches?pbid=[pbid1],[pbid2].
```
```
One related model breach will always be the system AI Analyst::AI Analyst Investigation
model which is used to trigger investigations. The top level pbid field in the response also refers to this
system model only, and cannot be used to review standard associated model breaches.
```
- investigateTime defines the time period AI Analyst should investigate the device at, not the time the
    investigation was created at. When an investigation is triggered, AI Analyst will perform a close analysis of the
    activity for the device or user for a period of roughly one hour, using the time provided as a central point.

###### Example Requests

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all manual investigations in the month of December 2023:

```
https://[instance]/aianalyst/investigations?starttime=1701388800&endtime=1704067199
```
2. GET the status of a specific investigation with the id 52c75821-7c17-4a69-b07f-1c74789a9452:

```
https://[instance]/aianalyst/investigations?investigationId=52c75821-7c17-4a69-
b07f-1c74789a9452&responsedata=status
```
3. POST to create an investigation for a device with did 12345 at 9am on December 1st 2023:

```
https://[instance]/aianalyst/investigations with body {"investigateTime": "1701421200" ,
"did": 12345}
```
###### Example Response

_Request: /aianalyst/investigations_


[
{
"investigationId": "52c75821-7c17-4a69-b07f-1c74789a9452",
"time": 1702310487,
"investigationTime": 1701864000,
"did": 12345,
"version": 2,
"status": "finished",
"createdBy": "i_west",
"noticeUid": "NvUIJpg9MfXywYtc",
"pbid": 630,
"incidentId": "af763617-2626-4e4c-84fc-e03d5cd8e6c8",
"summarizer": "SaasHijackSummary",
"incidents": [
{
"uuid": "af763617-2626-4e4c-84fc-e03d5cd8e6c8",
"related": [
630,
608
],
"summariser": "SaasHijackSummary"
}
]
},
{
"investigationId": "31bc2686-fd5f-427b-804a-7c35c021ac7d",
"time": 1702307136,
"investigationTime": 1702306946,
"did": 3456,
"version": 2,
"status": "finished",
"createdBy": "c_hurst",
"noticeUid": "NhJ3HCRJdVvWLRmM",
"pbid": 477,
"incidents": []
},
{
"investigationId": "35007d49-24d8-444e-9c2b-7dc679ea4a32",
"time": 1700047467,
"investigationTime": 1699442520,
"did": 5678,
"version": 2,
"status": "finished",
"createdBy": "b_ash",
"noticeUid": "NzDnJeWAU7iQ9Kxa",
"pbid": 462,
"incidents": []
}
]


## /AIANALYST/INVESTIGATIONS RESPONSE SCHEMA

###### The summariser / summarizer Field

The Darktrace AI Analyst operates a hypothesis- based analysis approach, where activity is evaluated against a number of

possible, relevant hypotheses and a determination is taken of which (if any) hold based upon the evidence gathered and

investigations performed. These hypotheses are represented by “summarizers” – grouped investigative steps, analysis

approaches, or classifiers – which each try to locate activity or indicators relevant to their field of investigation.

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
investigationId string
52c75821-7c17-4a69-
b07f-1c74789a9452 A unique identifier for the investigation itself.
```
```
time numeric 1702310487
The time at which the investigation was created
in epoch time.
```
```
investigationTime numeric 1701864000 The timestamp around which the investigation
was focused in epoch time.
```
```
did numeric 12345
The device identifier of the device that was
investigated.
```
version numeric (^2) A system field
status string finished
The current status of the investigation. Can be
“pending”, “processing”, or “finished”.
createdBy string i_west The user who triggered the investigation.
noticeUid string NvUIJpg9MfXywYtc A system field.
pbid numeric 9182907
A system field. The model breach id of the “AI
Analyst Investigation” model breach that initiated
the investigation.
incidentId string
af763617-2626-4e4c-
84fc-e03d5cd8e6c8
The unique identifier of the AI Analyst incident
event created to describe the activity found. Can
be used with other AI Analyst API endpoints to
review in more detail. Only present if the
investigation resulted in findings.
summarizer string SaasHijackSummary
In this case, the system name for the summarizer
which identified the activity AI Analyst chose to
surface to the end user. See above for more
details.
incidents array
An array of AI Analyst incident events created as
a result of the investigation. Empty if no activity is
surfaced as a result.
incidents.uuid string
af763617-2626-4e4c-
84fc-e03d5cd8e6c8
Same as incidentID field above.
incidents.related array (^91829)
incidents.summariser string SaasHijackSummary Same as summarizer above.

###### Example Response

_Request: /aianalyst/investigations_


[
{
"investigationId": "52c75821-7c17-4a69-b07f-1c74789a9452",
"time": 1702310487,
"investigationTime": 1701864000,
"did": 12345,
"version": 2,
"status": "finished",
"createdBy": "i_west",
"noticeUid": "NvUIJpg9MfXywYtc",
"pbid": 630,
"incidentId": "af763617-2626-4e4c-84fc-e03d5cd8e6c8",
"summarizer": "SaasHijackSummary",
"incidents": [
{
"uuid": "af763617-2626-4e4c-84fc-e03d5cd8e6c8",
"related": [
630,
608
],
"summariser": "SaasHijackSummary"
}
]
},
{
"investigationId": "31bc2686-fd5f-427b-804a-7c35c021ac7d",
"time": 1702307136,
"investigationTime": 1702306946,
"did": 3456,
"version": 2,
"status": "finished",
"createdBy": "c_hurst",
"noticeUid": "NhJ3HCRJdVvWLRmM",
"pbid": 477,
"incidents": []
},
{
"investigationId": "35007d49-24d8-444e-9c2b-7dc679ea4a32",
"time": 1700047467,
"investigationTime": 1699442520,
"did": 5678,
"version": 2,
"status": "finished",
"createdBy": "b_ash",
"noticeUid": "NzDnJeWAU7iQ9Kxa",
"pbid": 462,
"incidents": []
}
]


## /AIANALYST/INCIDENTS (DEPRECATED)

The following endpoint is now considered legacy and is preserved for backwards compatibility. To request AI Analyst

incidents from the API in Darktrace Threat Visualizer 5.2 and above, please use _/aianalyst/groups_ and

_/aianalyst/incidentevents_.

The Darktrace Cyber AI Analyst investigates, analyzes and reports upon threats seen within your Darktrace environment; as

a starting point, it reviews and investigates all Model Breaches that occur on the system. If anomalies or patterns of activity

are identified during this analysis process, an event is created.

The /aianalyst/incidents endpoint provides access to AI Analyst events - a group of anomalies or network activity

investigated by Cyber AI Analyst that pose a likely cyber threat. The endpoint supports pre-5.2 incident construction.

AI Analyst incidents in the Threat Visualizer UI are comprised of one or more events, where an event is a tab within each

incident. In 5.1 and below, incidents were created by grouping events by the device triggering the activity or by grouping by

activity itself. Incidents can still be constructed around devices using the pre-5.2 methodology. Cross-network events -

events which were created by grouping similar activity - are now deprecated.

For users wishing to create alerts and construct incidents from the events returned by the API using the pre-5.2 method,

important information about how events should be grouped are provided by the grouping and activity IDs. Each event

returned by the API contains an activityId, one or more groupingIds, and a groupByActivity field which may be

```
true or false. The activityId is an identifier for the specific activity detected by AI Analyst, and each entry in the
groupingIDs array refers to a device that triggered the activity detection.
```
Where groupByActivity=true, events which are returned during the timeframe should be aggregated by the

```
activityId to create cross-device incidents. Where groupByActivity=false, events which are returned during the
```
timeframe should be aggregated by the groupingIds to create device-based incidents.

_Please note, AI Analyst incidents constructed using the pre-5.2 methodology are aggregations of events within a_

_timeframe. Incidents as presented in the User Interface may not directly correlate with those constructed from the API due_

_to differing time or scoring parameters._

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
includeacknowledged boolean Include acknowledged events in the data.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
locale string
```
```
The language for returned strings. Currently supported are de_DE (German), en_GB (English UK),
en_US (English US), es_ES (Spanish ES), es_419 (Spanish LATAM), fr_FR (French), it_IT
(Italian), ja_JP (Japanese), ko_KR (Korean) , pt_BR (Portuguese BR), zh_Hans (Chinese
(Simplified)), zh_Hant (Chinese (Traditional))
```
```
uuid string A unique identifier for an AI Analyst event. Takes multiple values comma-separated.
```
```
did numeric Identification number of a device modelled in the Darktrace system.
```
```
mergeEvents boolean Cross-Network events are deprecated as of 5.2. This parameter is no longer available.
```
```
includeallpinned boolean
```
```
True by default. Controls whether pinned events are returned alongside those from the timeframe
specified.
```
```
includeincidenturl boolean
```

```
PARAMETER TYPE DESCRIPTION
```
```
Controls whether links to events are included in the response - requires the FQDN value to be set
and valid for the queried instance.
```
###### Notes

- A time window for the returned events can be specified using starttime/endtime and unix time in
    milliseconds.

```
◦ Where only endtime is set,starttime will default to 1 week before endtime. Where only
starttime is set, endtime will default to the current time.
```
```
◦ If no time parameters are specified, events from the last seven days (and pinned events, if applicable)
will be returned.
```
- Events that are pinned or part of pinned incidents will always be returned, regardless of the time period
    specified. This can be prevented with includeallpinned=false
- Where locale is not specified or not supported in the current software version, strings will default to en_GB.
- Where the specified locale uses non-ascii characters, these will be returned in unicode format and must be
    parsed.
- As of 5.2, cross-network events - events where more than one uuid may appear in the children array - are
    now deprecated. The mergeEvents parameter is no longer supported.

```
◦ The id field seen in the JSON response is a system field intended for use by the Threat Visualizer
interface. Although for many event types the contents of the children field and the id field are
consistent, some event types (such as cross-network events) utilize a pseudo-identifier in the id field
which will not return data when used with the uuid parameter. As cross-network events are now
deprecated, both values (id or children) can now be used.
```
- Links back to the Threat Visualizer can be included in the response with includeincidenturl=true.

_Please see the response schema for a full breakdown of the_ details _array._

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all AI Analyst events for the device with did=100 - including acknowledged events - for the 7 day period
    from 3rd to 9th July 2020:

```
https://[instance]/aianalyst/incidents?
starttime=1593734400000&endtime=1594166399000&includeacknowledged=true&did=100&includeal
lpinned=false
```
2. GET details of an AI Analyst event with uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633 in French:

```
https://[instance]/aianalyst/incidents?uuid=04a3f36e-4u8w-v9dh-
x6lb-894778cf9633&locale=fr_FR
```

3. GET details of a cross-network AI Analyst event with three child events -

```
c0ec5c71-b4fb-429b-82a7-4d6a73cbcaed, ve9cpd8n-j8mh-fyh3-leev-sz8s8xwfwrs5 &
c5r8131w-yev6-if7b-7alc-b6jp1v8ewon2:
```
```
https://[instance]/aianalyst/incidents?uuid=c0ec5c71-
b4fb-429b-82a7-4d6a73cbcaed,ve9cpd8n-j8mh-fyh3-leev-sz8s8xwfwrs5,c5r8131w-yev6-
if7b-7alc-b6jp1v8ewon2
```

###### Example Response

_Request: /aianalyst/incidents?uuid=04a3f36e-4u8w-v9dh-x6lb-894778cf9633&locale=en_US_

```
[
{
"aiaScore": 100,
"children": [
"04a3f36e-4u8w-v9dh-x6lb-894778cf9633"
],
"summary": "A chain of administrative connections were observed between multiple
devices, which occurred around the same time, and included workstation-local-82.",
"id": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"pinned": true,
"acknowledged": false,
"details": [
[
{
"header": "First Hop",
"contents": [
{
"type": "timestampRange",
"key": "Time",
"values": [
{
"start": 1579710063121,
"end": 1579711920166
}
]
},
{
"type": "device",
"key": "Source device",
"values": [
{
"sid": 12,
"mac": "56:2d:4b:9c:18:42",
"ip": "10.12.14.2",
"identifier": "Finance File Server",
"did": 532,
"hostname": null,
"subnet": null
}
]
},
...
]
}
],
[
...
]
}
]
],
"summariser": "LateralMovementCrawler",
"relatedBreaches": [
{
"timestamp": 1579710173000,
"threatScore": 19,
"pbid": 252317,
"modelName": "Anomalous Connection / Active SSH Tunnel"
}
],
"breachDevices": [
{
```
_continued..._


```
"sid": 10,
"mac": "93:gb:28:g1:fc:g1",
"ip": "10.0.18.224",
"identifier": "workstation-local-82",
"did": 230,
"hostname": "workstation-local-82",
"subnet": null
}
],
"periods": [
{
"start": 1579708374972,
"end": 1579711920166
}
],
"attackPhases": [
5
],
"mitreTactics": [
"lateral-movement"
],
"groupingIds": [
"544a6ce7"
],
"activityId": "ae463dc8",
"groupByActivity": false,
"title": "Suspicious Chain of Administrative Connections"
}
]
```
_Response is abbreviated._


## /AIANALYST/INCIDENTS RESPONSE SCHEMA

## (DEPRECATED)

The following endpoint is now considered legacy and is preserved for backwards compatibility. To request AI Analyst

incidents from the API in v5.2 and above, please use _/aianalyst/groups_ and _/aianalyst/incidentevents_.

_Incident events created prior to v5.2 will not contain values for_ currentGroup _and_ groupPreviousGroups_._

###### Understanding the details array

The details array and sub-arrays contain all contextual information and analysis output regarding the event. The outer array

groups sections of information together which are related, and the inner array groups together subsections that make up

that section. Each subsection has a header and one or more objects (in the contents array) containing relevant information

- subsections are interrelated and should not be moved outside their parent section.

For example, an event concerns a suspicious SaaS activity. The details array contains two sub-arrays (sections), the first

section concerns the SaaS account itself and contains only one subsection, the second section concerns the activity itself

and contains three subsections. This would be structured as follows:

```
"details": [
[ // Section 1
{
"header": "SaaS User Details", // Subsection 1.1
"contents": [ // Information relevant to Subsection 1.1
...
]
}
], // End of Section 1
[ // Section 2
{
"header": "Agent Carrying out Suspicious Activity", // Subsection 2.1
"contents": [ // Information relevant to Subsection 2.1
...
]
},
{
"header": "Summary of Activity", // Subsection 2.2
"contents": [ // Information relevant to Subsection 2.2
...
]
},
{
"header": "Activity Details", // Subsection 2.3
"contents": [ // Information relevant to Subsection 2.3
...
]
}
]
], // End of Section 2
```
It is important to preserve the sectioning of information as it directly relates to one another, particularly where multiple

actors or connections appear within the event. For example, if an event contained two connections - one with data transfer

and one without - it is essential that the subsection concerning the data that was transferred stays with the information

about the connection it was transferred over.


###### ### The summariser / summarizer Field

The Darktrace AI Analyst operates a hypothesis- based analysis approach, where activity is evaluated against a number of

possible, relevant hypotheses and a determination is taken of which (if any) hold based upon the evidence gathered and

investigations performed. These hypotheses are represented by “summarizers” – grouped investigative steps, analysis

approaches, or classifiers – which each try to locate activity or indicators relevant to their field of investigation.

#### Response Schema - Single Event

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
aiaScore numeric 100
The reportability of the event as classified by AI
Analyst - out of 100.
```
```
children array
```
```
c0ec5c71-
b4fb-429b-82a7-4d6a
73cbcaed
```
```
A unique identifier that can be used to request
this AI Analyst event. This array will only contain
one entry as of v5.2 and above.
```
```
createdAt numeric 1646389417644 Timestamp for event creation in epoch time.
```
```
category string suspicious
```
```
The behavior category associated with the
incident event. Relevant for v5.2+ incident
construction only.
```
```
currentGroup string
```
```
gc0ec5c71-
b4fb-429b-82a7-4d6a
73cbcaed
```
```
The UUID of the current incident this event
belongs to. Used for v5.2+ incident construction.
```
```
summary string
```
```
A chain of
administrative
connections were
observed between
multiple
devices, which
occurred around the
same time, and
included
workstation-
local-82.
```
```
A textual summary of the suspicious activity.
```
```
id string
```
```
c0ec5c71-
b4fb-429b-82a7-4d6a
73cbcaed
```
```
A unique identifier that can be used to request
this AI Analyst event.
```
```
pinned boolean TRUE
```
```
Whether the event, or an incident that the event
is associated with, is pinned within the Threat
Visualizer user interface. Pinned events will
always return regardless of the timeframe
specified.
```
```
acknowledged boolean FALSE Whether the event has been acknowledged.
```
```
details array
```
```
An array of multiple sections (sub-arrays) of
event information. Please see Understanding the
details array” above. ”
```
```
details.header string First Hop
A short title describing the section of
information.
```
```
details.contents array
```
```
An array of multiple objects describing relevant
information for this subsection, such as involved
devices, relevant external hosts, ports used and
anomaly scorings.
```
```
details.contents.type string device
The type of information contained within the
object. A full list of examples is available.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

details.contents.key string Source device
Assigns meaning to the values in the values
field - a short description of the data.

details.contents.values array

```
One or more values that relate to the key. For
example, a series of ports or hostnames. Full
examples of all data types are available.
```
summariser string
LateralMovementCraw
ler

```
In this case, the system name for the summarizer
which identified the activity AI Analyst chose to
surface to the end user. See above for more
details.
```
relatedBreaches array
An array of model breaches related to the activity
investigated by AI analyst.

relatedBreaches.timestamp numeric 1579710173000 The timestamp at which the model breach
occurred in epoch time.

relatedBreaches.threatScore numeric 19
The breach score of the associated model
breach - out of 100.

relatedBreaches.pbid numeric 252317 The “policy breach ID” unique identifier of the
model breach.

relatedBreaches.modelName string

```
Anomalous
Connection / Active
SSH Tunnel
```
```
The name of the model that breached.
```
sender string example@example.com

```
If the incident event is created from Darktrace/
Email activity, this field will be populated with an
email address representing the sender of the
anomalous email or email campaign
investigated. Otherwise, null.
```
breachDevices array

```
An array of devices involved in the related model
breach(es). For incident events created from
Darktrace/Email activity, this array is empty.
```
breachDevices.sid numeric 10
The subnet id for the subnet the device is
currently located in.

breachDevices.mac string 93:gb:28:g1:fc:g1 The MAC address associated with the device.

breachDevices.ip string 10.15.3.39 The IP associated with the device.

breachDevices.identifier string
workstation-
local-82

```
An identifier for the device used when
constructing summaries or reports. May be the
device label, hostname or IP, depending on
availability.
```
breachDevices.did numeric 561

```
The unique “device id” identifier for the device
that triggered the breach. This field is used to
group events into device-based incidents within
the Threat Visualizer.
```
breachDevices.hostname string
workstation-
local-82

```
The hostname associated with the device, if
available.
```
breachDevices.subnet string Finance Subnet
The subnet label for the corresponding subnet, if
available.

periods array

```
An array of one or more periods of time where
anomalous activity occurred that AI Analyst
investigated.
```
periods.start numeric 1579708374972 A timestamp for the start of the activity period in
epoch time.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

periods.end numeric 1579711920166
A timestamp for the end of the activity period in
epoch time.

attackPhases array 5 Of the six attack phases, which phases are
applicable to the activity.

mitreTactics array lateral-movement
An array of MITRE ATT&CK Framework tactics
that have been mapped to this event.

groupingIds array 544a6ce7

```
Each entry in the groupingIDs array refers to
a device that triggered the activity detection. In
single events, should only contain one ID. If
groupByActivity=false, this field should be
used to group events together into an incident.
Used by pre-v5.2 legacy incident construction.
```
activityId string ae463dc8

```
An identifier for the specific activity detected by
AI Analyst. If groupByActivity=true, this
field should be used to group events together
into an incident. Used by pre-v5.2 legacy incident
construction.
```
groupByActivity boolean false

```
Indicates whether the event should be
aggregated by activity or by device to create an
incident. When true, the event should be
aggregated by activityID, and when false,
aggregated by groupingID(s). Used by pre-v5.2
legacy incident construction.
```
title string

```
Suspicious Chain of
Administrative
Connections
```
```
A title describing the activity that occurred.
```
groupCategory string suspicious

```
The behavior category associated with the
incident overall. Relevant for v5.2+ incident
construction only.
```
groupPreviousGroups array

```
If the incident event was part of an incident which
was later merged with another, the UUIDs of the
incidents before they were merged. Used for
v5.2+ incident construction.
```
groupScore numeric 27.72702944

```
The current overall score of the incident this
event is part of. Relevant for v5.2+ incident
construction only.
```
userTriggered boolean FALSE
Whether the event was created as a result of a
user-triggered AI Analyst investigation.

externalTriggered boolean FALSE
Whether the event was created as a result of an
externally triggered AI Analyst investigation.


###### Example Response

```
[
{
"aiaScore": 100,
"children": [
"04a3f36e-4u8w-v9dh-x6lb-894778cf9633"
],
"createdAt": 1646389417644,
"category": "suspicious",
"currentGroup": "g00b14e94-f744-5ecb-a35a-35a2dda23162",
"summary": "A chain of administrative connections were observed between multiple
devices, which occurred around the same time, and included workstation-local-82.",
"id": "04a3f36e-4u8w-v9dh-x6lb-894778cf9633",
"pinned": true,
"acknowledged": false,
"details": [
[
{
"header": "First Hop",
"contents": [
{
"type": "timestampRange",
"key": "Time",
"values": [
{
"start": 1579710063121,
"end": 1579711920166
}
]
},
{
"type": "device",
"key": "Source device",
"values": [
{
"sid": 12,
"mac": "56:2d:4b:9c:18:42",
"ip": "10.12.14.2",
"identifier": "Finance File Server",
"did": 532,
"hostname": null,
"subnet": null
}
]
},
...
]
}
],
[
...
]
}
]
],
"summariser": "LateralMovementCrawler",
"relatedBreaches": [
{
"timestamp": 1579710173000,
"threatScore": 19,
"pbid": 252317,
"modelName": "Anomalous Connection / Active SSH Tunnel"
}
```
_continued..._


```
],
"sender": null,
"breachDevices": [
{
"sid": 10,
"mac": "93:gb:28:g1:fc:g1",
"ip": "10.0.18.224",
"identifier": "workstation-local-82",
"did": 230,
"hostname": "workstation-local-82",
"subnet": null
}
],
"periods": [
{
"start": 1579708374972,
"end": 1579711920166
}
],
"attackPhases": [
5
],
"mitreTactics": [
"lateral-movement"
],
"groupingIds": [
"544a6ce7"
],
"activityId": "ae463dc8",
"groupByActivity": false,
"groupCategory": "suspicious",
"groupScore": 70,
"groupPreviousGroups": [],
"title": "Suspicious Chain of Administrative Connections"
}
]
```
_Response is abbreviated._

#### Response Schema - Cross-Network Event

_Cross-Network events are deprecated as of v5.2_

#### Example details entries

###### "type": "string"

```
{
"type": "string",
"key": "Application protocol",
"values": [
"SSH"
]
}
```

###### "type": "device"

```
{
"type": "device",
"key": "Source device",
"values": [
{
"sid": 12,
"mac": "93:gb:28:g1:fc:g1",
"ip": "10.140.15.33",
"identifier": "Workstation 12",
"did": 57,
"hostname": null,
"subnet": null
}
]
}
```
###### "type": "externalHost"

```
{
"type": "externalHost",
"key": "Endpoint",
"values": [
{
"ip": null,
"hostname": "stackoverflow.com"
}
]
}
```
###### "type": "timestamp"

```
{
"type": "timestamp",
"key": "Hostname first observed",
"values": [
1593646723036
],
},
```
###### "type": "duration"

```
{
"type": "duration",
"key": "Median beacon period",
"values": [
30
]
}
```

###### "type": "integer"

```
{
"type": "integer",
"key": "Destination port",
"values": [
22
]
}
```
###### "type": "float"

```
{
"type": "float",
"key": "Latitude",
"values": [
12.46
]
}
```
###### "type": "percentage"

```
{
"type": "percentage",
"key": "Hostname rarity",
"values": [
100
]
}
```
###### "type": "dataVolume"

```
{
"type": "dataVolume",
"key": "Total data in",
"values": [
142271
]
}
```

###### "type": "ratio"

```
{
"type": "ratio",
"key": "Validation Statuses",
"values": [
{
"percentage": 50
"value": "ok",
},
{
"percentage": 50
"value": "Unknown",
}
]
}
```
###### "type":

###### "timestampRange"

```
{
"type": "timestampRange",
"key": "Time",
"values": [
{
"start": 1579710063121,
"end": 1579711920166
}
]
}
```
###### "type": "integerRange"

```
{
"type": "integerRange",
"key": "Range of connections per hour",
"values": [
{
"start": 1
"end": 6,
}
]
}
```
###### "type": "durationRange"

```
{
"type": "durationRange",
"key": "Range of periods",
"values": [
{
"start": 30
"end": 79,
}
]
}
```

###### "type":

###### "dataVolumeRange"

```
{
"type": "dataVolumeRange",
"key": "Range of data volumes sent per external connection",
"values": [
{
"start": 717
"end": 944,
}
]
}
```
###### "type":

###### "percentageRange"

```
{
"type": "percentageRange",
"key": "Rarity of all endpoints",
"values": [
{
"start": 100
"end": 100,
}
]
}
```
###### "type": "stringRange"

```
{
"type": "stringRange",
"key": "Days of activity",
"values": [
{
"start": "Wednesday"
"end": "Sunday",
}
]
}
```

## /ANTIGENA

The /antigena endpoint returns information about current and past Darktrace RESPOND/Network (formerly Antigena

Network) actions. It can be used to retrieve a list of currently quarantined devices or Darktrace RESPOND Actions requiring

approval. Information from active integrations such as firewalls is not included in this data.

If a time window is not specified, the request will return all current actions with a future expiry date and all historic actions

with an expiry date in the last 14 days. Actions which were not activated will still be returned.

To create manual Darktrace RESPOND actions via the API, the /antigena/manual endpoint can be used (6.0+). Please

see _/antigena/manual_ for more information.

###### POST Requests

As of Darktrace Threat Visualizer 6.0.16, the _state_ of a RESPOND action can be changed via POST requests to this endpoint.

This includes activation of pending actions.

This can be combined into a simple workflow where /antigena/summary is regularly polled for new entries in the

```
pendingActionDevices array. These entries represent did values which can then be used to query the /antigena
```
endpoint with the did parameter, using the includehistory parameter to identify actions for the device with the

current state "action": "Created (requires confirmation)". The codeid for these actions can then be used for

POST requests to the /antigena endpoint with "activate": true and an optional duration.

Changes made via the API will show the username of the user the API token is associated with in the action history.

Requests must be made in JSON format. There are four main formats for these requests:

**Activate (pending action)**

```
{"codeid":123,"activate":true,"reason":"Example reason"}
```
Actions created by models will have a default duration, defined by the “Darktrace RESPOND Action Duration” setting on the

model. If not duration value is provided, the action is activated for the default time period.

**Extend (active action)**

```
{"codeid":123,"duration":100,"reason":"Example reason"}
```
The duration value defines the length the action should cover; a POST including this value will cause the action duration

to be _changed_. For example, if an action has 100 seconds remaining, a POST request with "duration": 110 will extend

the length of the action by 10 seconds. Conversely, a POST request with "duration": 10 will reduce the remaining time

to 10 seconds, causing the action to expire 90 seconds early.

This parameter should therefore be used carefully.

**Clear (active, pending or expired action)**

```
{"codeid":123,"clear":true,"reason":"Example reason"}
```

Clearing an active action will also suppress the combination of Darktrace RESPOND action and model breach conditions for

the remainder of the time the action was active for. The duration parameter does not impact the length that an action/

condition combination is cleared for.

It is also possible to clear an expired action. Doing so will remove it from the returned results unless includecleared is

used.

###### Reactivate (cleared or expired action)

```
{"codeid":123,"activate":true,"duration": 100,"reason":"Example reason"}
```
To reactivate a cleared or expired action, a duration must be supplied.

###### Request Type(s)

```
[GET] [POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
fulldevicedetails boolean
Returns the full device detail objects for all devices referenced by data in an API response. Use of
this parameter will alter the JSON structure of the API response for certain calls.
```
```
includecleared boolean Returns all Darktrace RESPOND actions including those already cleared. Defaults to false.
```
```
includehistory boolean
Include additional history information about the action state, such as when it was created or
extended.
```
```
needconfirming boolean
```
```
Filters returned Darktrace RESPOND actions by those that need human confirmation or do not need
human confirmation.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
from string Start time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
to string End time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
includeconnections boolean Adds a connections object which returns connections blocked by a Darktrace RESPOND action.
```
```
responsedata string
When given the name of a top-level field or object, restricts the returned JSON to only that field or
object.
```
```
pbid numeric
```
```
Only return the Darktrace RESPOND actions created as a result of the model breach with the
specified ID.
```
```
codeid numeric Unique numeric identifier of a RESPOND action. Valid for POST requests only.
```
```
activate boolean
```
```
For POST requests, if true, indicates the request should activate an action. Cannot be combined
with "clear": true. Valid for POST requests only.
```
```
clear boolean
```
```
For POST requests, if true, indicates the request should clear an action. Cannot be combined with
"activate": true. Valid for POST requests only.
```
```
reason string free text field to specify the action purpose. Valid (and recommended) for POST requests only.
```
```
duration numeric
```
```
Specify how long the state change should apply for (optional) in seconds. For extensions, should
contain the current duration plus the amount the action should be extended for. Valid for POST
requests only.
```

###### Notes

- Time parameters must always be specified in pairs.
- When fulldevicedetails=true, actions will be contained in an actions: object and devices in a
    devices: object
- active=true means the action has been activated, either by human confirmation or automatically in fully
    autonomous mode. If a Darktrace RESPOND Action is cleared manually, active will show false. If a
    Darktrace RESPOND action expires, it will continue to show active=true.
- Actions manually cleared by a user will have the value cleared=true, expired actions will have
    cleared=false. When an action is cleared manually, it will also set the active value to false.
- The includehistory parameter adds an additional history object to each action which describes all the
    historic states the action has been in, when the state changed, and the user that triggered the change.

```
The valid states are created, created (requires confirmation), extended, cleared,
reactivated (expired) and reactivated (cleared).
```
- If includeconnections=true, a connections object will be added with details of all connections that were
    blocked by active Darktrace RESPOND actions.
- Manual Darktrace RESPOND/Network actions can be identified by "manual": true in the response. These
    actions will contain an object describing the triggerer of the action.

```
For manual actions, the response fields model and modeluuid will appear empty and the model score will
be set to 0 or 0.0.
```
- For POST requests, if the “Audit Antigena” setting is enabled on the Darktrace System Config page, requests will
    fail unless the reason parameter is also specified.

```
This parameter is otherwise optional, but the value will populate in the action history window (refer to
Understanding the Darktrace RESPOND Actions page (Customer Portal)) if supplied.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all Darktrace RESPOND Actions that require approval and retrieve full details for associated devices:

```
https://[instance]/antigena?fulldevicedetails=true&needconfirming=true
```
2. GET all actions on January 10th 2020 (including cleared actions) and any blocked connections:

```
https://[instance]/antigena?
from=2020-01-10T12:00:00&to=2020-01-10T12:00:00&includecleared=true&includeconnections=t
rue
```
3. GET all actions created as a result of the model breach with pbid=1234 and include the historic state of the
    actions:

```
https://[instance]/antigena?pbid=1234&includehistory=true
```

4. POST to activate a pending action with id 1234 and provide a reason for the action:

```
https://[instance]/antigena with body {"codeid":123,"activate":true,"reason":"Example
reason"}
```

###### Example Response

_Request: /antigena?includeconnections=true&fulldevicedetails=true_

```
{
"actions": [
{
"codeid": 4764,
"did": 316,
"ip": "10.0.18.224",
"action": "quarantine",
"manual": false,
"triggerer": "null"
"label": "Quarantine device",
"detail": "",
"score": 0.3,
"pbid": 442301,
"model": "Antigena / Network / External Threat / Antigena Quarantine Example",
"modeluuid": "d92d6f73-gc1b-cg96-d4g8-df8a79f2a3cd",
"start": 1582038124000,
"expires": 1582041724000,
"blocked": true,
"agemail": false,
"active": true,
"cleared": false
},
...
}
],
"connections": [
{
"action": "quarantine",
"label": "Quarantine device",
"did": 316,
"direction": "outgoing",
"ip": "10.0.18.224",
"port": 443,
"timems": 1582033860000,
"time": "2020-02-18 13:51:00"
},
...
],
"devices": [
{
"did": 316,
"ip": "10.0.18.224",
"ips": [
{
"ip": "10.0.18.224",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"did": 316,
"sid": 23,
"hostname": "Sarah Development",
"firstseen": 1528807092000,
"lastseen": 1581510431000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
"tags": [
{
"tid": 9,
```
_continued..._


```
"expiry": 0,
"thid": 9,
"name": "Antigena All",
"restricted": false,
"data": {
"auto": false,
"color": 200,
"description": ""
},
"isReferenced": true
},
...
]
},
...
]
}
```
_Response is abbreviated._


## /ANTIGENA RESPONSE SCHEMA

To accompany the introduction of manual Darktrace RESPOND/Network actions in Darktrace Threat Visualizer 6, additional

fields/objects manual and triggerer are now returned in all responses.

#### Response Schema

###### fulldevicedetails=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
codeid numeric 4894 A unique id for the Darktrace RESPOND action.
```
```
did numeric 532 The “device id” of the device the action is applied
against.
```
```
ip string 10.0.18.224 The IP that the action is applied against.
```
```
action string quarantine The type of action being performed.
```
```
manual boolean FALSE
Whether the action was triggered manually by a
user.
```
```
triggerer
string/
array
```
```
If triggered manually, an object describing the
user who triggered the action. If triggered by
Darktrace RESPOND automatically, “null”.
```
```
triggerer.username string b.ash
Username of the user who triggered the manual
action. Only present for manual actions.
```
```
triggerer.reason string
```
```
The “reason” provided by the user for the action
trigger, where the “reason” field is required by
deployment configuration. Only present for
manual actions.
```
```
label string Quarantine device
The readable label for the action being
performed.
```
```
detail string
Any additional detail about the action being
performed.
```
```
score numeric 0.3
The model breach score of the model breach
that triggered the Darktrace RESPOND action.
```
```
pbid numeric 449854
The model breach ‘policy breach id’ of the model
breach that triggered the action.
```
```
model string
```
```
Anomalous
File::Masqueraded
File Transfer
```
```
The name of the model that triggered the
Darktrace RESPOND action.
```
```
modeluuid string
ee88d329-6cdd-8dd3-
5baa-2e323g3fa833
```
```
The unique identifier for the model that triggered
the Darktrace RESPOND action.
```
```
start numeric 1586190000000 The start time of the action in epoch time.
```
```
expires numeric 1586190000000 The expiry time of the action in epoch time.
```
```
blocked boolean FALSE
Whether the action blocked any matching
connections.
```
```
updated string 1585910000000 When the action was last updated. For example,
a user extending an action.
```
```
agemail boolean FALSE
Whether the action was triggered by Darktrace/
Email.
```

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
aghost boolean FALSE
Whether the action was triggered for Darktrace
RESPOND/Endpoint agents.
```
```
active boolean FALSE Whether the action has been activated at some
point.
```
```
cleared boolean FALSE
Whether the action has been manually cleared
by an operator.
```
###### Example Response

```
[
{
"codeid": 4764,
"did": 316,
"ip": "10.0.18.224",
"action": "quarantine",
"manual": false,
"triggerer": null,
"label": "Quarantine device",
"detail": "",
"score": 0.3,
"pbid": 442301,
"model": "Antigena / Network / External Threat / Antigena Quarantine Example",
"modeluuid": "d92d6f73-gc1b-cg96-d4g8-df8a79f2a3cd",
"start": 1582038124000,
"expires": 1582041724000,
"blocked": true,
"agemail": false,
"aghost": false,
"active": true,
"cleared": false
},
...
]
```
_Response is abbreviated._

###### fulldevicedetails=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
actions array An array of Darktrace RESPOND actions.
```
```
actions.codeid numeric 4895 A unique id for the Darktrace RESPOND action.
```
```
actions.did numeric 101
The “device id” of the device the action is applied
against.
```
```
actions.ip string 192.168.72.4 The IP that the action is applied against.
```
```
actions.action string quarantine The type of action being performed.
```
```
actions.manual boolean FALSE Whether the action was triggered manually by a
user.
```
```
actions.triggerer
string/
array
```
```
If triggered manually, an object describing the
user who triggered the action. If triggered by
Darktrace RESPOND automatically, “null”.
```
```
actions.triggerer.username string b.ash
Username of the user who triggered the manual
action. Only present for manual actions.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

actions.triggerer.reason string

```
The “reason” provided by the user for the action
trigger, where the “reason” field is required by
deployment configuration. Only present for
manual actions.
```
actions.label string Quarantine device
The readable label for the action being
performed.

actions.detail string
Any additional detail about the action being
performed.

actions.score numeric 0.3
The model breach score of the model breach
that triggered the Darktrace RESPOND action.

actions.pbid numeric 449859
The model breach ‘policy breach id’ of the model
breach that triggered the action.

actions.model string

```
Anomalous
File::Masqueraded
File Transfer
```
```
The name of the model that triggered the
Darktrace RESPOND action.
```
actions.modeluuid string
ee88d329-6cdd-8dd3-
5baa-2e323g3fa833

```
The unique identifier for the model that triggered
the Darktrace RESPOND action.
```
actions.start numeric 1586937600000 The start time of the action in epoch time.

actions.expires numeric 1584265931000 The expiry time of the action in epoch time.

actions.blocked boolean FALSE
Whether the action blocked any matching
connections.

actions.updated string 1584265931000
When the action was last updated. For example,
a user extending an action.

actions.agemail boolean FALSE
Whether the action was triggered by Darktrace/
Email.

actions.aghost boolean FALSE
Whether the action was triggered for Darktrace
RESPOND/Endpoint agents.

actions.cleared boolean FALSE
Whether the action has been manually cleared
by an operator.

devices array
An array of devices that correspond to the “did”
values in the actions array.

devices.did numeric (^101) The “device id”, a unique identifier.
devices.quarantine numeric 1586937600000
The time that quarantine began upon the device
in epoch time.
devices.ip string 192.168.72.4 The current IP associated with the device.
devices.ips array IPs associated with the device historically.
devices.ips.ip string 192.168.72.4 A historic IP associated with the device.
devices.ips.timems numeric 1584265931000
The time the IP was last seen associated with
that device in epoch time.
devices.ips.time string 2020-03-15 09:52:11
The time the IP was last seen associated with
that device in readable format.
devices.ips.sid numeric (^12) The subnet id for the subnet the IP belongs to.
devices.sid numeric 12
The subnet id for the subnet the device is
currently located in.
devices.firstSeen numeric 1528812000000 The first time the device was seen on the
network.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

devices.lastSeen numeric 1584265931000
The last time the device was seen on the
network.

devices.os string
Linux 3.11 and
newer

```
The device operating system if Darktrace is able
to derive it.
```
devices.typename string desktop The device type in system format.

devices.typelabel string Desktop The device type in readable format.

devices.tags array An object describing tags applied to the device.

devices.tags.tid numeric 50 The “tag id”. A unique value.

devices.tags.expiry numeric 0 The expiry time for the tag when applied to a
device.

devices.tags.thid numeric 50
The “tag history” id. Increments if the tag is
edited.

devices.tags.name string Multi-use The tag label displayed in the user interface or in
objects that reference the tag.

devices.tags.restricted boolean FALSE
Indicates a read-only tag - these tags can only be
modified or applied by Darktrace.

devices.tags.data object An object containing information about the tag.

devices.tags.data.auto boolean FALSE Whether the tag was auto-generated.

devices.tags.data.color numeric 200
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.

devices.tags.data.description string
Device is a pool
device.

```
An optional description summarizing the
purpose of the tag.
```
devices.tags.isReferenced boolean TRUE A system field.

devices.tags.data.visibility string Public
Whether the tag is used by one or more model
components.

devices.macaddress string 56:2d:4b:9c:18:42
The current MAC address associated with the
device.

devices.vendor string
The vendor of the device network card as
derived by Darktrace from the MAC address.

devices.hostname string ws173 The current device hostname.


###### Example Response

```
{
"actions": [
{
"codeid": 4764,
"did": 316,
"ip": "10.0.18.224",
"action": "quarantine",
"manual": false,
"triggerer": null,
"label": "Quarantine device",
"detail": "",
"score": 0.3,
"pbid": 442301,
"model": "Antigena / Network / External Threat / Antigena Quarantine Example",
"modeluuid": "d92d6f73-gc1b-cg96-d4g8-df8a79f2a3cd",
"start": 1582038124000,
"expires": 1582041724000,
"blocked": true,
"agemail": false,
"aghost": false,
"active": true,
"cleared": false
},
...
],
"devices": [
{
"did": 316,
"ip": "10.0.18.224",
"ips": [
{
"ip": "10.0.18.224",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"did": 316,
"sid": 23,
"hostname": "Sarah Development",
"firstseen": 1528807092000,
"lastseen": 1581510431000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
"tags": [
{
"tid": 9,
"expiry": 0,
"thid": 9,
"name": "Darktrace RESPOND All",
"restricted": false,
"data": {
"auto": false,
"color": 200,
"description": ""
},
"isReferenced": true
},
...
]
```
_Response is abbreviated._


###### Response Schema - includeconnections=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
actions array An array of Darktrace RESPOND actions.
```
actions.codeid numeric (^4895) A unique id for the Darktrace RESPOND action.
actions.did numeric 239
The “device id” of the device the action is applied
against.
actions.ip string 10.12.14.2 The IP that the action is applied against.
actions.action string quarantine The type of action being performed.
actions.manual boolean FALSE
Whether the action was triggered manually by a
user.
actions.triggerer
string/
array
If triggered manually, an object describing the
user who triggered the action. If triggered by
Darktrace RESPOND automatically, “null”.
actions.triggerer.username string b.ash
Username of the user who triggered the manual
action. Only present for manual actions.
actions.triggerer.reason string
The “reason” provided by the user for the action
trigger, where the “reason” field is required by
deployment configuration. Only present for
manual actions.
actions.label string Quarantine device
The readable label for the action being
performed.
actions.detail string
Any additional detail about the action being
performed.
actions.score numeric 0.3
The model breach score of the model breach
that triggered the Darktrace RESPOND action.
actions.pbid numeric 449859
The model breach ‘policy breach id’ of the model
breach that triggered the action.
actions.model string
Anomalous
File::Masqueraded
File Transfer
The name of the model that triggered the
Darktrace RESPOND action.
actions.modeluuid string
ee88d329-6cdd-8dd3-
5baa-2e323g3fa833
The unique identifier for the model that triggered
the Darktrace RESPOND action.
actions.start numeric 1586190000000 The start time of the action in epoch time.
actions.expires numeric 1586190000000 The expiry time of the action in epoch time.
actions.blocked boolean FALSE Whether the action blocked any matching
connections.
actions.updated string 1586190000000
When the action was last updated. For example,
a user extending an action.
actions.agemail boolean FALSE Whether the action was triggered by Darktrace/
Email.
actions.aghost boolean FALSE
Whether the action was triggered for Darktrace
RESPOND/Endpoint agents.
actions.active boolean TRUE Whether the action has been activated at some
point.
actions.cleared boolean FALSE
Whether the action has been manually cleared
by an operator.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

connections array
An array of connections blocked by one or more
Darktrace RESPOND actions.

connections.action string quarantine The type of action being performed that blocked
the connection.

connections.label string Quarantine device
The readable label for the action being
performed.

connections.did numeric 239 The “device id” of the device the action is applied
against.

connections.direction string outgoing
The direction of the blocked connection in
relation to the actioned device.

connections.ip string 10.0.18.224

```
Depending on connection direction, the IP that
the actioned device is connecting to or is being
connected to by.
```
connections.port numeric 3128

```
Depending on connection direction, the port that
the actioned device is connecting to or is being
connected to on.
```
connections.timems numeric 1584265931000
The time that the blocked connection was
attempted in epoch time.

connections.time string 2020-03-15 09:52:11
The time that the blocked connection was
attempted in readable format.


###### Example Response

```
{
"actions": [
{
"codeid": 4764,
"did": 316,
"ip": "10.0.18.224",
"action": "quarantine",
"manual": false,
"triggerer": null,
"label": "Quarantine device",
"detail": "",
"score": 0.3,
"pbid": 442301,
"model": "Antigena / Network / External Threat / Antigena Quarantine Example",
"modeluuid": "d92d6f73-gc1b-cg96-d4g8-df8a79f2a3cd",
"start": 1582038124000,
"expires": 1582041724000,
"blocked": true,
"agemail": false,
"aghost": false,
"active": true,
"cleared": false
},
...
],
"connections": [
{
"action": "quarantine",
"label": "Quarantine device",
"did": 316,
"direction": "outgoing",
"ip": "10.0.18.224",
"port": 443,
"timems": 1582033860000,
"time": "2020-02-18 13:51:00"
},
...
]
}
```
_Response is abbreviated._

###### Response Schema - includehistory=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
codeid numeric 4894 A unique id for the Darktrace RESPOND action.
```
```
did numeric 532 The “device id” of the device the action is applied
against.
```
```
ip string 10.0.18.224 The IP that the action is applied against.
```
```
action string quarantine The type of action being performed.
```
```
manual boolean FALSE
Whether the action was triggered manually by a
user.
```
```
triggerer
string/
array
```
```
If triggered manually, an object describing the
user who triggered the action. If triggered by
Darktrace RESPOND automatically, “null”.
```
```
triggerer.username string b.ash
Username of the user who triggered the manual
action. Only present for manual actions.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

triggerer.reason string

```
The “reason” provided by the user for the action
trigger, where the “reason” field is required by
deployment configuration. Only present for
manual actions.
```
history array

```
An array describing the history of the action
state. Action states include active, cleared,
extended, expired or reactivated.
```
history.family string NETWORK The Darktrace RESPOND action type.

history.username string hurstc The user that triggered the action state change.

history.action string cleared The new action state at the change.

history.reason string clear

```
The “reason” provided by the user for the action
state change, where the “reason” field is required
by deployment configuration.
```
history.time numeric 1657279887000 The time the action state was changed.

label string Quarantine device The readable label for the action being
performed.

detail string
Any additional detail about the action being
performed.

score numeric 0.3 The model breach score of the model breach
that triggered the Darktrace RESPOND action.

pbid numeric 449854
The model breach ‘policy breach id’ of the model
breach that triggered the action.

model string

```
Anomalous
File::Masqueraded
File Transfer
```
```
The name of the model that triggered the
Darktrace RESPOND action.
```
modeluuid string
ee88d329-6cdd-8dd3-
5baa-2e323g3fa833

```
The unique identifier for the model that triggered
the Darktrace RESPOND action.
```
start numeric (^1586190000000) The start time of the action in epoch time.
expires numeric 1586190000000 The expiry time of the action in epoch time.
blocked boolean FALSE
Whether the action blocked any matching
connections.
updated string 1585910000000
When the action was last updated. For example,
a user extending an action.
agemail boolean FALSE
Whether the action was triggered by Darktrace/
Email.
aghost boolean FALSE
Whether the action was triggered for Darktrace
RESPOND/Endpoint agents.
active boolean FALSE
Whether the action has been activated at some
point.
cleared boolean FALSE
Whether the action has been manually cleared
by an operator.


###### Example Response

```
[
{
"codeid": 4764,
"did": 316,
"ip": "10.0.18.224",
"action": "quarantine",
"manual": true,
"triggerer": {
"username": "c.hurst",
"reason": ""
},
"history": [
{
"family": "NETWORK",
"username": "c.hurst",
"action": "created",
"reason": "",
"time": 1662648025000
},
{
"family": "NETWORK",
"username": "b.ash",
"action": "reactivated (expired)",
"reason": "",
"time": 1664542011000
},
{
"family": "NETWORK",
"username": "b.ash",
"action": "cleared",
"reason": "",
"time": 1664548137000
}
],
"label": "Quarantine device",
"detail": "",
"score": 0.0,
"pbid": 442301,
"model": "",
"modeluuid": "",
"start": 1582038124000,
"expires": 1582041724000,
"blocked": true,
"agemail": false,
"aghost": false,
"active": true,
"cleared": false
},
...
]
```
_Response is abbreviated._


## /ANTIGENA/MANUAL

The /antigena/manual endpoint can be used to create manual Darktrace RESPOND/Network actions from Darktrace

Threat Visualizer 6.

This endpoint does not support GET requests. POST requests to this endpoint must be made with JSON in one of two

supported formats:

```
{"did":1234,"action":"quarantineIncoming","duration":60,"reason":"Test"}
{"did":1234,"action":"connection","duration":120,"reason":"","connections":
[{"src":"10.10.10.10","dst":"8.8.8.8","port":443}]}
```
To create actions, the system code for Darktrace RESPOND/Network inhibitors must be used. The following mapping can

be used to match inhibitors to action values:

```
DARKTRACE RESPOND/NETWORK INHIBITOR ACTION
```
```
Block Matching Connections connection
```
```
Enforce pattern of life pol
```
```
Enforce group pattern of life gpol
```
```
Quarantine device quarantine
```
```
Block all outgoing traffic quarantineOutgoing
```
```
Block all incoming traffic quarantineIncoming
```
If an action is successfully created, the system will respond with the codeid - a unique numeric ID for the action.

###### Request Type(s)

```
[POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
did numeric Identification number of a device modelled in the Darktrace system.
```
```
action string The type of action to be created. Supported types are listed above.
```
```
duration numeric The duration of the action in seconds.
```
```
reason string free text field to specify the action purpose.
```
```
connections array An array of connection pairs to block against. Only valid for the connection action type.
```
```
src string
```
```
An IP or hostname of an endpoint to block connections to/from. Must be specified in pairs with a dst key/
value. Only valid for the connection action type.
```
```
dst string
An IP or hostname of an endpoint to block connections to/from. Must be specified in pairs with a src key/
value. Only valid for the connection action type.
```
```
port numeric
Optional port for dst value. Must be specified with a dst key/value. Only valid for the connection action
type.
```

###### Notes

- The action reason and the username associated with the API token and will appear in the action history in the
    Threat Visualizer.

```
These values are also returned from /antigena as triggerer.username and triggerer.reason.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. POST to create a “Enforce group pattern of life” action against device with did=12 for 2 minutes with the
    reason “Test”:

```
https://[instance]/antigena/manual with body {"did":12,"action":"gpol","duration":
120,"reason":"Test"}
```
2. POST to create a “Block Matching Connections” action against a device with IP 10.10.10.10 and did=12 for
    connections to example.com (on port 443) and 8.8.8.8 for 10 minutes:

```
https://[instance]/antigena/manual with body {"did":12,"action":"connection","duration":
600,"reason":"","connections":[{"src":"10.10.10.10","dst":"8.8.8.8"},
{"src":"10.10.10.10","dst":"example.com","port":443}]}
```
###### Example Response

_Request: /antigena/manual with JSON body_

```
{
"code": 10170
}
```

## /ANTIGENA/SUMMARY

The /summary extension of the /antigena endpoint is a simple summary of active and pending Darktrace RESPOND

actions. If a time window is not specified, the request will return the state of actions now. If queried with a time window, the

endpoint will return information about active actions during that time window.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
###### Notes

- This endpoint only identified devices by their system id - did. This value can be used to query /devices for
    more information.
- Historic information about which actions were pending at a given point in time is not available from this
    endpoint. Pending action information is only returned if starttime/endtime parameters are not specified,
    and is only valid for the time of query.

```
This information should instead by sought from the /antigena endpoint using the includehistory
parameter to include full information about action state over time.
```
- Time parameters must always be specified in pairs.
- The endpoint will return information about all devices with active actions during the timeframe - information
    about when those specific actions were active, and for how long, is not included.

```
It is therefore recommended that small time periods are queried. For more complex queries, the /antigena
endpoint is recommended.
```
- A device may have more than one active or pending against it - the number of actions may therefore not match
    the total number of impacted devices.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET info about active and pending Darktrace RESPOND Actions at this moment:

```
https://[instance]/antigena/summary
```
2. GET info about devices with active Darktrace RESPOND actions against them between 00:00 and 00:01 on
    November 1st 2022:

```
https://[instance]/antigena/summary?startTime=1667260800000&endTime=1667260860000
```

###### Example Response

_Request: /antigena/summary_

```
{
"pendingCount": 8,
"activeCount": 29,
"pendingActionDevices": [
11
],
"activeActionDevices": [
123,
551,
202,
6,
1301
]
}
```

## /ANTIGENA/SUMMARY RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
pendingCount numeric 4
```
```
The number of pending Darktrace RESPOND
actions at the time of query. Will always be 0 if
time parameters are specified as information
about historically pending actions is not
available.
```
```
activeCount numeric 3
```
```
The number of active Darktrace RESPOND
actions at the time of query or across the queried
time period.
```
```
pendingActionDevices array 36599
An array of did values - unique device
identifiers - for devices with pending actions.
```
```
activeActionDevices array 551
An array of did values - unique device
identifiers - for devices with active actions.
```
###### Example Response

```
{
"pendingCount": 8,
"activeCount": 29,
"pendingActionDevices": [
11
],
"activeActionDevices": [
123,
551,
202,
6,
1301
]
}
```

## /COMPONENTS

Components are segments of model logic that are evaluated; the /components endpoint returns a list of all component

parts of defined models, identified by their cid. The cid is referenced in the data attribute for model breaches.

A component is a series of filters which an event or connection is assessed against as part of a larger model. The first part of

the component describes the combinations of filters that must occur for the component to fire, where each filter is

identified by a capital letter. The second part of the response describes the logic of each filter. Filters with an ID like “A” or “F”

are referenced in the model logic, whereas filters with an ID like “d1” or “d4” are display filters - filters that are displayed in the

UI when a breach occurs and have no impact on the component logic.

For certain filtertypes, the returned argument is a numeric value that corresponds to an enumerated type. See

( _/enums_ ) for a full list.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET information about all model components:

```
https://[instance]/components
```
2. GET the component with cid: 8977:

```
https://[instance]/components/8977
```

###### Example Response

_Request: /components/8977_

```
{
"cid": 8977,
"chid": 15524,
"mlid": 33,
"threshold": 5242880,
"interval": 3600,
"logic": {
"data": {
"left": "A",
"operator": "AND",
"right": {
"left": "B",
"operator": "AND",
"right": {
"left": "C",
"operator": "AND",
"right": {
"left": "D",
"operator": "AND",
"right": "E"
}
}
}
},
"version": "v0.1"
},
"filters": [{
"id": "A",
"cfid": 59205,
"cfhid": 99603,
"filtertype": "Direction",
"comparator": "is",
"arguments": {
"value": "out"
}
},
{
"id": "B",
"cfid": 59206,
"cfhid": 99604,
"filtertype": "Tagged internal source",
"comparator": "does not have tag",
"arguments": {
"value": 38
}
} {
"id": "C",
"cfid": 59207,
"cfhid": 99605,
"filtertype": "Internal source device type",
"comparator": "is not",
"arguments": {
"value": "9"
}
},
{
"id": "D",
"cfid": 59208,
"cfhid": 99606,
"filtertype": "Internal source device type",
"comparator": "is not",
```
_continued..._


"arguments": {
"value": "13"
}
},
{
"id": "E",
"cfid": 59209,
"cfhid": 99607,
"filtertype": "Connection hostname",
"comparator": "matches regular expression",
"arguments": {
"value": "^(.+\\.)?dropbox.com$"
}
},
{
"id": "d1",
"cfid": 59210,
"cfhid": 99608,
"filtertype": "Connection hostname",
"comparator": "display",
"arguments": {}
}
],
"active": true
}


## /COMPONENTS RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
cid numeric 4650 The “component id”. A unique identifier.
```
```
chid numeric 6664
The “component history id”. Increments when
the component is edited.
```
```
mlid numeric 232 The ‘metric logic id’ for the metric used in the
component.
```
```
threshold numeric 1
The threshold value that the size must exceed for
the component to breach.
```
```
interval numeric 7200 The timeframe in seconds within which the
threshold must be satisfied.
```
```
logic object An object describing the component logic.
```
```
logic.data object
```
```
An object representing the logical relationship
between component filters. Each filter is given an
alphabetical reference and the contents of this
object describe the relationship between those
objects.
```
```
logic.data.left object
Objects on the left will be compared with the
object on the right using the specified operator.
```
```
logic.data.operator string OR A logical operator to compare filters with.
```
```
logic.data.right object
Objects on the left will be compared with the
object on the right using the specified operator.
```
```
logic.version string v0.1 The version of the component logic.
```
```
filters array The filters that comprise the component.
```
```
filters.id string A
```
```
A filter that is used in the component logic. All
filters are given alphabetical identifiers. Display
filters - those that appear in the breach
notification - can be identified by a lowercase ‘d’
and a numeral.
```
```
filters.cfid numeric 34019
The ‘component filter id’. A unique identifier for
the filter as part of a the component.
```
```
filters.cfhid numeric 46783
The “component filter history id”. Increments
when the filter is edited.
```
```
filters.filtertype string Message
```
```
The filtertype that is used in the filter. A full list of
filtertypes can be found on the /filtertypes
endpoint.
```
```
filters.comparator string
matches regular
expression
```
```
The comparator. A full list of comparators
available for each filtertype can be found on the /
filtertypes endpoint.
```
```
filters.arguments object An object containing the value to be compared.
Display filters will have an empty object.
```
```
filters.arguments.value string (Anomalous Compromise
```
```
active boolean TRUE Whether the component is currently active as
part of a model.
```

###### Example Response

_Request: /components/8977_

```
{
"cid": 8977,
"chid": 15524,
"mlid": 33,
"threshold": 5242880,
"interval": 3600,
"logic": {
"data": {
"left": "A",
"operator": "AND",
"right": {
"left": "B",
"operator": "AND",
"right": {
"left": "C",
"operator": "AND",
"right": {
"left": "D",
"operator": "AND",
"right": "E"
}
}
}
},
"version": "v0.1"
},
"filters": [
{
"id": "A",
"cfid": 59205,
"cfhid": 99603,
"filtertype": "Direction",
"comparator": "is",
"arguments": {
"value": "out"
}
},
{
"id": "B",
"cfid": 59206,
"cfhid": 99604,
"filtertype": "Tagged internal source",
"comparator": "does not have tag",
"arguments": {
"value": 38
}
} {
"id": "C",
"cfid": 59207,
"cfhid": 99605,
"filtertype": "Internal source device type",
"comparator": "is not",
"arguments": {
"value": "9"
}
},
{
"id": "D",
"cfid": 59208,
"cfhid": 99606,
"filtertype": "Internal source device type",
```
_continued..._


"comparator": "is not",
"arguments": {
"value": "13"
}
},
{
"id": "E",
"cfid": 59209,
"cfhid": 99607,
"filtertype": "Connection hostname",
"comparator": "matches regular expression",
"arguments": {
"value": "^(.+\\.)?dropbox.com$"
}
},
{
"id": "d1",
"cfid": 59210,
"cfhid": 99608,
"filtertype": "Connection hostname",
"comparator": "display",
"arguments": {}
}
],
"active": true
}


## /CVES

_Please note, this endpoint is only available for Darktrace/OT environments._

The /cves endpoint can be used to retrieve information on device CVEs created by the Darktrace/OT ICS Vulnerability

Tracker integration programmatically.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
did numeric Identification number of a device modelled in the Darktrace system.
```
```
fulldevicedetails boolean
Returns the full device detail objects for all devices referenced by data in an API response. Use of this
parameter will alter the JSON structure of the API response for certain calls.
```
###### Notes

- fulldevicedetails=true will add a devices object with full details of the devices referenced in the results
array.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET a list of all the CVEs associated with devices in the network:

```
https://[instance]/cves
```
2. GET a list of all the CVEs associated with the device with device ID 12 and include detailed information about
    the device:

```
https://[instance]/cves?did=12&fulldevicedetails=true
```

###### Example Response

_Request: /cves_

```
{
"results": [
{
"did": 12,
"platform mappings (CPEs)": [
{
"vendor": "rockwellautomation",
"product": "compactlogix_1769-l16er-bb1b",
"version": "All ",
"patch": "",
"cves": [
{
"LAST_MODIFIED_DATE": "2018-05-20",
"CVE_ID": "CVE-2016-2279",
"BASE_SEVERITY": "Medium",
"DESCRIPTION": "Cross-site scripting (XSS) vulnerability in the web server in
Rockwell Automation Allen-Bradley CompactLogix 1769-L* before 28.011+ allows remote
attackers to inject arbitrary web script or HTML via unspecified vectors."
}
],
"applies to": [
"CVE-2016-2279"
]
}
],
"cves": [
{
"LAST_MODIFIED_DATE": "2018-05-20",
"CVE_ID": "CVE-2016-2279",
"BASE_SEVERITY": "Medium",
"DESCRIPTION": "Cross-site scripting (XSS) vulnerability in the web server in
Rockwell Automation Allen-Bradley CompactLogix 1769-L* before 28.011+ allows remote
attackers to inject arbitrary web script or HTML via unspecified vectors."
}
]
}
...
]
}
```

## /CVES RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
results array
An array of devices and the CVEs associated with
those devices.
```
```
results.did numeric 186
A unique identifier of a device in the Darktrace
system.
```
```
results.platform mappings (CPEs) array
```
```
An array of CVEs matched to the device, grouped
by CPE. Some CVEs may be matched by multiple
corresponding CPEs.
```
```
results.platform mappings
(CPEs).vendor
string rockwellautomation
The vendor of the device that the CPE
corresponds to.
```
```
results.platform mappings
(CPEs).product
string
compactlogix_1769-
l16er-bb1b
```
```
The product (CPE) that has been matched.
Some CVEs may be matched by product and
firmware version (CPE
“bmxp342020h_firmware”) while other CVEs
apply to the whole PLC family in general (CPE
“bmxp342020”)
```
```
results.platform mappings
(CPEs).version
string All The product version the CVEs are applicable to.
```
```
results.platform mappings (CPEs).patch string
```
```
To mitigate, update
to a version
greater than 2.2
```
```
If a patch is available for the CVE, what software
version is required to mitigate.
```
```
results.platform mappings (CPEs).cves array
An array of the specific CVEs matched to that
device by CPE.
```
```
results.platform mappings
(CPEs).cves.LAST_MODIFIED_DATE string
09/10/2019 The date that the CVE was last updated.
```
```
results.platform mappings
(CPEs).cves.CVE_ID
string CVE-2016-2279
The ID of a CVE matched to the device by this
CPE.
```
```
results.platform mappings
(CPEs).cves.BASE_SEVERITY string
Medium The base severity of the CVE, as denoted by
NIST.
```
```
results.platform mappings
(CPEs).cves.DESCRIPTION
string
```
```
Cross-site
scripting (XSS)
vulnerability in
the web server in
Rockwell Automation
Allen-Bradley
CompactLogix 1769-
L* before 28.011+
allows remote
attackers to inject
arbitrary web
script or HTML via
unspecified
vectors.
```
```
The description of the CVE, as provided by NIST.
```
```
results.platform mappings
(CPEs).applies to
array
An array of the CVE ID for all CVEs matched by
this CPE.
```
```
results.cves array An array of all CVEs that were successfully
matched to the device.
```
```
results.cves.LAST_MODIFIED_DATE string 2019-10-09 The date that the CVE was last updated.
```

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
results.cves.CVE_ID string CVE-2016-2279
The ID of a CVE matched to the device by this
CPE.
```
```
results.cves.BASE_SEVERITY string Medium The base severity of the CVE, as denoted by
NIST.
```
```
results.cves.DESCRIPTION string
```
```
Cross-site
scripting (XSS)
vulnerability in
the web server in
Rockwell Automation
Allen-Bradley
CompactLogix 1769-
L* before 28.011+
allows remote
attackers to inject
arbitrary web
script or HTML via
unspecified
vectors.
```
```
The description of the CVE, as provided by NIST.
```
###### Example Response

_Request: /cves_

```
{
"results": [
{
"did": 123,
"platform mappings (CPEs)": [
{
"vendor": "rockwellautomation",
"product": "compactlogix_1769-l16er-bb1b",
"version": "All ",
"patch": "",
"cves": [
{
"LAST_MODIFIED_DATE": "2018-05-20",
"CVE_ID": "CVE-2016-2279",
"BASE_SEVERITY": "Medium",
"DESCRIPTION": "Cross-site scripting (XSS) vulnerability in the web server in
Rockwell Automation Allen-Bradley CompactLogix 1769-L* before 28.011+ allows remote
attackers to inject arbitrary web script or HTML via unspecified vectors."
}
],
"applies to": [
"CVE-2016-2279"
]
}
],
"cves": [
{
"LAST_MODIFIED_DATE": "2018-05-20",
"CVE_ID": "CVE-2016-2279",
"BASE_SEVERITY": "Medium",
"DESCRIPTION": "Cross-site scripting (XSS) vulnerability in the web server in
Rockwell Automation Allen-Bradley CompactLogix 1769-L* before 28.011+ allows remote
attackers to inject arbitrary web script or HTML via unspecified vectors."
}
]
}
...
]
}
```
_Response is abbreviated._


## /DETAILS

The /details endpoint returns a time-sorted list of connections and events for a device or entity (such as a SaaS

credential). The request requires either a device (did), a model breach ID (pbid), a message field value (msg), or the

```
blockedconnections parameter.
```
This advanced endpoint can be used to gather detailed information about a specific device and its connections for

investigation or monitoring purposes. It is primarily used to populate log elements such as device event logs, model breach

event logs, metric logs and other chronological event log interfaces.

###### Darktrace RESPOND/Network Actions

The blockedconnections parameter is used to filter connection events to those that Darktrace RESPOND/Network

attempted to action. Connections which triggered the creation and sending of a RESPOND RST will contain the

```
antigenablocked key. At the time the action is taken, "antigenablocked": "true" is added to the connection entry.
```
As this is performed at action time, Darktrace is unable to ascertain if the action was successful until the connection has

demonstrably ended - this state therefore represents an attempt to block only.

If, after the action, Darktrace detects that the connection continued and the action was unsuccessful,

```
"antigenablocked": "true" is updated to "antigenablocked": "false". This is only possible where Darktrace can
```
clearly ascertain that the action was unsuccessful, so there may be scenarios such as very short-lived connections, where

this is impossible to derive. This field value change is performed retrospectively; if data is requested at the time of

connection, all entries where blocks where attempted will show "antigenablocked": "true". A short delay is therefore

recommended when ascertaining whether an action failed to end a connection.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
applicationprotocol string
This filter can be used to filter the returned data by application protocol. See /enums for the list of
application protocols.
```
```
count numeric Specifies the maximum number of items to return.
```
```
ddid numeric Identification number of a destination device modelled in the Darktrace system to restrict data to.
```
```
deduplicate boolean Display only one equivalent connection per hour.
```
```
destinationport numeric This filter can be used to filter the returned data by destination port.
```
```
did numeric Identification number of a device modelled in the Darktrace system.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
eventtype string
```
```
Specifies an type of event to return details for. Possible values are connection, unusualconnection,
newconnection, notice, devicehistory, modelbreach.
```
```
externalhostname string Specifies an external hostname to return details for.
```
```
from string Start time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
fulldevicedetails boolean
```
```
Returns the full device detail objects for all devices referenced by data in an API response. Use of
this parameter will alter the JSON structure of the API response for certain calls.
```
```
intext string
This filter can be used to filter the returned data to that which interacts with external sources and
destinations, or is restricted to internal. Valid values or internal and external.
```
```
msg string
```

```
PARAMETER TYPE DESCRIPTION
```
```
Specifies the value of the message field in notice events to return details for. Typically used to
specify user credential strings.
```
```
odid numeric
Other Device ID - Identification number of a device modelled in the Darktrace system to restrict
data to. Typically used with ddid and odid to specify device pairs regardless of source/destination.
```
```
pbid numeric Only return the model breach with the specified ID.
```
```
port numeric This filter can be used to filter the returned data by source or destination port.
```
```
protocol string This filter can be used to filter the returned data by IP protocol. See /enums for the list of protocols.
```
```
sourceport numeric This filter can be used to filter the returned data by source port.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
to string End time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
uid string Specifies a connection UID to return.
```
```
responsedata string
When given the name of a top-level field or object, restricts the returned JSON to only that field or
object.
```
```
blockedconnections string
Filters the results to connections Darktrace RESPOND attempted to action. Valid values are all,
failed,true.
```
###### Notes

- Time parameters must always be specified in pairs.
- If the from or starttime parameter is used in a request, the count parameter must not be used.
- The default eventtype is connection.
- User devices covered by Darktrace modules do not return connection information. All Darktrace/Apps, Cloud
    and Zero Trust user activity is eventtype=notice
- To review all connections Darktrace RESPOND/Network attempted to action - including those that failed - use
    blockedconnections=all. For those that failed only, blockedconnections=failed. Finally, for those
    where an attempt was performed use blockedconnections=true.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET the first 100 unusual connections for device with did=1:

```
https://[instance]/details?did=1&count=100&eventtype=unusualconnection
```
2. GET all connections from December 1st 2020 (12:00:00) to December 2nd 2020 (00:00:00) for device with
    did=1:

```
https://[instance]/details?did=1&from=2020-12-01T12:00:00&to=2020-12-02
```

###### Example Response

_Request: /details?did=1&count=100&eventtype=notice_

```
{
"time": "2020-04-06 16:50:50",
"timems": 1586191850000,
"action": "notice",
"eventType": "notice",
"nid": 8180165,
"uid": "ZJW3xVFQtEykPRPy",
"direction": "in",
"mlid": 339,
"type": "SSH::Heuristic_Login_Success",
"msg": "10.12.14.2 logged in to 192.168.72.4 successfully via SSH.",
"destinationPort": 22,
"details": "",
"sourceDevice": {
"id": -6,
"did": -6,
"ip": "10.12.14.2",
"sid": -6,
"time": "1528807047000",
"devicelabel": "Internal Traffic",
"typename": "networkrange",
"typelabel": "Network Range"
},
"destinationDevice": {
"id": 532,
"did": 532,
"macaddress": "93:gb:28:g1:fc:g1",
"ip": "192.168.72.4",
"ips": [
{
"ip": "192.168.72.4",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 12
}
],
"sid": 12,
"hostname": "workstation-local-82",
"time": "1528807077000",
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
},
"source": "Internal Traffic",
"destination": "workstation-local-82",
}
...
```
_Response is abbreviated._


## /DETAILS RESPONSE SCHEMA

Note: The /details endpoint response has a large number of variations. All major eventtypes are covered in this schema,

but the response will differ by protocol, model or platform (e.g., SaaS or ICS notices). Whether a proxy has been detected will

also affect all connection-type events.

#### Response Schema - eventtype=connection

Please note, the proxy fields included in this schema may appear in any connection-type event response.

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time string 2020-04-15 08:00:00
The timestamp when the record was created in
epoch time.
```
```
timems numeric 1586937600000
The timestamp when the record was created in
readable format.
```
```
action string connection
The action associated with the device that has
generated this record.
```
```
eventType string connection The event type.
```
```
uid string VGBIDXXfTVFPww1d
```
```
A unique identifier for the connection - can be
entered into Advanced Search or the omnisearch
bar to locate associated connections.
```
```
status string ongoing
```
```
Can contain “failed” for failed connections or
“ongoing” for continued connections. Completed
connections will not return this field.
```
```
proxyPort numeric 3128 If a proxy was detected - the port used.
```
```
sdid numeric 29
```
```
The device id of the source device. Will only
appear if the source device has been observed
by Darktrace.
```
```
ddid numeric 3765
```
```
The device id of the destination device. Will only
appear if the destination device has been
observed by Darktrace.
```
```
port numeric 443
In the majority of cases, the destination port
connected to.
```
```
sourcePort numeric 22 The port connected from on the source device.
```
```
destinationPort numeric 443 The port connected to on the destination device.
```
```
direction string out The direction of the connection.
```
```
applicationprotocol string HTTPS The application protocol used in the connection
as derived by Darktrace.
```
```
protocol string TCP
The network protocol used for the connection as
derived by Darktrace.
```
```
sourceDevice object
```
```
An object describing the source device. There
are multiple formats this may take, please see the
separate sourceDevice object schemas.
```
```
destinationDevice object
```
```
An object describing the destination device.
There are multiple formats this may take, please
see the separate destinationDevice object
schemas.
```
```
proxyDevice object
If a proxy was detected - an object describing the
proxy.
```

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
proxyDevice.ip string 10.0.18.224 If a proxy was detected - the proxy IP.
```
```
source string ws173 The hostname or IP of the source device.
```
```
destination string google.com The hostname or IP of the destination device.
```
```
proxy string 192.168.72.4 If a proxy was detected - the proxy IP.
```
###### Example Response

```
{
"time": "2020-04-20 09:44:35",
"timems": 1587375875452,
"action": "connection",
"eventType": "connection",
"uid": "VGBIDXXfTVFPww1d",
"status": "failed",
"sdid": 76,
"ddid": 532,
"port": 6514,
"sourcePort": 55498,
"destinationPort": 6514,
"direction": "out",
"applicationprotocol": "Unknown",
"protocol": "TCP",
"sourceDevice": {
"id": 76,
"did": 76,
"macaddress": "2g:d8:a2:a8:54:c6",
"ip": "10.12.14.2",
"ips": [
{
"ip": "10.12.14.2",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 15
}
],
"sid": 15,
"time": "1528807103000",
"os": "Linux 3.11 and newer",
"devicelabel": "Pool Laptop 6",
"typename": "desktop",
"typelabel": "Desktop"
},
"destinationDevice": {
"id": 532,
"did": 532,
"ip": "192.168.72.4",
"sid": 12,
"hostname": "workstation-local-82",
"time": "1528807077000",
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
},
"source": "10.12.14.2",
"destination": "workstation-local-82",
}
```

#### Response Schema - eventtype=newconnection

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time string 2020-03-15 09:52:11
The timestamp when the record was created in
epoch time.
```
```
timems numeric 1584265931000
The timestamp when the record was created in
readable format.
```
```
action string connection
The action associated with the device that has
generated this record.
```
```
eventType string connection The event type.
```
```
uid string ZJW3xVFQtEykPRPy
```
```
A unique identifier for the connection - can be
entered into Advanced Search or the omnisearch
bar to locate associated connections.
```
```
status string ongoing
```
```
Can contain “failed” for failed connections or
“ongoing” for continued connections. Completed
connections will not return this field.
```
```
sdid numeric 446
```
```
The device id of the source device. Will only
appear if the source device has been observed
by Darktrace.
```
```
ddid numeric 239
```
```
The device id of the destination device. Will only
appear if the destination device has been
observed by Darktrace.
```
```
port numeric 80
In the majority of cases, the destination port
connected to.
```
```
sourcePort numeric 80 The port connected from on the source device.
```
```
destinationPort numeric 80 The port connected to on the destination device.
```
```
info string
```
```
A new connection
internally on port
80
```
```
A message describing the event.
```
```
direction string out The direction of the connection.
```
```
applicationprotocol string DHCP The application protocol used in the connection
as derived by Darktrace.
```
```
protocol string UDP
The network protocol used for the connection as
derived by Darktrace.
```
```
sourceDevice object
```
```
An object describing the source device. There
are multiple formats this may take, please see the
separate sourceDevice object schemas.
```
```
destinationDevice object
```
```
An object describing the destination device.
There are multiple formats this may take, please
see the separate destinationDevice object
schemas.
```
```
source string D7S45E001 The hostname or IP of the source device.
```
```
destination string sarah-desktop-12 The hostname or IP of the destination device.
```

###### Example Response

```
[
{
"time": "2020-04-16 10:31:01",
"timems": 1587033061581,
"action": "connection",
"eventType": "connection",
"uid": "T6X3VCrEXAm4KJeZ",
"sdid": 76,
"ddid": 532,
"port": 67,
"sourcePort": 68,
"destinationPort": 67,
"info": "A new connection internally on port 67",
"direction": "out",
"applicationprotocol": "DHCP",
"protocol": "UDP",
"sourceDevice": {
"id": 76,
"did": 76,
"macaddress": "2g:d8:a2:a8:54:c6",
"ip": "10.12.14.2",
"ips": [
{
"ip": "10.12.14.2",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 15
}
],
"sid": 15,
"time": "1528807103000",
"os": "Linux 3.11 and newer",
"devicelabel": "Pool Laptop 6",
"typename": "desktop",
"typelabel": "Desktop"
},
"destinationDevice": {
"id": 532,
"did": 532,
"ip": "192.168.72.4",
"sid": 12,
"hostname": "workstation-local-82",
"time": "1528807077000",
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
},
"source": "10.12.14.2",
"destination": "workstation-local-82",
}
]
```

#### Response Schema - eventtype=unusualconnection

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time string 2020-03-15 09:52:11
The timestamp when the record was created in
epoch time.
```
```
timems numeric 1584265931000
The timestamp when the record was created in
readable format.
```
```
action string connection
The action associated with the device that has
generated this record.
```
```
eventType string connection The event type.
```
```
uid string VGBIDXXfTVFPww1d
```
```
A unique identifier for the connection - can be
entered into Advanced Search or the omnisearch
bar to locate associated connections.
```
```
status string ongoing
```
```
Can contain “failed” for failed connections or
“ongoing” for continued connections. Completed
connections will not return this field.
```
```
sdid numeric 239
```
```
The device id of the source device. Will only
appear if the source device has been observed
by Darktrace.
```
```
ddid numeric 772
```
```
The device id of the destination device. Will only
appear if the destination device has been
observed by Darktrace.
```
```
port numeric 443
In the majority of cases, the destination port
connected to.
```
```
sourcePort numeric 444 The port connected from on the source device.
```
```
destinationPort numeric 443 The port connected to on the destination device.
```
```
info string
```
```
An unusual
connection compared
with similar
devices internally
on
port 443
```
```
A message describing the event.
```
```
direction string out The direction of the connection.
```
```
applicationprotocol string HTTPS
The application protocol used in the connection
as derived by Darktrace.
```
```
protocol string TCP
The network protocol used for the connection as
derived by Darktrace.
```
```
sourceDevice object
```
```
An object describing the source device. There
are multiple formats this may take, please see the
separate sourceDevice object schemas.
```
```
destinationDevice object
```
```
An object describing the destination device.
There are multiple formats this may take, please
see the separate destinationDevice object
schemas.
```
```
source string
workstation-
local-82
The hostname or IP of the source device.
```
```
destination string ws83 The hostname or IP of the destination device.
```

###### Example Response

```
{
"time": "2020-04-15 07:38:05",
"timems": 1586936285538,
"action": "connection",
"eventType": "connection",
"uid": "K18S2Iqiu7Wz1jaN",
"sdid": 76,
"ddid": 5487,
"port": 22,
"sourcePort": 49568,
"destinationPort": 22,
"info": "A recent increase in incoming data volume from 10.12.14.2 port 22",
"direction": "out",
"applicationprotocol": "SSH",
"protocol": "TCP",
"sourceDevice": {
"id": 76,
"did": 76,
"macaddress": "2g:d8:a2:a8:54:c6",
"ip": "10.12.14.2",
"ips": [
{
"ip": "10.12.14.2",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 15
}
],
"sid": 15,
"time": "1528807103000",
"os": "Linux 3.11 and newer",
"devicelabel": "Pool Laptop 6",
"typename": "desktop",
"typelabel": "Desktop"
}
```

#### Response Schema - eventtype=notice

###### Generic Notice

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time string 2019-06-12 14:00:00
The timestamp when the record was created in
epoch time.
```
```
timems numeric 1528812000000
The timestamp when the record was created in
readable format.
```
```
action string notice
The action associated with the device that has
generated this record.
```
```
eventType string notice The event type.
```
```
nid numeric 8180398 A unique identifier for the notice.
```
```
uid string VGBIDXXfTVFPww1d
```
```
A unique identifier of the notice which can be
used to locate the notice and related
connections in Advanced Search.
```
```
direction string out
The direction of the connection that triggered
the notice.
```
```
mlid numeric 339
The metric id of the corresponding system
metric (where applicable) for this notice.
```
```
type string
SSH::Heuristic_Logi
n_Success
```
```
The notice type. A list of notices derived during
processing (without the “DT” prefix) can be found
in the Advanced Search documentation.
```
```
msg string
```
```
10.12.14.2 logged
in to 10.0.18.224
successfully via
SSH.
```
```
A human readable description of the notice.
```
```
destinationPort numeric 22 The destination port used by the device.
```
```
details string Details may be an object or a string describing
further information about the event.
```
```
sourceDevice object
```
```
An object describing the source device. There
are multiple formats this may take, please see the
separate sourceDevice object schemas.
```
```
destinationDevice object
```
```
An object describing the destination device.
There are multiple formats this may take, please
see the separate destinationDevice object
schemas.
```
```
source string sarah-desktop-12 The hostname or IP of the source device.
```
```
destination string 10.0.18.224 The hostname or IP of the destination device.
```

###### Example Response - details as a String

```
{
"time": "2020-04-06 16:50:50",
"timems": 1586191850000,
"action": "notice",
"eventType": "notice",
"nid": 8180165,
"uid": "ZJW3xVFQtEykPRPy",
"direction": "in",
"mlid": 339,
"type": "SSH::Heuristic_Login_Success",
"msg": "10.12.14.2 logged in to 192.168.72.4 successfully via SSH.",
"destinationPort": 22,
"details": "",
"sourceDevice": {
"id": -6,
"did": -6,
"ip": "10.12.14.2",
"sid": -6,
"time": "1528807047000",
"devicelabel": "Internal Traffic",
"typename": "networkrange",
"typelabel": "Network Range"
},
"destinationDevice": {
"id": 532,
"did": 532,
"macaddress": "93:gb:28:g1:fc:g1",
"ip": "192.168.72.4",
"ips": [
{
"ip": "192.168.72.4",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 12
}
],
"sid": 12,
"hostname": "workstation-local-82",
"time": "1528807077000",
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
},
"source": "Internal Traffic",
"destination": "workstation-local-82",
}
```

###### Example Response - details as an Object

```
{
"time": "2021-06-17 10:59:05",
"timems": 1623927545000,
"action": "notice",
"eventType": "notice",
"nid": 8180165,
"uid": "ZJW3xVFQtEykPRPy",
"direction": "in",
"mlid": 304,
"type": "Saas::Login",
"dpcode": "9223415003931661771",
"dpcodetitle": "SaaS Login on Saas",
"msg": "event=userloggedin,user=benjamin.ash@holdingsinc.com",
"detail": {
"account_id": "0",
"account_name": "Example",
"action": "Login",
"actor": "benjamin.ash@holdingsinc.com",
"event": "UserLoggedIn",
"event_id": "616e6f74-6865-722d-6578-616d706c652d",
"office365_application_id": "6578616d-706c-652d-7374-72696e672d2d",
"office365_associated_apps": "Azure Portal",
"service": "Office365",
"service_product": "Windows Azure Service Management API",
"software": "Chrome 91.0.4472",
"status_code": 0
},
"sourceDevice": {
"longitude": 0.0,
"latitude": 52.0,
"city": "Cambridge",
"country": "United Kingdom",
"countrycode": "GB",
"region": "Europe",
"ip": "104.20.203.23",
"ippopularity": "0"
},
"destinationDevice": {
"id": 123,
"did": 123,
"ip": "",
"sid": -9,
"hostname": "SaaS::Office365: benjamin.ash@holdingsinc.com",
"time": "1574700328000",
"typename": "saasprovider",
"typelabel": "SaaS Provider"
},
"source": "104.20.203.23",
"destination": "SaaS::Office365: benjamin.ash@holdingsinc.com",
"antigena-email": false
}
```

###### Model Breach Notice

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time string 2020-03-15 09:52:11
The timestamp when the record was created in
epoch time.
```
```
timems numeric 1584265931000 The timestamp when the record was created in
readable format.
```
```
action string notice
The action associated with the device that has
generated this record.
```
```
nuid string MMOiOUDO0EwgWYBW
```
```
Notices generated outside of DPI - those with
the “DT” prefix - will have a “notice unique
identifier” instead of a “uid”. This can be entered
into the omnisearch bar to locate the event.
```
```
eventType string notice The event type.
```
nid numeric (^8125619) A unique identifier for the notice.
uid string
Notices generated outside of DPI - those with
the “DT” prefix - do not have a uid value.
direction string out The direction of the connection that triggered
the notice.
mlid numeric 232
The metric id of the corresponding system
metric (where applicable) for this notice.
type string DT::ModelBreach
The notice type. A list of notices derived during
processing (without the “DT” prefix) can be found
in the Advanced Search documentation.
msg string
Anomalous File /
Masqueraded File
Transfer
A human readable description of the notice.
destinationPort numeric 80 The destination port used by the device.
size numeric 38 The model breach score (out of 100).
detail object
Details may be an object or a string describing
further information about the event. For model
breaches, it will contain information about the
model.
detail.pid numeric 486 The “policy id” of the breached model.
detail.pbid numeric (^315602) The “policy breach id” of the breached model.
detail.tags array Test An array describing tags applied to the model.
sourceDevice object
An object describing the source device. There
are multiple formats this may take, please see the
separate sourceDevice object schemas.
destinationDevice object
An object describing the destination device.
There are multiple formats this may take, please
see the separate destinationDevice object
schemas.
source string ws83 The hostname or IP of the source device.
destination string
workstation-
local-82
The hostname or IP of the destination device.
antigena-email boolean FALSE
Whether a hostname present in the notice has
been observed by Darktrace/Email in email
traffic.


###### Example Response

```
{
"time": "2020-04-07 02:55:59",
"timems": 1586228159000,
"action": "notice",
"nuid": "RLW8FVxUNkkA5Kfa",
"eventType": "notice",
"nid": 8186895,
"uid": "",
"direction": "out",
"mlid": 232,
"type": "DT::ModelBreach",
"msg": "Anomalous Connection / Multiple Failed Connections to Rare Endpoint",
"destinationPort": 80,
"size": 41,
"detail": {
"pid": 486,
"pbid": 315955,
"tags": [
"Admin",
"Test"
]
},
"sourceDevice": {
"id": 532,
"did": 532,
"macaddress": "93:gb:28:g1:fc:g1",
"ip": "192.168.72.4",
"ips": [
{
"ip": "192.168.72.4",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 12
}
],
"sid": 12,
"hostname": "workstation-local-82",
"time": "1528807077000",
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
},
"destinationDevice": {
"longitude": -122.075,
"latitude": 37.404,
"city": "Mountain View",
"country": "United States",
"countrycode": "US",
"asn": "AS15169 Google LLC",
"region": "North America",
"ip": "216.58.204.46",
"hostname": "google.com",
"hostnamepopularity": "100",
"domain": "google.com",
"domainpopularity": "100",
"ippopularity": "10"
},
"source": "workstation-local-82",
"destination": "google.com",
}
```

###### Similar Devices Notice

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time string 2020-04-15 08:04:41
The timestamp when the record was created in
epoch time.
```
```
timems numeric 1586937881000 The timestamp when the record was created in
readable format.
```
```
action string notice
The action associated with the device that has
generated this record.
```
```
nuid string IYA9RXjOCAGwwLYA
```
```
Notices generated outside of DPI - those with
the “DT” prefix - will have a “notice unique
identifier” instead of a “uid”. This can be entered
into the omnisearch bar to locate the event.
```
```
eventType string notice The event type.
```
nid numeric (^8105707) A unique identifier for the notice.
uid string
Notices generated outside of DPI - those with
the “DT” prefix - do not have a uid value.
mlid numeric 212 The metric id of the corresponding system
metric (where applicable) for this notice.
type string
DT::DeviceClusterCh
ange
The notice type. A list of notices derived during
processing (without the “DT” prefix) can be found
in the Advanced Search documentation.
similardevices string
BGF5ACF39CCB47FFF24
4A96293E2AC7FBBFB61
165AEF9F4911397CG89
4AA2F1381E3924367EF
G2A6F8G527F3B57194E
7
A token which can be provided to the /
similardevices endpoint to see the old and new
list of devices.
msg string
4 different similar
devices from a list
of 30
A human readable description of the notice.
size numeric 12 A system field.
details string
Details may be an object or a string describing
further information about the event. For model
breaches, it will contain information about the
model.
sourceDevice object
An object describing the source device. There
are multiple formats this may take, please see the
separate sourceDevice object schemas.
source string sarah-desktop-12 The hostname or IP of the source device.


###### Example Response

```
{
"time": "2020-04-06 13:39:10",
"timems": 1586180350000,
"action": "notice",
"nuid": "IYA9RXjOCAGwwLYA",
"eventType": "notice",
"nid": 8177463,
"uid": "",
"mlid": 212,
"type": "DT::DeviceClusterChange",
"similardevices":
"BGF5ACF39CCB47FFF244A96293E2AC7FBBFB61165AEF9F4911397CG894AA2F1381E3924367EFG2A6F8G527F3B5719
4E7",
"msg": "6 different similar devices from a list of 30",
"size": 17,
"details": "",
"sourceDevice": {
"id": 532,
"did": 532,
"macaddress": "93:gb:28:g1:fc:g1",
"ip": "192.168.72.4",
"ips": [
{
"ip": "192.168.72.4",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 12
}
],
"sid": 12,
"hostname": "workstation-local-82",
"time": "1528807077000",
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
},
"source": "workstation-local-82"
}
```

#### Response Schema - blockedconnections=all

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time string 2023-12-11 16:51:08
The timestamp when the record was created in
readable format.
```
```
timems numeric 1702313468828
The timestamp when the record was created in
epoch time.
```
```
action string connection
The action associated with the device that has
generated this record.
```
```
eventType string connection The event type.
```
```
nid numeric 4 A system field.
```
```
uid string
C5mcFh2K3MR4kT9bBc0
0
```
```
A unique identifier for the connection - can be
entered into Advanced Search or the omnisearch
bar to locate associated connections.
```
```
antigenablocked string TRUE
```
```
Indicates the event triggered the creation and
sending of a RESPOND RST. At the time the
```
```
action is taken,
```
```
"antigenablocked":
"true" is
added to the connection entry. As this is
performed at action time, Darktrace is unable to
ascertain if the action was successful until the
connection has demonstrably ended - this state
therefore represents an attempt to block only. If,
after the action, Darktrace detects that the
connection continued and the action was
unsuccessful, "antigenablocked": "true"
is updated to
"antigenablocked": "false".
```
```
antigenaconnectionend string TRUE Experimental field.
```
```
info string
```
```
A slightly unusual
time for a failed
connection to
10.11.12.12 on
port 22. A small
increase in failed
connections to
internal IPs
```
```
A message describing the event, or adding
commentary from Darktrace analysis.
```
```
status string failed
```
```
Can contain “failed” for failed connections or
“ongoing” for continued connections. Completed
connections will not return this field.
```
```
sdid numeric 29
```
```
The device id of the source device. Will only
appear if the source device has been observed
by Darktrace.
```
```
ddid numeric 3765
```
```
The device id of the destination device. Will only
appear if the destination device has been
observed by Darktrace.
```
```
port numeric 443
In the majority of cases, the destination port
connected to.
```
```
sourcePort numeric 22 The port connected from on the source device.
```
```
destinationPort numeric 443 The port connected to on the destination device.
```
```
direction string in The direction of the connection.
```

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
applicationprotocol string HTTPS
The application protocol used in the connection
as derived by Darktrace.
```
```
protocol string TCP The network protocol used for the connection as
derived by Darktrace.
```
```
sourceDevice object
```
```
An object describing the source device. There
are multiple formats this may take, please see the
separate sourceDevice object schemas.
```
```
destinationDevice object
```
```
An object describing the destination device.
There are multiple formats this may take, please
see the separate destinationDevice object
schemas.
```
```
source string ws173 The hostname or IP of the source device.
```
```
destination string google.com The hostname or IP of the destination device.
```
```
antigena-email boolean FALSE
```
```
Whether a hostname present in the notice has
been observed by Darktrace/Email in email
traffic.
```
###### Example Response

_Request: /details?blockedconnections=all_


```
{
"time": "2023-12-11 05:49:56",
"timems": 1702273796155,
"action": "connection",
"eventType": "connection",
"nid": 32767,
"uid": "CMtEGn3kBzavNfWgNd00",
"antigenablocked": "true",
"antigenaconnectionend": "true",
"status": "failed",
"sdid": 33,
"ddid": 44,
"port": 22,
"sourcePort": 39260,
"destinationPort": 22,
"info": "A slightly unusual time for a failed connection to 10.11.12.12 on port 22. A
small increase in failed connections to internal IPs",
"direction": "in",
"applicationprotocol": "SSH",
"protocol": "TCP",
"sourceDevice": {
"id": 33,
"did": 33,
"ip": "10.10.10.11",
"priority": 1,
"ips": [
{
"ip": "10.10.10.11",
"timems": 1702422000000,
"time": "2023-12-12 23:00:00",
"sid": 82,
"vlan": 0
}
],
"sid": 82,
"hostname": "ws-192",
"time": "1564391111000",
"os": "Linux 2.2.x-3.x",
"devicelabel": "ws-192",
"typename": "keyasset",
"typelabel": "Key Asset"
},
"destinationDevice": {
"id": 44,
"did": 44,
"ip": "10.11.12.12",
"ips": [
{
"ip": "10.11.12.12",
"timems": 1702422000000,
"time": "2023-12-12 23:00:00",
"sid": 269,
"vlan": 0
}
],
"sid": 269,
"time": "1571832370000",
"os": "Linux 2.2.x-3.x",
"typename": "server",
"typelabel": "Server"
},
"source": "ws-192",
```
_continued..._


"destination": "10.11.12.12",
"antigena-email": false,
"status": "ongoing"
}


#### Response Schema - sourceDevice and destinationDevice objects

###### Internal sourceDevice and destinationDevice objects

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
sourceDevice object
An object describing an internal source device
for the connection.
```
sourceDevice.id numeric (^76) The “device id”, a unique identifier.
sourceDevice.did numeric 76 The “device id”, a unique identifier.
sourceDevice.macaddress string bc:ee:7b:9c:9f:1e
The current MAC address associated with the
device.
sourceDevice.ip string 10.12.14.2 The current IP associated with the device.
sourceDevice.ips array IPs associated with the device historically.
sourceDevice.ips.ip string 10.12.14.2 A historic IP associated with the device.
sourceDevice.ips.timems numeric 1586937881000
The time the IP was last seen associated with
that device in epoch time.
sourceDevice.ips.time string 2020-04-15 08:04:41 The time the IP was last seen associated with
that device in readable format.
sourceDevice.ips.sid numeric 25 The subnet id for the subnet the IP belongs to.
sourceDevice.sid numeric 25
The subnet id for the subnet the device is
currently located in.
sourceDevice.hostname string
workstation-
local-82
The current device hostname.
sourceDevice.time string 1564090000000
The first time the device was seen on the
network.
sourceDevice.os string
Linux 3.11 and
newer
The device operating system if Darktrace is able
to derive it.
sourceDevice.typename string desktop The device type in system format.
sourceDevice.typelabel string Desktop The device type in readable format.
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
destinationDevice object An object describing an internal destination
device for the connection.
destinationDevice.id numeric 239 The “device id”, a unique identifier.
destinationDevice.did numeric (^239) The “device id”, a unique identifier.
destinationDevice.macaddress string 6e:b7:31:d5:33:6c
The current MAC address associated with the
device.
destinationDevice.ip string 10.0.18.224 The current IP associated with the device.
destinationDevice.ips array IPs associated with the device historically.
destinationDevice.ips.ip string 10.0.18.224 A historic IP associated with the device.
destinationDevice.ips.timems numeric 1584265931000 The time the IP was last seen associated with
that device in epoch time.


```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
destinationDevice.ips.time string 2020-03-15 09:52:11
The time the IP was last seen associated with
that device in readable format.
```
destinationDevice.ips.sid numeric (^25) The subnet id for the subnet the IP belongs to.
destinationDevice.sid numeric 25
The subnet id for the subnet the device is
currently located in.
destinationDevice.hostname string
workstation-
local-82 The current device hostname.
destinationDevice.time string 1564090000000
The first time the device was seen on the
network.
destinationDevice.os string Windows 10
The device operating system if Darktrace is able
to derive it.
destinationDevice.typename string desktop The device type in system format.
destinationDevice.typelabel string Desktop The device type in readable format.

###### Example Object

```
"sourceDevice": {
"id": 532,
"did": 532,
"macaddress": "93:gb:28:g1:fc:g1",
"ip": "192.168.72.4",
"ips": [
{
"ip": "192.168.72.4",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 12
}
],
"sid": 12,
"hostname": "workstation-local-82",
"time": "1528807077000",
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
}
```

###### External sourceDevice and destinationDevice objects

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
sourceDevice object
An object describing an external source device
for the connection.
```
```
sourceDevice.hostname string
customerportal.dark
trace.com
The hostname of the external source.
```
```
sourceDevice.hostnamepopularity string 10
The popularity of that hostname within the
network.
```
```
sourceDevice.connectionhostnamepopular
ity
string 0
The popularity of connections with the same
profile to that hostname within the network.
```
```
sourceDevice.domain string darktrace.com The domain of the hostname.
```
sourceDevice.domainpopularity string (^10) The popularity of the domain within the network.
sourceDevice.connectiondomainpopularit
y
string 0
The popularity of connections with the same
profile to that domain within the network.
sourceDevice.ippopularity string (^0) The popularity of the IP within the network.
sourceDevice.connectionippopularity string 0
The popularity of connections with the same
profile to that IP within the network.
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
destinationDevice object
An object describing an external destination
device for the connection.
destinationDevice.hostname string google.com The hostname of the external destination.
destinationDevice.hostnamepopularity string 10
The popularity of that hostname within the
network.
destinationDevice.connectionhostnamepo
pularity
string 0
The popularity of connections with the same
profile to that hostname within the network.
destinationDevice.domain string google.com The domain of the hostname.
destinationDevice.domainpopularity string 10 The popularity of the domain within the network.
destinationDevice.connectiondomainpopu
larity string
0 The popularity of connections with the same
profile to that domain within the network.
destinationDevice.ippopularity string 0 The popularity of the IP within the network.
destinationDevice.connectionippopulari
ty
string 0
The popularity of connections with the same
profile to that IP within the network.


###### External sourceDevice and destinationDevice objects with fulldevicedetails=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
sourceDevice object
An object describing an external source device
for the connection.
```
```
sourceDevice.longitude numeric -97.822
For the reported IP location, the longitude value
to plot the corresponding IP on a map.
```
```
sourceDevice.latitude numeric 37.751
For the reported IP location, the latitude value to
plot the corresponding IP on a map.
```
```
sourceDevice.country string United States
The country that the corresponding IP is located
in.
```
```
sourceDevice.countrycode string US
The system country code for the country that the
corresponding IP is located in.
```
```
sourceDevice.asn string AS13335 Cloudflare The ASN for the corresponding IP.
```
```
sourceDevice.region string North America
The geographical region the corresponding IP is
located in.
```
```
sourceDevice.ip string 151.101.1.69 The corresponding IP for the hostname.
```
```
sourceDevice.hostname string stackoverflow.com The hostname of the external source.
```
```
sourceDevice.hostnamepopularity string 40
The popularity of that hostname within the
network.
```
```
sourceDevice.connectionhostnamepopular
ity
string 20
The popularity of connections with the same
profile to that hostname within the network.
```
```
sourceDevice.domain string stackoverflow.com The domain of the hostname.
```
```
sourceDevice.domainpopularity string 40 The popularity of the domain within the network.
```
```
sourceDevice.connectiondomainpopularit
y
string 20
The popularity of connections with the same
profile to that domain within the network.
```
sourceDevice.ippopularity string (^40) The popularity of the IP within the network.
sourceDevice.connectionippopularity string 20
The popularity of connections with the same
profile to that IP within the network.
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
destinationDevice object
An object describing an external destination
device for the connection.
destinationDevice.longitude numeric -30 For the reported IP location, the longitude value
to plot the corresponding IP on a map.
destinationDevice.latitude numeric 35
For the reported IP location, the latitude value to
plot the corresponding IP on a map.
destinationDevice.country string United States The country that the corresponding IP is located
in.
destinationDevice.countrycode string US
The system country code for the country that the
corresponding IP is located in.
destinationDevice.asn string
AS16509 Amazon.com
Inc. The ASN for the corresponding IP.


```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
destinationDevice.region string North America
The geographical region the corresponding IP is
located in.
```
```
destinationDevice.ip string 104.20.203.23 The corresponding IP for the hostname.
```
```
destinationDevice.hostname string darktrace.com The hostname of the external destination.
```
```
destinationDevice.hostnamepopularity string 40
The popularity of that hostname within the
network.
```
```
destinationDevice.connectionhostnamepo
pularity
string 20
The popularity of connections with the same
profile to that hostname within the network.
```
```
destinationDevice.domain string darktrace.com The domain of the hostname.
```
destinationDevice.domainpopularity string (^40) The popularity of the domain within the network.
destinationDevice.connectiondomainpopu
larity
string 20
The popularity of connections with the same
profile to that domain within the network.
destinationDevice.ippopularity string (^40) The popularity of the IP within the network.
destinationDevice.connectionippopulari
ty
string 20
The popularity of connections with the same
profile to that IP within the network.

###### Example Object

```
"destinationDevice": {
"longitude": -122.075,
"latitude": 37.404,
"city": "Mountain View",
"country": "United States",
"countrycode": "US",
"asn": "AS15169 Google LLC",
"region": "North America",
"ip": "216.58.204.46",
"hostname": "google.com",
"hostnamepopularity": "100",
"domain": "google.com",
"domainpopularity": "100",
"ippopularity": "10"
}
```

#### Response Schema - eventtype=modelbreach

_Please note, a previous version of this schema incorrectly classified the_ .acknowledged _key as a boolean. This field may_

_also appear as an object if the model breach is acknowledged._

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time string 2020-03-15 09:52:11
The timestamp when the record was created in
epoch time.
```
```
timems numeric 1584265931000
The timestamp when the record was created in
readable format.
```
```
pbid numeric 315602 The “policy breach ID” of the model breach.
```
pid numeric (^486) The “policy id” of the model that was breached.
phid numeric 3125
The model “policy history” id. Increments when
the model is modified.
action string policybreach
The action associated with the device that has
generated this record.
eventType string policybreach The event type.
creationTime numeric 1584265931000
The timestamp that the record of the breach was
created in epoch time.
creationTimestamp string 2020-03-15 09:52:11
The timestamp that the record of the breach was
created in readable format.
name string
Unusual
Activity::Unusual
DNS
Name of the model that was breached.
components array 1090
An array of ‘cid’ values which correspond to the
components that are part of the model that
breached.
didRestrictions array The device ids of devices on the blacklist for this
model.
didExclusions array
The device ids of devices on the whitelist for this
model.
throttle numeric 3600 For an individual device, this is the value in
seconds for which this model will not fire again.
sharedEndpoints boolean TRUE
For models that contain multiple components
that reference an endpoint, this value indicates
whether all endpoints should be identical for the
model to fire.
interval numeric 0
Where a model contains multiple components,
this interval represents the time window in
seconds in which all the components should fire
for this model to be breached.
sequenced boolean FALSE A system field.
active boolean TRUE Whether the model is active or not.
retired boolean FALSE The model has since been deleted.
instanceID numeric (^19000) A system field.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

acknowledged
boolean/
object
FALSE

```
Whether the model breach has been
acknowledged. If false, a boolean. If true, an
object containing the user who acknowledged
the event and the time of acknowledgement.
```
state string New A system field.

score numeric 0.372238
The model breach score, represented by a value
between 0 and 1.

commentCount numeric 0
The number of comments made against this
breach.

componentBreaches array 1090

```
Of the components associated with this model,
the component ID(s) of those that were
breached to trigger the alert.
```
componentBreachTimes array 1590000000000
The time at which the component breach(es)
occurred.

devices array 3877
The device ids of the devices involved in this
breach.

deviceLabels array D7S45E001
The corresponding device labels for devices
involved in this breach.


#### Response Schema - eventtype=devicehistory

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time string 2020-04-15 08:00:00
The timestamp when the record was created in
epoch time.
```
```
timems numeric 1586937600000
The timestamp when the record was created in
readable format.
```
```
eventType string deviceHistory The event type.
```
```
name string mac The type of change or the changed value.
```
```
value string 93:gb:28:g1:fc:g1
The new or removed value, depending on the
eventType.
```
```
reason string DHCP
The initiator of the change - it may be a model, an
expiry, a user, a protocol etc.
```
```
device object
An object describing the device in its current
state.
```
```
device.id numeric 76 The “device id”, a unique identifier.
```
device.did numeric (^76) The “device id”, a unique identifier.
device.macaddress string 93:gb:28:g1:fc:g1
The current MAC address associated with the
device.
device.ip string 10.15.3.39 The current IP associated with the device.
device.ips array IPs associated with the device historically.
device.ips.ip string 10.15.3.39 A historic IP associated with the device.
device.ips.timems numeric 1586937600000 The time the IP was last seen associated with
that device in epoch time.
device.ips.time string 2020-04-15 08:00:00
The time the IP was last seen associated with
that device in readable format.
device.ips.sid numeric (^83) The subnet id for the subnet the IP belongs to.
device.sid numeric 83
The subnet id for the subnet the device is
currently located in.
device.hostname string sarah-desktop-12 The current device hostname.
device.time string 1564090000000
The first time the device was seen on the
network.
device.os string
Linux 3.11 and
newer
The device operating system if Darktrace is able
to derive it.
device.typename string desktop The device type in system format.
device.typelabel string Desktop The device type in readable format.


###### Example Response

```
{
"time": "2020-04-10 00:43:43",
"timems": 1586479423000,
"eventType": "deviceHistory",
"name": "removehostname",
"value": "sarah-desktop-12",
"reason": "Expired",
"device": {
"id": 76,
"did": 76,
"macaddress": "2g:d8:a2:a8:54:c6",
"ip": "10.12.14.2",
"ips": [
{
"ip": "10.12.14.2",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 15
}
],
"sid": 15,
"time": "1528807103000",
"os": "Linux 3.11 and newer",
"devicelabel": "Pool Laptop 6",
"typename": "desktop",
"typelabel": "Desktop"
}
}
```

## /DEVICEINFO

The /deviceinfo endpoint returns the data used in the “Connections Data” view for a specific device that can be

accessed from the Threat Visualizer omnisearch. The data returned covers a 4 week period.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
datatype string Return data for either connections (co), data size out (sizeout) or data size in (sizein).
```
```
did numeric Identification number of a device.
```
```
externaldomain string Restrict external data to a particular domain name
```
```
fulldevicedetails boolean
Returns the full device detail objects for all devices referenced by data in an API response. Use of this
parameter will alter the JSON structure of the API response for certain calls.
```
```
odid numeric Identification number of a destination device modelled in the Darktrace system to restrict data to.
```
```
showallgraphdata boolean Return an entry for all time intervals in the graph data, including zero counts.
```
```
similardevices numeric Return data for the primary device and this number of similar devices.
```
```
port numeric Restricts returned connection data to the port specified.
```
```
intervalhours numeric The size in hours that the returned time series data is grouped by.
```
###### Notes

- The minimum time interval width is 1 hour. A value greater than 1 can be specified with intervalhours to
    create a larger interval for connection grouping.
- Setting showallgraphdata to false will remove empty time intervals with from the returned data - this can be
    helpful to reduce noise.
- To get external connectivity, use odid=0 in the request parameters. This will add additional information to the
    response JSON about the external locations accessed.
- Only the top results across the four week interval will be returned - results below a certain threshold will be
    grouped into an ‘others’ category.
- Restricting the data to a domain or adding similar devices will change the structure of the returned JSON.
- fulldevicedetails=true will add a devices object with full details of the devices connected to and the
    device specified
- Specifying a number of similar devices to return will result in multiple objects in the deviceinfo array.


###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET the data transfer volume downloaded by the device with did=1 on port 443 and return 3 devices with
    similar patterns of life:

```
https://[instance]/deviceinfo?
did=1&showallgraphdata=true&port=443&datatype=sizein&similardevices=3
```
2. GET the number of connections from the device with did=1 to the device with did=100, grouped into 12
    hour windows:

```
https://[instance]/deviceinfo?
did=1&odid=100&datatype=co&similardevices=0&intervalhours=12&fulldevicedetails=false
```

###### Example Response

_Request:_

_/deviceinfo?did=316&intervalhours=12&showallgraphdata=true&datatype=co&port=443&externaldomain=google.com_

```
{
"deviceInfo": [
{
"did": 316,
"similarityScore": 100,
"domain": "google.com",
"graphData": [
{
"time": 1582243200000,
"count": 0
},
...
],
"info": {
"totalUsed": 302,
"totalServed": 0,
"totalDevicesAndPorts": 302,
"devicesAndPorts": [],
"externalDomains": [
{
"domain": "google.com",
"size": 100
}
],
"portsUsed": [
{
"port": 443,
"size": 100,
"firstTime": 1584529392000
}
],
"portsServed": [],
"devicesUsed": [
{
"did": 0,
"size": 100,
"firstTime": 1584529392000
}
],
"devicesServed": []
}
}
]
}
```
_Response is abbreviated._


## /DEVICEINFO RESPONSE SCHEMA

#### Response Schema

###### fulldevicedetails=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
deviceInfo array
An array of graphable connection information for
the specified device.
```
deviceInfo.did numeric (^225) The “device id”, a unique identifier.
deviceInfo.similarityScore numeric 100
A score describing how similar this device is in
comparison to the original device. The original
device will always return 100.
deviceInfo.graphData array An array of time series grouped connection data
to be displayed graphically.
deviceInfo.graphData.time numeric 1580000000000
Timestamp for the interval of grouped
connection / data transfer data in epoch time.
deviceInfo.graphData.count numeric 355 The volume of connections or data for that
interval.
deviceInfo.info object Information about the connections.
deviceInfo.info.totalUsed numeric 374112
The amount of data or connections where the
device was the client.
deviceInfo.info.totalServed numeric 45
The amount of data or connections where the
device was the server.
deviceInfo.info.totalDevicesAndPorts numeric 374157 The amount of data or connections.
deviceInfo.info.devicesAndPorts array
An array of device/port pairs used in the
connections or data transfers.
deviceInfo.info.devicesAndPorts.device
AndPort
object
An object describing the device/port pairs and
the direction of transfer.
deviceInfo.info.devicesAndPorts.device
AndPort.direction
string out The direction of data flow.
deviceInfo.info.devicesAndPorts.device
AndPort.device
numeric -6
The “device id” of the device that connected to,
or was connected to by, the original device.
deviceInfo.info.devicesAndPorts.device
AndPort.port
numeric 443
The port used or served by the original device,
depending on the connection direction.
deviceInfo.info.devicesAndPorts.size numeric 27
What percentage of the total connections or data
transfer used this port/device pair.
deviceInfo.info.portsUsed array
An array of ports used by the device when
making the connections returned in graph data.
deviceInfo.info.portsUsed.port numeric 443 The port used.
deviceInfo.info.portsUsed.size numeric 44 What percentage of the total outbound
connections or data transfer used this port.
deviceInfo.info.portsUsed.firstTime numeric 1530000000000 The first time this port was used by the device.
deviceInfo.info.portsServed array An array of ports served by the device when
making the connections returned in graph data.
deviceInfo.info.portsServed.port numeric 22 The port that was served by the device.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

deviceInfo.info.portsServed.size numeric 53
What percentage of the total inbound
connections or data transfer used this port.

deviceInfo.info.portsServed.firstTime numeric 1530000000000 The first time this port was served by the device
in epoch time.

deviceInfo.info.devicesUsed array

```
An array of devices connected to by the original
device when making the connections returned in
graph data.
```
deviceInfo.info.devicesUsed.did numeric -6
The “device id” of a device that was connected to
by the original device.

deviceInfo.info.devicesUsed.size numeric 72

```
The percentage of the total outbound
connections or data transfer that used this
device.
```
deviceInfo.info.devicesUsed.firstTime numeric 1530000000000
The first time this device was connected to by
the original device in epoch time.

deviceInfo.info.devicesServed array

```
An array of devices that connected to the original
device when making the connections returned in
graph data.
```
deviceInfo.info.devicesServed.did numeric 354
The “device id” of a device that connected to the
original device.

deviceInfo.info.devicesServed.size numeric 53

```
The percentage of the total inbound connections
or data transfer that involved this device
connecting to the original device.
```

###### Example Response

```
{
"deviceInfo": [
{
"did": 316,
"similarityScore": 100,
"graphData": [
{
"time": 1582243200000,
"count": 0
},
...
],
"info": {
"totalUsed": 6284,
"totalServed": 0,
"totalDevicesAndPorts": 6284,
"devicesAndPorts": [
{
"deviceAndPort": {
"direction": "out",
"device": 0,
"port": 443
},
"size": 74
},
...
],
"portsUsed": [
{
"port": 443,
"size": 100,
"firstTime": 1576136929000
}
],
"portsServed": [],
"devicesUsed": [
{
"did": 0,
"size": 74,
"firstTime": 1584529027000
},
...
],
"devicesServed": []
}
}
]
}
```
_Response is abbreviated._


###### fulldevicedetails=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
deviceInfo array
An array of graphable connection information for
the specified device.
```
```
deviceInfo.did numeric 230 The “device id”, a unique identifier.
```
```
deviceInfo.similarityScore numeric 100
```
```
A score describing how similar this device is in
comparison to the original device. The original
device will always return 100.
```
```
deviceInfo.graphData array
An array of time series grouped connection data
to be displayed graphically.
```
```
deviceInfo.graphData.time numeric 1580000000000
Timestamp for the interval of grouped
connection / data transfer data in epoch time.
```
```
deviceInfo.graphData.count numeric 355
The volume of connections or data for that
interval.
```
```
deviceInfo.info object Information about the connections.
```
```
deviceInfo.info.totalUsed numeric 374112
The amount of data or connections where the
device was the client.
```
```
deviceInfo.info.totalServed numeric 45
The amount of data or connections where the
device was the server.
```
deviceInfo.info.totalDevicesAndPorts numeric (^374157) The amount of data or connections.
deviceInfo.info.devicesAndPorts array
An array of device/port pairs used in the
connections or data transfers.
deviceInfo.info.devicesAndPorts.device
AndPort object
An object describing the device/port pairs and
the direction of transfer.
deviceInfo.info.devicesAndPorts.device
AndPort.direction
string out The direction of data flow.
deviceInfo.info.devicesAndPorts.device
AndPort.device numeric
-6 The “device id” of the device that connected to,
or was connected to by, the original device.
deviceInfo.info.devicesAndPorts.device
AndPort.port
numeric 443
The port used or served by the original device,
depending on the connection direction.
deviceInfo.info.devicesAndPorts.size numeric 27 What percentage of the total connections or data
transfer used this port/device pair.
deviceInfo.info.portsUsed array
An array of ports used by the device when
making the connections returned in graph data.
deviceInfo.info.portsUsed.port numeric (^443) The port used.
deviceInfo.info.portsUsed.size numeric 44
What percentage of the total outbound
connections or data transfer used this port.
deviceInfo.info.portsUsed.firstTime numeric 1530000000000 The first time this port was used by the device.
deviceInfo.info.portsServed array
An array of ports served by the device when
making the connections returned in graph data.
deviceInfo.info.portsServed.port numeric 22
What percentage of the total inbound
connections or data transfer used this port.
deviceInfo.info.portsServed.size numeric 53
The first time this port was served by the device
in epoch time.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

deviceInfo.info.devicesUsed array

```
An array of devices connected to by the original
device when making the connections returned in
graph data.
```
deviceInfo.info.devicesUsed.did numeric -6
The “device id” of a device that was connected to
by the original device.

deviceInfo.info.devicesUsed.size numeric 72

```
The percentage of the total outbound
connections or data transfer that used this
device.
```
deviceInfo.info.devicesUsed.firstTime numeric 1530000000000
The first time this device was connected to by
the original device in epoch time.

deviceInfo.info.devicesServed array

```
An array of devices that connected to the original
device when making the connections returned in
graph data.
```
deviceInfo.info.devicesServed.did numeric 354
The “device id” of a device that connected to the
original device.

deviceInfo.info.devicesServed.size numeric 53

```
The percentage of the total inbound connections
or data transfer that involved this device
connecting to the original device.
```
devices array

```
An array of information about the original device
and any devices it interacted with as part of the
connections.
```
devices.did numeric (^57) The “device id”, a unique identifier.
devices.macaddress string 93:gb:28:g1:fc:g1
The current MAC address associated with the
device.
devices.vendor string
Belkin
International Inc.
The vendor of the device network card as
derived by Darktrace from the MAC address.
devices.ip string 10.15.3.39 The current IP associated with the device.
devices.ips array IPs associated with the device historically.
devices.ips.ip string 10.15.3.39 A historic IP associated with the device.
devices.ips.timems numeric 1584265931000
The time the IP was last seen associated with
that device in epoch time.
devices.ips.time string 2020-03-15 09:52:11
The time the IP was last seen associated with
that device in readable format.
devices.ips.sid numeric 17 The subnet id for the subnet the IP belongs to.
devices.sid numeric 17 The subnet id for the subnet the device is
currently located in.
devices.hostname string ws83 The current device hostname.
devices.firstSeen numeric 1528810000000
The first time the device was seen on the
network.
devices.lastSeen numeric 1585140000000
The last time the device was seen on the
network.
devices.os string
Linux 3.11 and
newer
The device operating system if Darktrace is able
to derive it.
devices.devicelabel string Workstation 83
An optional label applied to the device in Device
Admin.
devices.typename string laptop The device type in system format.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

devices.typelabel string Laptop The device type in readable format.

devices.tags array An object describing tags applied to the device.

devices.tags.tid numeric 180 The “tag id”. A unique value.

devices.tags.expiry numeric 0
The expiry time for the tag when applied to a
device.

devices.tags.thid numeric 172
The “tag history” id. Increments if the tag is
edited.

devices.tags.name string Finance
The tag label displayed in the user interface or in
objects that reference the tag.

devices.tags.restricted boolean FALSE
Indicates a read-only tag - these tags can only be
modified or applied by Darktrace.

devices.tags.data object An object containing information about the tag.

devices.tags.data.auto boolean FALSE Whether the tag was auto-generated.

devices.tags.data.color numeric 200
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.

devices.tags.data.description string

```
Device is part of
the Finance
network.
```
```
An optional description summarizing the
purpose of the tag.
```
devices.tags.data.visibility string A system field.

devices.tags.isReferenced boolean TRUE
Whether the tag is used by one or more model
components.


###### Example Response

```
{
"deviceInfo": [
{
"did": 316,
"similarityScore": 100,
"graphData": [
{
"time": 1582243200000,
"count": 0
},
...
],
"info": {
"totalUsed": 125,
"totalServed": 0,
"totalDevicesAndPorts": 125,
"devicesAndPorts": [
{
"deviceAndPort": {
"direction": "out",
"device": 18,
"port": 443
},
"size": 100
}
],
"portsUsed": [
{
"port": 443,
"size": 100,
"firstTime": 1584529073000
}
],
"portsServed": [],
"devicesUsed": [
{
"did": 2719,
"size": 100,
"firstTime": 1584529073000
}
],
"devicesServed": []
}
}
],
"devices": [
{
"did": 2719,
"ip": "192.168.120.39",
"ips": [
{
"ip": "192.168.120.39",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 6
}
],
"sid": 6,
"hostname": "sarah's iphone",
"firstSeen": 1576581851000,
"lastSeen": 1582131590000,
```
_continued..._


```
"os": "Mac OS X",
"typename": "mobile",
"typelabel": "Mobile",
"tags": [
{
"tid": 17,
"expiry": 0,
"thid": 17,
"name": "iOS device",
"restricted": false,
"data": {
"auto": false,
"color": 181,
"description": "",
"visibility": "Public"
},
"isReferenced": true
}
]
},
...
{
"did": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"sid": 23,
"hostname": "Sarah Development",
"firstSeen": 1581591070000,
"lastSeen": 1582645442000,
"typename": "desktop",
"typelabel": "Desktop"
"tags": [
{
"tid": 50,
"expiry": 0,
"thid": 50,
"name": "Admin",
"restricted": false,
"data": {
"auto": false,
"color": 200,
"description": "A device that has been inactive for at least 4 weeks has re-
appeared on the network in the past 48 hours.",
"visibility": "Public"
},
"isReferenced": true
}
]
}
]
}
```
_Response is abbreviated._


#### Response Schema - externaldomain

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
deviceInfo array
An array of graphable connection information for
the specified device.
```
```
deviceInfo.did numeric 57 The “device id”, a unique identifier.
```
```
deviceInfo.similarityScore numeric 100
```
```
A score describing how similar this device is in
comparison to the original device. The original
device will always return 100.
```
```
deviceInfo.domain string google.com
The external domain that connections or data
transfer is limited to.
```
```
deviceInfo.graphData array
An array of time series grouped connection data
to be displayed graphically.
```
```
deviceInfo.graphData.time numeric 1580000000000
Timestamp for the interval of grouped
connection / data transfer data in epoch time.
```
```
deviceInfo.graphData.count numeric 1
The volume of connections or data for that
interval.
```
```
deviceInfo.info object Information about the connections.
```
```
deviceInfo.info.totalUsed numeric 3397
The amount of data or connections where the
device was the client.
```
```
deviceInfo.info.totalServed numeric 0
The amount of data or connections where the
device was the server.
```
```
deviceInfo.info.totalDevicesAndPorts numeric 3397 The amount of data or connections.
```
```
deviceInfo.info.devicesAndPorts array
An array of device/port pairs used in the
connections or data transfers.
```
```
deviceInfo.info.devicesAndPorts.device
AndPort
object
An object describing the device/port pairs and
the direction of transfer.
```
```
deviceInfo.info.devicesAndPorts.device
AndPort.direction
string out The direction of data flow.
```
```
deviceInfo.info.devicesAndPorts.device
AndPort.device
numeric -6
The “device id” of the device that connected to,
or was connected to by, the original device.
```
```
deviceInfo.info.devicesAndPorts.device
AndPort.port
numeric 443
The port used or served by the original device,
depending on the connection direction.
```
```
deviceInfo.info.devicesAndPorts.size numeric 27
What percentage of the total connections or data
transfer used this port/device pair.
```
```
deviceInfo.info.externalDomains array
An array of the external domains that were
connected to.
```
```
deviceInfo.info.externalDomains.domain string google.com An external domain that was accessed.
```
```
deviceInfo.info.externalDomains.size numeric 100
What percentage of the total connections or data
transfer involved this external domain.
```
```
deviceInfo.info.portsUsed array An array of ports used by the device when
making the connections returned in graph data.
```
```
deviceInfo.info.portsUsed.port numeric 443 The port used.
```
```
deviceInfo.info.portsUsed.size numeric 44
What percentage of the total outbound
connections or data transfer used this port.
```
```
deviceInfo.info.portsUsed.firstTime numeric 1530000000000 The first time this port was used by the device.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

deviceInfo.info.portsServed array
An array of ports served by the device when
making the connections returned in graph data.

deviceInfo.info.portsServed.port numeric (^22) The port that was served by the device.
deviceInfo.info.portsServed.size numeric 53
What percentage of the total inbound
connections or data transfer used this port.
deviceInfo.info.portsServed.firstTime numeric 1530000000000
The first time this port was served by the device
in epoch time.
deviceInfo.info.devicesUsed array
An array of devices connected to by the original
device when making the connections returned in
graph data.
deviceInfo.info.devicesUsed.did numeric -6 The “device id” of a device that was connected to
by the original device.
deviceInfo.info.devicesUsed.size numeric 72
The percentage of the total outbound
connections or data transfer that used this
device.
deviceInfo.info.devicesUsed.firstTime numeric 1530000000000
The first time this device was connected to by
the original device in epoch time.
deviceInfo.info.devicesServed array
An array of devices that connected to the original
device when making the connections returned in
graph data.
deviceInfo.info.devicesServed.did numeric 354
The “device id” of a device that connected to the
original device.
deviceInfo.info.devicesServed.size numeric 53
The percentage of the total inbound connections
or data transfer that involved this device
connecting to the original device.


###### Example Response

```
{
"deviceInfo": [
{
"did": 316,
"similarityScore": 100,
"domain": "google.com",
"graphData": [
{
"time": 1582243200000,
"count": 0
},
...
],
"info": {
"totalUsed": 302,
"totalServed": 0,
"totalDevicesAndPorts": 302,
"devicesAndPorts": [],
"externalDomains": [
{
"domain": "google.com",
"size": 100
}
],
"portsUsed": [
{
"port": 443,
"size": 100,
"firstTime": 1584529392000
}
],
"portsServed": [],
"devicesUsed": [
{
"did": 0,
"size": 100,
"firstTime": 1584529392000
}
],
"devicesServed": []
}
}
]
}
```
_Response is abbreviated._


#### Response Schema - odid=0

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
deviceInfo array
An array of graphable connection information for
the specified device.
```
```
deviceInfo.did numeric 230 The “device id”, a unique identifier.
```
```
deviceInfo.similarityScore numeric 100
```
```
A score describing how similar this device is in
comparison to the original device. The original
device will always return 100.
```
```
deviceInfo.graphData array
An array of time series grouped connection data
to be displayed graphically.
```
```
deviceInfo.graphData.time numeric 1582680000000
Timestamp for the interval of grouped
connection / data transfer data in epoch time.
```
```
deviceInfo.graphData.count numeric 72
The volume of connections or data for that
interval.
```
```
deviceInfo.info object Information about the connections.
```
```
deviceInfo.info.totalUsed numeric 321662
The amount of data or connections where the
device was the client.
```
```
deviceInfo.info.totalServed numeric 0
The amount of data or connections where the
device was the server.
```
```
deviceInfo.info.totalDevicesAndPorts numeric 321662 The amount of data or connections.
```
```
deviceInfo.info.devicesAndPorts array
An array of device/port pairs used in the
connections or data transfers.
```
```
deviceInfo.info.devicesAndPorts.device
AndPort
object
An object describing the device/port pairs and
the direction of transfer.
```
```
deviceInfo.info.devicesAndPorts.device
AndPort.direction
string out The direction of data flow.
```
```
deviceInfo.info.devicesAndPorts.device
AndPort.device
numeric 0
The “device id” of the device that connected to,
or was connected to by, the original device.
```
```
deviceInfo.info.devicesAndPorts.device
AndPort.port
numeric 443
The port used or served by the original device,
depending on the connection direction.
```
```
deviceInfo.info.devicesAndPorts.size numeric 19
What percentage of the total connections or data
transfer used this port/device pair.
```
```
deviceInfo.info.externalASNs array
An array of external ASNs who served the
external domains connected to by the device.
```
```
deviceInfo.info.externalASNs.asn string AS15169 Google LLC An ASN.
```
```
deviceInfo.info.externalASNs.size numeric 53 The percentage of connections that involved this
ASN.
```
```
deviceInfo.info.externalDomains array
An array of the external domains that were
connected to.
```
```
deviceInfo.info.externalDomains.domain string google.com An external domain that was accessed.
```
```
deviceInfo.info.externalDomains.size numeric 26
What percentage of the total connections or data
transfer involved this external domain.
```
```
deviceInfo.info.portsUsed array
An array of ports used by the device when
making the connections returned in graph data.
```
```
deviceInfo.info.portsUsed.port numeric 443 The port used.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

deviceInfo.info.portsUsed.size numeric 44
What percentage of the total outbound
connections or data transfer used this port.

deviceInfo.info.portsUsed.firstTime numeric (^1530000000000) The first time this port was used by the device.
deviceInfo.info.portsServed array
An array of ports served by the device when
making the connections returned in graph data.
deviceInfo.info.portsServed.port numeric 22 The port that was served by the device.
deviceInfo.info.portsServed.size numeric 53
What percentage of the total inbound
connections or data transfer used this port.
deviceInfo.info.portsServed.firstTime numeric 1530000000000
The first time this port was served by the device
in epoch time.
deviceInfo.info.devicesUsed array
An array of devices connected to by the original
device when making the connections returned in
graph data.
deviceInfo.info.devicesUsed.did numeric -6
The “device id” of a device that was connected to
by the original device.
deviceInfo.info.devicesUsed.size numeric 72
The percentage of the total outbound
connections or data transfer that used this
device.
deviceInfo.info.devicesUsed.firstTime numeric 1530000000000 The first time this device was connected to by
the original device in epoch time.
deviceInfo.info.devicesServed array
An array of devices that connected to the original
device when making the connections returned in
graph data.
deviceInfo.info.devicesServed.did numeric 354
The “device id” of a device that connected to the
original device.
deviceInfo.info.devicesServed.size numeric 53
The percentage of the total inbound connections
or data transfer that involved this device
connecting to the original device.


###### Example Response

```
{
"deviceInfo": [
{
"did": 316,
"similarityScore": 100,
"graphData": [
{
"time": 1582243200000,
"count": 0
},
...
],
"info": {
"totalUsed": 21124,
"totalServed": 0,
"totalDevicesAndPorts": 21124,
"devicesAndPorts": [
{
"deviceAndPort": {
"direction": "out",
"device": 0,
"port": 443
},
"size": 22
}
],
"externalASNs": [
{
"asn": "AS15169 Google LLC.",
"size": 8
},
...
],
"externalDomains": [
{
"domain": "google.com",
"size": 21
},
...
],
"portsUsed": [
{
"port": 443,
"size": 100,
"firstTime": 1584529027000
}
],
"portsServed": [],
"devicesUsed": [
{
"did": 0,
"size": 22,
"firstTime": 1584529027000
}
],
"devicesServed": []
}
}
]
}
```
_Response is abbreviated._


## /DEVICES

The /devices endpoint returns a list of devices identified by Darktrace or details of a specific device given a time window.

When a did is specified, the endpoint returns the information displayed in the UI pop-up when hovering over a device.

Changes to a device can be made with a POST request. The fields that can be changed are the device type (in enum

format), the priority and the label.

```
POST requests to this endpoint can be made in JSON or parameter format. Fields which are not supported will be ignored
```
when included in POST requests. Device objects can therefore be retrieved, modified and resubmitted to this endpoint to

make changes.

For targeted searches, the /devicesearch endpoint is recommended.

###### Request Type(s)

```
[GET] [POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
did numeric Identification number of a device modelled in the Darktrace system.
```
```
ip string IP of the device modelled in the Darktrace system.
```
```
iptime string Returns the device which had the IP at a given time.
```
```
mac string Returns the device with this MAC address.
```
```
seensince string
```
```
Relative offset for activity. Devices with activity in the specified time period are returned. The format is
either a number representing a number of seconds before the current time, or a number with a modifier
such as second, minute, hour day or week (Minimum=1 second).
```
```
sid numeric Identification number of a subnet modelled in the Darktrace system.
```
```
count numeric The number of devices to return. Only limits the number of devices within the current timeframe.
```
```
includetags boolean Whether to include tags applied to the device in the response.
```
```
label string An optional label to add to the device. Available for POST requests only.
```
```
priority numeric
The device priority on a scale of -5 to 5 - priority affects the model breach score for the device and can be
used to filter alert outputs. Available for POST requests only.
```
```
type numeric
```
```
The device type in enum format (see /enums?responsedata=sourcedevicetypes ). Only device types
which do not have hidden=true are available to set. Industrial device types are not available outside the
Darktrace/OT environment. Available for POST requests only.
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
```
cloudsecurity boolean When true, limits the devices returned to those identified by Darktrace Cloud Security.
```
```
saasfilter string
Can be used to limit returned devices to specific Darktrace/Apps, Cloud or Zero Trust module users. Can
be repeated multiple times.
```

###### Notes

- Device objects may not have values for all of the attributes available. If a device does not have a MAC address, a
    label, credentials, or a hostname, they will not be included in the returned JSON.
- Devices with a priority of 0 will not have a priority attribute returned.
- This endpoint does not support searching outside the did, sid, ip and saasfilter parameters. To
    perform custom searches, the /devicesearch endpoint is recommended.
- The default timeframe is 7 days.
- When accessing the /devices endpoint from a browser, an additional parameter - minscore - is required.
    This parameter controls the devices that return by their device score (score of associated model breaches) and
    takes values from 0 to 1, where a score threshold of 70% would be minscore=0.7. To return all devices
    regardless of score, minscore=0 should be added to the query. This parameter is not available when using the
    API programmatically with an authentication token - minscore is set to 0.
- As of Darktrace 6.1, device types altered by API requests can only be overridden by manual changes or further
    API requests.

```
Passive analysis, model actions or hostname expressions are no longer able to override types set via the API.
```
- The saasfilter parameter takes a wildcard string which is matched to the SaaS::[platform] value
    (e.g. SaaS::Office365). Multiple filters can be applied to include multiple modules - for example,
       saasfilter=gcp*&saasfilter=office365*. A wildcard (*) _must be specified_ at the end of this parameter
    value.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET a list of all the devices on the 10.0.0.0/24 subnet (sid=25) in the last 2 minutes:

```
https://[instance]/devices?seensince=2min&sid=25
```
2. GET a device with IP 10.0.0.1:

```
https://[instance]/devices?ip=10.0.0.1
```
3. GET a list of all the devices seen in the last hour:

```
https://[instance]/devices?seensince=1hour
```
```
https://[instance]/devices?seensince=3600
```
4. GET a list of Google Cloud Platform and Microsoft 365 devices, with only the device identifier and username
    returned:

```
https://[instance]/devices?
saasfilter=gcp*&saasfilter=office365*&responsedata=did,hostname
```

5. POST to update the label and change the device type to “Key Asset” for the device with did=100:

```
https://[instance]/devices with body {"did":100,"label": "Finance File Server", "type":
10}
```
###### Example Response

_Request: /devices?seensince=2hour&sid=23_

```
[
{
"id": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"did": 316,
"sid": 23,
"hostname": "Sarah Development",
"quarantine": 1623669514000,
"time": 1528807083000,
"endtime": 1587135192000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
"customFields": {
"DT-MANUAL": {
"notes": "Test Note"
}
}
]
```

## /DEVICES RESPONSE SCHEMA

Device objects may not have values for all of the attributes available. If a device does not have a MAC address, a label,

credentials, or a hostname, they will not be included in the returned JSON.

Additional examples have now been added below for Darktrace/Endpoint and VDI devices.

#### Response Schema - Network Device

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
id numeric 227
```
```
The “device id”, a unique identifier. Only appears
in device objects retrieved from the \devices
endpoint.
```
```
macaddress string 56:2d:4b:9c:18:42
The current MAC address associated with the
device.
```
```
vendor string Apple
The vendor of the device network card as
derived by Darktrace from the MAC address.
```
```
ip string 10.0.18.224 The current IP associated with the device.
```
```
ips array IPs associated with the device historically.
```
```
ips.ip string 10.0.18.224 A historic IP associated with the device.
```
```
ips.timems numeric 1586937881000
The time the IP was last seen associated with
that device in epoch time.
```
```
ips.time string 2020-04-15 08:04:41 The time the IP was last seen associated with
that device in readable format.
```
```
ips.sid numeric 10 The subnet id for the subnet the IP belongs to.
```
```
did numeric 230 The “device id”, a unique identifier.
```
```
sid numeric 10
The subnet id for the subnet the device is
currently located in.
```
```
hostname string sarah-desktop-12 The current device hostname.
```
```
quarantine numeric 1528810000000
```
```
A timestamp of the most recent Darktrace
RESPOND action against the device. Will only
return if a recent, active action has been taken.
Only appears in device objects retrieved from the
\devices endpoint.
```
```
time numeric 1528810000000
```
```
The first time the device was seen on the
network. Will only appear in device objects
retrieved from the \devices endpoint -
equivalent field is firstSeen when device
objects are retrieved from other endponts.
```
```
endtime numeric 1585310000000
```
```
The last time the device was seen on the
network. Will only appear in device objects
retrieved from the \devices endpoint -
equivalent field is lastSeen when device
objects are retrieved from other endponts.
```
```
os string
Linux 3.11 and
newer
```
```
The device operating system if Darktrace is able
to derive it.
```
```
devicelabel string Sarah Development
An optional label applied to the device in the
Device Admin page.
```
```
typename string desktop The device type in system format.
```

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
typelabel string Desktop The device type in readable format.
```
```
customFields object
```
```
An object containing additional custom fields
with data about the devices. Custom fields
include SaaS context data and notes added to
the device on the Device Admin page.
```
```
customFields.DT-MANUAL object An object containing custom fields.
```
```
customFields.DT-MANUAL.notes string Test Note A custom field.
```
###### Example Response

```
{
"id": 212,
"macaddress": "6e:b7:31:d5:33:6c",
"vendor": "Micro-Star INTL CO., LTD.",
"ip": "10.12.14.2",
"ips": [
{
"ip": "10.12.14.2",
"timems": 1587132000000,
"time": "2020-04-17 14:00:00",
"sid": 12
}
],
"did": 212,
"sid": 12,
"hostname": "sarah-desktop-12",
"quarantine": 1623669514000,
"time": 1528807083000,
"endtime": 1587135192000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
"customFields": {
"DT-MANUAL": {
"notes": "Test Note"
}
}
}
```

#### Response Schema - SaaS Device

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
id numeric 4841
```
```
The “device id”, a unique identifier. Only appears
in device objects retrieved from the \devices
endpoint.
```
```
did numeric 4841 The “device id”, a unique identifier.
```
```
sid numeric -9
The subnet id for the subnet the device belongs
to.
```
```
hostname string
```
```
SaaS::Office365:
benjamin.ash@holdin
gsinc.com
```
```
The SaaS device name as constructed by
Darktrace from the user name and SaaS service.
```
```
credentials array
An array of credentials associated with the
device entity.
```
```
credentials.lastSeen numeric 1623927545000
The time the credential was last seen associated
with that device in epoch time.
```
```
credentials.credential string
benjamin.ash@holdin
gsinc.com
A credential associated with the device entity.
```
```
time numeric 1574700328000
```
```
The first time the device was seen on the
network. Will only appear in device objects
retrieved from the \devices endpoint -
equivalent field is firstSeen when device
objects are retrieved from other endponts.
```
```
endtime numeric 1624013903000
```
```
The last time the device was seen on the
network. Will only appear in device objects
retrieved from the \devices endpoint -
equivalent field is lastSeen when device
objects are retrieved from other endponts.
```
```
typename string saasprovider The device type in system format.
```
```
typelabel string SaaS Provider The device type in readable format.
```
###### Example Response

```
{
"id": 4841,
"did": 4841,
"sid": -9,
"hostname": "SaaS::Office365: benjamin.ash@holdingsinc.com",
"credentials": [
{
"lastSeen": 1624029774000,
"credential": "benjamin.ash@holdingsinc.com"
}
],
"time": 1574700328000,
"endtime": 1624029927000,
"typename": "saasprovider",
"typelabel": "SaaS Provider",
}
```

#### Response Schema - includetags=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
id numeric 227
```
```
The “device id”, a unique identifier. Only appears
in device objects retrieved from the \devices
endpoint.
```
```
macaddress string 56:2d:4b:9c:18:42 The current MAC address associated with the
device.
```
```
vendor string Apple
The vendor of the device network card as
derived by Darktrace from the MAC address.
```
```
ip string 10.0.18.224 The current IP associated with the device.
```
```
ips array IPs associated with the device historically.
```
```
ips.ip string 10.0.18.224 A historic IP associated with the device.
```
```
ips.timems numeric 1586937881000
The time the IP was last seen associated with
that device in epoch time.
```
```
ips.time string 43936.33659
The time the IP was last seen associated with
that device in readable format.
```
```
ips.sid numeric 10 The subnet id for the subnet the IP belongs to.
```
```
did numeric 227 The “device id”, a unique identifier.
```
```
sid numeric 10 The subnet id for the subnet the device is
currently located in.
```
```
hostname string sarah-desktop-12 The current device hostname.
```
```
time numeric 1528810000000
```
```
The first time the device was seen on the
network. Will only appear in device objects
retrieved from the \devices endpoint -
equivalent field is firstSeen when device
objects are retrieved from other endponts.
```
```
endtime numeric 1585310000000
```
```
The last time the device was seen on the
network. Will only appear in device objects
retrieved from the \devices endpoint -
equivalent field is lastSeen when device
objects are retrieved from other endponts.
```
```
quarantine numeric 1528810000000
```
```
A timestamp of the most recent Darktrace
RESPOND action against the device. Will only
return if a recent, active action has been taken.
Only appears in device objects retrieved from the
\devices endpoint.
```
```
tags array An object describing tags applied to the device.
```
```
tags.tid numeric 22 The “tag id”. A unique value.
```
```
tags.expiry numeric 0
The expiry time for the tag when applied to a
device.
```
```
tags.thid numeric 22
The “tag history” id. Increments if the tag is
edited.
```
```
tags.name string Admin
The tag label displayed in the user interface or in
objects that reference the tag.
```
```
tags.restricted boolean FALSE
Indicates a read-only tag - these tags can only be
modified or applied by Darktrace.
```
```
tags.data object An object containing information about the tag.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

tags.data.auto boolean FALSE Whether the tag was auto-generated.

tags.data.color numeric 200
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.

tags.data.description string
Testing the use of
tags.

```
An optional description summarizing the
purpose of the tag.
```
tags.data.visibility string A system field.

tags.isReferenced boolean TRUE
Whether the tag is used by one or more model
components.

os string
Linux 3.11 and
newer

```
The device operating system if Darktrace is able
to derive it.
```
devicelabel string Sarah Development
An optional label applied to the device in the
Device Admin page.

typename string desktop The device type in system format.

typelabel string Desktop The device type in readable format.

customFields object

```
An object containing additional custom fields
with data about the devices. Custom fields
include SaaS context data and notes added to
the device on the Device Admin page.
```
customFields.DT-MANUAL object An object containing custom fields.

customFields.DT-MANUAL.notes string Test Note A custom field.


###### Example Response

```
{
"id": 212,
"macaddress": "6e:b7:31:d5:33:6c",
"vendor": "Micro-Star INTL CO., LTD.",
"ip": "10.12.14.2",
"ips": [
{
"ip": "10.12.14.2",
"timems": 1587132000000,
"time": "2020-04-17 14:00:00",
"sid": 12
}
],
"did": 212,
"sid": 12,
"hostname": "sarah-desktop-12",
"quarantine": 1623669514000,
"time": 1528807083000,
"endtime": 1587135192000,
"tags": [
{
"tid": 131,
"expiry": 0,
"thid": 62,
"name": "Re-Activated Device",
"restricted": false,
"data": {
"auto": false,
"color": 142,
"description": "A device that has been inactive for at least 4 weeks has re-appeared
on the network in the past 48 hours.",
"visibility": "Public"
},
"isReferenced": true
}
],
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
"customFields": {
"DT-MANUAL": {
"notes": "Test Note"
}
}
}
```

###### Threat Intelligence Data

Threat intelligence data such as CVEs retrieved from integrations like Microsoft Defender Advanced Hunting will also

appear in the device object. This data is within the customFields object, for example:

```
{
"id": 212,
"macaddress": "6e:b7:31:d5:33:6c",
"vendor": "Micro-Star INTL CO., LTD.",
"ip": "10.12.14.2",
"ips": [
{
"ip": "10.12.14.2",
"timems": 1587132000000,
"time": "2020-04-17 14:00:00",
"sid": 12
}
],
"did": 212,
"sid": 12,
"hostname": "sarah-desktop-12.holdingsinc.com",
"quarantine": 1623669514000,
"time": 1528807083000,
"endtime": 1587135192000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
"customFields": {
"MicrosoftDefenderFields": {
"OSArchitecture": "64-bit",
"OSBuild": "19043",
"OSPlatform": "Windows10",
"OSVersion": "21H1"
},
"Vuln-Microsoft-Defender": {
"CVE Count": "115",
"FieldOrder": "['CVE Count', 'Hostname', 'IP Address', 'Url', 'Model']",
"Hostname": "sarah-desktop-12.holdingsinc.com",
"IP Address": "10.12.14.2",
"Model": "Windows10",
"Url": "https://security.microsoft.com/machines/[placeholder]/vulnerabilities"
}
}
}
```
_Response is abbreviated._


###### Darktrace TSA VDI Devices

Devices created by the Darktrace TSA to represent VDI users also have a slightly different format. The vdihost array

describes the TSA server the user was detected upon:

```
{
"id": 123,
"did": 123,
"sid": -6,
"hostname": "VDI: user1234",
"firstSeen": 1635436041000,
"lastSeen": 1668607153000,
"typename": "virtualdesktop",
"typelabel": "Virtual Desktop",
"vdihost": [
{
"type": "vdi",
"ips": [
{
"ip": "10.10.10.10",
"time": 1668606199
}
]
}
]
}
...
```
_Response is abbreviated._

###### Darktrace/Endpoint Devices

Devices monitored by Darktrace/Endpoint cSensor agents will have additional data present:

- aghuuid represents a unique UUID of the cSensor agent.
- aghpublicip represents the public IP that the agent is communicating to the Darktrace/Endpoint infrastructure
from.
- aghasn and aghcountry are the ASN and country associated with the public IP above.
- interfaces is an array that describes all network interfaces associated with the monitored device.


```
{
"id": 123,
"aghuuid": "5b6fea29-74a6-482f-92c2-a90bf2ff50ed",
"aghpublicip": "172.217.169.36",
"aghasn": "AS15169 GOOGLE",
"aghcountry": "US",
"did": 123,
"sid": -11,
"hostname": "ws-199",
"firstSeen": 1641558623000,
"lastSeen": 1667815313000,
"os": "Windows 10 Enterprise 21H2",
"devicelabel": "Example",
"typename": "laptop",
"typelabel": "Laptop",
"credentials": [
{
"credential": "ad//b_ash",
"lastSeen": 1667657237000
}
],
"tags": [
{
"tid": 111,
"expiry": 0,
"thid": 127,
"name": "cSensor",
"data": {...},
"isReferenced": true
}
],
"interfaces": [
{
"mac": "00:12:34:ab:56:cd",
"vendor": "Example Vendor 1",
"ips": [
{
"ip": "10.10.10.10",
"sid": -11,
"hostname": "ws-199",
"time": 1667814649
}
]
},
...
{
"mac": "00:34:56:ab:78:cd",
"vendor": "Example Vendor 2",
"ips": [
{
"ip": "10.0.0.1",
"sid": -11,
"hostname": "ws-199",
"time": 1667814649
}
]
},
]
}
...
```
_Response is abbreviated._

###### Miscellaneous Fields

The generatedLabel field (boolean) will appear for devices with a device label generated by the system automatically.

This field is most frequently observed for inactive devices.


For example:

```
{
"id": 1234,
"did": 45392,
"sid": 3,
"time": 1701982903000,
"endtime": 1701983149000,
"generatedlabel": true,
"devicelabel": "Inactive device",
"typename": "desktop",
"typelabel": "Desktop"
}
```

## /DEVICESEARCH

The /devicesearch endpoint provides a highly filterable search capacity to interrogate the list of devices Darktrace has

seen on the network. It is more suited for inventory management and general queries than the /devices endpoint as it

provides sorting and string searching capabilities.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
count numeric The number of devices to return. If unspecified, defaults to 100. Maximum value is 300.
```
```
orderBy string
Orders the response by the specified filter, default value is lastSeen. Valid values are priority,
hostname, ip, macaddress, vendor, os, firstSeen, lastSeen, devicelabel or typelabel.
```
```
order string
Sets the sort order for returned devices as ascending or descending, can take asc or desc. Default is
ascending.
```
```
query string
An optional string search. Can query all fields or take a specific field filter from label, tag, type,
hostname, ip, mac, vendor and os.
```
```
offset numeric An offset for the results returned.
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
```
seensince string
```
```
Relative offset for activity. Devices with activity in the specified time period are returned. The format is
either a number representing a number of seconds before the current time, or a number with a modifier
such as second, minute, hour day or week (Minimum=1 second).
```
###### Notes

- The query parameter can take a string directly to search all key/value pairs (.e.g query="value") or be
    limited to a certain data type (.e.g query=label:"test"). Wildcards (*) are supported.

```
Multiple queries can be space-separated, for example query=tag:"*T*" label:"Test" or
query=type:"laptop" type:"desktop". Repeated field filters are treated as “or”. The space must be
percent-encoded when making the final request but not when producing the signature.
```
- The priority field will not be included in the response for a device if the value is 0.
- Returned data can be paginated by limiting the count value and making multiple requests, incrementing the
    offset value by the count value each time (e.g., count=50, multiple queries for
    offset=0, offset=50, offset=100). This is necessary for requests which return greater than 300 values.
- The default time frame is four weeks (28 days). This can be altered with the seensince parameter.


###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET a list of devices with “sarah” anywhere in the device information (e.g., hostname, label, tags):

```
https://[instance]/devicesearch?&query="sarah"
```
2. GET a list of devices tagged with “Security Device”, ordered by oldest lastSeen time:

```
https://[instance]/devicesearch?query=tag:"Security Device"&orderBy=lastSeen&order=asc
```
```
If using cUrl, ensure the space is percent-encoded when making the final request
```
3. GET a list of 10 highest priority devices with any “Antigena” tag in the subnet 10.0.1.0/24, sorted by descending
    priority:

```
https://[instance]/devicesearch?count=10&query=tag:"Antigena*"
ip:"10.0.1.*"&orderBy=priority&order=desc
```
```
If using cUrl, ensure the space is percent-encoded when making the final request
```
###### Example Response


_Request: /devicesearch?query=“sarah”_

```
{
"totalCount": 2185,
"devices": [
{
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"did": 316,
"sid": 23,
"hostname": "Sarah Development",
"firstseen": 1528807092000,
"lastseen": 1581510431000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
},
{
"ip": "192.168.120.39",
"ips": [
{
"ip": "192.168.120.39",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 6
}
],
"did": 2719,
"sid": 6,
"hostname": "sarah's iphone",
"firstSeen": 1576581851000,
"lastSeen": 1582131590000,
"os": "Mac OS X",
"typename": "mobile",
"typelabel": "Mobile",
"tags": [
{
"tid": 17,
"expiry": 0,
"thid": 17,
"name": "iOS device",
"restricted": false,
"data": {
"auto": false,
"color": 181,
"description": "",
"visibility": "Public"
},
"isReferenced": true
}
]
}
]
}
```

## /DEVICESEARCH RESPONSE SCHEMA

#### Response Schema - Network Device

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
totalCount numeric 2191
The total number of devices that meet the query
parameters.
```
```
devices array
An array of devices that meet the query
parameters.
```
```
devices.did numeric 227 The “device id”, a unique identifier.
```
```
devices.macaddress string 56:2d:4b:9c:18:42
The current MAC address associated with the
device.
```
```
devices.vendor string Apple The vendor of the device network card as
derived by Darktrace from the MAC address.
```
```
devices.ip string 10.0.18.224 The current IP associated with the device.
```
```
devices.ips array IPs associated with the device historically.
```
```
devices.ips.ip string 10.0.18.224 A historic IP associated with the device.
```
```
devices.ips.timems numeric 1586937881000
The time the IP was last seen associated with
that device in epoch time.
```
```
devices.ips.time string 2020-04-15 08:04:41
The time the IP was last seen associated with
that device in readable format.
```
```
devices.ips.sid numeric 10 The subnet id for the subnet the IP belongs to.
```
```
devices.sid numeric 10 The subnet id for the subnet the device is
currently located in.
```
```
devices.hostname string sarah-desktop-12 The current device hostname.
```
```
devices.firstSeen numeric 1528810000000 The first time the device was seen on the
network.
```
```
devices.lastSeen numeric 1585310000000
The last time the device was seen on the
network.
```
```
devices.os string
Linux 3.11 and
newer
```
```
The device operating system if Darktrace is able
to derive it.
```
```
devices.devicelabel string Sarah Development
An optional label applied to the device in the
Device Admin page.
```
```
devices.typename string desktop The device type in system format.
```
```
devices.typelabel string Desktop The device type in readable format.
```
```
devices.tags array An object describing tags applied to the device.
```
devices.tags.tid numeric (^73) The “tag id”. A unique value.
devices.tags.expiry numeric 0
The expiry time for the tag when applied to a
device.
devices.tags.thid numeric 78 The “tag history” id. Increments if the tag is
edited.
devices.tags.name string Test Tag
The tag label displayed in the user interface or in
objects that reference the tag.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

devices.tags.restricted boolean FALSE
Indicates a read-only tag - these tags can only be
modified or applied by Darktrace.

devices.tags.data object An object containing information about the tag.

devices.tags.data.auto boolean FALSE Whether the tag was auto-generated.

devices.tags.data.color numeric 134
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.

devices.tags.data.description string
Testing the use of
tags.

```
An optional description summarizing the
purpose of the tag.
```
devices.tags.data.visibility string Public A system field.

devices.tags.isReferenced boolean FALSE
Whether the tag is used by one or more model
components.


###### Example Response

_Request: /devicesearch?&query=“sarah”_

```
{
"totalCount": 2185,
"devices": [
{
"id": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"did": 316,
"sid": 23,
"hostname": "Sarah Development",
"firstseen": 1528807092000,
"lastseen": 1581510431000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
},
{
"id": 2719,
"ip": "192.168.120.39",
"ips": [
{
"ip": "192.168.120.39",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 6
}
],
"did": 2719,
"sid": 6,
"hostname": "sarah's iphone",
"firstSeen": 1576581851000,
"lastSeen": 1582131590000,
"os": "Mac OS X",
"typename": "mobile",
"typelabel": "Mobile",
"tags": [
{
"tid": 17,
"expiry": 0,
"thid": 17,
"name": "iOS device",
"restricted": false,
"data": {
"auto": false,
"color": 181,
"description": "",
"visibility": "Public"
},
"isReferenced": true
}
]
}
]
}
```

#### Response Schema - SaaS Device

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
totalCount numeric 1
The total number of devices that meet the query
parameters.
```
```
devices array
```
```
An array of devices that meet the query
parameters.
```
```
devices.did numeric 1234 The “device id”, a unique identifier.
```
```
devices.sid numeric -9
```
```
The subnet id for the subnet the device is
currently located in.
```
```
devices.saasmodule string Office365
```
```
The Darktrace/Apps, Cloud or Zero Trust
module which observed the device entity. This
field appears for user devices on endpoints
such as /devicesearch, /modelbreaches
and /tags. It is not returned by the /devices
endpoint.
```
```
devices.hostname string
```
```
SaaS::Office365:
benjamin.ash@holdingsinc.com
```
```
The SaaS device name as constructed by
Darktrace from the user name and SaaS service.
```
```
devices.firstSeen numeric 1683885806000
The first time the device was seen on the
network.
```
```
devices.lastSeen numeric 1704361887000
The last time the device was seen on the
network.
```
```
devices.typename string saasprovider The device type in system format.
```
```
devices.typelabel string SaaS Provider The device type in readable format.
```
```
devices.credentials array
An array of credentials associated with the
device entity.
```
```
devices.credentials.credential string benjamin.ash@holdingsinc.com
The time the credential was last seen
associated with that device in epoch time.
```
```
devices.credentials.lastSeen numeric 1704359090000 A credential associated with the device entity.
```
```
devices.tags array An object describing tags applied to the device.
```
```
devices.tags.tid numeric 531 The “tag id”. A unique value.
```
```
devices.tags.thid numeric 538
The “tag history” id. Increments if the tag is
edited.
```
```
devices.tags.name string Global Admin (CG)
The tag label displayed in the user interface or in
objects that reference the tag.
```
```
devices.tags.restricted boolean FALSE
```
```
Indicates a read-only tag - these tags can only
be modified or applied by Darktrace.
```
```
devices.tags.data object An object containing information about the tag.
```
```
devices.tags.data.color numeric 100
```
```
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.
```
```
devices.tags.data.description string
```
```
(SaaS) This device has global admin
privileges. This tag is automatically applied
to and removed from devices.
```
```
An optional description summarizing the
purpose of the tag.
```
```
devices.tags.isReferenced boolean FALSE
Whether the tag is used by one or more model
components.
```
```
devices.tags.data.auto boolean FALSE Whether the tag was auto-generated.
```

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
devices.tags.data.visibility string Public A system field.
```
```
devices.customFields object
```
```
An object containing additional custom fields
with data about the devices. Custom fields
include SaaS context data and notes added to
the device on the Device Admin page.
```
###### Example Response

_Request: /devicesearch?count=1&query=hostname%3A”office365”_

```
{
"totalCount": 1,
"devices": [
{
"did": 1234,
"sid": -9,
"saasmodule": "Office365",
"hostname": "SaaS::Office365: benjamin.ash@holdingsinc.com",
"firstSeen": 1683885806000,
"lastSeen": 1704361887000,
"typename": "saasprovider",
"typelabel": "SaaS Provider",
"credentials": [
{
"credential": "benjamin.ash@holdingsinc.com",
"lastSeen": 1704359090000
}
],
"tags": [
{
"tid": 531,
"thid": 538,
"name": "Global Admin (CG)",
"restricted": false,
"data": {
"color": 100,
"description": "(SaaS) This device has global admin privileges. This tag is
automatically applied to and removed from devices."
},
"isReferenced": false
}
],
"customFields": {...}
}
]
}
```
_Response is abbreviated._


## /DEVICESUMMARY

The /devicesummary endpoint returns contextual information for a device, aggregated from /devices,

```
/similardevices, /modelbreaches, /deviceinfo and /details. When a did is specified, the endpoint returns
```
the information displayed in the UI “Device Summary” window.

Information from /devices is at the time of query; other endpoints cover a 28 day period.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
did numeric Identification number of a device modelled in the Darktrace system. Required.
```
###### Notes

- Depending on the device type or whether any relevant model breaches have occurred, some endpoints may not
return any data. In this case, the object will return empty.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET contextual information for the devices 10.10.10.10 with did=25:

```
https://[instance]/devicesummary?did=25
```

###### Example Response

_Request: /devicesummary?did=316

```
{
"data": {
"devices": {
"id": 316,
"ip": "10.0.56.12",
...
},
"similardevices": [
{
"did": 34,
"score": 100,
"ip": "10.91.44.12",
...
},
...
],
"deviceinfo": {
"deviceInfo": [
{
"did": 316,
"similarityScore": 100,
"graphData": [
{
"time": 1582243200000,
"count": 0
},
...
],
"info": {
...
}
],
"devices": [
{
"did": 34,
"score": 100,
"ip": "10.91.44.12",
...
},
...
]
},
"details": [],
"modelbreaches": [
{
"creationTime": 1582213002000,
"commentCount": 0,
"pbid": 123,
"time": 1582212986000,
"model": {
"then":{
...
}
},
"now": {
...
}
},
"triggeredComponents": [
{
...
```
_continued..._


```
}
],
"score": 0.325
},
...
]
}
}
```
_Example is heavily abbreviated as response contains output from other API endpoints in their entirety._


## /DEVICESUMMARY RESPONSE SCHEMA

This endpoint aggregates output from other API endpoints. Please refer to the schemas for these endpoints for specific

field information.

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
data
An object containing the output aggregated
from other endpoints queried.
```
```
data.devices object -
```
```
Contains a device object, equivalent to querying
/devices for the did. Please refer to
/devices Response Schema.
```
```
data.similardevices object -
```
```
Contains multiple device objects considered
similar to this device by the system, equivalent to
querying /similardevices for the did.
Please refer to
/similardevices Response Schema.
```
```
data.details object -
```
```
Infrequently populated. When populated,
contains information equivalent to querying
/details for the did. Please refer to
/details Response Schema.
```
```
data.deviceinfo object -
```
```
Contains data about how the device has
interacted with other devices on the network
over an historic 28 day period, equivalent to
querying
/deviceinfo?
showallgraphdata=true&fulldevicedeta
ils=true
for the did. Please refer to
/deviceinfo Response Schema.
```
```
data.modelbreaches object -
```
```
Contains model breach data for the selected
device over an historic 28 day period , equivalent
to querying
/
modelbreaches&deviceattop=false&incl
udeacknowledged=true&historicmodelon
ly=false
for the did. Please refer to
/modelbreaches Response Schema.
```

###### Example Response

```
{
"data": {
"devices": {
"id": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"did": 316,
"sid": 23,
"hostname": "Sarah Development",
"quarantine": 1623669514000,
"time": 1528807083000,
"endtime": 1587135192000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
"customFields": {
"DT-MANUAL": {
"notes": "Test Note"
}
},
"similardevices": [
{
"did": 34,
"score": 100,
"ip": "10.91.44.12",
"ips": [
{
"ip": "10.91.44.12",
"timems": 1581933600000,
"time": "2020-02-17 10:00:00",
"sid": 7
}
],
"sid": 7,
"firstSeen": 1550492002000,
"lastSeen": 1581935040000,
"os": "Linux 2.2.x-3.x",
"typename": "desktop",
"typelabel": "Desktop"
},
...
],
"deviceinfo": {
"deviceInfo": [
{
"did": 316,
"similarityScore": 100,
"domain": "google.com",
"graphData": [
{
"time": 1582243200000,
"count": 0
},
...
```
_continued..._


```
],
"info": {
"totalUsed": 302,
"totalServed": 0,
"totalDevicesAndPorts": 302,
"devicesAndPorts": [],
"externalDomains": [
{
"domain": "google.com",
"size": 100
}
],
"portsUsed": [
{
"port": 443,
"size": 100,
"firstTime": 1584529392000
}
],
"portsServed": [],
"devicesUsed": [
{
"did": 0,
"size": 100,
"firstTime": 1584529392000
}
],
"devicesServed": []
}
}
],
"devices": [
{
"did": 34,
"score": 100,
"ip": "10.91.44.12",
"ips": [
{
"ip": "10.91.44.12",
"timems": 1581933600000,
"time": "2020-02-17 10:00:00",
"sid": 7
}
],
"sid": 7,
"firstSeen": 1550492002000,
"lastSeen": 1581935040000,
"os": "Linux 2.2.x-3.x",
"typename": "desktop",
"typelabel": "Desktop"
},
{
"did": 72,
"score": 99,
...
},
{
"did": 78,
"score": 72,
...
},
...
]
```
_continued..._


```
},
"details": [],
"modelbreaches": [
{
"creationTime": 1582213002000,
"commentCount": 0,
"pbid": 123,
"time": 1582212986000,
"model": {
"then":{
...
}
},
"now": {
...
}
},
"triggeredComponents": [
{
"time": 1582212985000,
"cbid": 305422,
"cid": 265,
"chid": 265,
"size": 3,
"threshold": 2,
"interval": 14400,
"logic": {
"data": {
"left": "A",
"operator": "AND",
"right": {
"left": "B",
"operator": "AND",
"right": {
...
}
},
"version": "v0.1"
},
"metric": {
"mlid": 1,
"name": "externalconnections",
"label": "External Connections"
},
"device": {
"did": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"sid": 23,
"hostname": "Sarah Development",
"firstSeen": 1581591070000,
"lastSeen": 1582645442000,
"typename": "desktop",
"typelabel": "Desktop"
},
"triggeredFilters": [
```
_continued..._


```
{
"cfid": 2087,
"id": "A",
"filterType": "Rare external endpoint",
"arguments": {
"value": 90
},
"comparatorType": ">",
"trigger": {
"value": "94"
}
},
...
]
}
],
"score": 0.325
},
...
]
}
}
```
_Response is abbreviated._


## /ENDPOINTDETAILS

```
/endpointdetails returns location, IP address and (optionally) device connection information for external IPs and
```
hostnames. It can be used to return intel about endpoints and the devices that have been seen accessing them.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
additionalinfo boolean Return additional information about the endpoint.
```
```
devices boolean Return a list of devices which have recently connected to the endpoint.
```
```
score boolean Return rarity data for this endpoint.
```
```
hostname string Return data for this hostname.
```
```
ip string Return data for this ip address.
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
```
score boolean Return rarity data for this endpoint.
```
###### Notes

- The “popularity” score = 100 – (IP or domain) rarity score.
- For hostname queries, additionalinfo=true will add an ips object and a locations object with details
    of the IP addresses Darktrace has seen associated with the hostname and the physical locations of those IPs
    where derivable.
- Queries for IPs that are internal (or treated as such) will return "name": "internal_ip", in the response and
    different key/value fields.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET details for 8.8.8.8:

```
https://[instance]/endpointdetails?ip=8.8.8.8
```
2. GET details for darktrace.com, including a list of devices that have connected to it:

```
https://[instance]/endpointdetails?hostname=darktrace.com&devices=true
```

###### Example Response

_Request: /endpointdetails?hostname=darktrace.com&devices=true_

```
{
"hostname": "darktrace.com",
"firsttime": 1528807217000,
"devices": [
{
"did": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"sid": 23,
"hostname": "Sarah Development",
"firstSeen": 1528807078000,
"lastSeen": 1581960902000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop"
},
...
]
```
_Response is abbreviated._


## /ENDPOINTDETAILS RESPONSE SCHEMA

#### Response Schema - ip=[external IP]

###### devices=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
ip string 8.8.8.8 The IP being queried.
```
```
firsttime numeric 1528810000000
The first time the queried IP was seen on the
network in epoch time.
```
```
country string United States The country that the IP is located in.
```
```
asn string AS15169 Google LLC The ASN for the IP.
```
```
city string If available, the city the IP is located in.
```
```
region string North America The geographical region the IP is located in.
```
```
name string If an internal IP, this field will return “internal_ip”
```
```
longitude numeric -97.822 For the reported IP location, the longitude value
to plot the IP on a map.
```
```
latitude numeric 37.751
For the reported IP location, the latitude value to
plot the IP on a map.
```
###### Example Response

```
{
"ip": "172.217.169.36",
"firsttime": 1528807105000,
"country": "United States",
"asn": "AS15169 Google LLC",
"city": "",
"region": "North America",
"name": "",
"longitude": -97.822,
"latitude": 37.751
}
```

###### devices=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
ip string 8.8.8.8 The IP being queried.
```
```
firsttime numeric 1586937600000
The first time the queried IP was seen on the
network in epoch time.
```
```
country string United States The country that the IP is located in.
```
```
asn string AS15169 Google LLC The ASN for the IP.
```
```
city string If available, the city the IP is located in.
```
```
region string North America The geographical region the IP is located in.
```
```
name string If an internal IP, this field will return “internal_ip”
```
```
longitude numeric -97.822
For the reported IP location, the longitude value
to plot the IP on a map.
```
```
latitude numeric 37.751 For the reported IP location, the latitude value to
plot the IP on a map.
```
```
devices array
An array of devices that have been seen
connecting to the IP.
```
devices.did numeric (^228) The “device id”, a unique identifier.
devices.ip string 10.12.14.2 The current IP associated with the device.
devices.ips array IPs associated with the device historically.
devices.ips.ip string 10.12.14.2 A historic IP associated with the device.
devices.ips.timems numeric 1586937600000
The time the IP was last seen associated with
that device in epoch time.
devices.ips.time string 2020-04-15 08:00:00 The time the IP was last seen associated with
that device in readable format.
devices.ips.sid numeric 14 The subnet id for the subnet the IP belongs to.
devices.sid numeric 14
The subnet id for the subnet the device is
currently located in.
devices.hostname string ws83 The current device hostname.
devices.firstSeen numeric 1582720000000
The first time the device was seen on the
network.
devices.lastSeen numeric 1584990000000
The last time the device was seen on the
network.
devices.os string Windows NT kernel
The device operating system if Darktrace is able
to derive it.
devices.typename string desktop The device type in system format.
devices.typelabel string Desktop The device type in readable format.


###### Example Response

```
{
"ip": "172.217.169.36",
"firsttime": 1528807105000,
"country": "United States",
"asn": "AS15169 Google LLC",
"city": "",
"region": "North America",
"name": "",
"longitude": -97.822,
"latitude": 37.751,
"devices": [
{
"did": 3870,
"macaddress": "56:2d:4b:9c:18:42",
"vendor": "LCFC(HeFei) Electronics Technology co., ltd",
"ip": "10.0.18.224",
"ips": [
{
"ip": "10.0.18.224",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 17
}
],
"sid": 17,
"firstSeen": 1564064256000,
"lastSeen": 1587137042000,
"os": "Windows NT kernel",
"typename": "desktop",
"typelabel": "Desktop"
}
]
}
```
#### Response Schema - hostname

###### devices=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
hostname string darktrace.com The hostname being queried.
```
```
firsttime numeric 1528810000000
The first time the queried hostname was seen on
the network in epoch time.
```
###### Example Response

```
{
"hostname": "darktrace.com",
"firsttime": 1528807217000
}
```

###### devices=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
hostname string darktrace.com The IP being queried.
```
```
firsttime numeric 1528810000000
The first time the queried IP was seen on the
network in epoch time.
```
```
devices array
An array of devices that have connected to this
endpoint.
```
devices.did numeric (^227) The “device id”, a unique identifier.
devices.ip string 10.0.18.224 The current IP associated with the device.
devices.ips array IPs associated with the device historically.
devices.ips.ip string 10.0.18.224 A historic IP associated with the device.
devices.ips.timems numeric 1586937881000
The time the IP was last seen associated with
that device in epoch time.
devices.ips.time string 2020-04-15 08:04:41
The time the IP was last seen associated with
that device in readable format.
devices.ips.sid numeric 10 The subnet id for the subnet the IP belongs to.
devices.sid numeric 10 The subnet id for the subnet the device is
currently located in.
devices.hostname string sarah-desktop-12 The current device hostname.
devices.firstSeen numeric 1528810000000
The first time the device was seen on the
network.
devices.lastSeen numeric 1585310000000
The last time the device was seen on the
network.
devices.os string Windows NT kernel
The device operating system if Darktrace is able
to derive it.
devices.typename string desktop The device type in system format.
devices.typelabel string Desktop The device type in readable format.


###### Example Response

```
{
"hostname": "darktrace.com",
"firsttime": 1528807217000,
"devices": [
{
"did": 3870,
"macaddress": "56:2d:4b:9c:18:42",
"vendor": "LCFC(HeFei) Electronics Technology co., ltd",
"ip": "10.0.18.224",
"ips": [
{
"ip": "10.0.18.224",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 17
}
],
"sid": 17,
"firstSeen": 1564064256000,
"lastSeen": 1587137042000,
"os": "Windows NT kernel",
"typename": "desktop",
"typelabel": "Desktop"
}
]
}
```
#### Response Schema - ip=[internal IP]

###### devices=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
subnetlabel string Finance
The label assigned to the subnet in the Threat
Visualizer that the IP is contained within.
```
```
subnetid string 18
A unique “subnet id” for the subnet that the IP is
contained within.
```
```
subnetnetwork string 10.0.18.0/24
The IP address range that describes the subnet
that the IP is contained within.
```
```
country string The country that the IP is located in.
```
```
city string If available, the city the IP is located in.
```
```
region string The geographical region the IP is located in.
```
```
name string internal_ip If an internal IP, this field will return “internal_ip”
```
```
longitude numeric -0.01
The longitude value provided to Subnet Admin
which is used to plot the subnet on a map.
```
```
latitude numeric 0.01
The latitude value provided to Subnet Admin
which is used to plot the subnet on a map.
```

###### Example Response

```
{
"subnetlabel": "",
"subnetid": "19",
"subnetnetwork": "10.160.14.0/24",
"country": "",
"city": "",
"region": "",
"name": "internal_ip",
"longitude": 0.0,
"latitude": 0.0
}
```
###### devices=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
subnetlabel string Finance
The label assigned to the subnet in the Threat
Visualizer that the IP is contained within.
```
```
subnetid string 18
A unique “subnet id” for the subnet that the IP is
contained within.
```
```
subnetnetwork string 10.0.18.0/24
The IP address range that describes the subnet
that the IP is contained within.
```
```
country string The country that the IP is located in.
```
```
city string If available, the city the IP is located in.
```
```
region string The geographical region the IP is located in.
```
```
name string internal_ip If an internal IP, this field will return “internal_ip”
```
```
longitude numeric -0.01
The longitude value provided to Subnet Admin
which is used to plot the subnet on a map.
```
```
latitude numeric 0.01
The latitude value provided to Subnet Admin
which is used to plot the subnet on a map.
```
```
devices array
An array of devices that have connected to the
IP.
```
```
devices.did numeric 228 The “device id”, a unique identifier.
```
```
devices.ip string 10.12.14.2 The current IP associated with the device.
```
```
devices.ips array IPs associated with the device historically.
```
```
devices.ips.ip string 10.12.14.2 A historic IP associated with the device.
```
```
devices.ips.timems numeric 1586937600000
The time the IP was last seen associated with
that device in epoch time.
```
```
devices.ips.time string 2020-04-15 08:00:00
The time the IP was last seen associated with
that device in readable format.
```
```
devices.ips.sid numeric 14 The subnet id for the subnet the IP belongs to.
```
```
devices.sid numeric 14
The subnet id for the subnet the device is
currently located in.
```
```
devices.hostname string ws83 The current device hostname.
```

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
devices.firstSeen numeric 1582720000000
The first time the device was seen on the
network.
```
```
devices.lastSeen numeric 1584990000000 The last time the device was seen on the
network.
```
```
devices.os string Windows NT kernel
The device operating system if Darktrace is able
to derive it.
```
```
devices.typename string desktop The device type in system format.
```
```
devices.typelabel string Desktop The device type in readable format.
```
###### Example Response

```
{
"subnetlabel": "",
"subnetid": "19",
"subnetnetwork": "10.160.14.0/24",
"country": "",
"city": "",
"region": "",
"name": "internal_ip",
"longitude": 0.0,
"latitude": 0.0
"devices": [
{
"did": 3870,
"macaddress": "56:2d:4b:9c:18:42",
"vendor": "LCFC(HeFei) Electronics Technology co., ltd",
"ip": "10.0.18.224",
"ips": [
{
"ip": "10.0.18.224",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 17
}
],
"sid": 17,
"firstSeen": 1564064256000,
"lastSeen": 1587137042000,
"os": "Windows NT kernel",
"typename": "desktop",
"typelabel": "Desktop"
}
]
}
```

## /ENUMS

The /enums endpoint returns the corresponding string values for numeric codes (enumerated types) used in many API

responses. As enums are derived for use in models, the selection of enums and enum categories that return will be

dependent on your environment and the modules and integrations deployed.

The list of enums can be filtered using the responsedata parameter. Using extensions is no longer supported.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET a list of all enumerated types:

```
https://[instance]/enums
```
2. GET a list of all enumerated country types:

```
https://[instance]/enums?responsedata=countries
```
###### Example Response

_Request: /enums_

```
[
{
"code": "0",
"name": "None",
"hidden": true
"code": "1",
"name": "Unknown"
},
{
"code": "2",
"name": "Laptop"
},
{
"code": "3",
"name": "Mobile"
},
...
]
```
_Response is abbreviated._


## /ENUMS RESPONSE SCHEMA

Please note, the name of some keys may have changed due to changes to product taxonomy. For example, the key “AGE

Model” is now “Darktrace/Email Model”. These changes are minimal and will be specific to your environment.

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
Country array
An array of countries and their corresponding
system codes.
```
```
Country.code string AD The country code.
```
```
Country.name string Andorra The readable country name.
```
```
Matching metrics array
```
```
An array of standard metrics used throughout
the Threat Visualizer interface. The standard
metrics available in your environment may differ
from this list due to additional protocols seen or
additional modules contributing data.
```
```
Matching metrics.code string activeconnections The system name for the metric.
```
```
Matching metrics.name string Active Connections The readable metric name.
```
```
DNS response code array
An array of DNS Response codes that may be
seen in DNS requests.
```
```
DNS response code.code string NOERROR The system name for the DNS Code.
```
```
DNS response code.name string NOERROR The readable DNS Code name.
```
```
Proxied connection array
Boolean values for whether the connection was
proxied.
```
```
Proxied connection.code string TRUE The system code for the boolean.
```
```
Proxied connection.name string TRUE The readable representation of the boolean.
```
```
Trusted hostname array
Boolean values for whether the hostname is
trusted.
```
```
Trusted hostname.code string TRUE The system code for the boolean.
```
```
Trusted hostname.name string TRUE The readable representation of the boolean.
```
```
Day of the week array An array of days of the week.
```
```
Day of the week.code string Sunday The system name for the day.
```
```
Day of the week.name string Sunday The readable day of the week.
```
```
System message array
An array of system messages that may be fired
as notices.
```
```
System message.code string IP range excluded The system message code.
```
```
System message.name string IP range excluded The system message text.
```
```
Internal source device type array
An array of device types that an internal source
device may be identified as.
```
Internal source device type.code string (^2) The system code for the device type.
Internal source device type.name string Laptop The readable device type.
Internal destination device type array
An array of device types that an internal
destination device may be identified as.


```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
Internal destination device type.code string 2 The system code for the device type.
```
```
Internal destination device type.name string Laptop The readable device type.
```
```
Protocol array
An array of network protocols that may be
identified within the network.
```
```
Protocol.code string 1 The system code for the protocol.
```
```
Protocol.name string ICMP The readable protocol name.
```
```
Application protocol array
An array of application protocols that may be
identified within the network.
```
Application protocol.code string (^1053) The system code for the protocol.
Application protocol.name string BITTORRENT The readable protocol name.
Malformed traffic type array
An array of types of malformed traffic which may
be detected in the traffic fed to Darktrace, and
their corresponding system codes.
Malformed traffic type.code string bad_HTTP_reply The system code for the traffic type.
Malformed traffic type.name string Bad HTTP reply The readable traffic type.
Vendor array
An array of network card vendors and their
corresponding system codes.
Vendor.code string -16579579 The system code for the vendor.
Vendor.name string Cisco Systems, Inc The actual vendor name.
Destination Resource Type array
An array of destination resource types for SaaS
resources.
Destination Resource Type.name string File The system code for the resource type.
Destination Resource Type.code string File The readable resource type.
Access Method array
An array of access method types for SaaS
resources.
Access Method.name string API The system code for the access type.
Access Method.code string API The readable access method.
Resource Type array An array of resource types for SaaS resources.
Resource Type.name string File The system code for the resource type.
Resource Type.code string File The readable resource type.
Action Direction array
An array of action directions that a SaaS actor
can perform - denotes whether the action was
performed by or performed on a user.
Action Direction.name string Outbound The system code for the action direction.
Action Direction.code string Outbound The readable direction.

###### Example Response

_Request: /enums_


```
{
"Country": [
{
"code": "0",
"name": "Unknown"
}
...
]
"Matching metrics": [
{
"code": "activeconnections",
"name": "Active Connections"
},
...
```
_Response is abbreviated._


## /FILTERTYPES

```
/filtertypes returns all internal Darktrace filters used in the Model Editor, their filter type (for example, boolean or
```
numeric) and the available comparators.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET a list of all filter types:

```
https://[instance]/filtertypes
```
###### Example Response

_Request: /filtertypes_


```
[
...
{
"filtertype": "Data ratio",
"valuetype": "numeric",
"comparators": [
"<",
"<=",
"=",
"!=",
">=",
">"
]
},
{
"filtertype": "Tagged internal destination",
"valuetype": "id",
"comparators": [
"has tag",
"does not have tag"
]
},
{
"filtertype": "Tagged internal source",
"valuetype": "id",
"comparators": [
"has tag",
"does not have tag"
]
},
{
"filtertype": "HTTP no referrer",
"valuetype": "flag",
"comparators": [
"is"
]
}
...
]
```
_Response is abbreviated._


## /FILTERTYPES RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
filtertype string Destination IP The filter name.
```
```
valuetype string ipv4 The data type expected by the filter.
```
```
graphable boolean TRUE Optional field. Will return as “true” if the filter can
be used on a graph.
```
```
comparators array matches
The comparators available when creating model
components or filtering using the filtertype.
```
###### Example Response

_Request: /filtertypes_

```
[
{
"filtertype": "Product",
"valuetype": "string",
"comparators": [
"matches",
"does not match",
"contains",
"does not contain",
"matches regular expression",
"does not match regular expression",
"is longer than",
"is shorter than"
]
},
{
"filtertype": "Volume Size",
"valuetype": "numeric",
"comparators": [
"<",
"<=",
"=",
"!=",
">=",
">"
]
},
...
```
_Response is abbreviated._


## /INTELFEED

```
/intelfeed is the programmatic way to access Watched Domains (Customer Portal), a list of domains, IPs and
```
hostnames utilized by the Darktrace system, Darktrace Inoculation and STIX/TAXII integration to create model breaches.

Watched domains are categorized by sources: if no source is specified in a request, the source string will be set to “default”.

Multiple watched domains can be added and removed in one request.

```
POST requests to these endpoints can be made with parameters or JSON (6.0+).
```
###### Request Type(s)

```
[GET] [POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
addentry string Add an external domain, hostname or IP address. Available for POST requests.
```
```
addlist string
```
```
Add a new line or comma separated list of external domains, hostnames and IP addresses. Available for POST
requests.
```
```
description string
```
```
Provide a description for added entries. The description must be under 256 characters. Available for POST
requests
```
```
expiry string Set an expiration time for added items. Available for POST requests
```
```
hostname boolean Set to true to treat the added items as hostnames rather than domains. Available for POST requests.
```
```
removeall boolean Remove all external domains, hostnames and IP addresses.
```
```
removeentry string
```
```
Remove an external domain, hostname or IP address. A source must also be defined if multiple sources are in
place.
```
```
source string
```
```
Provide a source for added entries or restrict a retrieved list of entries to a particular source. A source is a
textual label used to manage multiple lists of entities. Sources must be under 64 characters in length. The
source of a watched endpoint entry can be used as a filter in models. A single entry can belong to any
number of sources. Available for POST requests.
```
```
sources boolean Return the current set of sources rather than the list of watched endpoint/intelfeed entries.
```
```
fulldetails boolean Return full details about expiry time and description for each entry.
```
```
iagn boolean
Enables automatic Darktrace RESPOND/Network (formerly Antigena Network) actions against the endpoint.
Not applicable to IP ranges. Available for POST requests.
```
###### Notes

- The removeall and addlist parameters can be used together
- When supplying a description, do not use quotes around the string - this will result in a double-quoted string.
- Hostnames can be supplied using the hostname=true parameter. Hostnames will be treated as exact values
    and are indicated on the Watched Domains list with a *.
- The removeall parameter will remove all watched domain entries, regardless of source.


###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET the intelfeed list for the default source:

```
https://[instance]/intelfeed
```
2. GET a list of sources for entries on the intelfeed list:

```
https://[instance]/intelfeed?sources=true
```
3. GET the intel feed list for all entries under the ‘CustomSet1’ source:

```
https://[instance]/intelfeed?source=CustomSet1
```
4. POST a new entry to the intel feed (example.com) with description ‘Test’ and source ‘test’

```
https://[instance]/intelfeed with body
{"addentry":"example.com","description":"test","source":"test"}
```
5. POST a list of entries to the intel feed with the source “ThreatIntel” and the entry description “Test”

```
https://[instance]/intelfeed with body
addlist=example1.com,example2.com,example3.com,example4.com&description=Test&source=Thre
atIntel
```
###### Example Response

_Request: /intelfeed?fulldetails=true_

```
[
{
"name": "example.net",
"description": "Test"
"expiry": "2020-04-03 15:23:20"
},
...
]
```
_Response is abbreviated._


## /INTELFEED RESPONSE SCHEMA

#### Response Schema

The response will be an array of domains.

###### Example Response

```
[
"example1.com",
"example2.com",
"0.0.0.0"
]
```
###### Response Schema - fulldetails=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
name string example1.com The domain, IP or hostname on the watch list.
```
```
description string
Example
description.
```
```
An optional description of why the entry has
been added.
```
```
expiry string 2020-12-31T12:00:00
An optional expiry time at which the entry will be
removed from the list.
```
```
strength numeric 100
```
```
A confidence score out of 100 - can be assigned
manually or by a populating threat intelligence
feed.
```
```
iagn boolean true
```
```
Whether the domain should trigger an automatic
Darktrace RESPOND/Network (formerly Antigena
Network) action if seen.
```
###### Example Response

```
[
{
"name": "example1.com",
"description": "Test"
},
{
"name": "example2.com",
"description": "Test"
},
{
"name": "example3.com",
"description": "Test"
},
{
"name": "example4.com",
"description": "Test"
},
{
"name": "example5.com",
"strength": "100",
"iagn": true
"expiry": "2020-04-03 15:23:20"
}
]
```

###### Response Schema - sources=true

The response will be an array of sources.

###### Example Response

```
[
"Default",
"Test",
"ThreatIntel"
]
```

## /MBCOMMENTS

The /mbcomments endpoint returns all comments across model breaches, or for a specific model breach.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
```
count numeric The number of comments to return. Only limits the number of comments within the specified timeframe.
```
```
pbid numeric Only return comments for the model breach with the specified ID.
```
###### Notes

- If not supplied, count will default to 100.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all comments on model breaches on August 19th 2020:

```
https://[instance]/mbcomments?starttime=1597795200000&endtime=1597881599000
```
2. GET all comments for a model breach with pbid=123:

```
https://[instance]/mbcomments?pbid=123
```

###### Example Response

_Request: /mbcomments_

```
[
{
"time": 1597837975000,
"pbid": 1432,
"username": "lryan",
"message": "Investigation completed",
"pid": 17,
"name": "Compliance::Messaging::Facebook Messenger"
},
{
"time": 1586937600000,
"pbid": 1329,
"username": "ajohnston",
"message": "Concerning behavior. Investigating possible compromise.",
"pid": 52,
"name": "Anomalous File::Masqueraded File Transfer"
}
]
```

## /MBCOMMENTS RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
time numeric 1597837975000
The time the comment was posted in epoch
time.
```
```
pbid numeric 1432
The “policy breach ID” of the model breach
commented on.
```
```
username string lryan The user who made the comment.
```
```
message string
Investigation
completed.
The comment text.
```
```
pid numeric 17 The “policy id” of the model breach that was
commented on.
```
```
name string
```
```
Compliance::Messagi
ng::Facebook
Messenger
```
```
Name of the model that was breached.
```
###### Example Response

```
[
{
"time": 1597837975000,
"pbid": 1432,
"username": "lryan",
"message": "Investigation completed",
"pid": 17,
"name": "Compliance::Messaging::Facebook Messenger"
},
{
"time": 1586937600000,
"pbid": 1329,
"username": "ajohnston",
"message": "Concerning behavior. Investigating possible compromise.",
"pid": 52,
"name": "Anomalous File::Masqueraded File Transfer"
}
]
```

## /METRICDATA

The /metricdata endpoint returns time series data for one or more metrics for a device. This information is shown in the

Threat Visualizer when the ‘Open Graph’ button is clicked after searching for a device in the Omnisearch bar.

To specify a metric, use the system name - the name field found on /metrics - rather than the label. For example,

when using the metric “External Data Transfer” (mlid=1), the system name “externaldatatransfervolume” must be

specified in the query.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
applicationprotocol string
```
```
This filter can be used to filter the returned data by application protocol. See /enums for the list of
application protocols.
```
```
breachtimes boolean Return additional information for the model breach times for the device.
```
```
ddid numeric Identification number of a destination device modelled in the Darktrace system to restrict data to.
```
```
destinationport numeric This filter can be used to filter the returned data by destination port.
```
```
did numeric Identification number of a device modelled in the Darktrace system.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
from string Start time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
fulldevicedetails boolean
```
```
Returns the full device detail objects for all devices referenced by data in an API response. Use of
this parameter will alter the JSON structure of the API response for certain calls.
```
```
interval numeric Time interval size to group data into in seconds. The maximum value for any interval is returned.
```
```
metric string Name of a metric. See /metrics for the full list of current metrics.
```
```
odid numeric
```
```
Other Device ID - Identification number of a device modelled in the Darktrace system to restrict
data to. Typically used with ddid to specify device pairs.
```
```
port numeric This filter can be used to filter the returned data by source or destination port.
```
```
protocol string This filter can be used to filter the returned data by IP protocol. See /enums for the list of protocols.)
```
```
sourceport numeric This filter can be used to filter the returned data by source port.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
to string End time of data to return in YYYY-MM-DD HH:MM:SS format.
```
###### Notes

- Time parameters must always be specified in pairs.
- To specify multiple metrics to return time-series data for, replace the metric parameter with metric1=,
    metric2=, etc. Multiple metric objects will then be returned.
- The interval value allows data to be grouped into wider ‘bars’ for time-series graphs. The default interval is 1
    minute (interval=60).
- breachtimes=true will return any model breaches that happened within the timeframe on the device or
    within the subnet specified. This parameter will alter the structure of the returned data.


###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all connections for the device with did=1 for 20th March 2020 at an interval of 1 hour:

```
https://[instance]/metricdata?
did=1&metric=connections&from=2020-03-20T00:00:00&to=2020-03-20T23:59:59&interval=3600
```
2. GET the number of TCP connections from the device with did=1 to the device with did=18 between 9am
    and 10am for 20th March 2020 at an interval of 5 minutes:

```
https://[instance]/metricdata?
metric=internalconnections&startTime=1584694800000&endTime=1584698400000&did=1&&ddid=18&
protocol=6&interval=300
```
###### Example Response

_Request:_

_/metricdata?_

_metric=externalconnections&startTime=1582900189000&endTime=1582921789000&did=1&interval=60&breachtimes=true_

```
[
{
"breachtimes": [
{
"pid": 341,
"pbid": 292504,
"score": 0.6043,
"name": "Compromise::Sustained SSL or HTTP Increase",
"time": 1582902068000
},
...
]
},
{
"metric": "externalconnections",
"data": [
{
"time": "2020-02-28 14:29:00",
"timems": 1582900140000,
"size": 14,
"in": 0,
"out": 14
},
{
"time": "2020-02-28 14:30:00",
"timems": 1582900200000,
"size": 18,
"in": 0,
"out": 18
},
]
}
]
```
_Response is abbreviated._


## /METRICDATA RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
metric string connections The metric data is returned for.
```
```
data array A list of time series data for the metric.
```
```
data.time string 2019-03-24 00:00:00 A timestamp in readable format for the data.
Time series data is grouped by intervals.
```
```
data.timems numeric 1550000000000
A timestamp in epoch time for the data. Time
series data is grouped by intervals.
```
data.size numeric (^12) The total size of the data (in and out).
data.in numeric 1
The number of inbound events or the total
amount of inbound data (metric-dependent)
seen during the time interval.
data.out numeric 11
The number of outbound events or the total
amount of outbound data (metric-dependent)
seen during the time interval.

###### Example Response

_Request: /metricdata?metric=connections&did=1_

```
[
{
"metric": "connections",
"data": [
{
"time": "2020-02-28 14:29:00",
"timems": 1582900140000,
"size": 14,
"in": 0,
"out": 14
},
{
"time": "2020-02-28 14:30:00",
"timems": 1582900200000,
"size": 18,
"in": 0,
"out": 18
},
...
]
}
]
```
_Response is abbreviated._


#### Response Schema - breachtimes=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
breachtimes array
An array of model breaches seen on the device
or subnet during the time window provided.
```
```
breachtimes.pid numeric 341 The “policy id” of the model that was breached.
```
```
breachtimes.pbid numeric 292504 The “policy breach ID” of the model breach.
```
```
breachtimes.score numeric 0.6043
The model breach score, represented by a value
between 0 and 1.
```
```
breachtimes.name string
```
```
Compromise::Sustain
ed SSL or HTTP
Increase
```
```
Name of the model that was breached.
```
```
breachtimes.time numeric 1583310000000
The timestamp when the record was created in
epoch time.
```
```
metric string connections The metric data is returned for.
```
```
data array A list of time series data for the metric.
```
```
data.time string 2020-03-15 09:52:11 A timestamp in readable format for the data.
Time series data is grouped by intervals.
```
```
data.timems numeric 1584265931000
A timestamp in epoch time for the data. Time
series data is grouped by intervals.
```
data.size numeric (^9) The total size of the data (in and out).
data.in numeric 0
The number of inbound events or the total
amount of inbound data (metric-dependent)
seen during the time interval.
data.out numeric 9
The number of outbound events or the total
amount of outbound data (metric-dependent)
seen during the time interval.


###### Example Response

_Request: /metricdata?metric=connections&breachtimes=true&did=1_

```
[
{
"breachtimes": [
{
"pid": 341,
"pbid": 292504,
"score": 0.6043,
"name": "Compromise::Sustained SSL or HTTP Increase",
"time": 1582902068000
},
...
]
},
{
"metric": "connections",
"data": [
{
"time": "2020-02-28 14:29:00",
"timems": 1582900140000,
"size": 14,
"in": 0,
"out": 14
},
{
"time": "2020-02-28 14:30:00",
"timems": 1582900200000,
"size": 18,
"in": 0,
"out": 18
},
]
}
]
```
_Response is abbreviated._


## /METRICS

This endpoint returns the list of metrics available for filtering other API calls and for use in model making.

See metrics (Customer Portal) for definitions of a subset of standard metrics available for model editing.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
###### Notes

- Metrics with a set value of “C” are used for visual analysis and are not available for model making.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET a list of all metrics available for models:

```
https://[instance]/metrics
```
2. GET information about the metric “Internal Data Transfer”:

```
https://[instance]/metrics/4
```

###### Example Response

_Request: /metrics/13_

```
{
"mlid": 13,
"name": "multicasts",
"label": "Multicasts",
"units": "",
"filtertypes": [
"Feature model",
"Process popularity",
"Destination IP",
"Protocol",
"Source port",
"Destination port",
"Same port",
"Application protocol",
"Internal source device type",
"Internal source",
"New connection",
"Unusual connectivity",
"Unusual incoming data volume",
"Unusual outgoing data volume",
"Unusual number of connections",
"Unusual sustained connectivity for group",
"Unusual individual connection for group",
"Unique ports",
"Time since first connection",
"Day of the week",
"Hour of the day"
],
"unitsinterval": 3600,
"lengthscale": 9999960
}
```

## /METRICS RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
mlid numeric 1 The “metric logic” id - unique identifier.
```
```
name string externalconnections
The metric which data is returned for in system
format.
```
```
label string
External
Connections
```
```
The metric which data is returned for in readable
format.
```
```
units string The units the metric is measured in, if applicable.
```
```
filtertypes array Direction An array of filters which can be used with this
metric.
```
```
unitsinterval numeric 3600 The default time interval for the metric.
```
```
lengthscale numeric 9999960 A system field.
```
###### Example Response

```
[
{
"mlid": 4,
"name": "internaldatatransfervolume",
"label": "Internal Data Transfer",
"set": "A",
"units": "bytes",
"filtertypes": [
"Feature model",
"DNS host lookup",
"Process popularity",
...
],
"unitsinterval": 3600,
"lengthscale": 9999960
},
...
]
```
_Response is abbreviated._


## /MODELS

The /models endpoint returns a list of all models that currently exist on the Threat Visualizer, including custom models and

de-activated models. The returned JSON does not contain full model logic - this can be sourced from the /components

endpoint using the numerical values in the data array as cid’s.

This endpoint only supports filtering on the uuid parameter. To search for models by any other attribute, the full list must

be returned and parsed.

As of Darktrace Threat Visualizer 6, models now include MITRE ATT&CK Mapping information, where relevant. The mitre

object will only appear for models which have been mapped.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
uuid string All models have a uuid and a pid. The uuid (universally unique identifier) is a 128-bit hexadecimal number.
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
###### Notes

- The uuid value is unique and consistent for models across Darktrace environments. The pid value is unique
only within the context of the given instance.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET a list of all models:

```
https://[instance]/models
```
2. GET the model “Anomalous File / Anomalous Octet Stream”:

```
https://[instance]/models?uuid=80010119-6d7f-0000-0305-5e0000000420
```
```
https://[instance]/models/12
```

###### Example Response

```
{
"name": "Anomalous Connection::New Internal TCP Callback",
"pid": 219,
"phid": 21888,
"uuid": "8aafe33f-eb10-45fe-9ace-66dda23f0cfa",
"logic": {
"data": [
23938,
23937
],
"type": "componentList",
"version": 1
},
"throttle": 3600,
"sharedEndpoints": true,
"actions": {
"alert": true,
"antigena": {},
"breach": true,
"model": true,
"setPriority": false,
"setTag": false,
"setType": false
},
"tags": [
"AP: Lateral Movement"
],
"interval": 30,
"delay": 0,
"sequenced": true,
"active": true,
"modified": "2022-07-27 16:06:12",
"activeTimes": {
"devices": {
"1234": [
{}
],
"5678": [
{}
]
},
"tags": {},
"type": "exclusions",
"version": 2
},
"autoUpdatable": true,
"autoUpdate": false,
"autoSuppress": true,
"description": "A device received an incoming connection, then proceeded to make an
outgoing connection back to the originator...",
"behaviour": "decreasing",
"defeats": [],
"created": {
"by": "System"
},
"edited": {
"by": "darktrace",
"userID": 2
},
"history": [
{
"modified": "2022-05-19 17:00:03",
```
_continued..._


```
"active": false,
"message": "ORed HTTPS with SSL",
"by": "System",
"phid": 19612
},
...
],
"message": "User set update to false via bulk edit.",
"version": 25,
"mitre": {
"tactics": [
"command-and-control",
"execution",
"lateral-movement"
],
"techniques": [
"T1203",
"T1210",
"T1219"
]
},
"priority": 2,
"category": "Informational",
"compliance": false
},
...
```
_Response is abbreviated._


## /MODELS RESPONSE SCHEMA

As of Darktrace Threat Visualizer 6, models now include MITRE ATT&CK Mapping information, where relevant. The mitre

object will only appear for models which have been mapped.

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
name string
```
```
Anomalous
File::Anomalous
Octet Stream
```
```
The name of the model.
```
pid numeric (^12) The “policy id” of the model.
phid numeric 2842
The model “policy history” id. Increments when
the model is modified.
uuid string
80010119-6d7f-0000-
0305-5e0000000420
A unique ID that is generated on creation of the
model.
logic object
A data structure that describes the conditions to
bring about a breach.
logic.data array 3621
If the model is a checklist type this will be a list of
component ID numbers. If this model is a
weighted type this will be a list of component ID,
weight object pairs.
logic.type string componentList The type of model.
logic.version numeric 1 A number representing the version of model
logic.
throttle numeric 3600
For an individual device, this is the value in
seconds for which this model will not fire again.
sharedEndpoints boolean FALSE
For models that contain multiple components
that reference an endpoint, this value indicates
whether all endpoints should be identical for the
model to fire.
actions object
The action to perform as a result of matching this
model firing.
actions.alert boolean TRUE
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
actions.antigena object
An object containing the Darktrace RESPOND
response to be applied as a result of the model
breaching.
actions.breach boolean TRUE
If true, generates a model breach that will appear
in the threat tray.
actions.model boolean TRUE
If true, creates an event in the device’s event log
without creating an alert/ model breach in the
threat tray.
actions.setPriority boolean FALSE
If no priority change action, a false boolean. If the
priority is to be changed on breach, the numeric
value it should become.
actions.setTag boolean FALSE
If no tag action, a false boolean. If a tag is to be
applied on model breach, a single number or
array of the system ID for the tag(s) to be applied.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

actions.setType boolean FALSE

```
If no change device type action is applied to the
model, a false boolean. If a change device type
action is to be applied on model breach, the
numeric system ID for the label to be applied.
```
tags array AP: Tooling DNS Server

interval numeric 0

```
Where a model contains multiple components,
this interval represents the time window in
seconds in which all the components should fire
for this model to be breached.
```
delay numeric 0

```
Minimum delay in seconds after a positive-
scoring component has fired before the overall
model score is calculated.
```
sequenced boolean FALSE

```
Whether the components are required to fire in
the specified order for the model breach to
occur.
```
active boolean TRUE Whether the model is enabled or disabled.

modified string 2023-08-15 12:27:32 The time in UTC at which the model was last
modified.

activeTimes object
An object describing device whitelisting or
blacklisting configured for this model.

activeTimes.devices object The device ids for devices on the list.

activeTimes.tags object A system field.

activeTimes.type string exclusions
The type of list: “restrictions” indicates a blacklist,
“exclusions” a whitelist.

activeTimes.version numeric 2 A system field.

autoUpdatable boolean FALSE Whether the model is suitable for auto update.

autoUpdate boolean TRUE Whether the model is enabled for auto update.

autoSuppress boolean TRUE
Whether the model will automatically be
suppressed in the case of over-breaching.

description string

```
A device has
downloaded a rare
data stream which
is not specifying a
specific data type.
\n\nAction:
Investigate the
endpoint the data
is
being sent from and
consider
downloading a PCAP
or reviewing the
hash if
you believe the
endpoint to be
untrustworthy.
```
```
The optional description of the model.
```
behaviour string decreasing
The score modulation function as set in the
editor.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

defeats array

```
An array of defeats applied to the model. Defeats
do not impact model auto-update eligibility. The
relationship between defeats is AND. Within the
array, single defeats appear as objects,
conditional defeats appear as arrays of multiple
defeat objects.
```
defeats.arguments object
An object describing the value the defeat
condition is compared against.

defeats.arguments.value string 6 An example value that the defeat condition is
compared against.

defeats.comparator string is
The comparator used to compare the filter type
to the value to form the defeat.

defeats.defeatID
numeric/
string
1

```
An id for the defeat within the context of the
model. If defeats are conditional, their id will
indicate the relationship - e.g., a condition for
defeat with id 1 will have ID 1-1. In this case,
the id will be a string.
```
defeats.filtertype string
Internal source
device type The filter used to form the defeat.

created object An object describing the creation of the model.

created.by string smartinez_admin Username that created the model.

edited object User ID that created the model.

edited.by string ajohnston Username that last edited the model.

edited.userID numeric (^24) User ID that last edited the model.
history array
An object describing the edit history of the
model.
history.modified string 2019-11-15 11:42:00 The last modified date in UTC.
history.active boolean TRUE
Whether the model was enabled or disabled at
the time.
history.message string
Improved rarity
filters
The most recent commit message for the model.
history.by string ajohnston The user who made the change.
history.phid numeric 2842 The “policy history id” at that change.
history.defeatsOnly boolean TRUE
If the changes made did not alter the model’s
autoupdate eligibility, will be true. This
includes changes to defeats, model priority, etc.
Please refer to the model update guidance for
more information.
history.accepted string 1686578003000 In epoch time, when the model update was
accepted.
history.acceptedby string ajohnston
The user who accepted the model update.
Autoupdated models will display “System” in this
field.
message string
Altered priority
value.
The most recent commit message for the model.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

mitre object

```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```
mitre.tactics array initial-access
An array of MITRE ATT&CK framework tactics the
model has been mapped to.

mitre.techniques array T1133 An array of MITRE ATT&CK framework
techniques the model has been mapped to.

version numeric 40 The model version, increments on edit.

priority numeric 40

```
The numeric behavior category associated with
the model: 0-3 equates to informational, 4
equates to suspicious and 5 equates to critical.
```
category string Critical
The behavior category associated with the
model.

compliance boolean false

```
Whether the model is in the compliance model
category. If true, takes priority over the value of
category.
```

###### Example Response

_Request: /models?uuid=80010119-6d7f-0000-0305-5e0000000420_

```
{
"name": "Anomalous File::Anomalous Octet Stream",
"pid": 12,
"phid": 2842,
"uuid": "80010119-6d7f-0000-0305-5e0000000420",
"logic": {
"data": [
3621
],
"type": "componentList",
"version": 1
},
"throttle": 3600,
"sharedEndpoints": false,
"actions": {
"alert": true,
"antigena": {},
"breach": true,
"model": true,
"setPriority": false,
"setTag": false,
"setType": false
},
"tags": [
"AP: Tooling",
"DNS Server"
],
"interval": 0,
"delay": 0,
"sequenced": false,
"active": true,
"modified": "2023-08-15 12:27:32",
"activeTimes": {
"devices": {},
"tags": {},
"type": "exclusions",
"version": 2
},
"priority": 2,
"autoUpdatable": false,
"autoUpdate": true,
"autoSuppress": true,
"description": "A device has downloaded a rare data stream which is not specifying a
specific data type...",
"behaviour": "decreasing",
"defeats": [
[
{
"arguments": {
"value": "6"
},
"comparator": "is",
"defeatID": 1,
"filtertype": "Internal source device type"
},
{
"defeatID": "1-1",
"filtertype": "Destination port",
"comparator": "!=",
"arguments": {
"value": 80
}
```
_continued..._


```
}
],
{
"arguments": {
"value": "7"
},
"comparator": "is",
"defeatID": 2,
"filtertype": "Internal source device type"
},
{
"arguments": {
"value": "7"
},
"comparator": "is",
"defeatID": 3,
"filtertype": "Internal source device type"
},
{
"arguments": {
"value": "1"
},
"comparator": "is",
"defeatID": 4,
"filtertype": "Internal source device type"
}
],
"created": {
"by": "System"
},
"edited": {
"by": "Sarah",
"userID": 24
},
"history": [
{
"modified": "2023-08-15 12:27:32",
"active": true,
"message": "Improved rarity filters, and merged exclusion filters",
"by": "Sarah",
"phid": 2842
},
{
"modified": "2023-05-31 13:47:22",
"active": false,
"message": "Updating regex filters",
"accepted": 1686578003000,
"acceptedBy": "Sarah",
"by": "System",
"phid": 2675
},
...
],
"message": "Altered priority value.",
"mitre": {
"tactics": [
"command-and-control",
"execution",
"lateral-movement"
],
"techniques": [
"T1203",
"T1210",
```
_continued..._


```
"T1219"
]
},
"version": 53,
"priority": 2,
"category": "Critical",
"compliance": false
}
```
_Response is abbreviated._


## /MODELBREACHES

The /modelbreaches endpoint returns a time-sorted list of model breaches, filtered by the specified parameters. This

endpoint is the most important for organizations who wish to integrate Darktrace programmatically into their SOC

environment.

The following recommendations represent a good starting point when initially approaching the query parameters. These

parameters may change over time in response to your business logic and concerns of each security team. Organizations

with a defined playbook may start with a different set of parameters - the API call can always be refined at a later date.

- Busy network environments with many devices may produce a large volume of alerts over a short space of time.
    It is recommended, therefore, that queries are made at more frequent intervals and cover a shorter duration of
    time. A shorter query time frame will always return a response faster.
- Organizations that want more data returned for use in their external system can use the minimal=false and
    fulldevicedetails=true parameters. Setting these parameters will return full model component and
    device information in the JSON response, allowing for more investigation to be carried within the SOC
    environment.
- Acknowledged breaches can be optionally returned by this endpoint - this can be useful for logging resolved
    events to an external server or reporting on historic acknowledgment. Depending on your organizational
    approach and workflow, you may prefer to export all breaches to an external system - including acknowledged
    breaches - and make the decision there on whether the breach needs to be investigated or discussed further.
    This will, however, produce a large number of alerts so should be reviewed on a regular basis.
- Like the Email Alerting and the Mobile App, alert score can be used as a threshold to return model breaches.
    Using minscore will only return breaches above the specified fractional amount (e.g., 0.8 is a breach score of
    80%). This parameter can be used to mimic the “Minimum Breach Score” on the System Config page to match
    other alerting formats if desired.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
deviceattop boolean
```
```
Return the device JSON object as a value of the top-level object rather than within each matched
component. Defaults to true in the Threat Visualizer UI and in JSON alert formats and false for the
programmatic API. requests.
```
```
did numeric Identification number of a device modelled in the Darktrace system.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
expandenums boolean Expand numeric enumerated types to their descriptive string representation.
```
```
from string Start time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
historicmodelonly boolean
```
```
Return the JSON for the historic version of the model details only, rather than both the historic and
current definition.
```
```
includeacknowledged boolean Include acknowledged breaches in the data.
```
```
includebreachurl boolean
```
```
Return a URL for the model breach in the long form of the model breach data, this requires that the
FQDN configuration parameter is set.
```
```
minimal boolean
```
```
Reduce the amount of data returned for the API call. In the Threat Visualizer, this parameter
defaults to false when any of the starttime, from, pid, uuid, pbid or did parameters are
used. When accessed programmatically, always defaults to false.
```

```
PARAMETER TYPE DESCRIPTION
```
```
minscore numeric Return only breaches with a minimum score.
```
```
pbid numeric Only return the model breach with the specified ID.
```
```
pid numeric Only return model breaches for the specified model.
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
to string End time of data to return in YYYY-MM-DD HH:MM:SS format
```
```
uuid string
Only return model breaches for the specified model. All models have a uuid and a pid. The uuid
(universally unique identifier) is a 128-bit hexadecimal number.
```
```
responsedata string
When given the name of a top-level field or object, restricts the returned JSON to only that field or
object.
```
```
saasonly boolean Restricts returned breaches to only those classified as SaaS breaches.
```
```
group string If group=device is used, modifies the score field to display the device score.
```
```
includesuppressed boolean Includes suppressed model breaches in the response. Default false.
```
```
saasfilter string
Can be used to limit returned model breaches to specific Darktrace/Apps, Cloud or Zero Trust
module users. Can be repeated multiple times.
```
```
creationtime boolean
```
```
When true, alters the behavior of time parameters to filters based on model breach creation.
When false (default), time filtering will instead limit by the timestamp of the first relevant activity
to the model logic.
```
###### Notes

- A time window for the returned model breaches can be specified using YYYY-MM-DD HH:MM:SS format with
    the to/from parameters, or starttime/endtime using unix time. If no time period is specified, breaches
    are pulled from beginning of memory with a limit of one year per response. Time parameters must always be
    specified in pairs.
- Time parameters limit data by the timestamp of the first activity that was relevant to the model breach, not the
    eventual model breach record creation. To filter on model breach creation, use creationtime=true. This
    time difference may be due to models which require multiple events over a long period, or may be due to
    events received with a delay from third-party platforms.
- Specifying historicmodelonly will return a single model object for the model entity at the time of breach.
- The includebreachURL parameter will only return a URL if minimal=false. This URL will be the second
    object returned and it will take the format
       "breachUrl": "https://darktrace-dt-XXX-YY/#modelbreach/123"
- expandenums toggles numeric values in certain nested lists to full strings - the numerical codes and
    associated strings for enums can be found at the /enums endpoint ( _/enums_ ).
- By default, the minimal parameter is false when accessing model breaches programmatically. This returns
    reduced model logic details for the model that breached. The /modelbreaches endpoint in the Threat
    Visualizer has minimal=true by default for multiple breaches and minimal=false when filtering by a pbid.
    Setting minimal to false will allow more investigation in the external environment but will also produce
    more noise in the returned JSON.
- By default, the deviceattop parameter is true when accessing model breaches programmatically. This
    means device information is contained in a top level JSON object “device”, rather than contained within the
       triggeredComponents object. The /modelbreaches endpoint in the Threat Visualizer has
       deviceattop=false by default, so device information is nested within the triggeredComponents object
    when viewed with a browser.


- Alert priority is only returned when minimal=false and cannot be used as a filter for returned breaches.
- The parameter group=device can be used to sort returned breaches by the breaching device and mimic the
    “Device” view of the Threat Tray. In this mode, the score (and devicescore) value will represent the device
    score associated with the breach. The model breach score is instead indicated by pbscore.
- If a model triggers model breaches too frequently, it will be automatically suppressed (if suppression is
    enabled). Suppressed model breaches are not displayed to Threat Visualizer users as standard. The parameter
       includesuppressed will include these suppressed model breaches in the output.
- The uuid value is unique and consistent for models across Darktrace environments. The pid value is unique
    only within the context of the given instance.
- The saasfilter parameter takes a wildcard string which is matched to the SaaS::[platform] value
    (e.g. SaaS::Office365). Multiple filters can be applied to include multiple modules - for example,
       saasfilter=gcp*&saasfilter=office365*. A wildcard (*) _must be specified_ at the end of this parameter
    value.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all model breaches - including acknowledged breaches - for the 7 day period from 3rd to 9th February
    2020:

```
https://[instance]/modelbreaches?
from=2020-02-03T00:00:00&to=2020-02-9T23:59:59&minimal=true&includeacknowledged=true
```
2. GET model breaches for the device with did=1 since January 1st 2020 with a breach score above 60%:

```
https://[instance]/modelbreaches?did=1&starttime=1577836800000&minscore=0.6
```
3. GET model breaches for the “Anomalous File / Anomalous Octet Stream” model:

```
https://[instance]/modelbreaches?uuid=80010119-6d7f-0000-0305-5e0000000420
```
4. GET the information for model breach pbid=123 with information about the model at the time of breach only:

```
https://[instance]/modelbreaches?pbid=123&historicmodelonly=true
```
```
https://[instance]/modelbreaches/123?historicmodelonly=true
```
5. GET a list of model breaches triggered by Azure and Office 365 users, but only return the model data, model
    score and user information:

```
https://[instance]/modelbreaches?
deviceattop=true&historicmodelonly=true&minimal=true&saasfilter=azure*&saasfilter=office
365*&responsedata=model,percentscore,device
```

###### Example Response

_Request: /modelbreaches/123?historicmodelonly=true_

```
{
"creationTime": 1582213002000,
"commentCount": 0,
"pbid": 287232,
"time": 1582212986000,
"model": {
"name": "Compromise::HTTP Beaconing to Rare Destination",
"pid": 143,
"phid": 123,
"uuid": "1a814475-5fef-499b-a467-4e2e68352cbb",
"logic": {
"data": [
265
],
"type": "componentList",
"version": 1
},
"throttle": 3600,
"sharedEndpoints": false,
"actions": {
"alert": true,
"antigena": {},
"breach": true,
"model": true,
"setPriority": false,
"setTag": false,
"setType": false
},
"tags": [
"AP: C2 Comms",
"DNS Server"
],
"interval": 0,
"sequenced": false,
"active": true,
"modified": "2019-11-15 11:42:21",
"activeTimes": {
"devices": {},
"tags": {},
"type": "exclusions",
"version": 2
},
"priority": 0,
"autoUpdatable": true,
"autoUpdate": true,
"autoSuppress": true,
"description": "A device is making regular HTTP connections to a rare external
location...",
"behaviour": "decreasing",
"defeats": [],
"created": {
"by": "System"
},
"edited": {
"by": "Sarah",
"userID": 24
},
"version": 16
},
"triggeredComponents": [
{
"time": 1582212985000,
```
_continued..._


```
"cbid": 305422,
"cid": 265,
"chid": 265,
"size": 3,
"threshold": 2,
"interval": 14400,
"logic": {
"data": {
"left": "A",
"operator": "AND",
"right": {
"left": "B",
"operator": "AND",
"right": {
...
}
},
"version": "v0.1"
},
"metric": {
"mlid": 1,
"name": "externalconnections",
"label": "External Connections"
},
"triggeredFilters": [
{
"cfid": 2087,
"id": "A",
"filterType": "Rare external endpoint",
"arguments": {
"value": 90
},
"comparatorType": ">",
"trigger": {
"value": "94"
}
},
...
]
}
],
"score": 0.325
"device": {
"did": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"sid": 23,
"hostname": "Sarah Development",
"firstSeen": 1581591070000,
"lastSeen": 1582645442000,
"typename": "desktop",
"typelabel": "Desktop"
}
}
```
_Response is abbreviated._


## /MODELBREACHES RESPONSE SCHEMA

For more detailed information on the structure of the defeats object, please refer to the schema for _/models_.

#### Response Schema - No Parameters

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
creationTime numeric 1528810000000
```
```
The timestamp that the record of the model
breach was created. This is distinct from the
“time” field.
```
```
commentCount numeric 2
The number of comments made against this
breach.
```
```
pbid numeric 123 The “policy breach ID” of the model breach.
```
```
time numeric 1528810000000 The timestamp of the first activity which met the
model criteria in epoch time.
```
```
model object
An object describing the model logic and history
of the model that was breached.
```
```
model.then object
```
```
An object describing the model logic at the time
of breach. Requires
historicModelOnly=false.
```
```
model.then.name string
```
```
Anomalous
Connection::1 GiB
Outbound
```
```
Name of the model that was breached.
```
```
model.then.pid numeric 1 The “policy id” of the model that was breached.
```
```
model.then.phid numeric 1
The model “policy history” id. Increments when
the model is modified.
```
```
model.then.uuid string
80010119-6d7f-0000-
0305-5e0000000215
```
```
A unique ID that is generated on creation of the
model.
```
```
model.then.mitre object
```
```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```
```
model.then.mitre.tactics array initial-access
An array of MITRE ATT&CK framework tactics the
model has been mapped to.
```
```
model.then.mitre.techniques array T1133
An array of MITRE ATT&CK framework
techniques the model has been mapped to.
```
```
model.then.logic object
A data structure that describes the conditions to
bring about a breach.
```
```
model.then.logic.data array 1
```
```
If the model is a checklist type this will be a list of
component ID numbers. If this model is a
weighted type this will be a list of component ID,
weight object pairs.
```
```
model.then.logic.type string componentList The type of model.
```
```
model.then.logic.version numeric 1
A number representing the version of model
logic.
```
```
model.then.throttle numeric 3600
For an individual device, this is the value in
seconds for which this model will not fire again.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.then.sharedEndpoints boolean FALSE

```
For models that contain multiple components
that reference an endpoint, this value indicates
whether all endpoints should be identical for the
model to fire.
```
model.then.actions object
The action to perform as a result of matching this
model firing.

model.then.actions.alert boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.then.actions.antigena object

```
An object containing the Darktrace RESPOND
response to be applied as a result of the model
breaching.
```
model.then.actions.breach boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.then.actions.model boolean TRUE

```
If true, creates an event in the device’s event log
without creating an alert/ model breach in the
threat tray.
```
model.then.actions.setPriority boolean FALSE

```
If the priority is to be changed on breach, the
numeric value it should become. If no priority
change action, a false boolean.
```
model.then.actions.setTag boolean FALSE

```
If a tag is to be applied on model breach, a single
number or array of the system ID for the tag(s) to
be applied. If no tag action, a false boolean.
```
model.then.actions.setType boolean FALSE

```
If a change device type action is to be applied on
model breach, the numeric system ID for the
label to be applied. If no change device type
action is applied to the model, a false boolean.
```
model.then.tags array AP: Egress
A list of tags that have been applied to this model
in the Threat Visualizer model editor.

model.then.interval numeric 0

```
Where a model contains multiple components,
this interval represents the time window in
seconds in which all the components should fire
for this model to be breached.
```
model.then.delay numeric 0

```
Minimum delay in seconds after a positive-
scoring component has fired before the overall
model score is calculated. Value at model breach
time. Only relevant for target score models.
```
model.then.sequenced boolean FALSE

```
Whether the components are required to fire in
the specified order for the model breach to
occur.
```
model.then.active boolean TRUE Whether the model is enabled or disabled.

model.then.modified string 2020-02-12 12:00:00
Timestamp at which the model was last modified,
in a readable format.

model.then.activeTimes object
An object describing device whitelisting or
blacklisting configured for this model.

model.then.activeTimes.devices object The device ids for devices on the list.

model.then.activeTimes.tags object A system field.

model.then.activeTimes.type string exclusions The type of list: “restrictions” indicates a blacklist,
“exclusions” a whitelist.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.then.activeTimes.version numeric 2 A system field.

model.then.priority numeric 5

```
The numeric behavior category associated with
the model at the time of model breach: 0-3
equates to informational, 4 equates to suspicious
and 5 equates to critical.
```
model.then.category string Critical
The behavior category associated with the
model at the time of model breach.

model.then.compliance boolean FALSE

```
Whether the model is in the compliance model
category at the time of model breach. If true,
takes priority over the value of category.
```
model.then.autoUpdatable boolean TRUE Whether the model is suitable for auto update.

model.then.autoUpdate boolean TRUE Whether the model is enabled for auto update.

model.then.autoSuppress boolean TRUE
Whether the model will automatically be
suppressed in the case of over-breaching.

model.then.description string

```
A device is moving
large volumes of
data (1GiB+) out of
the
network...
```
```
The optional description of the model.
```
model.then.behaviour string decreasing The score modulation function as set in the
model editor.

model.then.defeats array
An array of model defeats - AND conditions -
which if met, prevent the model from breaching.

model.then.defeats.arguments object An object describing the values associated with a
model defeat.

model.then.defeats.arguments.value string [http://www.example.com](http://www.example.com)
The value(s) that must match for the defeat to
take effect.

model.then.defeats.comparator string does not match The comparator that the value is compared
against the create the defeat.

model.then.defeats.defeatID numeric 1 A unique ID for the defeat.

model.then.defeats.filtertype string Connection hostname The filter the defeat is made from.

model.then.created object An object describing the creation of the model.

model.then.created.by string System Username that created the model.

model.then.edited object An object describing the edit history of the
model.

model.then.edited.by string smartinez_admin Username that last edited the model.

model.then.version numeric 16 The version of the model. Increments on each
edit.

model.now object

```
An object describing the model logic at the time
of request. Requires
historicModelOnly=false.
```
model.now.name string

```
Anomalous
Connection::1 GiB
Outbound
```
```
Name of the model that was breached.
```
model.now.pid numeric 1 The “policy id” of the model that was breached.

model.now.phid numeric 3343
The model “policy history” id. Increments when
the model is modified.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.now.uuid string
80010119-6d7f-0000-
0305-5e0000000215

```
A unique ID that is generated on creation of the
model.
```
model.now.mitre object

```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```
model.now.mitre.tactics array initial-access An array of MITRE ATT&CK framework tactics the
model has been mapped to.

model.now.mitre.techniques array T1133
An array of MITRE ATT&CK framework
techniques the model has been mapped to.

model.now.logic object A data structure that describes the conditions to
bring about a breach.

model.now.logic.data array 1

```
If the model is a checklist type this will be a list of
component ID numbers. If this model is a
weighted type this will be a list of component ID,
weight object pairs.
```
model.now.logic.type string componentList The type of model.

model.now.logic.version numeric 1
A number representing the version of model
logic.

model.now.throttle numeric 3600
For an individual device, this is the value in
seconds for which this model will not fire again.

model.now.sharedEndpoints boolean FALSE

```
For models that contain multiple components
that reference an endpoint, this value indicates
whether all endpoints should be identical for the
model to fire.
```
model.now.actions object
The action to perform as a result of matching this
model firing.

model.now.actions.alert boolean FALSE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.now.actions.antigena object

```
An object containing the Darktrace RESPOND
response to be applied as a result of the model
breaching.
```
model.now.actions.breach boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.now.actions.model boolean TRUE

```
If true, creates an event in the device’s event log
without creating an alert/ model breach in the
threat tray.
```
model.now.actions.setPriority boolean FALSE

```
If the priority is to be changed on breach, the
numeric value it should become. If no priority
change action, a false boolean.
```
model.now.actions.setTag boolean FALSE

```
If a tag is to be applied on model breach, a single
number or array of the system ID for the tag(s) to
be applied. If no tag action, a false boolean.
```
model.now.actions.setType boolean FALSE

```
If a change device type action is to be applied on
model breach, the numeric system ID for the
label to be applied. If no change device type
action is applied to the model, a false boolean.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.now.tags array AP: Egress AP: Bruteforce

model.now.interval numeric 0

```
Where a model contains multiple components,
this interval represents the time window in
seconds in which all the components should fire
for this model to be breached.
```
model.now.delay numeric 0

```
Minimum delay in seconds after a positive-
scoring component has fired before the overall
model score is calculated. Value at request time.
Only relevant for target score models.
```
model.now.sequenced boolean FALSE

```
Whether the components are required to fire in
the specified order for the model breach to
occur.
```
model.now.active boolean TRUE Whether the model is enabled or disabled.

model.now.modified string 2020-02-12 12:00:00
Timestamp at which the model was last modified,
in a readable format.

model.now.activeTimes object
An object describing device whitelisting or
blacklisting configured for this model.

model.now.activeTimes.devices object The device ids for devices on the list.

model.now.activeTimes.tags object A system field.

model.now.activeTimes.type string exclusions
The type of list: “restrictions” indicates a blacklist,
“exclusions” a whitelist.

model.now.activeTimes.version numeric 2 A system field.

model.now.priority numeric 5

```
The numeric behavior category associated with
the model at the time of request: 0-3 equates to
informational, 4 equates to suspicious and 5
equates to critical.
```
model.now.category string Critical
The behavior category associated with the
model at the time of request.

model.now.compliance boolean FALSE

```
Whether the model is in the compliance model
category at the time of request. If true, takes
priority over the value of category.
```
model.now.autoUpdatable boolean FALSE Whether the model is suitable for auto update.

model.now.autoUpdate boolean TRUE Whether the model is enabled for auto update.

model.now.autoSuppress boolean TRUE
Whether the model will automatically be
suppressed in the case of over-breaching.

model.now.description string

```
A device is moving
large volumes of
data (1GiB+) out of
the
network...
```
```
The optional description of the model.
```
model.now.behaviour string decreasing
The score modulation function as set in the
model editor.

model.now.defeats array
An array of model defeats - AND conditions -
which if met, prevent the model from breaching.

model.now.defeats.arguments object
An object describing the values associated with a
model defeat.

model.now.defeats.arguments.value string [http://www.example.com](http://www.example.com)
The value(s) that must match for the defeat to
take effect.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.now.defeats.comparator string does not match
The comparator that the value is compared
against the create the defeat.

model.now.defeats.defeatID numeric (^1) A unique ID for the defeat.
model.now.defeats.filtertype string Connection hostname The filter the defeat is made from.
model.now.created object An object describing the creation of the model.
model.now.created.by string System Username that created the model.
model.now.edited object
An object describing the edit history of the
model.
model.now.edited.by string smartinez_admin Username that last edited the model.
model.now.edited.userID numeric 24 Username that last edited the model.
model.now.message string
updated display
filters to simplify
output
The commit message for the change.
model.now.version numeric 24
The version of the model. Increments on each
edit.
triggeredComponents array
An array describing the model components that
were triggered to create the model breach.
triggeredComponents.time numeric 1528810000000
A timestamp in Epoch time at which the
components were triggered.
triggeredComponents.cbid numeric 1729
The “component breach id”. A unique identifier
for the component breach.
triggeredComponents.cid numeric 1 The “component id”. A unique identifier.
triggeredComponents.chid numeric 1
The “component history id”. Increments when
the component is edited.
triggeredComponents.size numeric 1155203452
The size of the value that was compared in the
component.
triggeredComponents.threshold numeric 1073741824
The threshold value that the size must exceed for
the component to breach.
triggeredComponents.interval numeric 3600
The timeframe in seconds within which the
threshold must be satisfied.
triggeredComponents.logic.data object
An object representing the logical relationship
between component filters. Each filter is given an
alphabetical reference and the contents of this
object describe the relationship between those
objects.
triggeredComponents.logic.data.left string A
Objects on the left will be compared with the
object on the right using the specified operator.
triggeredComponents.logic.data.operato
r
string AND A logical operator to compare filters with.
triggeredComponents.logic.data.right object D
Objects on the left will be compared with the
object on the right using the specified operator.
triggeredComponents.logic.version string v0.1 The version of the component logic.
triggeredComponents.metric object
An object describing the metric used in the
component that triggered the Model Breach.
triggeredComponents.metric.mlid numeric (^33) The “metric logic” id - unique identifier.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

triggeredComponents.metric.name string
externalclientdatat
ransfervolume

```
The metric which data is returned for in system
format.
```
triggeredComponents.metric.label string
External Data
Volume as a Client

```
The metric which data is returned for in readable
format.
```
triggeredComponents.triggeredFilters array
The filters that comprise the component that
were triggered to produce the model breach.

triggeredComponents.triggeredFilters.c
fid numeric
1 The ‘component filter id’. A unique identifier for
the filter as part of a the component.

triggeredComponents.triggeredFilters.i
d
string A

```
A filter that is used in the component logic. All
filters are given alphabetical identifiers. Display
filters - those that appear in the breach
notification - can be identified by a lowercase ‘d’
and a numeral.
```
triggeredComponents.triggeredFilters.f
ilterType
string Direction

```
The filtertype that is used in the filter. A full list of
filtertypes can be found on the /filtertypes
endpoint.
```
triggeredComponents.triggeredFilters.a
rguments object

```
An object describing the values and
comparisons made in the filter.
```
triggeredComponents.triggeredFilters.a
rguments.value
numeric out

```
The value the filtertype should be compared
against (using the specified comparator) to
create the filter.
```
triggeredComponents.triggeredFilters.c
omparatorType
string is

```
The comparator. A full list of comparators
available for each filtertype can be found on the /
filtertypes endpoint.
```
triggeredComponents.triggeredFilters.t
rigger
object
An object contaning the value to be compared.
Display filters will have an empty object.

triggeredComponents.triggeredFilters.t
rigger.value
string out The actual value that triggered the filter.

score numeric 0.443
The model breach score, represented by a value
between 0 and 1.

percentscore numeric 44
The model breach score as a simple percentage
equivalent.

device object An object describing a device seen by Darktrace.

device.did numeric (^96) The “device id”, a unique identifier.
device.ip string 10.0.18.224 The current IP associated with the device.
device.ips array IPs associated with the device historically.
device.ips.ip string 10.0.18.224 A historic IP associated with the device.
device.ips.timems numeric 1528812000000
The time the IP was last seen associated with
that device in epoch time.
device.ips.time string 2020-02-12 12:00:00
The time the IP was last seen associated with
that device in readable format.
device.ips.sid numeric 34 The subnet id for the subnet the IP belongs to.
device.sid numeric 34 The subnet id for the subnet the device is
currently located in.
device.hostname string fs182 The current device hostname.
device.firstSeen numeric 1528810000000
The first time the device was seen on the
network.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

device.lastSeen numeric 1528810000000
The last time the device was seen on the
network.

device.typename string server The device type in system format.

device.typelabel string Server The device type in readable format.


###### Example Response

_Request: /modelbreaches/123_

```
{
"creationTime": 1582213002000,
"commentCount": 0,
"pbid": 123,
"time": 1582212986000,
"model": {
"then":{
"name": "Compromise::HTTP Beaconing to Rare Destination",
"pid": 143,
"phid": 123,
"uuid": "1a814475-5fef-499b-a467-4e2e68352cbb",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"logic": {
"data": [
265
],
"type": "componentList",
"version": 1
},
"throttle": 3600,
"sharedEndpoints": false,
"actions": {
"alert": true,
"antigena": {},
"breach": true,
"model": true,
"setPriority": false,
"setTag": false,
"setType": false
},
"tags": [
"AP: C2 Comms",
"DNS Server"
],
"interval": 0,
"delay": 0,
"sequenced": false,
"active": true,
"modified": "2019-11-15 11:42:21",
"activeTimes": {
"devices": {},
"tags": {},
"type": "exclusions",
"version": 2
},
"priority": 5,
"category": "Critical",
"compliance": false
"autoUpdatable": true,
"autoUpdate": true,
"autoSuppress": true,
"description": "A device is making regular HTTP connections to a rare external
location...",
"behaviour": "decreasing",
"defeats": [
```
_continued..._


```
{
"arguments": {
"value": "www.example.com"
},
"comparator": "does not match",
"defeatID": 1,
"filtertype": "Connection hostname"
}
],
"created": {
"by": "System"
},
"edited": {
"by": "Sarah",
"userID": 24
},
"version": 16
}
},
"now": {
"name": "Compromise::HTTP Beaconing to Rare Destination",
"pid": 143,
"phid": 123,
"uuid": "1a814475-5fef-499b-a467-4e2e68352cbb",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"logic": {
"data": [
265
],
"type": "componentList",
"version": 1
},
"throttle": 3600,
"sharedEndpoints": false,
"actions": {
"alert": true,
"antigena": {},
"breach": true,
"model": true,
"setPriority": false,
"setTag": false,
"setType": false
},
"tags": [
"AP: C2 Comms",
"DNS Server"
],
"interval": 0,
"delay": 0,
"sequenced": false,
"active": true,
"modified": "2019-11-15 11:42:21",
"activeTimes": {
"devices": {},
"tags": {},
"type": "exclusions",
```
_continued..._


```
"version": 2
},
"priority": 5,
"category": "Critical",
"compliance": false
"autoUpdatable": true,
"autoUpdate": true,
"autoSuppress": true,
"description": "A device is making regular HTTP connections to a rare external
location...",
"behaviour": "decreasing",
"defeats": [
{
"arguments": {
"value": "www.example.com"
},
"comparator": "does not match",
"defeatID": 1,
"filtertype": "Connection hostname"
}
],
"created": {
"by": "System"
},
"edited": {
"by": "Sarah",
"userID": 24
},
"version": 16
}
},
"triggeredComponents": [
{
"time": 1582212985000,
"cbid": 305422,
"cid": 265,
"chid": 265,
"size": 3,
"threshold": 2,
"interval": 14400,
"logic": {
"data": {
"left": "A",
"operator": "AND",
"right": {
"left": "B",
"operator": "AND",
"right": {
...
}
},
"version": "v0.1"
},
"metric": {
"mlid": 1,
"name": "externalconnections",
"label": "External Connections"
},
"triggeredFilters": [
{
"cfid": 2087,
"id": "A",
"filterType": "Rare external endpoint",
"arguments": {
```
_continued..._


"value": 90
},
"comparatorType": ">",
"trigger": {
"value": "94"
}
},
...
]
}
],
"score": 0.325,
"percentscore": 33,
"device": {
"did": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"sid": 23,
"hostname": "Sarah Development",
"firstSeen": 1581591070000,
"lastSeen": 1582645442000,
"typename": "desktop",
"typelabel": "Desktop"
}
}


#### Response Schema - deviceattop=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
creationTime numeric 1528810000000
The timestamp that the record of the breach was
created. This is distinct from the “time” field.
```
```
breachUrl string
```
```
https://appliance-
fqdn/
#modelbreaches/123
```
```
A link to the specific model breach in the
Darktrace Threat Visualizer - the configuration
option FQDN must be set for this field to appear.
```
```
commentCount numeric 2
The number of comments made against this
breach.
```
pbid numeric (^123) The “policy breach ID” of the model breach.
time numeric 1528810000000
The timestamp of the first activity which met the
model criteria in epoch time.
model object
An object describing the model logic and history
of the model that was breached.
model.then object
An object describing the model logic at the time
of breach. Requires
historicModelOnly=false.
model.then.name string
Anomalous
Connection::1 GiB
Outbound
Name of the model that was breached.
model.then.pid numeric 1 The “policy id” of the model that was breached.
model.then.phid numeric 1 The model “policy history” id. Increments when
the model is modified.
model.then.uuid string
80010119-6d7f-0000-
0305-5e0000000215
A unique ID that is generated on creation of the
model.
model.then.mitre object
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
model.then.mitre.tactics array initial-access An array of MITRE ATT&CK framework tactics the
model has been mapped to.
model.then.mitre.techniques array T1133
An array of MITRE ATT&CK framework
techniques the model has been mapped to.
model.then.logic object A data structure that describes the conditions to
bring about a breach.
model.then.logic.data array 1
If the model is a checklist type this will be a list of
component ID numbers. If this model is a
weighted type this will be a list of component ID,
weight object pairs.
model.then.logic.type string componentList The type of model.
model.then.logic.version numeric 1
A number representing the version of model
logic.
model.then.throttle numeric 3600
For an individual device, this is the value in
seconds for which this model will not fire again.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.then.sharedEndpoints boolean FALSE

```
For models that contain multiple components
that reference an endpoint, this value indicates
whether all endpoints should be identical for the
model to fire.
```
model.then.actions object
The action to perform as a result of matching this
model firing.

model.then.actions.alert boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.then.actions.antigena object

```
An object containing the Darktrace RESPOND
response to be applied as a result of the model
breaching.
```
model.then.actions.breach boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.then.actions.model boolean TRUE

```
If true, creates an event in the device’s event log
without creating an alert/ model breach in the
threat tray.
```
model.then.actions.setPriority boolean FALSE

```
If the priority is to be changed on breach, the
numeric value it should become. If no priority
change action, a false boolean.
```
model.then.actions.setTag boolean FALSE

```
If a tag is to be applied on model breach, a single
number or array of the system ID for the tag(s) to
be applied. If no tag action, a false boolean.
```
model.then.actions.setType boolean FALSE

```
If a change device type action is to be applied on
model breach, the numeric system ID for the
label to be applied. If no change device type
action is applied to the model, a false boolean.
```
model.then.tags array AP: Egress
A list of tags that have been applied to this model
in the Threat Visualizer model editor.

model.then.delay numeric 0

```
Minimum delay in seconds after a positive-
scoring component has fired before the overall
model score is calculated. Value at model breach
time. Only relevant for target score models.
```
model.then.interval numeric 0

```
Where a model contains multiple components,
this interval represents the time window in
seconds in which all the components should fire
for this model to be breached.
```
model.then.sequenced boolean FALSE

```
Whether the components are required to fire in
the specified order for the model breach to
occur.
```
model.then.active boolean TRUE Whether the model is enabled or disabled.

model.then.modified string 2018-06-12 14:00:00
Timestamp at which the model was last modified,
in a readable format.

model.then.activeTimes object
An object describing device whitelisting or
blacklisting configured for this model.

model.then.activeTimes.devices object The device ids for devices on the list.

model.then.activeTimes.tags object A system field.

model.then.activeTimes.type string exclusions The type of list: “restrictions” indicates a blacklist,
“exclusions” a whitelist.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.then.activeTimes.version numeric 2 A system field.

model.then.priority numeric 5

```
The numeric behavior category associated with
the model at the time of model breach: 0-3
equates to informational, 4 equates to suspicious
and 5 equates to critical.
```
model.then.category string Critical
The behavior category associated with the
model at the time of model breach.

model.then.compliance boolean FALSE

```
Whether the model is in the compliance model
category at the time of model breach. If true,
takes priority over the value of category.
```
model.then.autoUpdatable boolean TRUE Whether the model is suitable for auto update.

model.then.autoUpdate boolean TRUE Whether the model is enabled for auto update.

model.then.autoSuppress boolean TRUE
Whether the model will automatically be
suppressed in the case of over-breaching.

model.then.description string

```
A device is moving
large volumes of
data (1GiB+) out of
the
network...
```
```
The optional description of the model.
```
model.then.behaviour string decreasing The score modulation function as set in the
model editor.

model.then.defeats array
An array of model defeats - AND conditions -
which if met, prevent the model from breaching.

model.then.defeats.arguments object An object describing the values associated with a
model defeat.

model.then.defeats.arguments.value string [http://www.example.com](http://www.example.com)
The value(s) that must match for the defeat to
take effect.

model.then.defeats.comparator string does not match The comparator that the value is compared
against the create the defeat.

model.then.defeats.defeatID numeric 1 A unique ID for the defeat.

model.then.defeats.filtertype string Connection hostname The filter the defeat is made from.

model.then.created object An object describing the creation of the model.

model.then.created.by string System Username that created the model.

model.then.edited object An object describing the edit history of the
model.

model.then.edited.by string smartinez_admin Username that last edited the model.

model.then.version numeric 16 The version of the model. Increments on each
edit.

model.now object

```
An object describing the model logic at the time
of request. Requires
historicModelOnly=false.
```
model.now.name string

```
Anomalous
Connection::1 GiB
Outbound
```
```
Name of the model that was breached.
```
model.now.pid numeric 1 The “policy id” of the model that was breached.

model.now.phid numeric 3343
The model “policy history” id. Increments when
the model is modified.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.now.uuid string
80010119-6d7f-0000-
0305-5e0000000215

```
A unique ID that is generated on creation of the
model.
```
model.now.mitre object

```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```
model.now.mitre.tactics array initial-access An array of MITRE ATT&CK framework tactics the
model has been mapped to.

model.now.mitre.techniques array T1133
An array of MITRE ATT&CK framework
techniques the model has been mapped to.

model.now.logic object A data structure that describes the conditions to
bring about a breach.

model.now.logic.data array 1

```
If the model is a checklist type this will be a list of
component ID numbers. If this model is a
weighted type this will be a list of component ID,
weight object pairs.
```
model.now.logic.type string componentList The type of model.

model.now.logic.version numeric 1
A number representing the version of model
logic.

model.now.throttle numeric 3600
For an individual device, this is the value in
seconds for which this model will not fire again.

model.now.sharedEndpoints boolean FALSE

```
For models that contain multiple components
that reference an endpoint, this value indicates
whether all endpoints should be identical for the
model to fire.
```
model.now.actions object
The action to perform as a result of matching this
model firing.

model.now.actions.alert boolean FALSE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.now.actions.antigena object

```
An object containing the Darktrace RESPOND
response to be applied as a result of the model
breaching.
```
model.now.actions.breach boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.now.actions.model boolean TRUE

```
If true, creates an event in the device’s event log
without creating an alert/ model breach in the
threat tray.
```
model.now.actions.setPriority boolean FALSE

```
If the priority is to be changed on breach, the
numeric value it should become. If no priority
change action, a false boolean.
```
model.now.actions.setTag boolean FALSE

```
If a tag is to be applied on model breach, a single
number or array of the system ID for the tag(s) to
be applied. If no tag action, a false boolean.
```
model.now.actions.setType boolean FALSE

```
If a change device type action is to be applied on
model breach, the numeric system ID for the
label to be applied. If no change device type
action is applied to the model, a false boolean.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.now.tags array AP: Egress AP: Bruteforce

model.now.interval numeric 0

```
Where a model contains multiple components,
this interval represents the time window in
seconds in which all the components should fire
for this model to be breached.
```
model.now.delay numeric 0

```
Minimum delay in seconds after a positive-
scoring component has fired before the overall
model score is calculated. Value at request time.
Only relevant for target score models.
```
model.now.sequenced boolean FALSE

```
Whether the components are required to fire in
the specified order for the model breach to
occur.
```
model.now.active boolean TRUE Whether the model is enabled or disabled.

model.now.modified string 2018-06-12 14:00:00
Timestamp at which the model was last modified,
in a readable format.

model.now.activeTimes object
An object describing device whitelisting or
blacklisting configured for this model.

model.now.activeTimes.devices object The device ids for devices on the list.

model.now.activeTimes.tags object A system field.

model.now.activeTimes.type string exclusions
The type of list: “restrictions” indicates a blacklist,
“exclusions” a whitelist.

model.now.activeTimes.version numeric 2 A system field.

model.now.priority numeric 5

```
The numeric behavior category associated with
the model at the time of request: 0-3 equates to
informational, 4 equates to suspicious and 5
equates to critical.
```
model.now.category string Critical
The behavior category associated with the
model at the time of request.

model.now.compliance boolean FALSE

```
Whether the model is in the compliance model
category at the time of request. If true, takes
priority over the value of category.
```
model.now.autoUpdatable boolean FALSE Whether the model is suitable for auto update.

model.now.autoUpdate boolean TRUE Whether the model is enabled for auto update.

model.now.autoSuppress boolean TRUE
Whether the model will automatically be
suppressed in the case of over-breaching.

model.now.description string

```
A device is moving
large volumes of
data (1GiB+) out of
the
network...
```
```
The optional description of the model.
```
model.now.behaviour string decreasing
The score modulation function as set in the
model editor.

model.now.defeats array
An array of model defeats - AND conditions -
which if met, prevent the model from breaching.

model.now.defeats.arguments object
An object describing the values associated with a
model defeat.

model.now.defeats.arguments.value string [http://www.example.com](http://www.example.com)
The value(s) that must match for the defeat to
take effect.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.now.defeats.comparator string does not match
The comparator that the value is compared
against the create the defeat.

model.now.defeats.defeatID numeric (^1) A unique ID for the defeat.
model.now.defeats.filtertype string Connection hostname The filter the defeat is made from.
model.now.created object An object describing the creation of the model.
model.now.created.by string System Username that created the model.
model.now.edited object
An object describing the edit history of the
model.
model.now.edited.by string smartinez_admin Username that last edited the model.
model.now.edited.userID numeric 24 Username that last edited the model.
model.now.message string
updated display
filters to simplify
output
The commit message for the change.
model.now.version numeric 24
The version of the model. Increments on each
edit.
triggeredComponents array
An array describing the model components that
were triggered to create the model breach.
triggeredComponents.time numeric 1528810000000
A timestamp in Epoch time at which the
components were triggered.
triggeredComponents.cbid numeric 1729
The “component breach id”. A unique identifier
for the component breach.
triggeredComponents.cid numeric 1 The “component id”. A unique identifier.
triggeredComponents.chid numeric 1
The “component history id”. Increments when
the component is edited.
triggeredComponents.size numeric 1155203452
The size of the value that was compared in the
component.
triggeredComponents.threshold numeric 1073741824
The threshold value that the size must exceed for
the component to breach.
triggeredComponents.interval numeric 3600
The timeframe in seconds within which the
threshold must be satisfied.
triggeredComponents.logic object An object describing the component logic.
triggeredComponents.logic.data object
An object representing the logical relationship
between component filters. Each filter is given an
alphabetical reference and the contents of this
object describe the relationship between those
objects.
triggeredComponents.logic.data.left string A Objects on the left will be compared with the
object on the right using the specified operator.
triggeredComponents.logic.data.operato
r
string AND A logical operator to compare filters with.
triggeredComponents.logic.data.right object D Objects on the left will be compared with the
object on the right using the specified operator.
triggeredComponents.logic.version string v0.1 The version of the component logic.
triggeredComponents.metric object
An object describing the metric used in the
component that triggered the Model Breach.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

triggeredComponents.metric.mlid numeric 33 The “metric logic” id - unique identifier.

triggeredComponents.metric.name string
externalclientdatat
ransfervolume

```
The metric which data is returned for in system
format.
```
triggeredComponents.metric.label string
External Data
Volume as a Client

```
The metric which data is returned for in readable
format.
```
triggeredComponents.device object An object describing a device seen by Darktrace.

triggeredComponents.device.did numeric 96 The “device id”, a unique identifier.

triggeredComponents.device.ip string 10.0.18.224 The current IP associated with the device.

triggeredComponents.device.ips array IPs associated with the device historically.

triggeredComponents.device.ips.ip string 10.0.18.224 A historic IP associated with the device.

triggeredComponents.device.ips.timems numeric 1528812000000
The time the IP was last seen associated with
that device in epoch time.

triggeredComponents.device.ips.time string 2018-06-12 14:00:00
The time the IP was last seen associated with
that device in readable format.

triggeredComponents.device.ips.sid numeric 34 The subnet id for the subnet the IP belongs to.

triggeredComponents.device.sid numeric 34
The subnet id for the subnet the device is
currently located in.

triggeredComponents.device.hostname string fs182 The current device hostname.

triggeredComponents.device.firstSeen numeric 1528810000000 The first time the device was seen on the
network.

triggeredComponents.device.lastSeen numeric 1528810000000
The last time the device was seen on the
network.

triggeredComponents.device.typename string server The device type in system format.

triggeredComponents.device.typelabel string Server The device type in readable format.

triggeredComponents.triggeredFilters array
The filters that comprise the component that
were triggered to produce the model breach.

triggeredComponents.triggeredFilters.c
fid
numeric 1
The ‘component filter id’. A unique identifier for
the filter as part of a the component.

triggeredComponents.triggeredFilters.i
d string
A

```
A filter that is used in the component logic. All
filters are given alphabetical identifiers. Display
filters - those that appear in the breach
notification - can be identified by a lowercase ‘d’
and a numeral.
```
triggeredComponents.triggeredFilters.f
ilterType
string Direction

```
The filtertype that is used in the filter. A full list of
filtertypes can be found on the /filtertypes
endpoint.
```
triggeredComponents.triggeredFilters.a
rguments
object
An object describing the values and
comparisons made in the filter.

triggeredComponents.triggeredFilters.a
rguments.value
string out

```
The value the filtertype should be compared
against (using the specified comparator) to
create the filter.
```
triggeredComponents.triggeredFilters.c
omparatorType
string is

```
The comparator. A full list of comparators
available for each filtertype can be found on the /
filtertypes endpoint.
```
triggeredComponents.triggeredFilters.t
rigger object

```
An object containing the value to be compared.
Display filters will have an empty object.
```

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
triggeredComponents.triggeredFilters.t
rigger.value
string out The actual value that triggered the filter.
```
```
score numeric 0.443 The model breach score, represented by a value
between 0 and 1.
```
```
percentscore numeric 44
The model breach score as a simple percentage
equivalent.
```
###### Example Response

_Request: /modelbreaches/123?deviceattop=false_


```
{
"creationTime": 1582213002000,
"commentCount": 0,
"pbid": 123,
"time": 1582212986000,
"model": {
"then":{
... (same as above)
}
},
"now": {
... (same as above)
}
},
"triggeredComponents": [
{
"time": 1582212985000,
"cbid": 305422,
"cid": 265,
"chid": 265,
"size": 3,
"threshold": 2,
"interval": 14400,
"logic": {
"data": {
"left": "A",
"operator": "AND",
"right": {
"left": "B",
"operator": "AND",
"right": {
...
}
},
"version": "v0.1"
},
"metric": {
"mlid": 1,
"name": "externalconnections",
"label": "External Connections"
},
"device": {
"did": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"sid": 23,
"hostname": "Sarah Development",
"firstSeen": 1581591070000,
"lastSeen": 1582645442000,
"typename": "desktop",
"typelabel": "Desktop"
},
"triggeredFilters": [
{
```
_continued..._


```
"cfid": 2087,
"id": "A",
"filterType": "Rare external endpoint",
"arguments": {
"value": 90
},
"comparatorType": ">",
"trigger": {
"value": "94"
}
},
...
]
}
],
"score": 0.325,
"percentscore": 33
}
```
_Response is abbreviated._

#### Response Schema - historicmodelonly=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
creationTime numeric 1530000000000
The timestamp that the record of the breach was
created. This is distinct from the “time” field.
```
```
breachUrl string
```
```
https://appliance-
fqdn/
#modelbreaches/123
```
```
A link to the specific model breach in the
Darktrace Threat Visualizer - the configuration
option FQDN must be set for this field to appear.
```
```
commentCount numeric 2 The number of comments made against this
breach.
```
```
pbid numeric 123 The “policy breach ID” of the model breach.
```
```
time numeric 1530000000000
The timestamp of the first activity which met the
model criteria in epoch time.
```
```
model object
```
```
An object describing the model logic at the time
of request. Requires
historicModelOnly=true.
```
```
model.name string
```
```
Anomalous
Connection::1 GiB
Outbound
```
```
Name of the model that was breached.
```
```
model.pid numeric 1 The “policy id” of the model that was breached.
```
```
model.phid numeric 1
The model “policy history” id. Increments when
the model is modified.
```
```
model.uuid string
80010119-6d7f-0000-
0305-5e0000000215
```
```
A unique ID that is generated on creation of the
model.
```
```
model.mitre object
```
```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```
```
model.mitre.tactics array initial-access
An array of MITRE ATT&CK framework tactics the
model has been mapped to.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.mitre.techniques array T1133
An array of MITRE ATT&CK framework
techniques the model has been mapped to.

model.logic object A data structure that describes the conditions to
bring about a breach.

model.logic.data array 1

```
If the model is a checklist type this will be a list of
component ID numbers. If this model is a
weighted type this will be a list of component ID,
weight object pairs.
```
model.logic.type string componentList The type of model.

model.logic.version numeric 1
A number representing the version of model
logic.

model.throttle numeric 3600
For an individual device, this is the value in
seconds for which this model will not fire again.

model.sharedEndpoints boolean FALSE

```
For models that contain multiple components
that reference an endpoint, this value indicates
whether all endpoints should be identical for the
model to fire.
```
model.actions object
The action to perform as a result of matching this
model firing.

model.actions.alert boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.actions.antigena object

```
An object containing the Darktrace RESPOND
response to be applied as a result of the model
breaching.
```
model.actions.breach boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.actions.model boolean TRUE

```
If true, creates an event in the device’s event log
without creating an alert/ model breach in the
threat tray.
```
model.actions.setPriority boolean FALSE

```
If the priority is to be changed on breach, the
numeric value it should become. If no priority
change action, a false boolean.
```
model.actions.setTag boolean FALSE

```
If a tag is to be applied on model breach, a single
number or array of the system ID for the tag(s) to
be applied. If no tag action, a false boolean.
```
model.actions.setType boolean FALSE

```
If a change device type action is to be applied on
model breach, the numeric system ID for the
label to be applied. If no change device type
action is applied to the model, a false boolean.
```
model.tags array AP: Egress
A list of tags that have been applied to this model
in the Threat Visualizer model editor.

model.interval numeric 0

```
Where a model contains multiple components,
this interval represents the time window in
seconds in which all the components should fire
for this model to be breached.
```
model.delay numeric 0

```
Minimum delay in seconds after a positive-
scoring component has fired before the overall
model score is calculated. Only applicable in
target score models.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.sequenced boolean FALSE

```
Whether the components are required to fire in
the specified order for the model breach to
occur.
```
model.active boolean TRUE Whether the model is enabled or disabled.

model.modified string 2018-06-12 14:00:00
Timestamp at which the model was last modified,
in a readable format.

model.activeTimes object An object describing device whitelisting or
blacklisting configured for this model.

model.activeTimes.devices object The device ids for devices on the list.

model.activeTimes.tags object A system field.

model.activeTimes.type string exclusions
The type of list: “restrictions” indicates a blacklist,
“exclusions” a whitelist.

model.activeTimes.version numeric 2 A system field.

model.priority numeric 5

```
The numeric behavior category associated with
the model at the time of request: 0-3 equates to
informational, 4 equates to suspicious and 5
equates to critical.
```
model.category string Critical
The behavior category associated with the
model at the time of request.

model.compliance boolean FALSE

```
Whether the model is in the compliance model
category at the time of request. If true, takes
priority over the value of category.
```
model.autoUpdatable boolean TRUE Whether the model is suitable for auto update.

model.autoUpdate boolean TRUE Whether the model is enabled for auto update.

model.autoSuppress boolean TRUE
Whether the model will automatically be
suppressed in the case of over-breaching.

model.description string

```
A device is moving
large volumes of
data (1GiB+) out of
the
network...
```
```
The optional description of the model.
```
model.behaviour string decreasing
The score modulation function as set in the
model editor.

model.defeats array
An array of model defeats - AND conditions -
which if met, prevent the model from breaching.

model.defeats.arguments object
An object describing the values associated with a
model defeat.

model.defeats.arguments.value string [http://www.example.com](http://www.example.com)
The value(s) that must match for the defeat to
take effect.

model.defeats.comparator string does not match
The comparator that the value is compared
against the create the defeat.

model.defeats.defeatID numeric 1 A unique ID for the defeat.

model.defeats.filtertype string Connection hostname The filter the defeat is made from.

model.created object An object describing the creation of the model.

model.created.by string System Username that created the model.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.edited object
An object describing the edit history of the
model.

model.edited.by string smartinez_admin Username that last edited the model.

model.version numeric 16
The version of the model. Increments on each
edit.

triggeredComponents array
An array describing the model components that
were triggered to create the model breach.

triggeredComponents.time numeric 1530000000000
A timestamp in Epoch time at which the
components were triggered.

triggeredComponents.cbid numeric 1729
The “component breach id”. A unique identifier
for the component breach.

triggeredComponents.cid numeric 1 The “component id”. A unique identifier.

triggeredComponents.chid numeric 1
The “component history id”. Increments when
the component is edited.

triggeredComponents.size numeric 1155203452
The size of the value that was compared in the
component.

triggeredComponents.threshold numeric 1073741824
The threshold value that the size must exceed for
the component to breach.

triggeredComponents.interval numeric 3600
The timeframe in seconds within which the
threshold must be satisfied.

triggeredComponents.logic object An object describing the component logic.

triggeredComponents.logic.data object

```
An object representing the logical relationship
between component filters. Each filter is given an
alphabetical reference and the contents of this
object describe the relationship between those
objects.
```
triggeredComponents.logic.data.left string A Objects on the left will be compared with the
object on the right using the specified operator.

triggeredComponents.logic.data.operato
r
string AND A logical operator to compare filters with.

triggeredComponents.logic.data.right object D Objects on the left will be compared with the
object on the right using the specified operator.

triggeredComponents.logic.version string v0.1 The version of the component logic.

triggeredComponents.metric object
An object describing the metric used in the
component that triggered the Model Breach.

triggeredComponents.metric.mlid numeric 33 The “metric logic” id - unique identifier.

triggeredComponents.metric.name string
externalclientdatat
ransfervolume

```
The metric which data is returned for in system
format.
```
triggeredComponents.metric.label string
External Data
Volume as a Client

```
The metric which data is returned for in readable
format.
```
triggeredComponents.triggeredFilters array
The filters that comprise the component that
were triggered to produce the model breach.

triggeredComponents.triggeredFilters.c
fid
numeric 1
The ‘component filter id’. A unique identifier for
the filter as part of a the component.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

triggeredComponents.triggeredFilters.i
d
string A

```
A filter that is used in the component logic. All
filters are given alphabetical identifiers. Display
filters - those that appear in the breach
notification - can be identified by a lowercase ‘d’
and a numeral.
```
triggeredComponents.triggeredFilters.f
ilterType
string Direction

```
The filtertype that is used in the filter. A full list of
filtertypes can be found on the /filtertypes
endpoint.
```
triggeredComponents.triggeredFilters.a
rguments object

```
An object describing the values and
comparisons made in the filter.
```
triggeredComponents.triggeredFilters.a
rguments.value
string out

```
The value the filtertype should be compared
against (using the specified comparator) to
create the filter.
```
triggeredComponents.triggeredFilters.c
omparatorType
string is

```
The comparator. A full list of comparators
available for each filtertype can be found on the /
filtertypes endpoint.
```
triggeredComponents.triggeredFilters.t
rigger
object
An object containing the value to be compared.
Display filters will have an empty object.

triggeredComponents.triggeredFilters.t
rigger.value
string out The actual value that triggered the filter.

score numeric 0.443
The model breach score, represented by a value
between 0 and 1.

percentscore numeric 44
The model breach score as a simple percentage
equivalent.

device object An object describing a device seen by Darktrace.

device.did numeric (^96) The “device id”, a unique identifier.
device.ip string 10.0.18.224 The current IP associated with the device.
device.ips array IPs associated with the device historically.
device.ips.ip string 10.0.18.224 A historic IP associated with the device.
device.ips.timems numeric 1528812000000
The time the IP was last seen associated with
that device in epoch time.
device.ips.time string 2018-06-12 14:00:00
The time the IP was last seen associated with
that device in readable format.
device.ips.sid numeric 34 The subnet id for the subnet the IP belongs to.
device.sid numeric 34 The subnet id for the subnet the device is
currently located in.
device.hostname string fs182 The current device hostname.
device.firstSeen numeric 1530000000000
The first time the device was seen on the
network.
device.lastSeen numeric 1530000000000
The last time the device was seen on the
network.
device.typename string server The device type in system format.
device.typelabel string Server The device type in readable format.


###### Example Response

_Request:/modelbreaches/123?historicmodelonly=true_

```
Where `deviceattop=true`
```
```
{
"creationTime": 1582213002000,
"commentCount": 0,
"pbid": 123,
"time": 1582212986000,
"model": {
"name": "Compromise::HTTP Beaconing to Rare Destination",
"pid": 143,
"phid": 123,
"uuid": "1a814475-5fef-499b-a467-4e2e68352cbb",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"logic": {
"data": [
265
],
"type": "componentList",
"version": 1
},
"throttle": 3600,
"sharedEndpoints": false,
"actions": {
"alert": true,
"antigena": {},
"breach": true,
"model": true,
"setPriority": false,
"setTag": false,
"setType": false
},
"tags": [
"AP: C2 Comms",
"DNS Server"
],
"interval": 0,
"delay": 0,
"sequenced": false,
"active": true,
"modified": "2019-11-15 11:42:21",
"activeTimes": {
"devices": {},
"tags": {},
"type": "exclusions",
"version": 2
},
"priority": 5,
"category": "Critical",
"compliance": false
"autoUpdatable": true,
"autoUpdate": true,
"autoSuppress": true,
"description": "A device is making regular HTTP connections to a rare external
location...",
"behaviour": "decreasing",
```
_continued..._


```
"defeats": [
{
"arguments": {
"value": "www.example.com"
},
"comparator": "does not match",
"defeatID": 1,
"filtertype": "Connection hostname"
}
],
"created": {
"by": "System"
},
"edited": {
"by": "Sarah",
"userID": 24
},
"version": 16
},
"triggeredComponents": [
{
"time": 1582212985000,
"cbid": 305422,
"cid": 265,
"chid": 265,
"size": 3,
"threshold": 2,
"interval": 14400,
"logic": {
"data": {
"left": "A",
"operator": "AND",
"right": {
"left": "B",
"operator": "AND",
"right": {
...
}
},
"version": "v0.1"
},
"metric": {
"mlid": 1,
"name": "externalconnections",
"label": "External Connections"
},
"device": {
"did": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"sid": 23,
"hostname": "Sarah Development",
"firstSeen": 1581591070000,
"lastSeen": 1582645442000,
"typename": "desktop",
"typelabel": "Desktop"
```
_continued..._


```
},
"triggeredFilters": [
{
"cfid": 2087,
"id": "A",
"filterType": "Rare external endpoint",
"arguments": {
"value": 90
},
"comparatorType": ">",
"trigger": {
"value": "94"
}
},
...
]
}
],
"score": 0.325,
"percentscore": 33
}
```
_Response is abbreviated._

#### Response Schema - historicmodelonly=true&deviceattop=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
creationTime numeric 1530000000000
The timestamp that the record of the breach was
created. This is distinct from the “time” field.
```
```
breachUrl string
```
```
https://appliance-
fqdn/
#modelbreaches/123
```
```
A link to the specific model breach in the
Darktrace Threat Visualizer - the configuration
option FQDN must be set for this field to appear.
```
```
commentCount numeric 2 The number of comments made against this
breach.
```
```
pbid numeric 123 The “policy breach ID” of the model breach.
```
```
time numeric 1530000000000
The timestamp of the first activity which met the
model criteria in epoch time.
```
```
model object
```
```
An object describing the model logic at the time
of request. Requires
historicModelOnly=true.
```
```
model.name string
```
```
Anomalous
Connection::1 GiB
Outbound
```
```
Name of the model that was breached.
```
```
model.pid numeric 1 The “policy id” of the model that was breached.
```
```
model.phid numeric 1 The model “policy history” id. Increments when
the model is modified.
```
```
model.uuid string
80010119-6d7f-0000-
0305-5e0000000215
```
```
A unique ID that is generated on creation of the
model.
```
```
model.mitre object
```
```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.mitre.tactics array initial-access
An array of MITRE ATT&CK framework tactics the
model has been mapped to.

model.mitre.techniques array T1133 An array of MITRE ATT&CK framework
techniques the model has been mapped to.

model.logic object
A data structure that describes the conditions to
bring about a breach.

model.logic.data array 1

```
If the model is a checklist type this will be a list of
component ID numbers. If this model is a
weighted type this will be a list of component ID,
weight object pairs.
```
model.logic.type string componentList The type of model.

model.logic.version numeric 1
A number representing the version of model
logic.

model.throttle numeric 3600
For an individual device, this is the value in
seconds for which this model will not fire again.

model.sharedEndpoints boolean FALSE

```
For models that contain multiple components
that reference an endpoint, this value indicates
whether all endpoints should be identical for the
model to fire.
```
model.actions object
The action to perform as a result of matching this
model firing.

model.actions.alert boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.actions.antigena object

```
An object containing the Darktrace RESPOND
response to be applied as a result of the model
breaching.
```
model.actions.breach boolean TRUE

```
If true, an alert turned on will be pushed out to
external systems if conditions for such alerting
are met.
```
model.actions.model boolean TRUE

```
If true, creates an event in the device’s event log
without creating an alert/ model breach in the
threat tray.
```
model.actions.setPriority boolean FALSE

```
If the priority is to be changed on breach, the
numeric value it should become. If no priority
change action, a false boolean.
```
model.actions.setTag boolean FALSE

```
If a tag is to be applied on model breach, a single
number or array of the system ID for the tag(s) to
be applied. If no tag action, a false boolean.
```
model.actions.setType boolean FALSE

```
If a change device type action is to be applied on
model breach, the numeric system ID for the
label to be applied. If no change device type
action is applied to the model, a false boolean.
```
model.tags array AP: Egress
A list of tags that have been applied to this model
in the Threat Visualizer model editor.

model.interval numeric 0

```
Where a model contains multiple components,
this interval represents the time window in
seconds in which all the components should fire
for this model to be breached.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.sequenced boolean FALSE

```
Whether the components are required to fire in
the specified order for the model breach to
occur.
```
model.active boolean TRUE Whether the model is enabled or disabled.

model.modified string 2018-06-12 14:00:00
Timestamp at which the model was last modified,
in a readable format.

model.activeTimes object An object describing device whitelisting or
blacklisting configured for this model.

model.activeTimes.devices object The device ids for devices on the list.

model.activeTimes.tags object A system field.

model.activeTimes.type string exclusions
The type of list: “restrictions” indicates a blacklist,
“exclusions” a whitelist.

model.activeTimes.version numeric 2 A system field.

model.priority numeric 1
The model’s priority affects the strength with
which it breaches (0-5 scale).

model.autoUpdatable boolean TRUE Whether the model is suitable for auto update.

model.autoUpdate boolean TRUE Whether the model is enabled for auto update.

model.autoSuppress boolean TRUE
Whether the model will automatically be
suppressed in the case of over-breaching.

model.description string

```
A device is moving
large volumes of
data (1GiB+) out of
the
network...
```
```
The optional description of the model.
```
model.behaviour string decreasing
The score modulation function as set in the
model editor.

model.defeats array
An array of model defeats - AND conditions -
which if met, prevent the model from breaching.

model.defeats.arguments object
An object describing the values associated with a
model defeat.

model.defeats.arguments.value string [http://www.example.com](http://www.example.com)
The value(s) that must match for the defeat to
take effect.

model.defeats.comparator string does not match
The comparator that the value is compared
against the create the defeat.

model.defeats.defeatID numeric 1 A unique ID for the defeat.

model.defeats.filtertype string Connection hostname The filter the defeat is made from.

model.created object An object describing the creation of the model.

model.created.by string System Username that created the model.

model.edited object
An object describing the edit history of the
model.

model.edited.by string smartinez_admin Username that last edited the model.

model.version numeric 16
The version of the model. Increments on each
edit.

triggeredComponents array
An array describing the model components that
were triggered to create the model breach.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

triggeredComponents.time numeric 1530000000000
A timestamp in Epoch time at which the
components were triggered.

triggeredComponents.cbid numeric 1729 The “component breach id”. A unique identifier
for the component breach.

triggeredComponents.cid numeric 1 The “component id”. A unique identifier.

triggeredComponents.chid numeric 1
The “component history id”. Increments when
the component is edited.

triggeredComponents.size numeric 1155203452
The size of the value that was compared in the
component.

triggeredComponents.threshold numeric 1073741824
The threshold value that the size must exceed for
the component to breach.

triggeredComponents.interval numeric 3600
The timeframe in seconds within which the
threshold must be satisfied.

triggeredComponents.logic object An object describing the component logic.

triggeredComponents.logic.data object

```
An object representing the logical relationship
between component filters. Each filter is given an
alphabetical reference and the contents of this
object describe the relationship between those
objects.
```
triggeredComponents.logic.data.left string A
Objects on the left will be compared with the
object on the right using the specified operator.

triggeredComponents.logic.data.operato
r
string AND A logical operator to compare filters with.

triggeredComponents.logic.data.right object D
Objects on the left will be compared with the
object on the right using the specified operator.

triggeredComponents.logic.version string v0.1 The version of the component logic.

triggeredComponents.metric object An object describing the metric used in the
component that triggered the Model Breach.

triggeredComponents.metric.mlid numeric 33 The “metric logic” id - unique identifier.

triggeredComponents.metric.name string
externalclientdatat
ransfervolume

```
The metric which data is returned for in system
format.
```
triggeredComponents.metric.label string
External Data
Volume as a Client

```
The metric which data is returned for in readable
format.
```
triggeredComponents.device object An object describing a device seen by Darktrace.

triggeredComponents.device.did numeric 96 The “device id”, a unique identifier.

triggeredComponents.device.ip string 10.0.18.224 The current IP associated with the device.

triggeredComponents.device.ips array IPs associated with the device historically.

triggeredComponents.device.ips.ip string 10.0.18.224 A historic IP associated with the device.

triggeredComponents.device.ips.timems numeric 1528812000000
The time the IP was last seen associated with
that device in epoch time.

triggeredComponents.device.ips.time string 2018-06-12 14:00:00
The time the IP was last seen associated with
that device in readable format.

triggeredComponents.device.ips.sid numeric 34 The subnet id for the subnet the IP belongs to.

triggeredComponents.device.sid numeric 34
The subnet id for the subnet the device is
currently located in.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

triggeredComponents.device.hostname string fs182 The current device hostname.

triggeredComponents.device.firstSeen numeric 1528810000000
The first time the device was seen on the
network.

triggeredComponents.device.lastSeen numeric 1528810000000
The last time the device was seen on the
network.

triggeredComponents.device.typename string server The device type in system format.

triggeredComponents.device.typelabel string Server The device type in readable format.

triggeredComponents.triggeredFilters array
The filters that comprise the component that
were triggered to produce the model breach.

triggeredComponents.triggeredFilters.c
fid
numeric 1
The ‘component filter id’. A unique identifier for
the filter as part of a the component.

triggeredComponents.triggeredFilters.i
d
string A

```
A filter that is used in the component logic. All
filters are given alphabetical identifiers. Display
filters - those that appear in the breach
notification - can be identified by a lowercase ‘d’
and a numeral.
```
triggeredComponents.triggeredFilters.f
ilterType
string Direction

```
The filtertype that is used in the filter. A full list of
filtertypes can be found on the /filtertypes
endpoint.
```
triggeredComponents.triggeredFilters.a
rguments
object
An object describing the values and
comparisons made in the filter.

triggeredComponents.triggeredFilters.a
rguments.value
string out

```
The value the filtertype should be compared
against (using the specified comparator) to
create the filter.
```
triggeredComponents.triggeredFilters.c
omparatorType
string is

```
The comparator. A full list of comparators
available for each filtertype can be found on the /
filtertypes endpoint.
```
triggeredComponents.triggeredFilters.t
rigger object

```
An object containing the value to be compared.
Display filters will have an empty object.
```
triggeredComponents.triggeredFilters.t
rigger.value
string out The actual value that triggered the filter.

score numeric 0.443
The model breach score, represented by a value
between 0 and 1.

percentscore numeric 44
The model breach score as a simple percentage
equivalent.


###### Example Response

_Request: /modelbreaches/123?historicmodelonly=true&deviceattop=false_

```
{
"creationTime": 1582213002000,
"commentCount": 0,
"pbid": 123,
"time": 1582212986000,
"model": {
"name": "Compromise::HTTP Beaconing to Rare Destination",
"pid": 143,
"phid": 123,
"uuid": "1a814475-5fef-499b-a467-4e2e68352cbb",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"logic": {
"data": [
265
],
"type": "componentList",
"version": 1
},
"throttle": 3600,
"sharedEndpoints": false,
"actions": {
"alert": true,
"antigena": {},
"breach": true,
"model": true,
"setPriority": false,
"setTag": false,
"setType": false
},
"tags": [
"AP: C2 Comms",
"DNS Server"
],
"interval": 0,
"delay": 0,
"sequenced": false,
"active": true,
"modified": "2019-11-15 11:42:21",
"activeTimes": {
"devices": {},
"tags": {},
"type": "exclusions",
"version": 2
},
"priority": 5,
"category": "Critical",
"compliance": false
"autoUpdatable": true,
"autoUpdate": true,
"autoSuppress": true,
"description": "A device is making regular HTTP connections to a rare external
location...",
"behaviour": "decreasing",
"defeats": [
{
```
_continued..._


```
"arguments": {
"value": "www.example.com"
},
"comparator": "does not match",
"defeatID": 1,
"filtertype": "Connection hostname"
}
],
"created": {
"by": "System"
},
"edited": {
"by": "Sarah",
"userID": 24
},
"version": 16
},
"triggeredComponents": [
{
"time": 1582212985000,
"cbid": 305422,
"cid": 265,
"chid": 265,
"size": 3,
"threshold": 2,
"interval": 14400,
"logic": {
"data": {
"left": "A",
"operator": "AND",
"right": {
"left": "B",
"operator": "AND",
"right": {
...
}
},
"version": "v0.1"
},
"metric": {
"mlid": 1,
"name": "externalconnections",
"label": "External Connections"
},
"device": {
"did": 316,
"ip": "10.0.56.12",
"ips": [
{
"ip": "10.0.56.12",
"timems": 1581508800000,
"time": "2020-02-12 12:00:00",
"sid": 23
}
],
"sid": 23,
"hostname": "Sarah Development",
"firstSeen": 1581591070000,
"lastSeen": 1582645442000,
"typename": "desktop",
"typelabel": "Desktop"
},
"triggeredFilters": [
```
_continued..._


```
{
"cfid": 2087,
"id": "A",
"filterType": "Rare external endpoint",
"arguments": {
"value": 90
},
"comparatorType": ">",
"trigger": {
"value": "94"
}
},
...
]
}
],
"score": 0.325,
"percentscore": 33
}
```
_Response is abbreviated._

**Checklist vs Weighted**

The examples given above describe a checklist model, where all components must be met for the model to breach. For

checklist models, the logic object contains an array of IDs for the underlying components. This object does not appear

when minimal=true.

For weighted models - where a target score must be reached - each component also carries weighting information:

```
...
"model": {
"then": {
"name": "Anomalous Connection::Download and Upload",
"pid": 97,
"phid": 8783,
"uuid": "80010119-6d7f-0000-0305-5e0000000222",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"logic": {
"data": [
{
"cid": 13293,
"weight": 2
},
{
"cid": 13292,
"weight": 1
},
{
"cid": 13291,
"weight": 1
}
],
"targetScore": 3,
"type": "weightedComponentList",
"version": 1
},
...
```

###### minimal=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
commentCount numeric 2
The number of comments made against this
breach.
```
```
pbid numeric 123 The “policy breach ID” of the model breach.
```
```
time numeric 1528812554000
The timestamp when the record was created in
epoch time.
```
```
model object
An object describing the model logic and history
of the model that was breached.
```
```
model.then object
```
```
An object describing the model logic at the time
of breach. Requires
historicModelOnly=false.
```
```
model.then.name string
```
```
Anomalous
Connection::1 GiB
Outbound
```
```
Name of the model that was breached.
```
model.then.pid numeric (^1) The “policy id” of the model that was breached.
model.then.phid numeric 1
The model “policy history” id. Increments when
the model is modified.
model.then.uuid string
80010119-6d7f-0000-
0305-5e0000000215
A unique ID that is generated on creation of the
model.
model.then.mitre object
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
model.then.mitre.tactics array initial-access
An array of MITRE ATT&CK framework tactics the
model has been mapped to.
model.then.mitre.techniques array T1133
An array of MITRE ATT&CK framework
techniques the model has been mapped to.
model.then.priority numeric 5
The numeric behavior category associated with
the model at the time of model breach: 0-3
equates to informational, 4 equates to suspicious
and 5 equates to critical.
model.then.category string Critical
The behavior category associated with the
model at the time of model breach.
model.then.compliance boolean FALSE
Whether the model is in the compliance model
category at the time of model breach. If true,
takes priority over the value of category.
model.now object
An object describing the model logic at the time
of request. Requires
historicModelOnly=false.
model.now.name string
Anomalous
Connection::1 GiB
Outbound
Name of the model that was breached.
model.now.pid numeric 1 The “policy id” of the model that was breached.
model.now.phid numeric 3343 The model “policy history” id. Increments when
the model is modified.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.now.uuid string
80010119-6d7f-0000-
0305-5e0000000215

```
A unique ID that is generated on creation of the
model.
```
model.now.mitre object

```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```
model.now.mitre.tactics array initial-access An array of MITRE ATT&CK framework tactics the
model has been mapped to.

model.now.mitre.techniques array T1133
An array of MITRE ATT&CK framework
techniques the model has been mapped to.

model.now.priority numeric 5

```
The numeric behavior category associated with
the model at the time of request: 0-3 equates to
informational, 4 equates to suspicious and 5
equates to critical.
```
model.now.category string Critical
The behavior category associated with the
model at the time of request.

model.now.compliance boolean FALSE

```
Whether the model is in the compliance model
category at the time of request. If true, takes
priority over the value of category.
```
triggeredComponents array A data structure that describes the conditions to
bring about a breach.

score numeric 0.443
The model breach score, represented by a value
between 0 and 1.

percentscore numeric 44 The model breach score as a simple percentage
equivalent.

device object An object describing a device seen by Darktrace.

device.did numeric 96 The “device id”, a unique identifier.

device.ip string 10.0.18.224 The current IP associated with the device.

device.ips array IPs associated with the device historically.

device.ips.ip string 10.0.18.224 A historic IP associated with the device.

device.ips.timems numeric 1528812000000
The time the IP was last seen associated with
that device in epoch time.

device.ips.time string 06/12/2022 14:00
The time the IP was last seen associated with
that device in readable format.

device.ips.sid numeric 34 The subnet id for the subnet the IP belongs to.

device.sid numeric 34
The subnet id for the subnet the device is
currently located in.

device.hostname string fs182 The current device hostname.

device.typename string server The device type in system format.

device.typelabel string Server The device type in readable format.


###### Example Response

```
{
"commentCount": 2,
"pbid": 123,
"time": 1528812554000,
"model": {
"then": {
"name": "Anomalous Connection::1 GiB Outbound",
"pid": 1,
"phid": 1,
"uuid": "80010119-6d7f-0000-0305-5e0000000215",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"priority": 5,
"category": "Critical",
"compliance": false
},
"now": {
"name": "Anomalous Connection::1 GiB Outbound",
"pid": 1,
"phid": 3343,
"uuid": "80010119-6d7f-0000-0305-5e0000000215",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"priority": 5,
"category": "Critical",
"compliance": false
}
},
"triggeredComponents": [
{}
],
"score": 0.443,
"percentscore": 44,
"device": {
"did": 96,
"ip": "10.0.18.224",
"ips": [
{
"ip": "10.0.18.224",
"timems": 1528812000000,
"time": "2018-06-12 14:00:00",
"sid": 34
}
],
"sid": 34,
"hostname": "fs182",
"typename": "server",
"typelabel": "Server"
}
```

#### Response Schema - minimal=true&deviceattop=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
commentCount numeric 2
The number of comments made against this
breach.
```
```
pbid numeric 123 The “policy breach ID” of the model breach.
```
```
time numeric 1528812554000
The timestamp when the record was created in
epoch time.
```
```
model object
An object describing the model logic and history
of the model that was breached.
```
```
model.then object
```
```
An object describing the model logic at the time
of breach. Requires
historicModelOnly=false.
```
```
model.then.name string
```
```
Anomalous
Connection::1 GiB
Outbound
```
```
Name of the model that was breached.
```
```
model.then.pid numeric 1 The “policy id” of the model that was breached.
```
```
model.then.phid numeric 1 The model “policy history” id. Increments when
the model is modified.
```
```
model.then.uuid string
80010119-6d7f-0000-
0305-5e0000000215
```
```
A unique ID that is generated on creation of the
model.
```
```
model.then.mitre object
```
```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```
```
model.then.mitre.tactics array initial-access An array of MITRE ATT&CK framework tactics the
model has been mapped to.
```
```
model.then.mitre.techniques array T1133
An array of MITRE ATT&CK framework
techniques the model has been mapped to.
```
```
model.then.priority numeric 5
```
```
The numeric behavior category associated with
the model at the time of model breach: 0-3
equates to informational, 4 equates to suspicious
and 5 equates to critical.
```
```
model.then.category string Critical
The behavior category associated with the
model at the time of model breach.
```
```
model.then.compliance boolean FALSE
```
```
Whether the model is in the compliance model
category at the time of model breach. If true,
takes priority over the value of category.
```
```
model.now object
```
```
An object describing the model logic at the time
of request. Requires
historicModelOnly=false.
```
```
model.now.name string
```
```
Anomalous
Connection::1 GiB
Outbound
```
```
Name of the model that was breached.
```
```
model.now.pid numeric 1 The “policy id” of the model that was breached.
```
```
model.now.phid numeric 3343
The model “policy history” id. Increments when
the model is modified.
```
```
model.now.uuid string
80010119-6d7f-0000-
0305-5e0000000215
```
```
A unique ID that is generated on creation of the
model.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

model.now.mitre object

```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```
model.now.mitre.tactics array initial-access
An array of MITRE ATT&CK framework tactics the
model has been mapped to.

model.now.mitre.techniques array T1133 An array of MITRE ATT&CK framework
techniques the model has been mapped to.

model.now.priority numeric 5

```
The numeric behavior category associated with
the model at the time of request: 0-3 equates to
informational, 4 equates to suspicious and 5
equates to critical.
```
model.now.category string Critical
The behavior category associated with the
model at the time of request.

model.now.compliance boolean FALSE

```
Whether the model is in the compliance model
category at the time of request. If true, takes
priority over the value of category.
```
triggeredComponents array
A data structure that describes the conditions to
bring about a breach.

triggeredComponents.device object An object describing a device seen by Darktrace.

triggeredComponents.device.did numeric 96 The “device id”, a unique identifier.

triggeredComponents.device.ip string 10.0.18.224 The current IP associated with the device.

triggeredComponents.device.ips array IPs associated with the device historically.

triggeredComponents.device.ips.ip string 10.0.18.224 A historic IP associated with the device.

triggeredComponents.device.ips.timems numeric 1528812000000
The time the IP was last seen associated with
that device in epoch time.

triggeredComponents.device.ips.time string 2020-04-07 19:00:00
The time the IP was last seen associated with
that device in readable format.

triggeredComponents.device.ips.sid numeric 34 The subnet id for the subnet the IP belongs to.

triggeredComponents.device.sid numeric 34
The subnet id for the subnet the device is
currently located in.

triggeredComponents.device.hostname string fs182 The current device hostname.

triggeredComponents.device.typename string server The device type in system format.

triggeredComponents.device.typelabel string Server The device type in readable format.

score numeric 0.443
The model breach score, represented by a value
between 0 and 1.

percentscore numeric 44
The model breach score as a simple percentage
equivalent.


###### Example Response

```
{
"commentCount": 2,
"pbid": 123,
"time": 1528812554000,
"model": {
"then": {
"name": "Anomalous Connection::1 GiB Outbound",
"pid": 1,
"phid": 1,
"uuid": "80010119-6d7f-0000-0305-5e0000000215",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"priority": 5,
"category": "Critical",
"compliance": false
},
"now": {
"name": "Anomalous Connection::1 GiB Outbound",
"pid": 1,
"phid": 3343,
"uuid": "80010119-6d7f-0000-0305-5e0000000215",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"priority": 5,
"category": "Critical",
"compliance": false
}
},
"triggeredComponents": [
{
"device": {
"did": 96,
"ip": "10.0.18.224",
"ips": [
{
"ip": "10.0.18.224",
"timems": 1528812000000,
"time": "2018-06-12 14:00:00",
"sid": 34
}
],
"sid": 34,
"hostname": "fs182",
"typename": "server",
"typelabel": "Server"
}
}
],
"score": 0.443,
```
_continued..._


```
"percentscore": 44
}
```
###### minimal=true&historicmodelonly=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
commentCount numeric 2
The number of comments made against this
breach.
```
```
pbid numeric 123 The “policy breach ID” of the model breach.
```
```
time numeric 1528812554000 The timestamp when the record was created in
epoch time.
```
```
model object
An object describing the model logic and history
of the model that was breached.
```
```
model.name string
```
```
Anomalous
Connection::1 GiB
Outbound
```
```
Name of the model that was breached.
```
```
model.pid numeric 1 The “policy id” of the model that was breached.
```
```
model.phid numeric 1 The model “policy history” id. Increments when
the model is modified.
```
```
model.uuid string
80010119-6d7f-0000-
0305-5e0000000215
```
```
A unique ID that is generated on creation of the
model.
```
```
model.mitre object
```
```
Models curated and maintained by the Darktrace
analyst team are mapped to the MITRE ATT&CK
framework, where applicable. This object will
appear on mapped models only and contains
information about the tactics and techniques
mapped.
```
```
model.mitre.tactics array initial-access An array of MITRE ATT&CK framework tactics the
model has been mapped to.
```
```
model.mitre.techniques array T1133
An array of MITRE ATT&CK framework
techniques the model has been mapped to.
```
```
model.priority numeric 5
```
```
The numeric behavior category associated with
the model at the time of request: 0-3 equates to
informational, 4 equates to suspicious and 5
equates to critical.
```
```
model.category string Critical
The behavior category associated with the
model at the time of request.
```
```
model.compliance boolean FALSE
```
```
Whether the model is in the compliance model
category at the time of request. If true, takes
priority over the value of category.
```
```
triggeredComponents array A data structure that describes the conditions to
bring about a breach.
```
```
score numeric 0.443
The model breach score, represented by a value
between 0 and 1.
```
```
percentscore numeric 44 The model breach score as a simple percentage
equivalent.
```
```
device object An object describing a device seen by Darktrace.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

device.did numeric 96 The “device id”, a unique identifier.

device.ip string 10.0.18.224 The current IP associated with the device.

device.ips array IPs associated with the device historically.

device.ips.ip string 10.0.18.224 A historic IP associated with the device.

device.ips.timems numeric 1528812000000 The time the IP was last seen associated with
that device in epoch time.

device.ips.time string 2020-04-07 19:00:00
The time the IP was last seen associated with
that device in readable format.

device.ips.sid numeric (^34) The subnet id for the subnet the IP belongs to.
device.sid numeric 34
The subnet id for the subnet the device is
currently located in.
device.hostname string fs182 The current device hostname.
device.typename string server The device type in system format.
device.typelabel string Server The device type in readable format.


###### Example Response

```
{
"commentCount": 2,
"pbid": 123,
"time": 1528812554000,
"model": {
"name": "Anomalous Connection::1 GiB Outbound",
"pid": 1,
"phid": 1,
"uuid": "80010119-6d7f-0000-0305-5e0000000215",
"mitre": {
"tactics": [
"lateral-movement"
],
"techniques": [
"T1210"
]
},
"priority": 5,
"category": "Critical",
"compliance": false
},
"triggeredComponents": [
{
"device": {
"did": 96,
"ip": "10.0.18.224",
"ips": [
{
"ip": "10.0.18.224",
"timems": 1528812000000,
"time": "2018-06-12 14:00:00",
"sid": 34
}
],
"sid": 34,
"hostname": "fs182",
"typename": "server",
"typelabel": "Server"
}
}
],
"score": 0.443,
"percentscore": 44
}
```

## /MODELBREACHES/[PBID]/COMMENTS

The /comments extension of the /modelbreaches endpoint returns current comments on a model breach and allows for

new comments to be posted, given a pbid value. The pbid must be specified as part of the extension in the format:

```
/modelbreaches/[pbid]/comments.
```
```
POST requests to this endpoint must be made in JSON format. Parameters are not supported.
```
###### Request Type(s)

```
[GET] [POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
responsedata string
When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
Available for GET requests only.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all comments for a model breach with pbid=123:

```
https://[instance]/modelbreaches/123/comments
```
2. POST a comment to a model breach with pbid=123:

```
https://[instance]/modelbreaches/123/comments with body {"message": "Test Comment"}
```
###### Example Response

_Request: /modelbreaches/123/comments_

```
[
{
"message": "Test Comment",
"username": "Sarah",
"time": 1582120499000,
"pid": 12
},
{
"message": "Test Comment 2",
"username": "Chris",
"time": 1582120616000,
"pid": 12
}
]
```

## /MODELBREACHES/[PBID]/COMMENTS RESPONSE

## SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
message string
```
```
Assigned to Aidan
Johnston for
investigation.
```
```
The comment text.
```
```
username string ecarr The user who made the comment.
```
```
time numeric 1580000000000
The time the comment was posted in epoch
time.
```
```
pid numeric 806 The policy id of the model that was breached.
```
###### Example Response

```
[
{
"message": "Test Comment",
"username": "ecarr",
"time": 1582120499000,
"pid": 12
},
{
"message": "Assigned to Aidan Johnston for investigation",
"username": "cchester_admin",
"time": 1582120616000,
"pid": 12
}
]
```

## /MODELBREACHES/[PBID]/ACKNOWLEDGE AND /

## UNACKNOWLEDGE

The /acknowledge and /unacknowledge extensions of the /modelbreaches endpoint allow for breaches to be

acknowledged or unacknowledged programmatically, given a pbid value. This can be very useful when integrating

Darktrace with other SOC or ticket-management tools.

The pbid must be specified as part of the extension in the format: /modelbreaches/[pbid]/acknowledge or

```
/modelbreaches/[pbid]/unacknowledge.
```
```
POST requests to these endpoints can be made with parameters or JSON (6.0+).
```
###### Request Type(s)

```
[POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
acknowledge boolean Acknowledge the model breach. Only available for the /acknowledge endpoint
```
```
PARAMETER TYPE DESCRIPTION
```
```
unacknowledge boolean Unacknowledge the model breach. Only available for the /unacknowledge endpoint
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. POST to acknowledge a model breach with pbid=123:

```
https://[instance]/modelbreaches/123/acknowledge with body {"acknowledge":true}
```
2. POST to unacknowledge a model breach with pbid=123:

```
https://[instance]/modelbreaches/123/unacknowledge with body unacknowledge=true
```

## /NETWORK

The /network endpoint returns data about connectivity between two or more devices - it can take a device or subnet

option - and can be used for investigative and monitoring purposes.

The default metric used is “Data Transfer Volume”, but any metric may be specified to monitor connectivity, behavior and

protocol usage. See _/metrics_ for details of how to review all metrics available, and metrics (Customer Portal) for definitions

of a subset of available metrics.

The statistics object returns the information found on the right-hand side of the Threat Visualizer

when a subnet is focused upon (Customer Portal).

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
applicationprotocol string
This filter can be used to filter the returned data by application protocol. See /enums for the list of
application protocols.
```
```
destinationport numeric This filter can be used to filter the returned data by destination port.
```
```
did numeric Identification number of a device modelled in the Darktrace system.
```
```
endtime numeric End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
from string Start time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
fulldevicedetails boolean
Returns the full device detail objects for all devices referenced by data in an API response. Use of
this parameter will alter the JSON structure of the API response for certain calls.
```
```
intext string
This filter can be used to filter the returned data to that which interacts with external sources and
destinations, or is restricted to internal. Valid values are internal and external.
```
```
ip string Return data for this IP address.
```
```
metric string Name of a metric. See the /metrics endpoint for the full list of current metrics.
```
```
port numeric This filter can be used to filter the returned data by source or destination port.
```
```
protocol string This filter can be used to filter the returned data by IP protocol. See /enums for the list of protocols.
```
```
sourceport numeric This filter can be used to filter the returned data by source port
```
```
starttime numeric Start time of data to return in millisecond format, relative to midnight January 1st 1970 UTC.
```
```
to string End time of data to return in YYYY-MM-DD HH:MM:SS format.
```
```
viewsubnet numeric Takes an sid value to focus on a specific subnet.
```
```
responsedata string
```
```
When given the name of a top-level field or object, restricts the returned JSON to only that field or
object.
```

###### Notes

- Time parameters must always be specified in pairs.
- The devices object contains any internal source/destination devices, the connection direction will not be
    specified. The connections object will specify source/target device pairs and directions.
- The default query for devices uses intext=internal, filtering the returned connections by internal only.
    Specifying intext=external will add an externaldevices object containing any external source/
    destination devices the device has interacted with. The default query for subnets will return both internal and
    external.
- The default timeframe is one hour.
- Please note, this endpoint does not support SaaS metrics.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET the data transfer volume for the device with id 1 on December 10th 2019:

```
https://[instance]/network?
did=1&metric=datatransfervolume&from=2019-12-10T12:00:00&to=2019-12-10
```

###### Example Response

_Request: /network?did=212&metric=datatransfervolume&fulldevicedetails=false_

```
{
"statistics": [
{
"Views": [
{
"View": "Single device",
"in": false,
"out": false
},
{
"View": "All devices",
"in": false,
"out": false
},
{
"View": "Breach devices",
"in": false,
"out": false
}
]
},
{
"Connection Status": [
{
"Connections": "Normal",
"in": 51430,
"out": 25305
},
{
"Connections": "New",
"in": 0,
"out": 0
},
{
"Connections": "Unusual",
"in": 0,
"out": 0
},
{
"Connections": "Breached",
"in": false,
"out": false
}
]
},
{
"Remote Ports": [
{
"rport": 53,
"in": 51430,
"out": 24990
}
...
]
},
{
"Local Ports": [
{
"lport": 58335,
"in": 51430,
"out": 24990
```
_continued..._


```
}
...
]
},
{
"devices": [
{
"device": "192.168.72.4",
"ip": "192.168.72.4",
"in": 43078,
"out": 16660
}
...
]
},
{
"Subnets": []
},
{
"intext": [
{
"intext": "Internal",
"in": 51430,
"out": 25305
}
]
},
{
"protocols": [
{
"protocol": "UDP",
"in": 51430,
"out": 25305
},
{
"protocol": "TCP",
"in": 0,
"out": 0
}
]
},
{
"applicationprotocols": [
{
"applicationprotocol": "DNS",
"in": 51430,
"out": 25305
},
{
"applicationprotocol": "Unknown",
"in": 0,
"out": 0
}
]
}
],
"subnets": [],
"devices": [
{
"did": 212,
"size": 76735,
"timems": 1587138366410,
"ips": [
```
_continued..._


"10.15.3.39"
],
"sid": 12,
"ip": "10.15.3.39",
"network": "10.15.3.0/24"
}
],
"metric": {
"mlid": 17,
"name": "datatransfervolume",
"label": "Data Transfer",
"units": "bytes",
"filtertypes": [
"Feature model",
...
],
"unitsinterval": 3600,
"lengthscale": 599997600
},
"connections": [
{
"source": {
"id": -6,
"type": "subnet"
},
"target": {
"id": 212,
"ip": "10.15.3.39",
"type": "device"
},
"timems": 1587138366593,
"size": 36000000
}
...
]
}


## /NETWORK RESPONSE SCHEMA

Note: The statistics object will always contain statistics about data transfer, regardless of the metric specified in the

request.

#### Response Schema - did

###### fulldevicedetails=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
statistics array
```
```
An array of statistics about the connections
made by the device or subnet. Regardless of the
metric specified, these statistics will always relate
to data transfer volumes.
```
```
statistics.Views array An array of system fields
```
```
statistics.Views.View string Single device A system field
```
```
statistics.Views.in boolean FALSE A system field
```
```
statistics.Views.out boolean FALSE A system field
```
```
statistics.Connection Status array
An array of statuses that the connections may be
classified as
```
```
statistics.Connection
Status.Connections
string Normal
A connection status. May be Normal, Unusual,
New or Breached.
```
```
statistics.Connection Status.in numeric 95567
The total inbound data transfer for the device
during the timeframe in bytes
```
```
statistics.Connection Status.out numeric 36964662
The total outbound data transfer for the device
during the timeframe in bytes
```
```
statistics.Remote Ports array
```
```
An array of remote ports (ports on other devices)
that the device has sent data to or received data
from
```
```
statistics.Remote Ports.rport numeric 51728
A remote port interacted with by the specified
device
```
```
statistics.Remote Ports.in numeric 41813 The amount of data received from the remote
port
```
```
statistics.Remote Ports.out numeric 36939077 The amount of data sent to the remote port
```
```
statistics.Local Ports array
```
```
An array of local ports (ports on the specified
device) that the device has sent data from or
received data to
```
```
statistics.Local Ports.lport numeric 22 A local port on the specified device
```
```
statistics.Local Ports.in numeric 41813 The amount of data received by that local port
```
```
statistics.Local Ports.out numeric 36939225 The amount of data sent from that local port
```
```
statistics.devices array
An array of other devices that the device has sent
data to or received data from
```
```
statistics.devices.device string 10.0.18.224 The hostname or IP of the other device
```
```
statistics.devices.ip string 10.0.18.224 The IP of the other device
```
```
statistics.devices.in numeric 41813 The amount of data received from that device
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

statistics.devices.out numeric 36939225 The amount of data sent to that device

statistics.Subnets array

```
When a subnet is specified, an array of subnets
that devices in the specified subnet have
interacted with.
```
statistics.intext array
An array of information about the type of
connection and data transferred

statistics.intext.intext string Internal The connection type filter - either external or
internal

statistics.intext.in numeric 95567
The total inbound data transfer for the device
during the timeframe in bytes

statistics.intext.out numeric 36964662 The total outbound data transfer for the device
during the timeframe in bytes

statistics.protocols array
An array of network protocols identified in the
connections

statistics.protocols.protocol string TCP A network protocol

statistics.protocols.in numeric 41813
The volume of inbound data transferred using
that protocol

statistics.protocols.out numeric 36939225
The volume of outbound data transferred using
that protocol

statistics.applicationprotocols array
An array of application protocols used in the
connections

statistics.applicationprotocols.applic
ationprotocol string
SSH An application protocol

statistics.applicationprotocols.in numeric 41813
The volume of inbound data transferred using
that protocol

statistics.applicationprotocols.out numeric 36939225
The volume of outbound data transferred using
that protocol

subnets array
An array of subnets that have been interacted
with by the device

devices array

```
When a single device is specified, information
about that specific device and any others it has
communicated with.
```
devices.did numeric 174 The “device id” of the specified device.

devices.size numeric 37060229

```
Depending on the metric specified, the amount
of data transferred in the connections involving
that device or the number of matching
connections.
```
devices.timems numeric 1586270000000
The time the IP was last seen associated with
that device in epoch time

devices.ips array 10.15.3.39 IPs associated with the device historically

devices.sid numeric 82
The subnet id for the subnet the device is
currently located in

devices.ip string 10.15.3.39 The current IP associated with the device

devices.network string 10.15.3.0/24
The IP address range that describes the subnet
the IP is contained within

metric object An object describing the metric queried upon


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

metric.mlid numeric 17 The “metric logic” id - unique identifier.

metric.name string datatransfervolume
The metric which data is returned for in system
format

metric.label string Data Transfer
The metric which data is returned for in readable
format

metric.units string bytes The units the metric is measured in, if applicable.

metric.filtertypes array
Unusual ASN for
domain

```
An array of filters which can be used with this
metric
```
metric.unitsinterval numeric 3600 The default time interval for the metric

metric.lengthscale numeric (^599997600) A system field
connections array
An array of connection objects associated with
the device and metric over the time period
connections.source object An object describing the source of a connection
connections.source.id numeric -6 The device id for the source of the connection
connections.source.ip string 10.15.3.39 The IP of the source device
connections.source.type string subnet
The type of device, host or entity originating the
connection.
connections.target object An object describing the source of a target
connections.target.id numeric (^174) The device id for the target of the connection
connections.target.ip string 10.15.3.39 The IP of the target device
connections.target.type string device
The type of device, host or entity targeted by the
connection.
connections.timems numeric 1586270000000 A timestamp for the connection in epoch time
connections.size numeric 36000000
The time frame covered by the initial request in
seconds x 10000


###### Example Response

```
{
"statistics": [
{
"Views": [
{
"View": "Single device",
"in": false,
"out": false
},
{
"View": "All devices",
"in": false,
"out": false
},
{
"View": "Breach devices",
"in": false,
"out": false
}
]
},
{
"Connection Status": [
{
"Connections": "Normal",
"in": 51430,
"out": 25305
},
{
"Connections": "New",
"in": 0,
"out": 0
},
{
"Connections": "Unusual",
"in": 0,
"out": 0
},
{
"Connections": "Breached",
"in": false,
"out": false
}
]
},
{
"Remote Ports": [
{
"rport": 53,
"in": 51430,
"out": 24990
}
...
]
},
{
"Local Ports": [
{
"lport": 58335,
"in": 51430,
"out": 24990
```
_continued..._


```
}
...
]
},
{
"devices": [
{
"device": "192.168.72.4",
"ip": "192.168.72.4",
"in": 43078,
"out": 16660
}
...
]
},
{
"Subnets": []
},
{
"intext": [
{
"intext": "Internal",
"in": 51430,
"out": 25305
}
]
},
{
"protocols": [
{
"protocol": "UDP",
"in": 51430,
"out": 25305
},
{
"protocol": "TCP",
"in": 0,
"out": 0
}
]
},
{
"applicationprotocols": [
{
"applicationprotocol": "DNS",
"in": 51430,
"out": 25305
},
{
"applicationprotocol": "Unknown",
"in": 0,
"out": 0
}
]
}
],
"subnets": [],
"devices": [
{
"did": 212,
"size": 76735,
"timems": 1587138366410,
"ips": [
```
_continued..._


```
"10.15.3.39"
],
"sid": 12,
"ip": "10.15.3.39",
"network": "10.15.3.0/24"
}
],
"metric": {
"mlid": 17,
"name": "datatransfervolume",
"label": "Data Transfer",
"units": "bytes",
"filtertypes": [
"Feature model",
...
],
"unitsinterval": 3600,
"lengthscale": 599997600
},
"connections": [
{
"source": {
"id": -6,
"type": "subnet"
},
"target": {
"id": 212,
"ip": "10.15.3.39",
"type": "device"
},
"timems": 1587138366593,
"size": 36000000
}
...
]
}
```
_Response is abbreviated._

###### fulldevicedetails=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
statistics array
```
```
An array of statistics about the connections
made by the device or subnet. Regardless of the
metric specified, these statistics will always relate
to data transfer volumes.
```
```
statistics.Views array An array of system fields.
```
```
statistics.Views.View string Single device A system field.
```
```
statistics.Views.in boolean FALSE A system field.
```
```
statistics.Views.out boolean FALSE A system field.
```
```
statistics.Connection Status array
An array of statuses that the connections may be
classified as.
```
```
statistics.Connection
Status.Connections
string Normal
A connection status. May be Normal, Unusual,
New or Breached.
```
```
statistics.Connection Status.in numeric 95747
The total inbound data transfer for the device
during the timeframe in bytes.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

statistics.Connection Status.out numeric 38059962
The total outbound data transfer for the device
during the timeframe in bytes.

statistics.Remote Ports array

```
An array of remote ports (ports on other devices)
that the device has sent data to or received data
from.
```
statistics.Remote Ports.rport numeric 51728
A remote port interacted with by the specified
device.

statistics.Remote Ports.in numeric 42137
The amount of data received from the remote
port.

statistics.Remote Ports.out numeric 38034377 The amount of data sent to the remote port.

statistics.Local Ports array

```
An array of local ports (ports on the specified
device) that the device has sent data from or
received data to.
```
statistics.Local Ports.lport numeric 22 A local port on the specified device.

statistics.Local Ports.in numeric (^42137) The amount of data received by that local port.
statistics.Local Ports.out numeric 38034525 The amount of data sent from that local port.
statistics.devices array
An array of other devices that the device has sent
data to or received data from.
statistics.devices.device string 10.0.18.224 The hostname or IP of the other device.
statistics.devices.ip string 10.0.18.224 The IP of the other device.
statistics.devices.in numeric (^42137) The amount of data received from that device.
statistics.devices.out numeric 38034525 The amount of data sent to that device.
statistics.Subnets array
When a subnet is specified, an array of subnets
that devices in the specified subnet have
interacted with.
statistics.intext array
An array of information about the type of
connection and data transferred.
statistics.intext.intext string Internal
The connection type filter - either external or
internal.
statistics.intext.in numeric 95747
The total inbound data transfer for the device
during the timeframe in bytes.
statistics.intext.out numeric 38059962
The total outbound data transfer for the device
during the timeframe in bytes.
statistics.protocols array
An array of network protocols identified in the
connections.
statistics.protocols.protocol string TCP A network protocol.
statistics.protocols.in numeric 42137
The volume of inbound data transferred using
that protocol.
statistics.protocols.out numeric 38034525
The volume of outbound data transferred using
that protocol.
statistics.applicationprotocols array
An array of application protocols used in the
connections.
statistics.applicationprotocols.applic
ationprotocol
string SSH An application protocol.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

statistics.applicationprotocols.in numeric 42137
The volume of inbound data transferred using
that protocol.

statistics.applicationprotocols.out numeric 38034525 The volume of outbound data transferred using
that protocol.

subnets array
An array of subnets that have been interacted
with by the device.

devices array

```
When a single device is specified, information
about that specific device and any others it has
communicated with.
```
devices.did numeric 532 The “device id” of the specified device.

devices.macaddress string 6e:b7:31:d5:33:6c The current MAC address associated with the
device.

devices.vendor string
ASUSTek COMPUTER
INC.

```
The vendor of the device network card as
derived by Darktrace from the MAC address.
```
devices.ip string 10.12.14.2 The current IP associated with the device.

devices.ips array IPs associated with the device historically.

devices.ips.ip string 10.12.14.2 The current IP associated with the device.

devices.ips.timems numeric 1586937881000
The time the IP was last seen associated with
that device in epoch time.

devices.ips.time string 2020-04-15 08:04:41
The time the IP was last seen associated with
that device in readable format.

devices.ips.sid numeric (^39) The subnet id for the subnet the IP belongs to.
devices.sid numeric 39
The subnet id for the subnet the device is
currently located in.
devices.hostname string sarah-desktop-12 The current device hostname.
devices.firstSeen numeric 1530000000000
The first time the device was seen on the
network.
devices.lastSeen numeric 1590000000000
The last time the device was seen on the
network.
devices.os string
Linux 3.11 and
newer
The device operating system if Darktrace is able
to derive it.
devices.typename string desktop The device type in system format.
devices.typelabel string Desktop The device type in readable format.
devices.tags array An object describing tags applied to the device.
devices.tags.tid numeric (^73) The “tag id”. A unique value.
devices.tags.expiry numeric 0
The expiry time for the tag when applied to a
device.
devices.tags.thid numeric 78
The “tag history” id. Increments if the tag is
edited.
devices.tags.name string Test Tag
The tag label displayed in the user interface or in
objects that reference the tag.
devices.tags.restricted boolean FALSE
Indicates a read-only tag - these tags can only be
modified or applied by Darktrace.
devices.tags.data object An object containing information about the tag.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

devices.tags.data.auto boolean FALSE Whether the tag was auto-generated.

devices.tags.data.color numeric 134
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.

devices.tags.data.description string
Testing the use of
tags.

```
An optional description summarizing the
purpose of the tag.
```
devices.tags.data.visibility string Public A system field.

devices.tags.isReferenced boolean FALSE
Whether the tag is used by one or more model
components.

devices.size numeric 38155709

```
Depending on the metric specified, the amount
of data transferred in the connections involving
that device or the number of matching
connections.
```
devices.timems numeric 1590000000000
A timestamp at which the data was gathered in
epoch time.

devices.network string 10.12.14.0/24 The IP address range that describes the subnet
the IP is contained within

metric object An object describing the metric queried upon.

metric.mlid numeric 17 The “metric logic” id - unique identifier.

metric.name string datatransfervolume
The metric which data is returned for in system
format.

metric.label string Data Transfer
The metric which data is returned for in readable
format.

metric.units string bytes The units the metric is measured in, if applicable.

metric.filtertypes array Direction
An array of filters which can be used with this
metric.

metric.unitsinterval numeric (^3600) The default time interval for the metric.
metric.lengthscale numeric 599997600 A system field.
connections array
An array of connection objects associated with
the device and metric over the time period.
connections.source object An object describing the source of a connection.
connections.source.id numeric -6 The device id for the source of the connection.
connections.source.ip string 10.15.3.39 The IP of the source device.
connections.source.type string subnet
The type of device, host or entity originating the
connection.
connections.target object An object describing the source of a target.
connections.target.id numeric 532 The device id for the target of the connection.
connections.target.ip string 10.12.14.2 The IP of the target device.
connections.target.type string device
The type of device, host or entity targeted by the
connection.
connections.timems numeric 1590000000000 A timestamp for the connection in epoch time.
connections.size numeric 36000000 The time frame covered by the initial request in
seconds x 10000.


###### Example Response

```
{
"statistics": [
{
"Views": [
{
"View": "Single device",
"in": false,
"out": false
},
{
"View": "All devices",
"in": false,
"out": false
},
{
"View": "Breach devices",
"in": false,
"out": false
}
]
},
{
"Connection Status": [
{
"Connections": "Normal",
"in": 51574,
"out": 25305
},
{
"Connections": "New",
"in": 0,
"out": 0
},
{
"Connections": "Unusual",
"in": 0,
"out": 0
},
{
"Connections": "Breached",
"in": false,
"out": false
}
]
},
{
"Remote Ports": [
{
"rport": 53,
"in": 51574,
"out": 24990
}
...
]
},
{
"Local Ports": [
{
"lport": 58335,
"in": 51574,
"out": 24990
```
_continued..._


```
}
...
]
},
{
"devices": [
{
"device": "192.168.72.4",
"ip": "192.168.72.4",
"in": 43078,
"out": 16660
}
...
]
},
{
"Subnets": []
},
{
"intext": [
{
"intext": "Internal",
"in": 51574,
"out": 25305
}
]
},
{
"protocols": [
{
"protocol": "UDP",
"in": 51574,
"out": 25305
}
...
]
},
{
"applicationprotocols": [
{
"applicationprotocol": "DNS",
"in": 51574,
"out": 25305
},
...
]
}
],
"subnets": [],
"devices": [
{
"did": 174,
"macaddress": "2g:d8:a2:a8:54:c6",
"vendor": "ASUSTek COMPUTER INC.",
"ip": "10.15.3.39",
"ips": [
{
"ip": "10.15.3.39",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 12
}
],
```
_continued..._


```
"sid": 12,
"hostname": "ws83",
"firstSeen": 1528807077000,
"lastSeen": 1587136632000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop",
"tags": [
{
"tid": 73,
"expiry": 0,
"thid": 78,
"name": "Admin",
"restricted": false,
"data": {
"auto": false,
"color": 134,
"description": "",
"visibility": "Public"
},
"isReferenced": false
}
],
"size": 76879,
"timems": 1587138396904,
"sid": 82,
"ip": "10.15.3.39",
"network": "10.15.3.0/24"
}
],
"metric": {
"mlid": 17,
"name": "datatransfervolume",
"label": "Data Transfer",
"units": "bytes",
"filtertypes": [
"Feature model",
...
],
"unitsinterval": 3600,
"lengthscale": 599997600
},
"connections": [
{
"source": {
"id": -6,
"type": "subnet"
},
"target": {
"id": 174,
"ip": "10.15.3.39",
"type": "device"
},
"timems": 1587138396904,
"size": 36000000
},
...
]
}
```
_Response is abbreviated._


#### Response Schema - did and intext=external

###### fulldevicedetails=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
statistics array
```
```
An array of statistics about the connections
made by the device or subnet. Regardless of the
metric specified, these statistics will always relate
to data transfer volumes.
```
```
statistics.Views array An array of system fields.
```
```
statistics.Views.View string Single device A system field.
```
```
statistics.Views.in boolean FALSE A system field.
```
```
statistics.Views.out boolean FALSE A system field.
```
```
statistics.Connection Status array
An array of statuses that the connections may be
classified as.
```
```
statistics.Connection
Status.Connections
string Normal
A connection status. May be Normal, Unusual,
New or Breached.
```
```
statistics.Connection Status.in numeric 20573
The total inbound data transfer for the device
during the timeframe in bytes.
```
```
statistics.Connection Status.out numeric 4793
The total outbound data transfer for the device
during the timeframe in bytes.
```
```
statistics.Remote Ports array
```
```
An array of remote ports (ports on other devices)
that the device has sent data to or received data
from.
```
```
statistics.Remote Ports.rport numeric 443
A remote port interacted with by the specified
device.
```
```
statistics.Remote Ports.in numeric 20573 The amount of data received from the remote
port.
```
```
statistics.Remote Ports.out numeric 4793 The amount of data sent to the remote port.
```
```
statistics.Local Ports array
```
```
An array of local ports (ports on the specified
device) that the device has sent data from or
received data to.
```
```
statistics.Local Ports.lport numeric 51416 A local port on the specified device.
```
```
statistics.Local Ports.in numeric 7955 The amount of data received by that local port.
```
```
statistics.Local Ports.out numeric 1733 The amount of data sent from that local port.
```
```
statistics.devices array
An array of other devices that the device has sent
data to or received data from.
```
```
statistics.devices.device string google.com The hostname or IP of the other device.
```
```
statistics.devices.ip string google.com
The IP of the other device. For external locations,
this may be a hostname.
```
statistics.devices.in numeric (^15023) The amount of data received from that device.
statistics.devices.out numeric 3467 The amount of data sent to that device.
statistics.intext array
An array of information about the type of
connection and data transferred.
statistics.intext.intext string External
The connection type filter - either external or
internal.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

statistics.intext.in numeric 20573
The total inbound data transfer for the device
during the timeframe in bytes.

statistics.intext.out numeric 4793 The total outbound data transfer for the device
during the timeframe in bytes.

statistics.protocols array
An array of network protocols identified in the
connections.

statistics.protocols.protocol string TCP A network protocol.

statistics.protocols.in numeric 20573
The volume of inbound data transferred using
that protocol.

statistics.protocols.out numeric 4793
The volume of outbound data transferred using
that protocol.

statistics.applicationprotocols array
An array of application protocols used in the
connections.

statistics.applicationprotocols.applic
ationprotocol string
HTTPS An application protocol.

statistics.applicationprotocols.in numeric 20573
The volume of inbound data transferred using
that protocol.

statistics.applicationprotocols.out numeric 4793
The volume of outbound data transferred using
that protocol.

subnets array
An array of subnets that have been interacted
with by the device.

devices array

```
When a single device is specified, information
about that specific device and any others it has
communicated with.
```
devices.did numeric 83 The “device id” of the specified device.

devices.size numeric 18490

```
Depending on the metric specified, the amount
of data transferred in the connections involving
that device or the number of matching
connections.
```
devices.timems numeric 1586937881000
A timestamp at which the data was gathered in
epoch time.

devices.ips array 10.15.3.39 IPs associated with the device historically.

devices.sid numeric 77
The subnet id for the subnet the device is
currently located in.

devices.ip string 10.15.3.39 The current IP associated with the device.

devices.network string 10.15.3.0/24
The IP address range that describes the subnet
the IP is contained within

externaldevices array
An array of external devices that the specified
device has interacted with.

externaldevices.id numeric 0

```
Where applicable, an id for the external device.
This can be cross-referenced with the
connections object.
```
externaldevices.size numeric 18490

```
Depending on the metric specified, the amount
of data transferred in the connections involving
that external location or the number of matching
connections.
```
externaldevices.timems numeric 1586937881000
A timestamp at which the data was gathered in
epoch time.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

externaldevices.hostname string google.com A hostname associated with the external device.

externaldevices.name string 104.20.203.23
A hostname or IP associated with the external
device.

externaldevices.hostnames array
An array of hostnames that have been historically
associated with the external location.

externaldevices.hostnames.hostname string google.com A hostname associated with the external device.

externaldevices.hostnames.count numeric 3
The number of connections to that hostname
during the specified timeframe.

externaldevices.ip string 172.217.169.36 The IP associated with the hostname.

externaldevices.longitude numeric 172.217.169.36
For the reported IP location, the longitude value
to plot the IP on a map.

externaldevices.latitude numeric 37.751
For the reported IP location, the latitude value to
plot the IP on a map.

externaldevices.country string United States The country that the IP is located in.

externaldevices.countrycode string US
The system country code for the country that the
IP is located in.

externaldevices.asn string AS15169 Google LLC The ASN for the IP.

externaldevices.region string North America The geographical region the IP is located in.

metric object An object describing the metric queried upon.

metric.mlid numeric (^17) The “metric logic” id - unique identifier.
metric.name string datatransfervolume
The metric which data is returned for in system
format.
metric.label string Data Transfer The metric which data is returned for in readable
format.
metric.units string bytes The units the metric is measured in, if applicable.
metric.filtertypes array Feature model
An array of filters which can be used with this
metric.
metric.unitsinterval numeric 3600 The default time interval for the metric.
metric.lengthscale numeric 599997600 A system field.
connections array
An array of connection objects associated with
the device and metric over the time period.
connections.source object An object describing the source of a connection.
connections.source.id numeric (^2899945802) The device id for the source of the connection.
connections.source.ip string 10.15.3.39
The IP of the source device. For external
locations, this field may not appear.
connections.source.type string externaldevice
The type of device, host or entity originating the
connection.
connections.target object An object describing the source of a target.
connections.target.id numeric 83 The device id for the target of the connection.
connections.target.ip string 192.168.72.4
The IP of the target device. For external locations,
this field may not appear.
connections.target.type string device
The type of device, host or entity targeted by the
connection.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

connections.timems numeric 1586937881000 A timestamp for the connection in epoch time.

connections.size numeric 36000000
The time frame covered by the initial request in
seconds x 10000.


###### Example Response

```
{
"statistics": [
{
"Views": [
{
"View": "Single device",
"in": false,
"out": false
},
{
"View": "All devices",
"in": false,
"out": false
},
{
"View": "Breach devices",
"in": false,
"out": false
}
]
},
{
"Connection Status": [
{
"Connections": "New",
"in": false,
"out": false
},
{
"Connections": "Unusual",
"in": false,
"out": false
},
{
"Connections": "Normal",
"in": false,
"out": false
},
{
"Connections": "Breached",
"in": false,
"out": false
}
]
},
{
"applicationprotocols": [
{
"applicationprotocol": "HTTPS",
"in": 13500,
"out": 4794
}
]
}
],
"subnets": [],
"devices": [
{
"did": 212,
"size": 76735,
"timems": 1587138366410,
```
_continued..._


```
"ips": [
"10.15.3.39"
],
"sid": 12,
"ip": "10.15.3.39",
"network": "10.15.3.0/24"
}
],
"externaldevices": [
{
"id": 3627731978,
"size": 15004,
"timems": 1587142558420,
"hostname": "google.com",
"name": "google.com",
"hostnames": [
{
"hostname": "google.com",
"count": 6
}
],
"longitude": -122.075,
"latitude": 37.404,
"city": "Mountain View",
"country": "United States",
"countrycode": "US",
"asn": "AS15169 Google LLC",
"region": "North America",
"ip": "172.217.169.36"
}
...
],
"metric": {
"mlid": 17,
"name": "datatransfervolume",
"label": "Data Transfer",
"units": "bytes",
"filtertypes": [
"Feature model",
...
],
"unitsinterval": 3600,
"lengthscale": 599997600
},
"connections": [
{
"source": {
"id": -6,
"type": "subnet"
},
"target": {
"id": 212,
"ip": "10.15.3.39",
"type": "device"
},
"timems": 1587138396904,
"size": 36000000
},
...
]
}
```
_Response is abbreviated._


###### fulldevicedetails=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
statistics array
```
```
An array of statistics about the connections
made by the device or subnet. Regardless of the
metric specified, these statistics will always relate
to data transfer volumes.
```
```
statistics.Views array An array of system fields.
```
```
statistics.Views.View string Single device A system field.
```
```
statistics.Views.in boolean FALSE A system field.
```
```
statistics.Views.out boolean FALSE A system field.
```
```
statistics.Connection Status array An array of statuses that the connections may be
classified as.
```
```
statistics.Connection
Status.Connections
string Normal
A connection status. May be Normal, Unusual,
New or Breached.
```
```
statistics.Connection Status.in numeric 20573 The total inbound data transfer for the device
during the timeframe in bytes.
```
```
statistics.Connection Status.out numeric 4793
The total outbound data transfer for the device
during the timeframe in bytes.
```
```
statistics.Remote Ports array
```
```
An array of remote ports (ports on other devices)
that the device has sent data to or received data
from.
```
```
statistics.Remote Ports.rport numeric 443
A remote port interacted with by the specified
device.
```
```
statistics.Remote Ports.in numeric 20573
The amount of data received from the remote
port.
```
```
statistics.Remote Ports.out numeric 4793 The amount of data sent to the remote port.
```
```
statistics.Local Ports array
```
```
An array of local ports (ports on the specified
device) that the device has sent data from or
received data to.
```
```
statistics.Local Ports.lport numeric 51416 A local port on the specified device.
```
statistics.Local Ports.in numeric (^7955) The amount of data received by that local port.
statistics.Local Ports.out numeric 1733 The amount of data sent from that local port.
statistics.devices array
An array of other devices that the device has sent
data to or received data from.
statistics.devices.device string google.com The hostname or IP of the other device.
statistics.devices.ip string google.com
The IP of the other device. For external locations,
this may be a hostname.
statistics.devices.in numeric (^15023) The amount of data received from that device.
statistics.devices.out numeric 3467 The amount of data sent to that device.
statistics.intext array
An array of information about the type of
connection and data transferred.
statistics.intext.intext string External
The connection type filter - either external or
internal.
statistics.intext.in numeric 20573
The total inbound data transfer for the device
during the timeframe in bytes.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

statistics.intext.out numeric 4793
The total outbound data transfer for the device
during the timeframe in bytes.

statistics.protocols array An array of network protocols identified in the
connections.

statistics.protocols.protocol string TCP A network protocol.

statistics.protocols.in numeric 20573
The volume of inbound data transferred using
that protocol.

statistics.protocols.out numeric 4793
The volume of outbound data transferred using
that protocol.

statistics.applicationprotocols array
An array of application protocols used in the
connections.

statistics.applicationprotocols.applic
ationprotocol
string HTTPS An application protocol.

statistics.applicationprotocols.in numeric 20573
The volume of inbound data transferred using
that protocol.

statistics.applicationprotocols.out numeric 4793
The volume of outbound data transferred using
that protocol.

subnets array
An array of subnets that have been interacted
with by the device.

devices array

```
When a single device is specified, information
about that specific device and any others it has
communicated with.
```
devices.did numeric (^3877) The “device id” of the specified device.
devices.macaddress string 93:gb:28:g1:fc:g1
The current MAC address associated with the
device.
devices.vendor string
ASUSTek COMPUTER
INC.
The vendor of the device network card as
derived by Darktrace from the MAC address.
devices.ip string 10.15.3.39 The current IP associated with the device.
devices.ips array IPs associated with the device historically.
devices.ips.ip string 10.15.3.39 The current IP associated with the device.
devices.ips.timems numeric 1586937881000
The time the IP was last seen associated with
that device in epoch time.
devices.ips.time string 2020-04-15 08:04:41 The time the IP was last seen associated with
that device in readable format.
devices.ips.sid numeric 82 The subnet id for the subnet the IP belongs to.
devices.sid numeric 82
The subnet id for the subnet the device is
currently located in.
devices.hostname string ws83 The current device hostname.
devices.firstSeen numeric 1528812000000
The first time the device was seen on the
network.
devices.lastSeen numeric 1586937881000
The last time the device was seen on the
network.
devices.os string
Linux 3.11 and
newer
The device operating system if Darktrace is able
to derive it.
devices.typename string desktop The device type in system format.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

devices.typelabel string Desktop The device type in readable format.

devices.tags array An object describing tags applied to the device.

devices.tags.tid numeric 73 The “tag id”. A unique value.

devices.tags.expiry numeric 0
The expiry time for the tag when applied to a
device.

devices.tags.thid numeric 78
The “tag history” id. Increments if the tag is
edited.

devices.tags.name string Test Tag
The tag label displayed in the user interface or in
objects that reference the tag.

devices.tags.restricted boolean FALSE
Indicates a read-only tag - these tags can only be
modified or applied by Darktrace.

devices.tags.data object An object containing information about the tag.

devices.tags.data.auto boolean FALSE Whether the tag was auto-generated.

devices.tags.data.color numeric 134
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.

devices.tags.data.description string
Testing the use of
tags.

```
An optional description summarizing the
purpose of the tag.
```
devices.tags.data.visibility string Public A system field.

devices.tags.isReferenced boolean FALSE
Whether the tag is used by one or more model
components.

devices.size numeric 18490

```
Depending on the meric specified, the amount of
data transferred in the connections involving that
device or the number of matching connections.
```
devices.timems numeric 1586937881000
A timestamp at which the data was gathered in
epoch time.

devices.network string 10.140.15.0/24
The IP address range that describes the subnet
the IP is contained within

externaldevices array
An array of external devices that the specified
device has interacted with.

externaldevices.id numeric 0

```
Where applicable, an id for the external device.
This can be corss-referenced with the
connections object.
```
externaldevices.hostname string google.com

```
Depending on the meric specified, the amount of
data transferred in the connections involving that
external location or the number of matching
connections.
```
externaldevices.name string google.com
A timestamp at which the data was gathered in
epoch time.

externaldevices.hostnames array A hostname associated with the external device.

externaldevices.hostnames.hostname string google.com
A hostname or IP associated with the external
device.

externaldevices.hostnames.count numeric 3
An array of hostnames that have been historically
associated with the external location.

externaldevices.ip string 172.217.169.36
A hostname or IP associated with the external
device.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

externaldevices.size numeric 18490
The number of connections to that hostname
during the specified timeframe.

externaldevices.timems numeric (^1586937881000) The IP associated with the hostname.
externaldevices.longitude numeric -97.822
For the reported IP location, the longitude value
to plot the IP on a map.
externaldevices.latitude numeric 37.751
For the reported IP location, the latitude value to
plot the IP on a map.
externaldevices.country string United States The country that the IP is located in.
externaldevices.countrycode string US
The system country code for the country that the
IP is located in.
externaldevices.asn string AS15169 Google LLC The ASN for the IP.
externaldevices.region string North America The geographical region the IP is located in.
metric object An object describing the metric queried upon.
metric.mlid numeric 17 The “metric logic” id - unique identifier.
metric.name string datatransfervolume
The metric which data is returned for in system
format.
metric.label string Data Transfer
The metric which data is returned for in readable
format.
metric.units string bytes The units the metric is measured in, if applicable.
metric.filtertypes array Direction
An array of filters which can be used with this
metric.
metric.unitsinterval numeric 3600 The default time interval for the metric.
metric.lengthscale numeric (^599997600) A system field.
connections array
An array of connection objects associated with
the device and metric over the time period.
connections.source object An object describing the source of a connection.
connections.source.ip string 172.217.169.36 The device id for the source of the connection.
connections.source.id numeric 2899945802
The IP of the source device. For external
locations, this field may not appear.
connections.source.type string externaldevice
The type of device, host or entity originating the
connection.
connections.target object An object describing the source of a target.
connections.target.id numeric (^938) The device id for the target of the connection.
connections.target.ip string 10.15.3.39
The IP of the target device. For external locations,
this field may not appear.
connections.target.type string device
The type of device, host or entity targeted by the
connection.
connections.timems numeric 1586937881000 A timestamp for the connection in epoch time.
connections.size numeric 36000000
The time frame covered by the initial request in
seconds x 10000.


###### Example Response

```
{
"statistics": [
{
"Views": [
{
"View": "Single device",
"in": false,
"out": false
},
{
"View": "All devices",
"in": false,
"out": false
},
{
"View": "Breach devices",
"in": false,
"out": false
}
]
},
{
"Connection Status": [
{
"Connections": "New",
"in": false,
"out": false
},
{
"Connections": "Unusual",
"in": false,
"out": false
},
{
"Connections": "Normal",
"in": false,
"out": false
},
{
"Connections": "Breached",
"in": false,
"out": false
}
]
},
{
"applicationprotocols": [
{
"applicationprotocol": "HTTPS",
"in": 13500,
"out": 4794
}
]
}
],
"subnets": [],
"devices": [
{
"did": 212,
"macaddress": "2g:d8:a2:a8:54:c6",
"vendor": "ASUSTek COMPUTER INC.",
```
_continued..._


```
"ip": "10.15.3.39",
"ips": [
{
"ip": "10.15.3.39",
"timems": 1587135600000,
"time": "2020-04-17 15:00:00",
"sid": 12
}
],
"sid": 12,
"hostname": "ws83",
"firstSeen": 1528807077000,
"lastSeen": 1587136632000,
"os": "Linux 3.11 and newer",
"typename": "desktop",
"typelabel": "Desktop",
"tags": [
{
"tid": 73,
"expiry": 0,
"thid": 78,
"name": "Admin",
"restricted": false,
"data": {
"auto": false,
"color": 134,
"description": "",
"visibility": "Public"
},
"isReferenced": false
}
],
"sid": 12,
"ip": "10.15.3.39",
"network": "10.15.3.0/24"
}
],
"externaldevices": [
{
"id": 3627731978,
"size": 15004,
"timems": 1587142558420,
"hostname": "google.com",
"name": "google.com",
"hostnames": [
{
"hostname": "google.com",
"count": 6
}
],
"longitude": -122.075,
"latitude": 37.404,
"city": "Mountain View",
"country": "United States",
"countrycode": "US",
"asn": "AS15169 Google LLC",
"region": "North America",
"ip": "172.217.169.36"
}
...
],
"metric": {
"mlid": 17,
```
_continued..._


```
"name": "datatransfervolume",
"label": "Data Transfer",
"units": "bytes",
"filtertypes": [
"Feature model",
...
], "unitsinterval": 3600,
"lengthscale": 599997600
},
"connections": [
{
"source": {
"id": -6,
"type": "subnet"
},
"target": {
"id": 212,
"ip": "10.15.3.39",
"type": "device"
},
"timems": 1587138396904,
"size": 36000000
},
...
]
}
```
_Response is abbreviated._


#### Response Schema = viewsubnet

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
statistics array
```
```
An array of statistics about the connections
made by the device or subnet. Regardless of the
metric specified, these statistics will always relate
to data transfer volumes.
```
```
statistics.Views array An array of system fields.
```
```
statistics.Views.View string All subnets A system field.
```
```
statistics.Views.in boolean FALSE A system field.
```
```
statistics.Views.out boolean FALSE A system field.
```
```
statistics.Connection Status array
An array of statuses that the connections may be
classified as.
```
```
statistics.Connection
Status.Connections
string Normal
A connection status. May be Normal, Unusual,
New or Breached.
```
```
statistics.Connection Status.in numeric 1273420401
The total inbound data transfer for the subnet
during the timeframe in bytes.
```
```
statistics.Connection Status.out numeric 1273420401
The total outbound data transfer for the subnet
during the timeframe in bytes.
```
```
statistics.devices array
An array of devices within the subnet that have
made connections which transferred data.
```
```
statistics.devices.device string sarah-desktop-12 The hostname or IP of the device.
```
```
statistics.devices.ip string 10.12.14.2 The IP of the device.
```
```
statistics.devices.in numeric 14857836 The amount of data received from by device.
```
```
statistics.devices.out numeric 574830077 The amount of data sent from that device.
```
```
statistics.Subnets array
```
```
When a subnet is specified, an array of subnets
that devices in the specified subnet have
interacted with.
```
```
statistics.Subnets.subnet string 10.0.18.0/24 The network range describing the subnet.
```
```
statistics.Subnets.in numeric 2024715 The amount of data received from this subnet.
```
statistics.Subnets.out numeric (^4329923) The amount of data sent to this subnet.
statistics.intext array
An array of information about the type of
connections and data transferred.
statistics.intext.intext string Internal
The connection type filter - either external or
internal.
statistics.intext.in numeric 972652917
The total inbound data transfer for the device
during the timeframe in bytes.
statistics.intext.out numeric 972652917
The total outbound data transfer for the device
during the timeframe in bytes.
statistics.protocols array
An array of network protocols identified in the
connections.
statistics.protocols.protocol string TCP A network protocol.
statistics.protocols.in numeric 1259912584
The volume of inbound data transferred using
that protocol.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

statistics.protocols.out numeric 1259912584
The volume of outbound data transferred using
that protocol.

statistics.applicationprotocols array An array of application protocols used in the
connections.

statistics.applicationprotocols.applic
ationprotocol
string SSH An application protocol.

statistics.applicationprotocols.in numeric 967854515 The volume of inbound data transferred using
that protocol.

statistics.applicationprotocols.out numeric 967854515
The volume of outbound data transferred using
that protocol.

subnets array An array of subnets that have interacted with the
subnet.

subnets.sid numeric -6 The subnet id for the other subnet.

subnets.size numeric 966432307
The amount of data transferred to or from that
subnet.

subnets.timems numeric 1586937881000
A timestamp at which the data was gathered in
epoch time.

subnets.network string The network range describing the subnet.

subnets.label string Internal Traffic
The subnet label applied in Subnet Admin (if
applicable).

devices array

```
When a subnet is specified, information about
the devices within that subnet and any devices
they have communicated with.
```
devices.did numeric 54 The “device id” of the device.

devices.size numeric 153541

```
Depending on the metric specified, the amount
of data transferred in the connections involving
that device or the number of matching
connections.
```
devices.timems numeric 1586937881000
A timestamp at which the data was gathered in
epoch time.

devices.ips array 10.12.14.2 IPs associated with the device historically.

devices.sid numeric 82
The subnet id for the subnet the device is
currently located in.

devices.ip string 10.12.14.2 The current IP associated with the device.

devices.network string 10.12.14.0/24
The IP address range that describes the subnet
the IP is contained within

metric object An object describing the metric queried upon.

metric.mlid numeric (^17) The “metric logic” id - unique identifier.
metric.name string datatransfervolume
The metric which data is returned for in system
format.
metric.label string Data Transfer The metric which data is returned for in readable
format.
metric.units string bytes The units the metric is measured in, if applicable.
metric.filtertypes array Direction
An array of filters which can be used with this
metric.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

metric.unitsinterval numeric 3600 The default time interval for the metric.

metric.lengthscale numeric 599997600 A system field.

connections array
An array of connection objects associated with
the subnet and metric over the time period.

connections.source object An object describing the source of a connection.

connections.source.id numeric -6
The device id or subnet id of the source of the
connection, where applicable.

connections.source.ip string 10.12.14.2 The IP of the source device.

connections.source.type string subnet The type of device, host or entity originating the
connection.

connections.target object An object describing the source of a target.

connections.target.id numeric -6
The device id or subnet id of the destination for
the connection, where applicable.

connections.target.ip string 10.0.18.224 The IP of the target device.

connections.target.type string subnet
The type of device, host or entity targeted by the
connection.

connections.timems numeric 1586937600000 A timestamp for the connection in epoch time.

connections.score numeric 18
Where a connection is deemed unusual, the
percentage unusualness of the connection.

connections.size numeric 36000000
The time frame covered by the initial request in
seconds x 10000.


###### Example Response

```
{
"statistics": [
{
"Views": [
{
"View": "All subnets",
"in": false,
"out": false
},
{
"View": "This subnet",
"in": false,
"out": false
}
]
},
{
"Connection Status": [
{
"Connections": "Normal",
"in": 4262370976,
"out": 4262370976
},
{
"Connections": "Unusual",
"in": 61505,
"out": 61505
},
{
"Connections": "New",
"in": 31284,
"out": 31284
},
{
"Connections": "Breached",
"in": false,
"out": false
}
]
},
{
"devices": [
{
"device": "workstation-local-82",
"ip": "10.0.18.224",
"in": 4372649,
"out": 3039203929
},
...
]
},
{
"Subnets": [
{
"subnet": "10.0.18.0/24",
"in": 37399591,
"out": 132264717
}
...
]
},
```
_continued..._


```
{
"intext": [
{
"intext": "Internal",
"in": 3983454402,
"out": 3983454402
},
{
"intext": "External",
"in": 278978079,
"out": 278978079
}
]
},
{
"protocols": [
{
"protocol": "TCP",
"in": 4248515456,
"out": 4248515456
}
...
]
},
{
"applicationprotocols": [
{
"applicationprotocol": "SSH",
"in": 3791388476,
"out": 3791388476
}
...
]
}
],
"subnets": [
{
"sid": -6,
"size": 3813839878,
"timems": 1587138425692,
"network": "10.0.18.0/24",
"label": "Workstations-1"
}
...
],
"devices": [
{
"did": 276,
"size": 4080311,
"timems": 1587138438745,
"ips": [
"10.15.3.41"
],
"sid": 12,
"ip": "10.15.3.41",
"network": "10.15.3.0/24"
},
...
],
"metric": {
"mlid": 17,
"name": "datatransfervolume",
"label": "Data Transfer",
```
_continued..._


```
"units": "bytes",
"filtertypes": [
"Feature model",
...
],
"unitsinterval": 3600,
"lengthscale": 599997600
},
"connections": [
{
"source": {
"id": -6,
"type": "subnet"
},
"target": {
"id": 174,
"ip": "10.15.3.39",
"type": "device"
},
"timems": 1587138396904,
"size": 36000000
}
...
]
}
```
_Response is abbreviated._


## /PCAPS

The /pcaps endpoint allows a list of current PCAPs to be retrieved and for new PCAPs to be generated programmatically.

A POST request is required to trigger creation - requests to this endpoint must be made in JSON format. Parameters are

not supported.

There are four valid formats:

```
{"ip1":"10.36.39.131","start":1605222041,"end":1605222281}
{"ip1":"10.2.3.4","ip2":"8.8.8.8","start":1598258905,"end":1598258910}
{"ip1":"10.2.3.4","ip2":"8.8.8.8","port2":80,"start":1598258905,"end":1598258910,
"protocol": "tcp"}
{"ip1":"10.2.3.4","port1":43723,"ip2":"8.8.8.8","port2":53,"start":1598258905,"end":
1598258910, "protocol": "udp"}
```
Once the status of a requested PCAP becomes "state": "finished", it can be retrieved with a GET request using the

full filename as an extension:

```
/pcaps/DCIP_20210330063306_20210330063307_10_36_39_131_35860_10_2_3_4_53_udp_Lx5blz.pcap
```
Where the filename is returned with a /tm prefix - for example, /tm/DCIP_20210330063306_20210330.... -, this

should be omitted when making a request to retrieve the file.

###### Request Type(s)

```
[GET] [POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
ip1 string The source IP - required.
```
```
ip2 string The destination IP.
```
```
port1 numeric The specific port for the source IP.
```
```
port2 numeric The specific port for the destination IP.
```
```
start numeric The start time for the packet capture in epoch time (seconds).
```
```
end numeric The end time for the packet capture in epoch time (seconds).
```
```
protocol string Allows the layer 3 protocol to be specified. Accepts “tcp” or “udp”
```

#### Notes

- The maximum timeframe for PCAP creation is 30 minutes.
- To use the protocol filter, the destination IP (ip2) and destination port (port2) must be specified.
- On success, the endpoint returns details of the PCAP creation request:

```
{
"tmqid": 101,
"startTime": 1605262345,
"filename":
"DCIP_20200824084825_20200824084830_10_2_3_4_8_8_8_8_80_tcp_loBSz0_m.pcap",
"index": "connection3",
"l3proto": "tcp",
"ip1": "10.2.3.4",
"ip2": "8.8.8.8",
"port2": 80,
"start": 1598258905,
"end": 1598258910,
"state": "pending"
}
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET a list of PCAPs and their status:

```
https://[instance]/pcaps
```
2. POST to create a new PCAP between 192.168.72.4 and 10.0.18.224 on November 13th 2020
    11:00-11:15am UTC.

```
https://[instance]/pcaps -d {"ip1":"192.168.72.4","ip2":"10.0.18.224","start":
1605265200,"end":1605266100}
```
3. POST to create a new PCAP of DNS requests made by 10.0.18.224 to Google DNS over UDP on November
    13th 2020 11:00-11:15am UTC.

```
https://[instance]/pcaps -d {"ip1":"10.0.18.224","ip2":"8.8.8.8","port2":53,"start":
1598258905,"end":1598258910, "protocol": "udp"}
```
4. GET a specific PCAP file:

```
https://[instance]/pcaps/
DCIP_20201112220038_20201112220039_10_0_18_224_3379_192_168_72_4_53_udp_Kjktpo_m.pcap
```
```
Please note, this will return the binary file directly. If using cUrl, it is strongly recommended to use the
--output <file> flag or a similar operation to output the retrieved binary file to a file.
```

###### Example Response

_Request: /pcaps_

```
{
"tmqid": 98,
"startTime": 1605262128,
"endTime": 1605262137,
"filename": "/tm/
DCIP_20201112220038_20201112220039_10_0_18_224_3379_192_168_72_4_53_udp_Kjktpo_m.pcap",
"index": "connection4",
"l3proto": "udp",
"ip1": "10.0.18.224",
"port1": 3379,
"ip2": "192.168.72.4",
"port2": 53,
"start": 1605218438,
"end": 1605218439,
"state": "finished"
},
{
"tmqid": 100,
"startTime": 1605262233,
"endTime": 1605262237,
"filename": "/tm/
DCIP_20200824084825_20200824084830_10_2_3_4_8_8_8_8_80_tcp_MAnhE6_m.pcap",
"index": "connection3",
"l3proto": "tcp",
"ip1": "10.2.3.4",
"ip2": "8.8.8.8",
"port2": 80,
"start": 1598258905,
"end": 1598258910,
"state": "finished"
},
...
```
_Response is abbreviated._


## /PCAPS RESPONSE SCHEMA

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
tmqid numeric 119
A unique identifier - tm query ID - for the packet
capture.
```
```
startTime numeric 1613122702
The start time at which the generation of the
PCAP began in epoch time.
```
```
endTime numeric 1613122715
The end time at which the generation of the
PCAP was completed in epoch time.
```
```
filename string
```
```
/tm/
DCIP_20210209121522
_20210209122523_192
_168_0_4_60527_10_1
0_10_22_443_tcp_qnX
kZE_m.pcap
```
```
The filename of the packet capture which can be
used to retrieve it. When retrieving via the API,
the /tm prefix should be omitted.
```
```
index string connection4 A system field.
```
```
l3proto string tcp The layer three protocol of the PCAP, if specified
during creation.
```
```
ip1 string 192.168.0.4
The source IP of connections in the packet
capture.
```
```
port1 numeric 60527 The source port of connections in the packet
capture, if specified during creation.
```
```
ip2 string 10.10.10.22
The destination IP of connections in the packet
capture, if specified during creation.
```
```
port2 numeric 443 The destination port of connections in the
packet capture, if specified during creation.
```
```
start numeric 1612872922
The start time of the packet capture in epoch
time.
```
```
end numeric 1612873523 The end time of the packet capture in epoch
time.
```
```
state string finished The current status of the packet capture request.
```

###### Example Response

```
[
{
"tmqid": 119,
"startTime": 1613122702,
"endTime": 1613122715,
"filename": "/tm/
DCIP_20210209121522_20210209122523_192_168_0_4_60527_10_10_10_22_443_tcp_qnXkZE_m.pcap",
"index": "connection4",
"l3proto": "tcp",
"ip1": "192.168.0.4",
"port1": 60527,
"ip2": "10.10.10.22",
"port2": 443,
"start": 1612872922,
"end": 1612873523,
"state": "finished"
}
]
```

## /SIMILARDEVICES

This endpoint returns a list of similar devices when given the did of a specific device on the network. This information is

shown in the Threat Visualizer when the ‘View Similar Devices’ button is clicked after searching for a device in the

Omnisearch bar.

The similarity between the specified device and the returned devices is indicated by the score. The returned data will be

ordered by similarity score, with the most similar device first.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
count numeric Specifies the maximum number of items to return.
```
```
fulldevicedetails boolean
```
```
Returns the full device detail objects for all devices referenced by data in an API response. Use of this
parameter will alter the JSON structure of the API response for certain calls.
```
```
token string
Takes a token value returned by a system notice about a change in similar devices for a specified
device. Will return the old and new list of devices.
```
```
responsedata string
When given the name of a top-level field or object, restricts the returned JSON to only that field or
object.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET a list of three most similar devices to the device with did=123:

```
https://[instance]/similardevices?did=123&count=3
```

###### Example Response

_Request: /similardevices?did=123&count=3_

```
[
{
"did": 34,
"score": 100,
"ip": "10.91.44.12",
"ips": [
{
"ip": "10.91.44.12",
"timems": 1581933600000,
"time": "2020-02-17 10:00:00",
"sid": 7
}
],
"sid": 7,
"firstSeen": 1550492002000,
"lastSeen": 1581935040000,
"os": "Linux 2.2.x-3.x",
"typename": "desktop",
"typelabel": "Desktop"
},
{
"did": 72,
"score": 99,
...
},
{
"did": 78,
"score": 72,
...
}
]
```
_Response is abbreviated._


## /SIMILARDEVICES RESPONSE SCHEMA

#### Response Schema - fulldevicedetails=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
did numeric (^112) The “device id”, a unique identifier.
score numeric 99
A score describing how similar this device is in
comparison to the original device.
ip string 10.15.3.39 The current IP associated with the device.
ips array IPs associated with the device historically.
ips.ip string 10.15.3.39 A historic IP associated with the device.
ips.timems numeric 1586937881000
The time the IP was last seen associated with
that device in epoch time.
ips.time string 2020-04-15 08:04:41
The time the IP was last seen associated with
that device in readable format.
ips.sid numeric (^29) The subnet id for the subnet the IP belongs to.
sid numeric 29
The subnet id for the subnet the device is
currently located in.
hostname string
workstation-
local-82 The current device hostname.
firstSeen numeric 2018-06-12 14:00:00
The first time the device was seen on the
network.
lastSeen numeric 2020-03-15 09:52:11 The last time the device was seen on the
network.
os string
Linux 3.11 and
newer
The device operating system if Darktrace is able
to derive it.
typename string desktop The device type in system format.
typelabel string Desktop The device type in readable format.


###### Example Response

_Request: /similardevices?did=123&count=3&fulldevicedetails=false_

```
[
{
"did": 34,
"score": 100,
"ip": "10.91.44.12",
"ips": [
{
"ip": "10.91.44.12",
"timems": 1581933600000,
"time": "2020-02-17 10:00:00",
"sid": 7
}
],
"sid": 7,
"firstSeen": 1550492002000,
"lastSeen": 1581935040000,
"os": "Linux 2.2.x-3.x",
"typename": "desktop",
"typelabel": "Desktop"
},
{
"did": 72,
"score": 99,
...
},
{
"did": 78,
"score": 72,
...
}
]
```
_Response is abbreviated._

#### Response Schema - fulldevicedetails=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
did numeric (^17) The “device id”, a unique identifier.
score numeric 99
A score describing how similar this device is in
comparison to the original device.
ip string 10.15.3.39 The current IP associated with the device.
ips array IPs associated with the device historically.
ips.ip string 10.15.3.39 A historic IP associated with the device.
ips.timems numeric 1586937600000
The time the IP was last seen associated with
that device in epoch time.
ips.time string 2020-04-15 08:00:00
The time the IP was last seen associated with
that device in readable format.
ips.sid numeric (^10) The subnet id for the subnet the IP belongs to.
sid numeric 10
The subnet id for the subnet the device is
currently located in.
hostname string ws83 The current device hostname.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

firstSeen numeric 2020-04-15 08:00:00
The first time the device was seen on the
network.

lastSeen numeric 2020-03-15 09:52:11 The last time the device was seen on the
network.

os string
Linux 3.11 and
newer

```
The device operating system if Darktrace is able
to derive it.
```
typename string desktop The device type in system format.

typelabel string Desktop The device type in readable format.

tags array An object describing tags applied to the device.

tags.tid numeric (^73) The “tag id”. A unique value.
tags.expiry numeric 0
The expiry time for the tag when applied to a
device.
tags.thid numeric 78 The “tag history” id. Increments if the tag is
edited.
tags.name string Multi-use
The tag label displayed in the user interface or in
objects that reference the tag.
tags.restricted boolean FALSE Indicates a read-only tag - these tags can only be
modified or applied by Darktrace.
tags.data object An object containing information about the tag.
tags.data.auto boolean FALSE Whether the tag was auto-generated.
tags.data.color numeric 134
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.
tags.data.description string
Device is a pool
device.
An optional description summarizing the
purpose of the tag.
tags.isReferenced boolean FALSE
Whether the tag is used by one or more model
components.


###### Example Response

```
[
{
"did": 34,
"score": 100,
"ip": "10.91.44.12",
"ips": [
{
"ip": "10.91.44.12",
"timems": 1581933600000,
"time": "2020-02-17 10:00:00",
"sid": 7
}
],
"sid": 7,
"firstSeen": 1550492002000,
"lastSeen": 1581935040000,
"os": "Linux 2.2.x-3.x",
"typename": "desktop",
"typelabel": "Desktop",
"tags": [
{
"tid": 50,
"expiry": 0,
"thid": 50,
"name": "Test",
"restricted": false,
"data": {
"auto": false,
"color": 200,
"description": "Test Tag"
},
"isReferenced": true
}
]
},
{
"did": 72,
"score": 99,
...
},
{
"did": 78,
"score": 72,
...
}
]
```
_Response is abbreviated._


## /SUBNETS

The /subnets endpoint allows subnets processed by Darktrace to be retrieved and edited programmatically. This can be

useful when automating changes to large number of subnets or managing the quality of traffic across the network.

```
POST requests to this endpoint can be made with parameters or JSON (6.0+). The /editsubnet endpoint for modifying
```
subnets has now been deprecated.

###### Request Type(s)

```
[GET] [POST]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
seensince string
```
```
Relative offset for activity. Subnets with activity in the specified time period are returned. The format is
either a number representing a number of seconds before the current time, or a number with a modifier
such as day or week (Minimum=1 second, Maximum=6 months).
```
```
sid numeric Identification number of a subnet modeled in the Darktrace system.
```
```
label string An optional label to identify the subnet by. Available for POST requests only.
```
```
network string The IP address range that describes the subnet. Available for POST requests only.
```
```
longitude numeric
For the actual location of the subnet as rendered on the Threat Visualizer, the longitude value. Available
for POST requests only.
```
```
latitude numeric
For the actual location of the subnet as rendered on the Threat Visualizer, the latitude value. Available for
POST requests only.
```
```
dhcp boolean Whether DHCP is enabled for the subnet. Available for POST requests only.
```
```
uniqueUsernames boolean Whether the subnet is tracking by credential. Available for POST requests only.
```
```
uniqueHostnames boolean Whether the subnet is tracking by hostname. Available for POST requests only.
```
```
excluded boolean Whether traffic in this subnet should not be processed at all. Available for POST requests only.
```
```
modelExcluded boolean
Whether devices within this subnet should be fully modeled. If true, the devices will be added to the
Internal Traffic subnet. Available for POST requests only.
```
```
responsedata string
When given the name of a top-level field or object, restricts the returned JSON to only that field or
object.
```
###### Notes

- When specifying how many minutes/hours/days in the seensince parameter, 3min = 3mins, 5hour = 5hours,
    6day = 6days, etc.
- This API call does not support searching for subnets by anything other than the sid. If the user needs to search
    for subnets by label, network, etc. they will need to download the full list first and then parse on the returned
    data
- When making a POST request to update the subnet location, both longitude and latitude must be
    specified.
- When supplying a label, do not use quotes around the string - this will result in a double-quoted string.
- If changing the latitude or longitude via the API, whole values must still be passed with a decimal point. For
    example, 10.0.


###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET information about the subnet with sid=25:

```
https://[instance]/subnets?sid=25
```
2. GET a list of all the subnets seen in the last hour:

```
https://[instance]/subnets?seensince=1hour
```
```
https://[instance]/subnets?seensince=3600
```
3. POST a label change for the subnet with sid=25:

```
https://[instance]/subnets -d sid=25&label=GuestWifi
```
4. POST to enable Tracking by Hostname and DHCP for a subnet with sid=25:

```
https://[instance]/subnets -d {"sid":
25,"uniqueUsernames":false,"uniqueHostnames":true,"dhcp":true}
```
###### Example Response

_Request: /subnets?sid=82_

```
[
{
"sid": 82,
"auto": false,
"dhcp": true,
"firstSeen": 1585930090000,
"label": "Test Subnet",
"lastSeen": 1585930212000,
"latitude": 12.0,
"longitude": 0.0,
"network": "10.12.32.0/24",
"shid": 144,
"uniqueHostnames": false,
"uniqueUsernames": false,
"confidence": 2,
"dhcpQuality": 0,
"kerberosQuality": 0,
"recentTrafficPercent": 100,
"clientDevices": 61,
"mostRecentTraffic": 1585930942000
}
]
```

## /SUBNETS RESPONSE SCHEMA

Please note, the additional keys serverDevices and icsDevices were added to this schema alongside changes related

to Darktrace Threat Visualizer 6 and 6.1. These keys may have been present in some environments prior to these software

releases.

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
sid numeric 12 A unique “subnet id”.
```
```
auto boolean FALSE
```
```
The subnet was created automatically from
processed traffic and was not created by
modifying a network range on the Subnet Admin
page.
```
```
dhcp boolean TRUE Whether DHCP is enabled for the subnet.
```
```
firstSeen numeric 1528812000000
The first time the subnet was seen on the
network in epoch time.
```
```
label string Finance
The label assigned to the subnet in the Threat
Visualizer.
```
```
lastSeen numeric 1584265931000
The last time the subnet was seen on the
network in epoch time.
```
```
latitude numeric 0.01
For the actual location of the subnet as rendered
on the Threat Visualizer, the latitude value.
```
```
longitude numeric -0.01
For the actual location of the subnet as rendered
on the Threat Visualizer, the longitude value.
```
```
network string 10.12.14.0/24 The IP address range that describes the subnet.
```
shid numeric (^104) The “subnet history id”. Increments on edit.
uniqueHostnames boolean TRUE Whether the subnet is tracking by hostname.
uniqueUsernames boolean FALSE Whether the subnet is tracking by credential.
confidence numeric -1 A system field.
lastDHCP numeric 1584265931000
The timestamp of the last DHCP seen for the
subnet in epoch time.
dhcpCount numeric 7 The number of DHCP client devices in the last 7
days.
kerberosCount numeric 0
The number of Kerberos client devices in the last
7 days.
dhcpQuality numeric 7
The proportion of DHCP client devices in
comparison to the overall number of client
devices.
kerberosQuality numeric 0
The proportion of Kerberos client devices in
comparison to the overall number of client
devices.
recentTrafficPercent numeric 100
What percentage of processed traffic involved
connections within this subnet. Inter-subnet
traffic is included in the percentage for both
subnets, so the total values may be greater than
100%.
clientDevices numeric (^89) The number of client devices within the subnet.


```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
serverDevices numeric 12 The number of server devices within the subnet.
```
```
icsDevices numeric 0
The number of industrial-type devices within the
subnet.
```
```
mostRecentTraffic numeric 1584265931000 The most recent traffic seen for the subnet.
```
###### Example Response

```
{
"sid": 25,
"auto": false,
"dhcp": true,
"firstSeen": 1585930090000,
"label": "Example Subnet",
"lastSeen": 1649348778000,
"latitude": 00.00,
"longitude": -00.00,
"network": "10.10.10.0/24",
"shid": 599,
"uniqueHostnames": true,
"uniqueUsernames": false,
"confidence": 6,
"lastDHCP": 1649321484000,
"recentTrafficPercent": 18,
"dhcpCount": 6,
"kerberosCount": 0,
"dhcpQuality": 8,
"kerberosQuality": 0,
"clientDevices": 69,
"serverDevices": 1,
"icsDevices": 0,
"mostRecentTraffic": 1649344509000
}
```

## /STATUS

Detailed system health information from the Status page can be accessed programmatically with the /status API

endpoint. This endpoint is ideal for monitoring in a NOC environment.

The format=json parameter is only required when accessing the endpoint in a browser; an authenticated API request will

return JSON as standard.

###### Request Type(s)

```
[GET]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
includechildren boolean Determine whether information about probes is returned or not. True by default.
```
```
fast boolean
When true, JSON will be returned faster but subnet connectivity information will not be included (if not
cached).
```
```
responsedata string
When given the name of a top-level field or object, restricts the returned JSON to only that field or
object.
```
###### Notes

- The fast=true parameter will return any currently available data and will not query for subnet connectivity.
    However, as /status data is cached for a short period, a request with fast=true may sometimes return
    subnet connectivity information if a request has recently been made.
- The responsedata can be utilized to return only information about probes, subnets or to retrieve a specific
    desired field only.
- In Unified View environments, information about subordinate master instances under the UV will return in an
    instances object.

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all status page information in JSON format:

```
https://[instance]/status
```

###### Example Response

_Request: /status?includechildren=false&fast=true_

```
{
"excessTraffic": false,
"time": "2023-12-08 10:21",
"installed": "2018-10-22",
"mobileAppConfigured": true,
"version": "5.1.0 (dd351a)",
"ipAddress": "10.0.18.224",
"label": "holdingsinc-master",
"modelsUpdated": "2023-12-26 11:20:48",
"modelPackageVersion": "4.0-8515~20230322143408~g300d5d",
"bundleVersion": "61016",
"bundleDate": "2023-12-24 18:33:59",
"bundleInstalledDate": "2023-12-24 20:20:33",
"hostname": "example-darktrace",
"maximumOSSensors": 255,
"uuid": "07dcf0e5-217b-4e98-96b9-549b3dd87706",
"inoculation": false,
"applianceOSCode": "x",
"license": "2024-12-30 00:00:00",
"saasConnectorLicense": "2029-06-01 00:00:00",
"antigenaSaasLicense": "2029-06-01 00:00:00",
"syslogTLSSHA1Fingerprint": "2D:JY:LP:YT:TF:P3:BJ:21:Q6:D9:OT:JZ:LQ:8A:X0:KG:N6:9P:XC:DI",
"syslogTLSSHA256Fingerprint": "C6:9U:6N:D5:QU:HQ:
78:3P:C4:CN:L3:K2:PI:ZF:BO:MD:GO:Q9:IJ:ED:WD:BD:9Z:18:Z8:UY:34:TQ:HF:AD:P1:C3",
"antigenaNetworkEnabled": true,
"antigenaNetworkConfirmationMode": true,
"antigenaNetworkLicense": "2025-12-31 00:00:00",
"logIngestionReplicated": 326,
"logIngestionProcessed": 463930,
"logIngestionTCP": 2,
"logIngestionUDP": 380126407,
"logIngestionTypes": {
"example-template": 213587,
},
"logIngestionMatches": {
"example-template": 214509,
},
"licenseCounts": {
"saas": {
"total": 0
},
"licenseIPCount": 880,
"licenseCloudIPCount": 12
},
"antigenaNetworkBlockedConnections": {
"attempted": 277149,
"failed": 1333
},
"diskSpaceUsed_": 98,
"type": "master",
"diskUtilization": 1,
"load": 10,
"cpu": 11,
"memoryUsed": 87,
"dataQueue": 0,
"darkflowQueue": 0,
"flowProcessingTimes": {},
"networkInterfacesState_eth0": "up",
...
"eventsPerMinuteCurrent": {
"cSensorNotices": 0,
...
```
_continued..._


```
},
"probes": {
"12": {
"id": 12,
"configuredServer": "example-vsensor-2.example.com",
"version": "6.1.23 (f35936c6)",
"ipAddress": "10.10.12.12",
"bundleVersion": "6.1.7",
"bundleDate": "2023-12-13 12:23:25",
"bundleInstalledDate": "2023-12-14 06:24:46",
"load": 25,
"cpu": 6,
"memoryUsed": 18,
"osSensors": [
"10.10.12.125"
],
"networkInterfacesState_eth0": "up",
"bandwidthCurrent": 542011,
"connectionsPerMinuteCurrent": 169,
"connectionsPerMinuteAverage": 156,
"connectionsPerMinute7DayPeak": 432,
"connectionsPerMinute2WeekPeak": 432
},
...
},
"connectionsPerMinuteCurrent": 7130,
"connectionsPerMinuteAverage": 5849,
"connectionsPerMinute7DayPeak": 8829,
"connectionsPerMinute2WeekPeak": 20975,
"operatingSystems": 16,
"credentials": 86,
"credentials7Days": 55,
"credentialSources": {
"NTLM": {
"4weeks": 6,
"7days": 4
},
"Saas": {
"4weeks": 80,
"7days": 51
}
},
"newDevices4Weeks": 244,
"newDevices7Days": 35,
"newDevices24Hours": 11,
"newDevicesHour": 0,
"activeDevices4Weeks": 2709,
"activeDevices7Days": 1420,
"activeDevices24Hours": 897,
"activeDevicesHour": 460,
"deviceHostnames": 337,
"deviceMACAddresses": 375,
"deviceRecentIPChange": 6,
"models": 695,
"modelsBreached": 403911,
"modelsSuppressed": 1872333,
"devicesModeled": 1420,
"recentUnidirectionalConnections": 0,
"mostRecentDHCPTraffic": "2023-12-08 10:14:00",
"mostRecentDNSTraffic": "2023-12-08 10:18:00",
...
"VLANs": {
"1": 0,
```
_continued..._


```
...
},
"internalIPRangeList": [
"10.0.0.0/8",
"192.168.0.0/16",
],
"internalIPRanges": 2,
"dnsServers": 38,
"internalDomains": 0,
"internalAndExternalDomainList": [
"holdingsinc.com",
"example.com"
],
"internalAndExternalDomains": 2,
"proxyServers": 1,
"proxyServerIPs": [
"192.168.72.4:443",
],
"subnets": 97,
"subnetData": [
{
"recentTrafficPercent": 3,
"recentUnidirectionalTrafficPercent": 2,
"sid": 8710,
"network": "10.12.14.0/24",
"devices": 235,
"clientDevices": 231,
"mostRecentTraffic": "2023-12-08 10:00:00",
"mostRecentDHCP": "Never"
},
...
]
}
```
_Response is abbreviated._


## /STATUS RESPONSE SCHEMA

```
/status data is cached for a short period. Therefore, a request with fast=true may sometimes return subnet
```
connectivity information if a request has recently been made.

The naming scheme and numbering of network interfaces returned will depend on your environment and the type of

probes connected.

###### Probes, Masters and Unified View Deployments

The parameter includechildren is true by default, so data from any child instances such as probes or subordinate

masters is included in the standard response from this endpoint.

The queried instance is represented by data at the top level. Probes - both vSensor and hardware - are then contained

within a probes object, with each probe identified by a numeric ID. In Unified View environments, when the Unified View

instance is queried, subordinate masters are contained within an instances object and identified with a numeric ID.

These submaster instances may each have their own probes object, describing the probes associated directly with them.

Example Unified View structure (includechildren=true):

```
{
"time": "2024-01-05 14:44",
"installed": "2016-06-09",
...
"instances": {
"1": {
"id": 1,
...
"probes": {
"123": {...}
}
},
"2": {
"id": 2,
...
"probes": {
"456": {...}
}
}
}
}
```
Example master structure (includechildren=true):

```
{
"time": "2024-01-05 14:44",
"installed": "2016-06-09",
...
"probes": {
"1": {...}
}
}
```
Example master structure with no probes, or where includechildren=false:


```
{
"time": "2024-01-05 14:44",
"installed": "2016-06-09",
...
}
```
#### Response Schema - No parameters ( fast=false )

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
excessTraffic boolean FALSE
Whether the instance is receiving more traffic
than it can reasonably process.
```
```
time string 2023-12-31 14:41:00 The current server time in UTC.
```
```
installed string 10/22/18
The date that the first data was received by the
instance.
```
```
mobileAppConfigured boolean TRUE Whether the Darktrace Mobile App is configured.
```
```
version string 6.1.23 (f35936c6)
```
```
The current installed version of the Model Engine
```
- the system that evaluates model logic against
metadata - which is distinct from the Threat
Visualizer and Model Update bundles.

```
ipAddress string 10.0.18.224 Where detectable, the IP address of the
management interface.
```
```
label string holdingsinc-master
A freetext label applied to the instance on the
System Config page to better identify it.
```
```
modelsUpdated string 2023-12-26 11:20:00 The last time default models were updated.
```
```
modelPackageVersion string 4.0-8515 20230322143408 The model bundle information.g300d5d
```
```
bundleVersion string 61016 The Threat Visualizer software bundle number.
```
```
bundleVariant string rc
```
```
The type of bundle. Early adopter customers may
receive release candidates as well as stable
builds.
```
```
bundleDate string 2023-12-24 18:33:00
The time that the Threat Visualizer software
bundle was downloaded.
```
```
bundleInstalledDate string 2023-12-24 20:20:00 The time that the Threat Visualizer software
bundle was installed.
```
```
maximumOSSensors numeric 255
The maximum number of osSensors that can be
associated with vSensors in this deployment.
```
```
hostname string
example-
darktrace-01 The instance hostname.
```
```
uuid string
07dcf0e5-217b-4e98-
96b9-549b3dd87706
A unique identifier for the instance.
```
```
inoculation boolean FALSE Whether the instance is subscribed to Darktrace
inoculation.
```
```
applianceOSCode string x A system field.
```
```
license string 2024-12-30 00:00:00
The expiry date for the current Threat Visualizer
license.
```
```
saasConnectorLicense string 2029-06-01 00:00:00
```
```
The expiry date for the current SaaS module
license. Where multiple modules are installed,
the date of the last expiring module.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

antigenaSaasLicense string 2029-06-01 00:00:00

```
The expiry date for the current Darktrace
RESPOND module license. Where multiple
modules across Darktrace/Apps, Darktrace/
Cloud and Darktrace/Zero Trust are licensed for
Darktrace RESPOND, the date of the last expiring
module.
```
cloudSecurityLicense string 2023-10-02 00:00:00
The expiry date for the current Darktrace Cloud
Security license.

syslogTLSSHA1Fingerprint string

```
2D:JY:LP:YT:TF:P3:B
J:
21:Q6:D9:OT:JZ:LQ:
8A:X0:KG:N6:9P:XC:D
I
```
```
The SHA1 Fingerprint of the current syslog
ingestion TLS Certificate. May also appear within
a probe object where a vSensor or probe is
ingesting TLS syslog.
```
syslogTLSSHA256Fingerprint string
C6:9U:6N:D5:QU:HQ:
78:3P...

```
The SHA256 Fingerprint of the current syslog
ingestion TLS Certificate. May also appear within
a probe object where a vSensor or probe is
ingesting TLS syslog.
```
antigenaNetworkEnabled boolean TRUE

```
Whether Darktrace RESPOND/Network (formerly
Antigena Network) is enabled in the instance
console.
```
antigenaNetworkRunning boolean TRUE

```
Whether Darktrace RESPOND/Network (formerly
Antigena Network) is currently running on the
given instance.
```
antigenaNetworkConfirmationMode boolean TRUE This field is deprecated.

antigenaNetworkLicense string 2025-12-31 00:00:00

```
The expiry date for the current Darktrace
RESPOND/Network (formerly Antigena Network)
license.
```
preventE2ELicense string 2025-12-31 00:00:00
The expiry date for the current Darktrace
PREVENT/E2E license, if configured.

logIngestionReplicated numeric 321

```
The number of ingested syslog lines from special
telemetry modules (e.g. Zscaler, Netskope)
across the instance lifetime.
```
logIngestionProcessed numeric 422406

```
The number of ingested syslog lines processed
across the instance lifetime. Log lines are
processed if they are found to contain and match
a valid Log Filter value for one or more telemetry
templates.
```
logIngestionTCP numeric 2

```
The number of syslog lines that were received via
TCP across the instance lifetime. Includes both
valid and invalid inputs.
```
logIngestionUDP numeric 329999225

```
The number of syslog lines that were received via
UDP across the instance lifetime. Includes both
valid and invalid inputs.
```
logIngestionMatches object

```
An object describing the log lines that were
processed (i.e., broken down on a per-template
basis.
```
logIngestionMatches.exampletemplate numeric 214509

```
An example log template and the number of
times log lines have been processed for that type
```
- i.e., evaluated against it.

logIngestionTypes object

```
An object describing the log lines that were
processed and matched successfully against
templates on this master instance, broken down
on a per-template basis.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

logIngestionTypes.exampletemplate numeric 213587

```
An example log template and the number of
times log lines have been processed and
matched successfully for that type on this
instance.
```
licenseCounts object

```
An object containing the number of devices and
user accounts seen across Darktrace DETECT
coverage areas.
```
licenseCounts.saas object

```
An object containing one or more SaaS modules
and the number of users seen from that module
in the last 7 days.
```
licenseCounts.saas.total numeric 0
The total number of SaaS users across all
modules in the last 7 days.

licenseCounts.licenseIPCount numeric 249

```
The peak value of the number of distinct internal
(not excluded) IP addresses seen within any 24
hour period over the last seven days. Does not
overlap with licenseCloudIPCount.
```
licenseCounts.licenseCloudIPCount numeric 12

```
The peak value of the number of distinct internal
(not excluded) IP addresses seen in a cloud
VLAN within any 24 hour period over the last
seven days. IP addresses will be located in cloud
VLANs if created from Darktrace Cloud Security
flow log ingestion, or created from traffic
observed by a compatible Darktrace vSensor.
Does not overlap with licenseIPCount.
```
antigenaNetworkBlockedConnections object

```
An object representing Darktrace RESPOND/
Network attempts to end connections and
number of those attempts where connectivity
demonstrably continued. These fields are
experimental and under active development, and
should not be relied upon, or expected to remain
stable, at the current time.
```
antigenaNetworkBlockedConnections.atte
mpted
numeric 277149

```
The culmulative number of attempts made to
end connections (fired RSTs) taken by Darktrace
RESPOND/Network on the given instance since it
was upgraded to a software version where this
value was recorded. One RESPOND action will
produce multiple attempts, as attempts are
recorded on a per-RST basis .This metric is
experimental and under active development.
```
antigenaNetworkBlockedConnections.fail
ed
numeric 1333

```
Attempts where Darktrace RESPOND/Network
has attempted to end a connection - and the
associated RST packet was seen by the instance
```
- but connectivity demonstrably continued after
the RST was sent and/or observed. This metric is
experimental and under active development.

diskSpaceUsed_ numeric 98 The percentage diskspace in use.

type string master The type of appliance.

diskUtilization numeric 1
This percentage value indicates the average disk
I/O.

load numeric 12
This percentage value indicates how in-demand
resources are in the instance processing.

cpu numeric 8
This percentage value indicates the average
amount of CPU usage (not idle).

memoryUsed numeric 87 The percentage of memory in use.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

dataQueue numeric 0 The current queue for event ordering in seconds.

darkflowQueue numeric 0
The current queue from bandwidth ingestion to
processing in seconds.

flowProcessingTimes object
An object describing the amount of connections
processed within 10 second intervals.

networkInterfacesState_eth0 string up Whether the network interface is up or down.

networkInterfacesAddress_eth0 string 10.0.18.224 The IP addresses if resolvable of the interface.

networkInterfacesState_eth1 string up Whether the network interface is up or down.

networkInterfacesState_eth2 string up Whether the network interface is up or down.

networkInterfacesState_eth3 string up Whether the network interface is up or down.

networkInterfacesReceived_eth0 numeric 37117054830 The number of bytes received by the interface

networkInterfacesReceived_eth1 numeric (^51298800000000) The number of bytes received by the interface
networkInterfacesReceived_eth2 numeric 1887340000000 The number of bytes received by the interface
networkInterfacesReceived_eth3 numeric 6176370000000 The number of bytes received by the interface
networkInterfacesTransmitted_eth0 numeric 112970000000 The number of bytes sent by the interface
networkInterfacesTransmitted_eth1 numeric 0 The number of bytes sent by the interface
networkInterfacesTransmitted_eth2 numeric (^0) The number of bytes sent by the interface
networkInterfacesTransmitted_eth3 numeric 0 The number of bytes sent by the interface
bandwidthCurrent numeric 386703428
Ingested bandwidth over the last 10 minutes.
Some bandwidth may not be processed due to
system settings.
bandwidthCurrentString string 386.70 Mbps
Ingested bandwidth over the last 10 minutes in a
readable format. Some bandwidth may not be
processed due to system settings.
bandwidthAverage numeric 391631000
Average bandwidth over the last 2 weeks. Some
bandwidth may not be processed due to system
settings.
bandwidthAverageString string 391.63 Mbps
Average bandwidth over the last 2 weeks in a
readable format. Some bandwidth may not be
processed due to system settings.
bandwidth7DayPeak numeric 1230235696
The highest ingested bandwidth observed in any
ten-minute interval over the last 7 days. Some
bandwidth may not be processed due to system
settings.
bandwidth7DayPeakString string 1.23 Gbps
The highest ingested bandwidth observed in any
ten-minute interval over the last 7 days in a
readable format. Some bandwidth may not be
processed due to system settings.
bandwidth2WeekPeak numeric 1645876703
The highest ingested bandwidth observed in any
ten-minute interval over the last 2 weeks. Some
bandwidth may not be processed due to system
settings.
bandwidth2WeekPeakString string 1.65 Gbps
The highest ingested bandwidth observed in any
ten-minute interval over the last 2 weeks in a
readable format. Some bandwidth may not be
processed due to system settings.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

processedBandwidthCurrent numeric 59938652 Processed bandwidth over the last 10 minutes.

processedBandwidthCurrentString string 59.94 Mbps
Processed bandwidth over the last 10 minutes in
a readable format.

processedBandwidthAverage numeric 142568480 Average bandwidth over the last 2 weeks.

processedBandwidthAverageString string 142.57 Mbps
Average bandwidth over the last 2 weeks in a
readable format.

processedBandwidth7DayPeak numeric 1139496509
The highest bandwidth observed in any ten-
minute interval over the last 7 days.

processedBandwidth7DayPeakString string 1.14 Gbps

```
The highest bandwidth observed in any ten-
minute interval over the last 7 days in a readable
format.
```
processedBandwidth2WeekPeak numeric 1223451790
The highest bandwidth observed in any ten-
minute interval over the last 2 weeks.

processedBandwidth2WeekPeakString string 1.22 Gbps

```
The highest bandwidth observed in any ten-
minute interval over the last 2 weeks in a
readable format.
```
eventsPerMinuteCurrent object

```
An object describing the average number of
events (for each event type) that was processed
in one minute over the last 10-20 minutes. More
detailed information is available from the /
summarystatistics endpoint.
```
eventsPerMinuteCurrent.cSensorNotices numeric 0

```
The number of non-connection events produced
by cSensor devices that were processed per
minute over the last 10-20 minutes.
```
eventsPerMinuteCurrent.cSensorDeviceDe
tails
numeric^0

```
The number of tracking events produced by
cSensor devices that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.cSensorModelEve
nts
numeric 1464

```
The number of modeling events produced by
cSensor devices that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.networkNotices numeric 69

```
The number of non-connection events produced
by network traffic that were processed per
minute over the last 10-20 minutes.
```
eventsPerMinuteCurrent.networkDeviceDe
tails numeric
4

```
The number of tracking events produced by
network traffic that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.networkModelEve
nts
numeric 131305

```
The number of modeling events produced by
network traffic that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.logInputNotices numeric 13

```
The number of non-connection events produced
by syslog ingestion that were processed per
minute over the last 10-20 minutes.
```
eventsPerMinuteCurrent.logInputDeviceD
etails
numeric 0

```
The number of tracking events produced by
syslog ingestion that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.logInputModelEv
ents
numeric 0

```
The number of modeling events produced by
syslog ingestion that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.saasNotices numeric 0

```
The number of events produced by SaaS
modules that were processed per minute over
the last 10-20 minutes.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

eventsPerMinuteCurrent.saasModelEvents numeric 0

```
The number of modeling events produced by
SaaS modules that were processed per minute
over the last 10-20 minutes.
```
probes object
An object describing any probes, whether
physical or virtualized.

probes.12 object
An object describing a specific probe. Probe
objects are identified by the numeric ID.

probes.12.id numeric (^12) The numeric probe ID.
probes.12.uuid string
6b3ed6f4-1823-4028-
b9a5-9ea9ec3ec70b
A unique identifier for the instance.
probes.12.version string 6.1.23 (f35936c6)) The probe software version currently installed.
probes.12.bundleVersion string 6.1.7
probes.12.bundleDate string 2023-12-13 12:23:25
probes.12.bundleInstalledDate string 2023-12-14 06:24:46
probes.12.configuredServer string
example-
vsensor-2.example.c
om
The endpoint at which the Darktrace instance
contacts the probe.
probes.12.ipAddress string 10.10.12.12
The probe IP address. May differ from the
configuredServer field depending on the
probe type.
probes.12.label string Testing 2019 A descriptive label provided for the probe.
probes.12.hostname string testprobe1 The probe hostname if applicable/ known.
probes.12.time string 2024-01-05 14:44 The current server time on the probe.
probes.12.metadata object
For compatible probe types and software
versions, this object will include metadata about
the vSensor location in AWS including VPC and
region information. Otherwise, null
probes.12.type string vSensor The type of probe.
probes.12.load numeric 14
This percentage value indicates how in-demand
resources are in the probe processing.
probes.12.cpu numeric 0
This percentage value indicates the average
amount of CPU usage (not idle) on the probe.
probes.12.memoryUsed numeric (^16) The percentage of memory in use on the probe.
probes.12.osSensors array 10.10.12.122
An array of IP addresses of one or more
associated osSensors. Only relevant for vSensor-
type probes.
probes.
12.antigenaNetworkBlockedConnections
object
An object representing Darktrace RESPOND/
Network attempts to end connections and
number of those attempts where connectivity
demonstrably continued. These fields are
experimental and under active development, and
should not be relied upon, or expected to remain
stable, at the current time.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

probes.
12.antigenaNetworkBlockedConnections.a
ttempted

```
numeric^1335
```
```
The culmulative number of attempts made to
end connections (fired RSTs) taken by Darktrace
RESPOND/Network on the given instance since it
was upgraded to a software version where this
value was recorded. One RESPOND action will
produce multiple attempts, as attempts are
recorded on a per-RST basis .This metric is
experimental and under active development.
```
probes.
12.antigenaNetworkBlockedConnections.f
ailed

```
numeric^12
```
```
Attempts where Darktrace RESPOND/Network
has attempted to end a connection - and the
associated RST packet was seen by the instance
```
- but connectivity demonstrably continued after
the RST was sent and/or observed. This metric is
experimental and under active development.

probes.12.osPacketsProcessed string 377634
The number of packets processed from child
osSensors on this parent probe.

probes.12.networkInterfacesState_eth0 string up
Whether the network interface is up or down on
the probe.

probes.
12.networkInterfacesAddress_eth0
string 10.10.12.12
The IP addresses if resolvable of the probe
network interface.

probes.
12.networkInterfacesReceived_eth0
numeric 559588000000
The number of bytes received by the interface on
the probe.

probes.
12.networkInterfacesTransmitted_eth0
numeric 39866733296
The number of bytes sent by the interface on the
probe.

probes.12.bandwidthCurrent numeric 1720840

```
Bandwidth ingested by the probe over the last 10
minutes. Some bandwidth may not be processed
due to system settings.
```
probes.12.bandwidthCurrentString string 1.72 Mbps

```
Bandwidth ingested by the probe over the last 10
minutes in a readable format. Some bandwidth
may not be processed due to system settings.
```
probes.12.bandwidthAverage numeric 0

```
Average bandwidth ingested by the probe over
the last 2 weeks. Some bandwidth may not be
processed due to system settings.
```
probes.12.bandwidthAverageString string 0 kbps

```
Average bandwidth ingested by the probe over
the last 2 weeks in a readable format. Some
bandwidth may not be processed due to system
settings.
```
probes.12.bandwidth7DayPeak numeric 0

```
The highest bandwidth ingested by the probe
observed in any ten-minute interval over the last
7 days. Some bandwidth may not be processed
due to system settings.
```
probes.12.bandwidth7DayPeakString string 0 kbps

```
The highest bandwidth ingested by the probe
observed in any ten-minute interval over the last
7 days in a readable format. Some bandwidth
may not be processed due to system settings.
```
probes.12.bandwidth2WeekPeak numeric 0

```
The highest bandwidth ingested by the probe
observed in any ten-minute interval over the last
2 weeks. Some bandwidth may not be processed
due to system settings.
```
probes.12.bandwidth2WeekPeakString string 0 kbps

```
The highest bandwidth ingested by the probe
observed in any ten-minute interval over the last
2 weeks in a readable format. Some bandwidth
may not be processed due to system settings.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

probes.12.processedBandwidthCurrent numeric 1720840
Bandwidth processed by the probe over the last
10 minutes.

probes.
12.processedBandwidthCurrentString string
1.72 Mbps Bandwidth processed by the probe over the last
10 minutes in a readable format.

probes.12.processedBandwidthAverage numeric 1041910
Average bandwidth processed by the probe over
the last 2 weeks.

probes.
12.processedBandwidthAverageString string
1.04 Mbps Average bandwidth processed by the probe over
the last 2 weeks in a readable format.

probes.12.processedBandwidth7DayPeak numeric 32829661

```
The highest bandwidth processed by the probe
observed in any ten-minute interval over the last
7 days.
```
probes.
12.processedBandwidth7DayPeakString
string 32.83 Mbps

```
The highest bandwidth processed by the probe
observed in any ten-minute interval over the last
7 days in a readable format.
```
probes.12.processedBandwidth2WeekPeak numeric 32829661

```
The highest bandwidth processed by the probe
observed in any ten-minute interval over the last
2 weeks.
```
probes.
12.processedBandwidth2WeekPeakString
string 32.83 Mbps

```
The highest bandwidth processed by the probe
observed in any ten-minute interval over the last
2 weeks in a readable format.
```
probes.12.connectionsPerMinuteCurrent numeric 331

```
Current number of connections processed by
the probe in the last minute - includes ongoing
(unfinished) connections and completed
connections.
```
probes.12.connectionsPerMinuteAverage numeric 326

```
Average number of connections processed by
the probe per minute in the last 2 weeks -
includes ongoing (unfinished) connections and
completed connections.
```
probes.12.connectionsPerMinute7DayPeak numeric 752

```
Highest number of connections processed by
the probe per minute in the last 7 days - includes
ongoing (unfinished) connections and
completed connections.
```
probes.
12.connectionsPerMinute2WeekPeak
numeric 752

```
Highest number of connections processed by
the probe per minute in the last 2 weeks -
includes ongoing (unfinished) connections and
completed connections.
```
probes.13 object An additional example of a probe object - here,
an errored probe.

probes.13.configuredServer string 10.15.3.39
The IP or hostname at which the master instance
will attempt to contact the probe.

probes.13.ipAddress string 10.15.3.39

```
The probe IP address. May differ from the
configuredServer field depending on the
probe type.
```
probes.13.label string Testing 2020 A descriptive label provided for the probe.

probes.13.error boolean TRUE

```
Whether the probe is experiencing an error, such
as being uncontactable by the master instance.
This field will only appear under specific
circumstances.
```
probes.13.lastContact string 2023-02-06 02:30:00
The last time the probe was contactable by the
master instance.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

connectionsPerMinuteCurrent numeric 7430

```
Current number of connections processed in the
last minute - includes ongoing (unfinished)
connections and completed connections.
```
connectionsPerMinuteAverage numeric 8768

```
Average number of connections processed per
minute in the last 2 weeks - includes ongoing
(unfinished) connections and completed
connections.
```
connectionsPerMinute7DayPeak numeric 20975

```
Highest number of connections processed per
minute in the last 7 days - includes ongoing
(unfinished) connections and completed
connections.
```
connectionsPerMinute2WeekPeak numeric 20975

```
Highest number of connections processed per
minute in the last 2 weeks - includes ongoing
(unfinished) connections and completed
connections.
```
credentials numeric 86
The number of credentials observed from all
sources over the last 4 weeks.

credentials7Days numeric 55
The number of credentials observed from all
sources over the last 7 days.

credentialSources object

```
An object describing the sources where
credentials were observed from. Sources will
differ depending upon connection make-up and
coverage areas deployed.
```
credentialSources.NTLM object
An object describing the number of credentials
which were seen in NTLM traffic.

credentialSources.NTLM.4weeks numeric 6
The number of credentials observed in NTLM
traffic over the last 4 weeks.

credentialSources.NTLM.7days numeric 4
The number of credentials observed in NTLM
traffic over the last 7 days.

credentialSources.Saas object

```
An object describing the number of credentials
which were observed in event data from
Darktrace/Apps, Cloud or Zero Trust modules.
```
credentialSources.Saas.4weeks numeric 80

```
The the number of credentials which were
observed in event data from Darktrace/Apps,
Cloud or Zero Trust modules over the last 4
weeks.
```
credentialSources.Saas.7days numeric 51

```
The the number of credentials which were
observed in event data from Darktrace/Apps,
Cloud or Zero Trust modules over the last 7 days.
```
operatingSystems numeric 16
The number of operating systems (as derived by
Darktrace) seen over the last 4 weeks.

newDevices4Weeks numeric 289
The number of new devices seen over the last 4
weeks.

newDevices7Days numeric 50
The number of new devices seen over the last 7
days.

newDevices24Hours numeric 8
The number of new devices seen over the last 24
hours.

newDevicesHour numeric 1
The number of new devices seen over the last
hour.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

activeDevices4Weeks numeric 2856

```
The number of active devices seen over the last
4 weeks. Active devices may also include
unmodelled devices such as broadcast traffic,
internal and external multicast traffic and any
excluded ip ranges if activity is seen.
```
activeDevices7Days numeric 1590

```
The number of active devices seen over the last
7 days. Active devices may also include
unmodelled devices such as broadcast traffic,
internal and external multicast traffic and any
excluded ip ranges.
```
activeDevices24Hours numeric 800

```
The number of active devices seen over the last
24 hours. Active devices may also include
unmodelled devices such as broadcast traffic,
internal and external multicast traffic and any
excluded ip ranges.
```
activeDevicesHour numeric 461

```
The number of active devices seen over the last
hour. Active devices may also include
unmodelled devices such as broadcast traffic,
internal and external multicast traffic and any
excluded ip ranges.
```
deviceHostnames numeric 348 The number of device hostnames seen in the last
4 weeks.

deviceMACAddresses numeric 417
The number of device MAC Addresses seen in
the last 4 weeks.

deviceRecentIPChange numeric 21 The nunber of devices that have changed IP in
the last 7 days.

models numeric 692
The number of active/enabled models on the
system.

modelsBreached numeric 401834

```
This figure represents the number of lifetime
model breaches, unless the instance is explicitly
configured to expire model breaches.
```
modelsSuppressed numeric 1869280

```
This figure represents the number of lifetime
model breaches that have been suppressed,
unless the instance is explicitly configured to
expire model breaches.
```
recentUnidirectionalConnections numeric 0

```
The percentage number of connections
identified as unidirectional over the last 30
minutes. If data is not available, an average over
the last 6 hours.
```
mostRecentDHCPTraffic string 2023-12-31 14:52:00
The timestamp of the most recent DHCP traffic
across all subnets in UTC.

mostRecentDNSTraffic string 2023-12-31 14:49:00
The timestamp of the most recent DNS traffic
across all subnets in UTC.

mostRecentDCE_RPCTraffic string 2023-12-31 14:50:00
The timestamp of the most recent DCE_RPC
traffic across all subnets in UTC.

mostRecentHTTPTraffic string 2023-12-31 14:52:00
The timestamp of the most recent HTTP traffic
across all subnets in UTC.

mostRecentHTTPSTraffic string 2023-12-31 14:51:00
The timestamp of the most recent HTTPS traffic
across all subnets in UTC.

mostRecentKERBEROSTraffic string 2023-12-31 14:50:00
The timestamp of the most recent Kerberos
traffic across all subnets in UTC.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

mostRecentLDAPTraffic string 2023-12-31 14:50:00
The timestamp of the most recent LDAP traffic
across all subnets in UTC.

mostRecentNTPTraffic string 2023-12-31 14:51:00 The timestamp of the most recent NTP traffic
across all subnets in UTC.

mostRecentSMBTraffic string 2023-12-31 14:51:00
The timestamp of the most recent SMB traffic
across all subnets in UTC.

mostRecentSMTPTraffic string 2023-12-31 14:52:00 The timestamp of the most recent SMTP traffic
across all subnets in UTC.

mostRecentSNMPTraffic string 2023-12-31 14:50:00
The timestamp of the most recent SNMP traffic
across all subnets in UTC.

mostRecentSSHTraffic string 2023-12-31 14:51:00 The timestamp of the most recent SSH traffic
across all subnets in UTC.

mostRecentSSLTraffic string 2023-12-31 14:51:00
The timestamp of the most recent SSL traffic
across all subnets in UTC.

VLANs object An object containing VLANs seen in network
traffic on the instance.

VLANs.1 numeric 0

```
The number of devices within the specified
VLAN. Keys may also include a colon -
e.g. VLANs.2:904
```
internalIPRangeList array 10.0.0.0/8 192.168.0.0/16

internalIPRanges numeric 2 The number of internal IP ranges.

dnsServers numeric (^38) The number of devices identified as DNS server.
internalDomains numeric 0 The number of internal domains.
internalAndExternalDomainList array holdingsinc.com example.com
internalAndExternalDomains numeric 2
The number of internally and externally
resolvable domains.
proxyServers numeric 1
The number of proxy servers detected by
Darktrace.
proxyServerIPs array 192.168.72.4:443 The IPs of servers identified as proxy servers.
subnets numeric 97
The number of subnets currently active on the
network and seen receiving/sending traffic within
the last 7 days.
subnetData array
An array of statistics about the quality and
volume of data associated with the subnet.
subnetData.sid numeric 87 The “subnet id”, a unique identifier.
subnetData.network string 10.12.14.0/24 The IP address range that describes the subnet.
subnetData.devices numeric 235
The number of devices associated with an IP
address that places them within the subnet,
where activity has been seen in the last 7 days.
subnetData.clientDevices numeric (^231) The number of client devices within the subnet.
subnetData.mostRecentTraffic string 2023-12-31 14:00:00 The most recent traffic seen for the subnet.
subnetData.mostRecentDHCP string Never
The timestamp of the last DHCP seen for the
subnet in epoch time.
subnetData.dhcpQuality numeric 50 The DHCP quality - out of 100.
subnetData.kerberosQuality numeric 100 The Kerberos quality - out of 100.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

uptime string 04:55:54
Time since the modelling engine on the instance
was last rebooted.

systemuptime string 1894:29:43 Time since the instance was last rebooted.


###### Example Response

```
{
"excessTraffic": false,
"time": "2023-04-08 10:21",
"installed": "2018-10-22",
"mobileAppConfigured": true,
"version": "5.1.0 (dd351a)",
"ipAddress": "10.0.18.224",
"label": "holdingsinc-master",
"modelsUpdated": "2023-12-26 11:20:48",
"modelPackageVersion": "4.0-8515~20230322143408~g300d5d",
"bundleVersion": "61016",
"bundleDate": "2023-12-24 18:33:59",
"bundleInstalledDate": "2023-12-24 20:20:33",
"hostname": "example-darktrace",
"maximumOSSensors": 255,
"uuid": "07dcf0e5-217b-4e98-96b9-549b3dd87706",
"inoculation": false,
"applianceOSCode": "x",
"license": "2024-12-30 00:00:00",
"saasConnectorLicense": "2029-06-01 00:00:00",
"antigenaSaasLicense": "2029-06-01 00:00:00",
"syslogTLSSHA1Fingerprint": "2D:JY:LP:YT:TF:P3:BJ:21:Q6:D9:OT:JZ:LQ:8A:X0:KG:N6:9P:XC:DI",
"syslogTLSSHA256Fingerprint": "C6:9U:6N:D5:QU:HQ:
78:3P:C4:CN:L3:K2:PI:ZF:BO:MD:GO:Q9:IJ:ED:WD:BD:9Z:18:Z8:UY:34:TQ:HF:AD:P1:C3",
"antigenaNetworkEnabled": true,
"antigenaNetworkConfirmationMode": true,
"antigenaNetworkLicense": "2025-12-31 00:00:00",
"logIngestionReplicated": 326,
"logIngestionProcessed": 463930,
"logIngestionTCP": 2,
"logIngestionUDP": 380126407,
"logIngestionTypes": {
"example-template": 213587,
},
"logIngestionMatches": {
"example-template": 214509,
},
"licenseCounts": {
"saas": {
"total": 0
},
"licenseIPCount": 880,
"licenseCloudIPCount": 12
},
"antigenaNetworkBlockedConnections": {
"attempted": 277149,
"failed": 1333
},
"diskSpaceUsed_": 98,
"type": "master",
"diskUtilization": 1,
"load": 10,
"cpu": 11,
"memoryUsed": 87,
"dataQueue": 0,
"darkflowQueue": 0,
"flowProcessingTimes": {},
"networkInterfacesState_eth0": "up",
"networkInterfacesAddress_eth0": "10.0.18.224",
"networkInterfacesState_eth1": "up",
"networkInterfacesState_eth2": "up",
"networkInterfacesState_eth3": "up",
```
_continued..._


```
"networkInterfacesReceived_eth0": 55917812135,
"networkInterfacesReceived_eth1": 56493627001058,
"networkInterfacesReceived_eth2": 2297745881495,
"networkInterfacesReceived_eth3": 8037133670928,
"networkInterfacesTransmitted_eth0": 171992610491,
"networkInterfacesTransmitted_eth1": 0,
"networkInterfacesTransmitted_eth2": 0,
"networkInterfacesTransmitted_eth3": 0,
"bandwidthCurrent": 298432931,
"bandwidthCurrentString": "298.43 Mbps",
"bandwidthAverage": 121018000,
"bandwidthAverageString": "121.02 Mbps",
"bandwidth7DayPeak": 983743947,
"bandwidth7DayPeakString": "983.74 Mbps",
"bandwidth2WeekPeak": 1184287168,
"bandwidth2WeekPeakString": "1.18 Gbps",
"processedBandwidthCurrent": 16391984,
"processedBandwidthCurrentString": "16.39 Mbps",
"processedBandwidthAverage": 32307984,
"processedBandwidthAverageString": "32.31 Mbps",
"processedBandwidth7DayPeak": 58944496,
"processedBandwidth7DayPeakString": "58.94 Mbps",
"processedBandwidth2WeekPeak": 1139496509,
"processedBandwidth2WeekPeakString": "1.14 Gbps",
"eventsPerMinuteCurrent": {
"cSensorNotices": 0,
"cSensorDeviceDetails": 0,
"cSensorModelEvents": 1112,
"networkNotices": 71,
"networkDeviceDetails": 4,
"networkModelEvents": 123437,
"logInputNotices": 18,
"logInputDeviceDetails": 0,
"logInputModelEvents": 0,
"saasNotices": 0,
"saasModelEvents": 0
},
"probes": {
"12": {
"id": 12,
"configuredServer": "example-vsensor-2.example.com",
"version": "6.1.23 (f35936c6)",
"ipAddress": "10.10.12.12",
"bundleVersion": "6.1.7",
"bundleDate": "2023-12-13 12:23:25",
"bundleInstalledDate": "2023-12-14 06:24:46",
"metadata": {
"tracking": {
"environment": "aws",
"vpc-id": "vpc-d8957336",
"label": "aws::vpc-d8957336"
},
"readonly": {
"instance-id": "i-ec731fdc113862a61",
"ami-id": "ami-465f145cd08a45b8w",
"region": "eu-west-1",
"account-id": "123456789101",
"availability-zone": "eu-west-1b",
"instance-type": "t2.medium",
"launch-time": "2023-12-08T13:04:14Z",
"environment": "aws",
"kernel-running": "5.11.0-1022-aws",
"mac-address-primary": "ab:12:bc:34:de:56",
```
_continued..._


```
"local-ipv4": "10.10.12.12"
},
"autovlan": 0
}
"load": 25,
"cpu": 6,
"memoryUsed": 18,
"osSensors": [
"10.10.12.125"
],
"networkInterfacesState_eth0": "up",
"networkInterfacesAddress_eth0": "10.10.12.12",
"networkInterfacesState_eth1": "up",
"networkInterfacesReceived_eth0": 1506525936,
"networkInterfacesReceived_eth1": 606743763992,
"networkInterfacesTransmitted_eth0": 7954105577,
"networkInterfacesTransmitted_eth1": 168,
"bandwidthCurrent": 542011,
"bandwidthCurrentString": "542 kbps",
"bandwidthAverage": 2093000,
"bandwidthAverageString": "2.09 Mbps",
"bandwidth7DayPeak": 6832456,
"bandwidth7DayPeakString": "6.83 Mbps",
"bandwidth2WeekPeak": 24167960,
"bandwidth2WeekPeakString": "24.17 Mbps",
"processedBandwidthCurrent": 9204,
"processedBandwidthCurrentString": "9 kbps",
"processedBandwidthAverage": 13610,
"processedBandwidthAverageString": "14 kbps",
"processedBandwidth7DayPeak": 41833,
"processedBandwidth7DayPeakString": "42 kbps",
"processedBandwidth2WeekPeak": 41833,
"processedBandwidth2WeekPeakString": "42 kbps",
"connectionsPerMinuteCurrent": 169,
"connectionsPerMinuteAverage": 156,
"connectionsPerMinute7DayPeak": 432,
"connectionsPerMinute2WeekPeak": 432
"antigenaNetworkBlockedConnections": {
"attempted": 1234,
"failed": 0
}
},
...
},
"connectionsPerMinuteCurrent": 7130,
"connectionsPerMinuteAverage": 5849,
"connectionsPerMinute7DayPeak": 8829,
"connectionsPerMinute2WeekPeak": 20975,
"operatingSystems": 16,
"credentials": 86,
"credentials7Days": 55,
"credentialSources": {
"NTLM": {
"4weeks": 6,
"7days": 4
},
"Saas": {
"4weeks": 80,
"7days": 51
}
},
"newDevices4Weeks": 244,
"newDevices7Days": 35,
```
_continued..._


```
"newDevices24Hours": 11,
"newDevicesHour": 0,
"activeDevices4Weeks": 2709,
"activeDevices7Days": 1420,
"activeDevices24Hours": 897,
"activeDevicesHour": 460,
"deviceHostnames": 337,
"deviceMACAddresses": 375,
"deviceRecentIPChange": 6,
"models": 695,
"modelsBreached": 403911,
"modelsSuppressed": 1872333,
"devicesModeled": 1420,
"recentUnidirectionalConnections": 0,
"mostRecentDHCPTraffic": "2023-04-08 10:14:00",
"mostRecentDNSTraffic": "2023-04-08 10:18:00",
...
"VLANs": {
"1": 0,
...
},
"internalIPRangeList": [
"10.0.0.0/8",
"192.168.0.0/16",
],
"internalIPRanges": 2,
"dnsServers": 38,
"internalDomains": 0,
"internalAndExternalDomainList": [
"holdingsinc.com",
"example.com"
],
"internalAndExternalDomains": 2,
"proxyServers": 1,
"proxyServerIPs": [
"192.168.72.4:443",
],
"subnets": 97,
"subnetData": [
{
"recentTrafficPercent": 3,
"recentUnidirectionalTrafficPercent": 2,
"sid": 8710,
"network": "10.12.14.0/24",
"devices": 235,
"clientDevices": 231,
"mostRecentTraffic": "2023-04-08 10:00:00",
"mostRecentDHCP": "Never"
},
...
],
"uptime": "05:12:56",
"systemuptime": "1894:46:44"
}
```
_Response is abbreviated._


#### Response Schema - includechildren=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
excessTraffic boolean FALSE
Whether the instance is receiving more traffic
than it can reasonably process.
```
```
time string 21-3-31 14:43 The current server time in UTC.
```
```
installed string 10/22/18
The date that the first data was received by the
instance.
```
```
mobileAppConfigured boolean TRUE Whether the Darktrace Mobile App is configured.
```
```
version string 6.1.23 (f35936c6)
```
```
The current installed version of the Model Engine
```
- the system that evaluates model logic against
metadata - which is distinct from the Threat
Visualizer and Model Update bundles.

```
ipAddress string 10.0.18.224
Where detectable, the IP address of the
management interface.
```
```
label string holdingsinc-master
A freetext label applied to the instance on the
System Config page to better identify it.
```
```
modelsUpdated string 2023-12-26 11:20:30 The last time default models were updated.
```
```
modelPackageVersion string 4.0-8515 20230322143408 The model bundle information.g300d5d
```
```
bundleVersion string 61016 The Threat Visualizer software bundle number.
```
```
bundleVariant string rc
```
```
The type of bundle. Early adopter customers may
receive release candidates as well as stable
builds.
```
```
bundleDate string 2023-12-26 11:20:30
The time that the Threat Visualizer software
bundle was downloaded.
```
```
bundleInstalledDate string 2023-12-26 11:20:30
The time that the Threat Visualizer software
bundle was downloaded.
```
```
maximumOSSensors numeric 255
The maximum number of osSensors that can be
associated with vSensors in this deployment.
```
```
hostname string
example-
darktrace-01
The instance hostname.
```
```
uuid string
07dcf0e5-217b-4e98-
96b9-549b3dd87706
A unique identifier for the instance.
```
```
inoculation boolean FALSE
Whether the instance is subscribed to Darktrace
inoculation.
```
```
applianceOSCode string x A system field.
```
```
license string 45656
The expiry date for the current Threat Visualizer
license.
```
```
saasConnectorLicense string 2029-06-01 00:00:00
```
```
The expiry date for the current SaaS module
license. Where multiple modules are installed,
the date of the last expiring module.
```
```
antigenaSaasLicense string 2029-06-01 00:00:00
```
```
The expiry date for the current Darktrace
RESPOND module license. Where multiple
modules across Darktrace/Apps, Darktrace/
Cloud and Darktrace/Zero Trust are licensed for
Darktrace RESPOND, the date of the last expiring
module.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

cloudSecurityLicense string 2023-10-02 00:00:00
The expiry date for the current Darktrace Cloud
Security license.

syslogTLSSHA1Fingerprint string

```
2D:JY:LP:YT:TF:P3:B
J:
21:Q6:D9:OT:JZ:LQ:
8A:X0:KG:N6:9P:XC:D
I
```
```
The SHA1 Fingerprint of the current syslog
ingestion TLS Certificate.
```
syslogTLSSHA256Fingerprint string
C6:9U:6N:D5:QU:HQ:
78:3P...

```
The SHA256 Fingerprint of the current syslog
ingestion TLS Certificate.
```
antigenaNetworkEnabled boolean TRUE

```
Whether Darktrace RESPOND/Network (formerly
Antigena Network) is enabled in the instance
console.
```
antigenaNetworkRunning boolean TRUE

```
Whether Darktrace RESPOND/Network (formerly
Antigena Network) is currently running on the
given instance.
```
antigenaNetworkConfirmationMode boolean TRUE This field is deprecated.

antigenaNetworkLicense string 2025-12-31 00:00:00

```
The expiry date for the current Darktrace
RESPOND/Network (formerly Antigena Network)
license.
```
preventE2ELicense string 2025-12-31 00:00:00
The expiry date for the current Darktrace
PREVENT/E2E license, if configured.

logIngestionReplicated numeric 321

```
The number of ingested syslog lines from special
telemetry modules (e.g. Zscaler, Netskope)
across the instance lifetime.
```
logIngestionProcessed numeric 422406

```
The number of ingested syslog lines processed
across the instance lifetime. Log lines are
processed if they are found to contain and match
a valid Log Filter value for one or more telemetry
templates.
```
logIngestionTCP numeric 2

```
The number of syslog lines that were received via
TCP across the instance lifetime. Includes both
valid and invalid inputs.
```
logIngestionUDP numeric 329999225

```
The number of syslog lines that were received via
UDP across the instance lifetime. Includes both
valid and invalid inputs.
```
logIngestionMatches object

```
An object describing the log lines that were
processed (i.e., broken down on a per-template
basis.
```
logIngestionMatches.exampletemplate numeric 214509

```
An example log template and the number of
times log lines have been processed for that type
```
- i.e., evaluated against it.

logIngestionTypes object

```
An object describing the log lines that were
processed and matched successfully against
templates on this master instance, broken down
on a per-template basis.
```
logIngestionTypes.exampletemplate numeric 213587

```
An example log template and the number of
times log lines have been processed and
matched successfully for that type on this
instance.
```
licenseCounts object

```
An object containing the number of devices and
user accounts seen across Darktrace DETECT
coverage areas.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

licenseCounts.saas object

```
An object containing one or more SaaS modules
and the number of users seen from that module
in the last 7 days.
```
licenseCounts.saas.total numeric 0
The total number of SaaS users across all
modules in the last 7 days.

licenseCounts.licenseIPCount numeric 249

```
The peak value of the number of distinct internal
(not excluded) IP addresses seen within any 24
hour period over the last seven days. Does not
overlap with licenseCloudIPCount.
```
antigenaNetworkBlockedConnections object

```
An object representing Darktrace RESPOND/
Network attempts to end connections and
number of those attempts where connectivity
demonstrably continued. These fields are
experimental and under active development, and
should not be relied upon, or expected to remain
stable, at the current time.
```
antigenaNetworkBlockedConnections.atte
mpted numeric
277149

```
The culmulative number of attempts made to
end connections (fired RSTs) taken by Darktrace
RESPOND/Network on the given instance since it
was upgraded to a software version where this
value was recorded. One RESPOND action will
produce multiple attempts, as attempts are
recorded on a per-RST basis .This metric is
experimental and under active development.
```
antigenaNetworkBlockedConnections.fail
ed
numeric 1333

```
Attempts where Darktrace RESPOND/Network
has attempted to end a connection - and the
associated RST packet was seen by the instance
```
- but connectivity demonstrably continued after
the RST was sent and/or observed. This metric is
experimental and under active development.

diskSpaceUsed_ numeric 98 The percentage diskspace in use.

type string master The type of appliance.

diskUtilization numeric 1
This percentage value indicates the average disk
I/O.

load numeric 12
This percentage value indicates how in-demand
resources are in the instance processing.

cpu numeric 8
This percentage value indicates the average
amount of CPU usage (not idle).

memoryUsed numeric (^87) The percentage of memory in use.
dataQueue numeric 0 The current queue for event ordering in seconds.
darkflowQueue numeric 0
The current queue from bandwidth ingestion to
processing in seconds.
flowProcessingTimes object
An object describing the amount of connections
processed within 10 second intervals.
networkInterfacesState_eth0 string up Whether the network interface is up or down.
networkInterfacesAddress_eth0 string 10.0.18.224 The IP addresses if resolvable of the interface.
networkInterfacesState_eth1 string up Whether the network interface is up or down.
networkInterfacesState_eth2 string up Whether the network interface is up or down.
networkInterfacesState_eth3 string up Whether the network interface is up or down.
networkInterfacesReceived_eth0 numeric 37120476833 The number of bytes received by the interface


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

networkInterfacesReceived_eth1 numeric 51300700000000 The number of bytes received by the interface

networkInterfacesReceived_eth2 numeric 1887530000000 The number of bytes received by the interface

networkInterfacesReceived_eth3 numeric 6177270000000 The number of bytes received by the interface

networkInterfacesTransmitted_eth0 numeric 112983000000 The number of bytes sent by the interface

networkInterfacesTransmitted_eth1 numeric (^0) The number of bytes sent by the interface
networkInterfacesTransmitted_eth2 numeric 0 The number of bytes sent by the interface
networkInterfacesTransmitted_eth3 numeric 0 The number of bytes sent by the interface
bandwidthCurrent numeric 386703428
Ingested bandwidth over the last 10 minutes.
Some bandwidth may not be processed due to
system settings.
bandwidthCurrentString string 386.70 Mbps
Ingested bandwidth over the last 10 minutes in a
readable format. Some bandwidth may not be
processed due to system settings.
bandwidthAverage numeric 391631000
Average bandwidth over the last 2 weeks. Some
bandwidth may not be processed due to system
settings.
bandwidthAverageString string 391.63 Mbps
Average bandwidth over the last 2 weeks in a
readable format. Some bandwidth may not be
processed due to system settings.
bandwidth7DayPeak numeric 1230235696
The highest ingested bandwidth observed in any
ten-minute interval over the last 7 days. Some
bandwidth may not be processed due to system
settings.
bandwidth7DayPeakString string 1.23 Gbps
The highest ingested bandwidth observed in any
ten-minute interval over the last 7 days in a
readable format. Some bandwidth may not be
processed due to system settings.
bandwidth2WeekPeak numeric 1645876703
The highest ingested bandwidth observed in any
ten-minute interval over the last 2 weeks. Some
bandwidth may not be processed due to system
settings.
bandwidth2WeekPeakString string 1.65 Gbps
The highest ingested bandwidth observed in any
ten-minute interval over the last 2 weeks in a
readable format. Some bandwidth may not be
processed due to system settings.
processedBandwidthCurrent numeric 59938652 Processed bandwidth over the last 10 minutes.
processedBandwidthCurrentString string 59.94 Mbps Processed bandwidth over the last 10 minutes in
a readable format.
processedBandwidthAverage numeric 142568480 Average bandwidth over the last 2 weeks.
processedBandwidthAverageString string 142.57 Mbps
Average bandwidth over the last 2 weeks in a
readable format.
processedBandwidth7DayPeak numeric 1139496509
The highest bandwidth observed in any ten-
minute interval over the last 7 days.
processedBandwidth7DayPeakString string 1.14 Gbps
The highest bandwidth observed in any ten-
minute interval over the last 7 days in a readable
format.
processedBandwidth2WeekPeak numeric 1223451790
The highest bandwidth observed in any ten-
minute interval over the last 2 weeks.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

processedBandwidth2WeekPeakString string 1.22 Gbps

```
The highest bandwidth observed in any ten-
minute interval over the last 2 weeks in a
readable format.
```
eventsPerMinuteCurrent object

```
An object describing the average number of
events (for each event type) that was processed
in one minute over the last 10-20 minutes. More
detailed information is available from the /
summarystatistics endpoint.
```
eventsPerMinuteCurrent.cSensorNotices numeric 0

```
The number of non-connection events produced
by cSensor devices that were processed per
minute over the last 10-20 minutes.
```
eventsPerMinuteCurrent.cSensorDeviceDe
tails
numeric 0

```
The number of tracking events produced by
cSensor devices that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.cSensorModelEve
nts
numeric 1456

```
The number of modeling events produced by
cSensor devices that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.networkNotices numeric 69

```
The number of non-connection events produced
by network traffic that were processed per
minute over the last 10-20 minutes.
```
eventsPerMinuteCurrent.networkDeviceDe
tails
numeric 4

```
The number of tracking events produced by
network traffic that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.networkModelEve
nts
numeric 130514

```
The number of modeling events produced by
network traffic that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.logInputNotices numeric 14

```
The number of non-connection events produced
by syslog ingestion that were processed per
minute over the last 10-20 minutes.
```
eventsPerMinuteCurrent.logInputDeviceD
etails
numeric 0

```
The number of tracking events produced by
syslog ingestion that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.logInputModelEv
ents
numeric^0

```
The number of modeling events produced by
syslog ingestion that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.saasNotices numeric 0

```
The number of events produced by SaaS
modules that were processed per minute over
the last 10-20 minutes.
```
eventsPerMinuteCurrent.saasModelEvents numeric 0

```
The number of modeling events produced by
SaaS modules that were processed per minute
over the last 10-20 minutes.
```
connectionsPerMinuteCurrent numeric 7430

```
Current number of connections processed in the
last minute - includes ongoing (unfinished)
connections and completed connections.
```
connectionsPerMinuteAverage numeric 8768

```
Average number of connections processed per
minute in the last 2 weeks - includes ongoing
(unfinished) connections and completed
connections.
```
connectionsPerMinute7DayPeak numeric 20975

```
Highest number of connections processed per
minute in the last 7 days - includes ongoing
(unfinished) connections and completed
connections.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

connectionsPerMinute2WeekPeak numeric 20975

```
Highest number of connections processed per
minute in the last 2 weeks - includes ongoing
(unfinished) connections and completed
connections.
```
credentials numeric 86
The number of credentials observed from all
sources over the last 4 weeks.

credentials7Days numeric 55
The number of credentials observed from all
sources over the last 7 days.

credentialSources object

```
An object describing the sources where
credentials were observed from. Sources will
differ depending upon connection make-up and
coverage areas deployed.
```
credentialSources.NTLM object An object describing the number of credentials
which were seen in NTLM traffic.

credentialSources.NTLM.4weeks numeric 6
The number of credentials observed in NTLM
traffic over the last 4 weeks.

credentialSources.NTLM.7days numeric 4 The number of credentials observed in NTLM
traffic over the last 7 days.

credentialSources.Saas object

```
An object describing the number of credentials
which were observed in event data from
Darktrace/Apps, Cloud or Zero Trust modules.
```
credentialSources.Saas.4weeks numeric 80

```
The the number of credentials which were
observed in event data from Darktrace/Apps,
Cloud or Zero Trust modules over the last 4
weeks.
```
credentialSources.Saas.7days numeric 51

```
The the number of credentials which were
observed in event data from Darktrace/Apps,
Cloud or Zero Trust modules over the last 7 days.
```
operatingSystems numeric 16
The number of operating systems (as derived by
Darktrace) seen over the last 4 weeks.

newDevices4Weeks numeric 289 The number of new devices seen over the last 4
weeks.

newDevices7Days numeric 50
The number of new devices seen over the last 7
days.

newDevices24Hours numeric 8 The number of new devices seen over the last 24
hours.

newDevicesHour numeric 1
The number of new devices seen over the last
hour.

activeDevices4Weeks numeric 2856

```
The number of active devices seen over the last
4 weeks. Active devices may also include
unmodeled devices such as broadcast traffic,
internal and external multicast traffic and any
excluded ip ranges if activity is seen.
```
activeDevices7Days numeric 1590

```
The number of active devices seen over the last
7 days. Active devices may also include
unmodeled devices such as broadcast traffic,
internal and external multicast traffic and any
excluded ip ranges.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

activeDevices24Hours numeric 800

```
The number of active devices seen over the last
24 hours. Active devices may also include
unmodeled devices such as broadcast traffic,
internal and external multicast traffic and any
excluded ip ranges.
```
activeDevicesHour numeric 467

```
The number of active devices seen over the last
hour. Active devices may also include
unmodeled devices such as broadcast traffic,
internal and external multicast traffic and any
excluded ip ranges.
```
deviceHostnames numeric 348
The number of device hostnames seen in the last
4 weeks.

deviceMACAddresses numeric 417
The number of device MAC Addresses seen in
the last 4 weeks.

deviceRecentIPChange numeric 21
The nunber of devices that have changed IP in
the last 7 days.

models numeric 692
The number of active/enabled models on the
system.

modelsBreached numeric 401834

```
This figure represents the number of lifetime
model breaches, unless the instance is explicitly
configured to expire model breaches.
```
modelsSuppressed numeric 1869280

```
This figure represents the number of lifetime
model breaches that have been suppressed,
unless the instance is explicitly configured to
expire model breaches.
```
devicesModeled numeric 1590
The current number of devices with active
‘pattern of life’ tracking.

recentUnidirectionalConnections numeric 0

```
The percentage number of connections
identified as unidirectional over the last 30
minutes. If data is not available, an average over
the last 6 hours.
```
mostRecentDHCPTraffic string 2023-12-31 14:52:00
The timestamp of the most recent DHCP traffic
across all subnets in UTC.

mostRecentDNSTraffic string 2023-12-31 14:49:00
The timestamp of the most recent DNS traffic
across all subnets in UTC.

mostRecentDCE_RPCTraffic string 2023-12-31 14:52:00
The timestamp of the most recent DCE_RPC
traffic across all subnets in UTC.

mostRecentHTTPTraffic string 2023-12-31 14:52:00
The timestamp of the most recent HTTP traffic
across all subnets in UTC.

mostRecentHTTPSTraffic string 2023-12-31 14:52:00
The timestamp of the most recent HTTPS traffic
across all subnets in UTC.

mostRecentKERBEROSTraffic string 2023-12-31 14:52:00
The timestamp of the most recent Kerberos
traffic across all subnets in UTC.

mostRecentLDAPTraffic string 2023-12-31 14:49:00
The timestamp of the most recent LDAP traffic
across all subnets in UTC.

mostRecentNTPTraffic string 2023-12-31 14:49:00
The timestamp of the most recent NTP traffic
across all subnets in UTC.

mostRecentSMBTraffic string 2023-12-31 14:49:00
The timestamp of the most recent SMB traffic
across all subnets in UTC.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

mostRecentSMTPTraffic string 2023-12-31 14:49:00
The timestamp of the most recent SMTP traffic
across all subnets in UTC.

mostRecentSNMPTraffic string 2023-12-31 14:49:00 The timestamp of the most recent SNMP traffic
across all subnets in UTC.

mostRecentSSHTraffic string 2023-12-31 14:49:00
The timestamp of the most recent SSH traffic
across all subnets in UTC.

mostRecentSSLTraffic string 2023-12-31 14:49:00 The timestamp of the most recent SSL traffic
across all subnets in UTC.

VLANs object
An object containing VLANs seen in network
traffic on the instance.

VLANs.1 numeric 0 The number of devices within the specified
VLAN.

internalIPRangeList array 10.0.0.0/8 192.168.0.0/16

internalIPRanges numeric 2 The number of internal IP ranges.

dnsServers numeric 38 The number of devices identified as DNS server.

internalDomains numeric 0 The number of internal domains.

internalAndExternalDomainList array holdingsinc.com example.com

internalAndExternalDomains numeric 2
The number of internally and externally
resolvable domains.

proxyServers numeric 1
The number of proxy servers detected by
Darktrace.

proxyServerIPs array 192.168.72.4:443 The IPs of servers identified as proxy servers.

subnets numeric 97

```
The number of subnets currently active on the
network and seen receiving/sending traffic within
the last 7 days.
```
subnetData array
An array of statistics about the quality and
volume of data associated with the subnet.

subnetData.sid numeric 87 The “subnet id”, a unique identifier.

subnetData.network string 10.12.14.0/24 The IP address range that describes the subnet.

subnetData.devices numeric 235

```
The number of devices associated with an IP
address that places them within the subnet,
where activity has been seen in the last 7 days.
```
subnetData.clientDevices numeric 231 The number of client devices within the subnet.

subnetData.mostRecentTraffic string 2023-12-31 14:00:00 The most recent traffic seen for the subnet.

subnetData.mostRecentDHCP string Never The timestamp of the last DHCP seen for the
subnet in epoch time.

subnetData.dhcpQuality numeric 50 The DHCP quality - out of 100.

subnetData.kerberosQuality numeric 100 The Kerberos quality - out of 100.

uptime string 04:55:54
Time since the modelling engine on the instance
was last rebooted.

systemuptime string 1894:29:43 Time since the instance was last rebooted.


###### Example Response

```
{
"excessTraffic": false,
"time": "2023-04-08 10:21",
"installed": "2018-10-22",
"mobileAppConfigured": true,
"version": "5.1.0 (dd351a)",
"ipAddress": "10.0.18.224",
"label": "holdingsinc-master",
"modelsUpdated": "2023-12-26 11:20:48",
"modelPackageVersion": "4.0-8515~20230322143408~g300d5d",
"bundleVersion": "61016",
"bundleDate": "2023-12-24 18:33:59",
"bundleInstalledDate": "2023-12-24 20:20:33",
"hostname": "example-darktrace",
"maximumOSSensors": 255,
"uuid": "07dcf0e5-217b-4e98-96b9-549b3dd87706",
"inoculation": false,
"applianceOSCode": "x",
"license": "2024-12-30 00:00:00",
"saasConnectorLicense": "2029-06-01 00:00:00",
"antigenaSaasLicense": "2029-06-01 00:00:00",
"syslogTLSSHA1Fingerprint": "2D:JY:LP:YT:TF:P3:BJ:21:Q6:D9:OT:JZ:LQ:8A:X0:KG:N6:9P:XC:DI",
"syslogTLSSHA256Fingerprint": "C6:9U:6N:D5:QU:HQ:
78:3P:C4:CN:L3:K2:PI:ZF:BO:MD:GO:Q9:IJ:ED:WD:BD:9Z:18:Z8:UY:34:TQ:HF:AD:P1:C3",
"antigenaNetworkEnabled": true,
"antigenaNetworkConfirmationMode": true,
"antigenaNetworkLicense": "2025-12-31 00:00:00",
"logIngestionReplicated": 326,
"logIngestionProcessed": 463930,
"logIngestionTCP": 2,
"logIngestionUDP": 380126407,
"logIngestionTypes": {
"example-template": 213587,
},
"logIngestionMatches": {
"example-template": 214509,
},
"licenseCounts": {
"saas": {
"total": 0
},
"licenseIPCount": 880,
"licenseCloudIPCount": 12
},
"antigenaNetworkBlockedConnections": {
"attempted": 277149,
"failed": 1333
},
"diskSpaceUsed_": 98,
"type": "master",
"diskUtilization": 1,
"load": 10,
"cpu": 11,
"memoryUsed": 87,
"dataQueue": 0,
"darkflowQueue": 0,
"flowProcessingTimes": {},
"networkInterfacesState_eth0": "up",
"networkInterfacesAddress_eth0": "10.0.18.224",
"networkInterfacesState_eth1": "up",
"networkInterfacesState_eth2": "up",
"networkInterfacesState_eth3": "up",
```
_continued..._


```
"networkInterfacesReceived_eth0": 55917812135,
"networkInterfacesReceived_eth1": 56493627001058,
"networkInterfacesReceived_eth2": 2297745881495,
"networkInterfacesReceived_eth3": 8037133670928,
"networkInterfacesTransmitted_eth0": 171992610491,
"networkInterfacesTransmitted_eth1": 0,
"networkInterfacesTransmitted_eth2": 0,
"networkInterfacesTransmitted_eth3": 0,
"bandwidthCurrent": 298432931,
"bandwidthCurrentString": "298.43 Mbps",
"bandwidthAverage": 121018000,
"bandwidthAverageString": "121.02 Mbps",
"bandwidth7DayPeak": 983743947,
"bandwidth7DayPeakString": "983.74 Mbps",
"bandwidth2WeekPeak": 1184287168,
"bandwidth2WeekPeakString": "1.18 Gbps",
"processedBandwidthCurrent": 16391984,
"processedBandwidthCurrentString": "16.39 Mbps",
"processedBandwidthAverage": 32307984,
"processedBandwidthAverageString": "32.31 Mbps",
"processedBandwidth7DayPeak": 58944496,
"processedBandwidth7DayPeakString": "58.94 Mbps",
"processedBandwidth2WeekPeak": 1139496509,
"processedBandwidth2WeekPeakString": "1.14 Gbps",
"eventsPerMinuteCurrent": {
"cSensorNotices": 0,
"cSensorDeviceDetails": 0,
"cSensorModelEvents": 1112,
"networkNotices": 71,
"networkDeviceDetails": 4,
"networkModelEvents": 123437,
"logInputNotices": 18,
"logInputDeviceDetails": 0,
"logInputModelEvents": 0,
"saasNotices": 0,
"saasModelEvents": 0
},
"connectionsPerMinuteCurrent": 7130,
"connectionsPerMinuteAverage": 5849,
"connectionsPerMinute7DayPeak": 8829,
"connectionsPerMinute2WeekPeak": 20975,
"operatingSystems": 16,
"credentials": 86,
"credentials7Days": 55,
"credentialSources": {
"NTLM": {
"4weeks": 6,
"7days": 4
},
"Saas": {
"4weeks": 80,
"7days": 51
}
},
"credentials": 86,
"credentials7Days": 55,
"credentialSources": {
"NTLM": {
"4weeks": 6,
"7days": 4
},
"Saas": {
"4weeks": 80,
```
_continued..._


```
"7days": 51
}
},
"newDevices4Weeks": 244,
"newDevices7Days": 35,
"newDevices24Hours": 11,
"newDevicesHour": 0,
"activeDevices4Weeks": 2709,
"activeDevices7Days": 1420,
"activeDevices24Hours": 897,
"activeDevicesHour": 460,
"deviceHostnames": 337,
"deviceMACAddresses": 375,
"deviceRecentIPChange": 6,
"models": 695,
"modelsBreached": 403911,
"modelsSuppressed": 1872333,
"devicesModeled": 1420,
"recentUnidirectionalConnections": 0,
"mostRecentDHCPTraffic": "2023-04-08 10:14:00",
"mostRecentDNSTraffic": "2023-04-08 10:18:00",
...
"VLANs": {
"1": 0,
...
},
"internalIPRangeList": [
"10.0.0.0/8",
"192.168.0.0/16",
],
"internalIPRanges": 2,
"dnsServers": 38,
"internalDomains": 0,
"internalAndExternalDomainList": [
"holdingsinc.com",
"example.com"
],
"internalAndExternalDomains": 2,
"proxyServers": 1,
"proxyServerIPs": [
"192.168.72.4:443",
],
"subnets": 97,
"subnetData": [
{
"recentTrafficPercent": 3,
"recentUnidirectionalTrafficPercent": 2,
"sid": 8710,
"network": "10.12.14.0/24",
"devices": 235,
"clientDevices": 231,
"mostRecentTraffic": "2023-04-08 10:00:00",
"mostRecentDHCP": "Never"
},
...
],
"uptime": "05:12:56",
"systemuptime": "1894:46:44"
}
```
_Response is abbreviated._


#### Response Schema - fast=true&includechildren=false

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
excessTraffic boolean FALSE
Whether the instance is receiving more traffic
than it can reasonably process.
```
```
time string 2023-12-31 14:53:57 The current server time in UTC.
```
```
installed string 10/22/18
The date that the first data was received by the
instance.
```
```
mobileAppConfigured boolean TRUE Whether the Darktrace Mobile App is configured.
```
```
version string 6.1.23 (f35936c6)
```
```
The current installed version of the Model Engine
```
- the system that evaluates model logic against
metadata - which is distinct from the Threat
Visualizer and Model Update bundles.

```
ipAddress string 10.0.18.224
Where detectable, the IP address of the
management interface.
```
```
label string holdingsinc-master
A freetext label applied to the instance on the
System Config page to better identify it.
```
```
modelsUpdated string 2023-12-26 11:20:00 The last time default models were updated.
```
```
modelPackageVersion string 4.0-8515 20230322143408 The model bundle information.g300d5d
```
```
bundleVersion string 61016 The Threat Visualizer software bundle number.
```
```
bundleVariant string rc
```
```
The type of bundle. Early adopter customers may
receive release candidates as well as stable
builds.
```
```
bundleDate string 2023-12-24 18:33:11
The time that the Threat Visualizer software
bundle was downloaded.
```
```
bundleInstalledDate string 2023-12-24 20:20:12
The time that the Threat Visualizer software
bundle was installed.
```
```
maximumOSSensors numeric 255
The maximum number of osSensors that can be
associated with vSensors in this deployment.
```
```
hostname string
example-
darktrace-01
The instance hostname.
```
```
uuid string
07dcf0e5-217b-4e98-
96b9-549b3dd87706
A unique identifier for the instance.
```
```
inoculation boolean FALSE
Whether the instance is subscribed to Darktrace
inoculation.
```
```
applianceOSCode string x A system field.
```
```
license string 2024-12-30 00:00:00
The expiry date for the current Threat Visualizer
license.
```
```
saasConnectorLicense string 2029-06-01 00:00:00
```
```
The expiry date for the current SaaS module
license. Where multiple modules are installed,
the date of the last expiring module.
```
```
antigenaSaasLicense string 2029-06-01 00:00:00
```
```
The expiry date for the current Darktrace
RESPOND module license. Where multiple
modules across Darktrace/Apps, Darktrace/
Cloud and Darktrace/Zero Trust are licensed for
Darktrace RESPOND, the date of the last expiring
module.
```
```
cloudSecurityLicense string 2023-10-02 00:00:00
The expiry date for the current Darktrace Cloud
Security license.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

syslogTLSSHA1Fingerprint string

```
2D:JY:LP:YT:TF:P3:B
J:
21:Q6:D9:OT:JZ:LQ:
8A:X0:KG:N6:9P:XC:D
I
```
```
The SHA1 Fingerprint of the current syslog
ingestion TLS Certificate.
```
syslogTLSSHA256Fingerprint string
C6:9U:6N:D5:QU:HQ:
78:3P...

```
The SHA256 Fingerprint of the current syslog
ingestion TLS Certificate.
```
antigenaNetworkEnabled boolean TRUE

```
Whether Darktrace RESPOND/Network (formerly
Antigena Network) is enabled in the instance
console.
```
antigenaNetworkRunning boolean TRUE

```
Whether Darktrace RESPOND/Network (formerly
Antigena Network) is currently running on the
given instance.
```
antigenaNetworkConfirmationMode boolean TRUE This field is deprecated.

antigenaNetworkLicense string 2025-12-31 00:00:00

```
The expiry date for the current Darktrace
RESPOND/Network (formerly Antigena Network)
license.
```
preventE2ELicense string 2025-12-31 00:00:00
The expiry date for the current Darktrace
PREVENT/E2E license, if configured.

logIngestionReplicated numeric 321

```
The number of ingested syslog lines from special
telemetry modules (e.g. Zscaler, Netskope)
across the instance lifetime.
```
logIngestionProcessed numeric 422406

```
The number of ingested syslog lines processed
across the instance lifetime. Log lines are
processed if they are found to contain and match
a valid Log Filter value for one or more telemetry
templates.
```
logIngestionTCP numeric 2

```
The number of syslog lines that were received via
TCP across the instance lifetime. Includes both
valid and invalid inputs.
```
logIngestionUDP numeric 329999225

```
The number of syslog lines that were received via
UDP across the instance lifetime. Includes both
valid and invalid inputs.
```
logIngestionMatches object

```
An object describing the log lines that were
processed (i.e., broken down on a per-template
basis.
```
logIngestionMatches.exampletemplate numeric 214509

```
An example log template and the number of
times log lines have been processed for that type
```
- i.e., evaluated against it.

logIngestionTypes object

```
An object describing the log lines that were
processed and matched successfully against
templates on this master instance, broken down
on a per-template basis.
```
logIngestionTypes.exampletemplate numeric 213587

```
An example log template and the number of
times log lines have been processed and
matched successfully for that type on this
instance.
```
licenseCounts object

```
An object containing the number of devices and
user accounts seen across Darktrace DETECT
coverage areas.
```
licenseCounts.saas object

```
An object containing one or more SaaS modules
and the number of users seen from that module
in the last 7 days.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

licenseCounts.saas.total numeric 0
The total number of SaaS users across all
modules in the last 7 days.

licenseCounts.licenseIPCount numeric 249

```
The peak value of the number of distinct internal
(not excluded) IP addresses seen within any 24
hour period over the last seven days. Does not
overlap with licenseCloudIPCount.
```
antigenaNetworkBlockedConnections object

```
An object representing Darktrace RESPOND/
Network attempts to end connections and
number of those attempts where connectivity
demonstrably continued. These fields are
experimental and under active development, and
should not be relied upon, or expected to remain
stable, at the current time.
```
antigenaNetworkBlockedConnections.atte
mpted
numeric 277149

```
The culmulative number of attempts made to
end connections (fired RSTs) taken by Darktrace
RESPOND/Network on the given instance since it
was upgraded to a software version where this
value was recorded. One RESPOND action will
produce multiple attempts, as attempts are
recorded on a per-RST basis .This metric is
experimental and under active development.
```
antigenaNetworkBlockedConnections.fail
ed
numeric 1333

```
Attempts where Darktrace RESPOND/Network
has attempted to end a connection - and the
associated RST packet was seen by the instance
```
- but connectivity demonstrably continued after
the RST was sent and/or observed. This metric is
experimental and under active development.

diskSpaceUsed_ numeric 98 The percentage diskspace in use.

type string master The type of appliance.

diskUtilization numeric 1 This percentage value indicates the average disk
I/O.

load numeric 13
This percentage value indicates how in-demand
resources are in the instance processing.

cpu numeric 7 This percentage value indicates the average
amount of CPU usage (not idle).

memoryUsed numeric 87 The percentage of memory in use.

dataQueue numeric 0 The current queue for event ordering in seconds.

darkflowQueue numeric 0
The current queue from bandwidth ingestion to
processing in seconds.

flowProcessingTimes object
An object describing the amount of connections
processed within 10 second intervals.

networkInterfacesState_eth0 string up Whether the network interface is up or down.

networkInterfacesAddress_eth0 string 10.0.18.224 The IP addresses if resolvable of the interface.

networkInterfacesState_eth1 string up Whether the network interface is up or down.

networkInterfacesState_eth2 string up Whether the network interface is up or down.

networkInterfacesState_eth3 string up Whether the network interface is up or down.

networkInterfacesReceived_eth0 numeric (^37149651815) The number of bytes received by the interface
networkInterfacesReceived_eth1 numeric 51312400000000 The number of bytes received by the interface
networkInterfacesReceived_eth2 numeric 1889020000000 The number of bytes received by the interface


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

networkInterfacesReceived_eth3 numeric 6185320000000 The number of bytes received by the interface

networkInterfacesTransmitted_eth0 numeric 113068000000 The number of bytes sent by the interface

networkInterfacesTransmitted_eth1 numeric 0 The number of bytes sent by the interface

networkInterfacesTransmitted_eth2 numeric 0 The number of bytes sent by the interface

networkInterfacesTransmitted_eth3 numeric (^0) The number of bytes sent by the interface
bandwidthCurrent numeric 341635184
Ingested bandwidth over the last 10 minutes.
Some bandwidth may not be processed due to
system settings.
bandwidthCurrentString string 341.64 Mbps
Ingested bandwidth over the last 10 minutes in a
readable format. Some bandwidth may not be
processed due to system settings.
bandwidthAverage numeric 391242000
Average bandwidth over the last 2 weeks. Some
bandwidth may not be processed due to system
settings.
bandwidthAverageString string 391.24 Mbps
Average bandwidth over the last 2 weeks in a
readable format. Some bandwidth may not be
processed due to system settings.
bandwidth7DayPeak numeric 1230235696
The highest ingested bandwidth observed in any
ten-minute interval over the last 7 days. Some
bandwidth may not be processed due to system
settings.
bandwidth7DayPeakString string 1.23 Gbps
The highest ingested bandwidth observed in any
ten-minute interval over the last 7 days in a
readable format. Some bandwidth may not be
processed due to system settings.
bandwidth2WeekPeak numeric 1645876703
The highest ingested bandwidth observed in any
ten-minute interval over the last 2 weeks. Some
bandwidth may not be processed due to system
settings.
bandwidth2WeekPeakString string 1.65 Gbps
The highest ingested bandwidth observed in any
ten-minute interval over the last 2 weeks in a
readable format. Some bandwidth may not be
processed due to system settings.
processedBandwidthCurrent numeric 15398020 Processed bandwidth over the last 10 minutes.
processedBandwidthCurrentString string 15.40 Mbps
Processed bandwidth over the last 10 minutes in
a readable format.
processedBandwidthAverage numeric 142077169 Average bandwidth over the last 2 weeks.
processedBandwidthAverageString string 142.08 Mbps
Average bandwidth over the last 2 weeks in a
readable format.
processedBandwidth7DayPeak numeric 1139496509
The highest bandwidth observed in any ten-
minute interval over the last 7 days.
processedBandwidth7DayPeakString string 1.14 Gbps
The highest bandwidth observed in any ten-
minute interval over the last 7 days in a readable
format.
processedBandwidth2WeekPeak numeric 1223451790
The highest bandwidth observed in any ten-
minute interval over the last 2 weeks.
processedBandwidth2WeekPeakString string 1.22 Gbps
The highest bandwidth observed in any ten-
minute interval over the last 2 weeks in a
readable format.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

eventsPerMinuteCurrent object

```
An object describing the average number of
events (for each event type) that was processed
in one minute over the last 10-20 minutes. More
detailed information is available from the /
summarystatistics endpoint.
```
eventsPerMinuteCurrent.cSensorNotices numeric 0

```
The number of non-connection events produced
by cSensor devices that were processed per
minute over the last 10-20 minutes.
```
eventsPerMinuteCurrent.cSensorDeviceDe
tails
numeric^0

```
The number of tracking events produced by
cSensor devices that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.cSensorModelEve
nts
numeric 1544

```
The number of modeling events produced by
cSensor devices that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.networkNotices numeric 72

```
The number of non-connection events produced
by network traffic that were processed per
minute over the last 10-20 minutes.
```
eventsPerMinuteCurrent.networkDeviceDe
tails numeric
3

```
The number of tracking events produced by
network traffic that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.networkModelEve
nts
numeric 138614

```
The number of modeling events produced by
network traffic that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.logInputNotices numeric 18

```
The number of non-connection events produced
by syslog ingestion that were processed per
minute over the last 10-20 minutes.
```
eventsPerMinuteCurrent.logInputDeviceD
etails
numeric 0

```
The number of tracking events produced by
syslog ingestion that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.logInputModelEv
ents
numeric 0

```
The number of modeling events produced by
syslog ingestion that were processed per minute
over the last 10-20 minutes.
```
eventsPerMinuteCurrent.saasNotices numeric 0

```
The number of events produced by SaaS
modules that were processed per minute over
the last 10-20 minutes.
```
eventsPerMinuteCurrent.saasModelEvents numeric 0

```
The number of modeling events produced by
SaaS modules that were processed per minute
over the last 10-20 minutes.
```
connectionsPerMinuteCurrent numeric 7745

```
Current number of connections processed in the
last minute - includes ongoing (unfinished)
connections and completed connections.
```
connectionsPerMinuteAverage numeric 8764

```
Average number of connections processed per
minute in the last 2 weeks - includes ongoing
(unfinished) connections and completed
connections.
```
connectionsPerMinute7DayPeak numeric 20975

```
Highest number of connections processed per
minute in the last 7 days - includes ongoing
(unfinished) connections and completed
connections.
```
connectionsPerMinute2WeekPeak numeric 20975

```
Highest number of connections processed per
minute in the last 2 weeks - includes ongoing
(unfinished) connections and completed
connections.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

credentials numeric 86
The number of credentials observed from all
sources over the last 4 weeks.

credentials7Days numeric 55 The number of credentials observed from all
sources over the last 7 days.

credentialSources object

```
An object describing the sources where
credentials were observed from. Sources will
differ depending upon connection make-up and
coverage areas deployed.
```
credentialSources.NTLM object
An object describing the number of credentials
which were seen in NTLM traffic.

credentialSources.NTLM.4weeks numeric 6
The number of credentials observed in NTLM
traffic over the last 4 weeks.

credentialSources.NTLM.7days numeric 4
The number of credentials observed in NTLM
traffic over the last 7 days.

credentialSources.Saas object

```
An object describing the number of credentials
which were observed in event data from
Darktrace/Apps, Cloud or Zero Trust modules.
```
credentialSources.Saas.4weeks numeric 80

```
The the number of credentials which were
observed in event data from Darktrace/Apps,
Cloud or Zero Trust modules over the last 4
weeks.
```
credentialSources.Saas.7days numeric 51

```
The the number of credentials which were
observed in event data from Darktrace/Apps,
Cloud or Zero Trust modules over the last 7 days.
```
operatingSystems numeric 16
The number of operating systems (as derived by
Darktrace) seen over the last 4 weeks.

models numeric 692
The number of active/enabled models on the
system.

modelsBreached numeric 401834

```
This figure represents the number of lifetime
model breaches, unless the instance is explicitly
configured to expire model breaches.
```
modelsSuppressed numeric 1869280

```
This figure represents the number of lifetime
model breaches that have been suppressed,
unless the instance is explicitly configured to
expire model breaches.
```
mostRecentDHCPTraffic string 2023-12-31 14:52:00
The timestamp of the most recent DHCP traffic
across all subnets in UTC.

mostRecentDNSTraffic string 2023-12-31 14:49:00
The timestamp of the most recent DNS traffic
across all subnets in UTC.

mostRecentDCE_RPCTraffic string 2023-12-31 14:50:00
The timestamp of the most recent DCE_RPC
traffic across all subnets in UTC.

mostRecentHTTPTraffic string 2023-12-31 14:52:00
The timestamp of the most recent HTTP traffic
across all subnets in UTC.

mostRecentHTTPSTraffic string 2023-12-31 14:51:00
The timestamp of the most recent HTTPS traffic
across all subnets in UTC.

mostRecentKERBEROSTraffic string 2023-12-31 14:50:00
The timestamp of the most recent Kerberos
traffic across all subnets in UTC.

mostRecentLDAPTraffic string 2023-12-31 14:50:00
The timestamp of the most recent LDAP traffic
across all subnets in UTC.


RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

mostRecentNTPTraffic string 2023-12-31 14:51:00
The timestamp of the most recent NTP traffic
across all subnets in UTC.

mostRecentSMBTraffic string 2023-12-31 14:51:00 The timestamp of the most recent SMB traffic
across all subnets in UTC.

mostRecentSMTPTraffic string 2023-12-31 14:52:00
The timestamp of the most recent SMTP traffic
across all subnets in UTC.

mostRecentSNMPTraffic string 2023-12-31 14:50:00 The timestamp of the most recent SNMP traffic
across all subnets in UTC.

mostRecentSSHTraffic string 2023-12-31 14:51:00
The timestamp of the most recent SSH traffic
across all subnets in UTC.

mostRecentSSLTraffic string 2023-12-31 14:51:00 The timestamp of the most recent SSL traffic
across all subnets in UTC.

VLANs object
An object containing VLANs seen in network
traffic on the instance.

VLANs.1 numeric 0 The number of devices within the specified
VLAN.

internalIPRangeList array 10.0.0.0/8 192.168.0.0/16

internalIPRanges numeric 2 The number of internal IP ranges.

dnsServers numeric 38 The number of devices identified as DNS server.

internalDomains numeric 0 The number of internal domains.

internalAndExternalDomainList array holdingsinc.com example.com

internalAndExternalDomains numeric 2
The number of internally and externally
resolvable domains.

proxyServers numeric 1
The number of proxy servers detected by
Darktrace.

proxyServerIPs array 192.168.72.4:443 The IPs of servers identified as proxy servers.

uptime string 04:55:54
Time since the modelling engine on the instance
was last rebooted.

systemuptime string 1894:29:43 Time since the instance was last rebooted.


###### Example Response

```
{
"excessTraffic": false,
"time": "2023-04-08 10:35",
"installed": "2018-10-22",
"mobileAppConfigured": true,
"version": "5.1.0 (dd351a)",
"ipAddress": "10.0.18.224",
"label": "holdingsinc-master",
"modelsUpdated": "2023-12-26 11:20:48",
"modelPackageVersion": "4.0-8515~20230322143408~g300d5d",
"bundleVersion": "61016",
"bundleDate": "2023-12-24 18:33:59",
"bundleInstalledDate": "2023-12-24 20:20:33",
"hostname": "example-darktrace",
"maximumOSSensors": 255,
"uuid": "07dcf0e5-217b-4e98-96b9-549b3dd87706",
"inoculation": false,
"applianceOSCode": "x",
"license": "2024-12-30 00:00:00",
"saasConnectorLicense": "2029-06-01 00:00:00",
"antigenaSaasLicense": "2029-06-01 00:00:00",
"syslogTLSSHA1Fingerprint": "2D:JY:LP:YT:TF:P3:BJ:21:Q6:D9:OT:JZ:LQ:8A:X0:KG:N6:9P:XC:DI",
"syslogTLSSHA256Fingerprint": "C6:9U:6N:D5:QU:HQ:
78:3P:C4:CN:L3:K2:PI:ZF:BO:MD:GO:Q9:IJ:ED:WD:BD:9Z:18:Z8:UY:34:TQ:HF:AD:P1:C3",
"antigenaNetworkEnabled": true,
"antigenaNetworkConfirmationMode": true,
"antigenaNetworkLicense": "2025-12-31 00:00:00",
"logIngestionReplicated": 326,
"logIngestionProcessed": 464128,
"logIngestionTCP": 2,
"logIngestionUDP": 380126407,
"logIngestionTypes": {
"example-template": 213587,
},
"logIngestionMatches": {
"example-template": 214509,
},
"licenseCounts": {
"saas": {
"total": 0
},
"licenseIPCount": 880,
"licenseCloudIPCount": 12
},
"antigenaNetworkBlockedConnections": {
"attempted": 277149,
"failed": 1333
},
"diskSpaceUsed_": 98,
"type": "master",
"diskUtilization": 1,
"load": 12,
"cpu": 11,
"memoryUsed": 88,
"dataQueue": 0,
"darkflowQueue": 0,
"flowProcessingTimes": {},
"networkInterfacesState_eth0": "up",
"networkInterfacesAddress_eth0": "10.0.18.224",
"networkInterfacesState_eth1": "up",
"networkInterfacesState_eth2": "up",
"networkInterfacesState_eth3": "up",
```
_continued..._


```
"networkInterfacesReceived_eth0": 55947124075,
"networkInterfacesReceived_eth1": 56536073801812,
"networkInterfacesReceived_eth2": 2300453722444,
"networkInterfacesReceived_eth3": 8049757131204,
"networkInterfacesTransmitted_eth0": 172077639292,
"networkInterfacesTransmitted_eth1": 0,
"networkInterfacesTransmitted_eth2": 0,
"networkInterfacesTransmitted_eth3": 0,
"bandwidthCurrent": 367475418,
"bandwidthCurrentString": "367.48 Mbps",
"bandwidthAverage": 120620000,
"bandwidthAverageString": "120.62 Mbps",
"bandwidth7DayPeak": 983743947,
"bandwidth7DayPeakString": "983.74 Mbps",
"bandwidth2WeekPeak": 1184287168,
"bandwidth2WeekPeakString": "1.18 Gbps",
"processedBandwidthCurrent": 18065814,
"processedBandwidthCurrentString": "18.07 Mbps",
"processedBandwidthAverage": 31781225,
"processedBandwidthAverageString": "31.78 Mbps",
"processedBandwidth7DayPeak": 58944496,
"processedBandwidth7DayPeakString": "58.94 Mbps",
"processedBandwidth2WeekPeak": 1139496509,
"processedBandwidth2WeekPeakString": "1.14 Gbps",
"eventsPerMinuteCurrent": {
"cSensorNotices": 0,
"cSensorDeviceDetails": 0,
"cSensorModelEvents": 1311,
"networkNotices": 67,
"networkDeviceDetails": 5,
"networkModelEvents": 143379,
"logInputNotices": 14,
"logInputDeviceDetails": 0,
"logInputModelEvents": 0,
"saasNotices": 0,
"saasModelEvents": 0
},
"connectionsPerMinuteCurrent": 8297,
"connectionsPerMinuteAverage": 5846,
"connectionsPerMinute7DayPeak": 8829,
"connectionsPerMinute2WeekPeak": 20975,
"operatingSystems": 16,
"credentials": 86,
"credentials7Days": 55,
"credentialSources": {
"NTLM": {
"4weeks": 6,
"7days": 4
},
"Saas": {
"4weeks": 80,
"7days": 51
}
},
"models": 695,
"modelsBreached": 403929,
"modelsSuppressed": 1872340,
"devicesModeled": 0,
"mostRecentDHCPTraffic": "2023-04-08 10:34:00",
...
"VLANs": {
"1": 0,
...
```
_continued..._


```
},
"internalIPRangeList": [
"10.0.0.0/8",
"192.168.0.0/16",
],
"internalIPRanges": 2,
"dnsServers": 38,
"internalDomains": 0,
"internalAndExternalDomainList": [
"holdingsinc.com",
"example.com"
],
"internalAndExternalDomains": 2,
"proxyServers": 1,
"proxyServerIPs": [
"192.168.72.4:443",
],
"uptime": "05:12:56",
"systemuptime": "1894:46:44"
}
```
_Response is abbreviated._


## /SUMMARYSTATISTICS

```
/summarystatistics returns simple statistics on device counts, processed bandwidth and the number of active
```
Darktrace RESPOND actions. It can be used for simple NOC monitoring of the instance device counts and processed

bandwidth.

###### Events

There are four categories of events (saas, csensor, network,loginput) and three types (notices,

```
devicedetails, modelevents). Categories refer to the component that produced the event, such as via syslog
```
ingestion or from a Darktrace Client Sensor (cSensor). For types, notices are non-connection events such as SaaS logins,

```
devicedetails are tracking events such as those that change the IP of a device (e.g. DHCP), and modelevents are
```
events associated with modeling (distinct from actual model breaches).

Categories and types can be requested independently, such as:

```
/summarystatistics?eventtype=saas
```
```
/summarystatistics?eventtype=devicedetails
```
Or, combined to request a count of only specific events:

```
/summarystatistics?eventtype=networkdevicedetails
```
Please note, category saas cannot be combined with type devicedetails.

###### MITRE ATT&CK Framework

Darktrace Threat Visualizer 6 introduced a new iteration of the homepage summary which visualizes how vast quantities of

raw events have been distilled by Darktrace analysis, and how these events are relevant to _tactics_ under the MITRE ATT&CK

framework.

- For model breaches and raw events, this data is retrieved from the /summarystatistics endpoint with the
    mitreTactics parameter.
- For AI Analyst, this data is returned in the groupStats.mitreTactics object returned from the
    /aianalyst/stats endpoint.

For more information on the summary panel, please refer to Understanding the Summary Panel (Customer Portal).

###### Request Type(s)

```
[GET]
```

###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
```
eventtype string
Changes the format of data to return numeric event counts for any of the four categories of events and/or
three types (see above).
```
```
endtime numeric
```
```
End time of data to return in millisecond format, relative to midnight January 1st 1970 UTC. Requires
eventtype.
```
```
to string End time of data to return in YYYY-MM-DD HH:MM:SS format. Requires eventtype.
```
```
hours numeric The number of hour intervals from the end time (or current time) to return. Requires eventtype.
```
```
csensor boolean
```
```
When true, only bandwidth statistics are returned for Darktrace/Endpoint cSensor agents. When false,
statistics returned are for Darktrace/Network bandwidth
```
```
mitreTactics boolean
```
```
When true, alters the returned data to display total processed raw events and analysis outputs, broken
down by MITRE ATT&CK Framework tactic.
```
###### Notes

- By default, the endpoint returns 28 days with one interval representing 24 hours.

```
◦ Count values (devicecount,subnets,totalClient, totalServer) are calculated as total unique
values in the last 7 days.
```
```
◦ licenseIPCount is calculated as peak unique IP address values in any 24 hour period in the last 7
days.
```
```
◦ usercredentialcount is calculated as total unique values in the last 28 days.
```
```
◦ patterns is calculated as total unique values in the last 12 weeks.
```
- When the eventtype parameter is used, intervals will represent 1 hour.

```
◦ Both endtime and to are supported when eventtype parameter is used. If an end time is
specified, 28 before the specified date will be returned.
```
```
◦ The hours parameter allows the number of hour intervals to be specified (backwards from the end
time). For example, with to=2021-02-12T12:00:00 and hours=3, 3 intervals: 2021-02-12 09:00:00,
2021-02-12 10:00:00, and 2021-02-12 11:00:00.
```
- Device counts and values returned by this endpoint are affected by visibility restrictions.
- Parameters which modify the response are not compatible with one another, only of of eventtype, csensor
    or mitreTactics may be used.

```
◦ The csensor parameter alters the output to just return time-series bandwidth information for
Darktrace/Endpoint cSensor agents. Please refer to the schema for examples and more detailed
information.
```
```
◦ The new mitreTactics parameter also significantly alters the response from this endpoint - no
device count information is returned if this parameter is used. Please refer to the schema for examples
and more detailed information.
```

###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET the system information displayed on the homepage:

```
https://[instance]/summarystatistics
```
2. GET the number of network traffic device tracking events in 24 hourly intervals from 12pm on February 12th
    2021:

```
https://[instance]/summarystatistics?
eventtype=networkdevicedetails&to=2021-02-12T12:00:00&hours=24
```
###### Example Response

_Request: /summarystatistics_

```
{
"usercredentialcount": 82,
"subnets": 23,
"patterns": 3278640,
"bandwidth": [
{
"timems": 1621528800000,
"time": "2021-05-20 16:40:00",
"kb": 310565202
},
...
{
"timems": 1623861600000,
"time": "2021-06-16 16:40:00",
"kb": 120772918
}
],
"antigenaDevices": 4,
"antigenaActions": 5,
"devicecount": {
"unknown": 7,
"laptop": 6,
"mobile": 1,
...
"saas": {
"Amazon": 3,
"AzureActiveDirectory": 39,
"Box": 2,
...
"total": 135
},
"licenseIPCount": 249,
"totalClient": 285,
"totalServer": 87,
"totalOther": 12,
"total": 519
}
}
```
_Response is abbreviated._


## /SUMMARYSTATISTICS RESPONSE SCHEMA

Darktrace Threat Visualizer 6 adds the new parameters csensor and mitretactics to this endpoint. When true, these

parameters change the format of returned data.

#### Response Schema (no parameters)

Please note, the previous iteration of this article (v5.1 and below) incorrectly identified the time range for the

```
deviceCount object as 28 days.
```
```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
usercredentialcount numeric 448
The number of active credentials seen by the
Darktrace system in the last 28 days.
```
```
subnets numeric 8
The number of active subnets seen by the
Darktrace system in the last seven days.
```
```
patterns numeric 3278640
```
```
Total unique connections, events or activity that
contribute to the overall understanding of your
digital environment over the last 12 weeks.
```
```
bandwidth array
```
```
Bandwidth of traffic ingested by Darktrace over
the last 7 or 28 days in the form of time-series
data.
```
```
bandwidth.timems numeric 1699962000000 Timestamp for the interval of grouped bandwidth
data in epoch time.
```
```
bandwidth.time string 2023-11-14 11:40:00
Timestamp for the interval of grouped bandwidth
data in human readable time.
```
```
bandwidth.kb numeric 109426603 The bandwidth volume ingested during the time
interval.
```
```
antigenaDevices numeric 4
```
```
The number of devices controlled by active
Darktrace RESPOND actions in the last seven
days.
```
```
antigenaActions numeric 5 The number of Darktrace RESPOND actions
triggered and activated in the last seven days.
```
```
devicecount object
An object describing the number of devices seen
in the last seven days.
```
```
devicecount.unknown numeric 6 The number of active devices seen by the
Darktrace system that cannot be categorized.
```
```
devicecount.laptop numeric 14
```
```
The number of active devices categorized
(automatically or manually) as laptops seen by
the Darktrace system.
```
```
devicecount.mobile numeric 8
```
```
The number of active devices categorized
(automatically or manually) as mobile phones
seen by the Darktrace system.
```
```
devicecount.tablet numeric 2
```
```
The number of active devices categorized
(automatically or manually) as tablets seen by the
Darktrace system.
```
```
devicecount.desktop numeric 84
```
```
The number of active devices categorized
(automatically or manually) as desktops seen by
the Darktrace system.
```
```
devicecount.server numeric 71
```
```
The number of active devices categorized
(automatically or manually) as servers seen by
the Darktrace system.
```

RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION

devicecount.router numeric 1

```
The number of active devices categorized
(automatically or manually) as routers seen by
the Darktrace system.
```
devicecount.keyasset numeric 2

```
The number of active devices manually
categorized as key assets seen by the Darktrace
system.
```
devicecount.dnsserver numeric 1

```
The number of active devices categorized
(automatically or manually) as DNS servers seen
by the Darktrace system.
```
devicecount.proxyserver numeric 3

```
The number of active devices categorized
(automatically or manually) as proxy servers seen
by the Darktrace system.
```
devicecount.logserver numeric 2

```
The number of active devices categorized
(automatically or manually) as log servers seen
by the Darktrace system.
```
devicecount.tv numeric 3

```
The number of active devices categorized
(automatically or manually) as internet-
connected TV devices seen by the Darktrace
system.
```
devicecount.camera numeric 2

```
The number of active devices categorized
(automatically or manually) as cameras seen by
the Darktrace system.
```
devicecount.fileserver numeric 4

```
The number of active devices categorized
(automatically or manually) as file servers seen
by the Darktrace system.
```
devicecount.ipphone numeric 2

```
The number of active devices categorized
(automatically or manually) as VoIP phones seen
by the Darktrace system.
```
devicecount.iot numeric 1

```
The number of active devices categorized
(automatically or manually) as IoT devices seen
by the Darktrace system.
```
devicecount.saas object

```
An object describing all SaaS services and the
number of devices created for observed users
for each service.
```
devicecount.saas.Amazon numeric 3
The number of active SaaS devices in the last
seven days for this SaaS service.

devicecount.saas.AzureActiveDirectory numeric 39 The number of active SaaS devices in the last
seven days for this SaaS service.

devicecount.saas.total numeric 135
The number of active devices created from users
of SaaS services seen by the Darktrace system.

devicecount.licenseIPCount numeric 249

```
The peak value of the number of distinct internal
(not excluded) IP addresses seen within any 24
hour period over the last seven days. Does not
overlap with licenseCloudIPCount.
```
devicecount.licenseCloudIPCount numeric 12

```
The peak value of the number of distinct internal
(not excluded) IP addresses seen in a cloud
VLAN within any 24 hour period over the last
seven days. IP addresses will be located in cloud
VLANs if created from Darktrace Cloud Security
flow log ingestion, or created from traffic
observed by a compatible Darktrace vSensor.
Does not overlap with licenseIPCount.
```

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
devicecount.totalClient numeric 106
The total number of active server devices seen
by the Darktrace system in the last seven days.
```
```
devicecount.totalServer numeric 20 The total number of active server devices seen
by the Darktrace system.
```
```
devicecount.totalOther numeric 6
```
```
The total number of active devices performing
other operations seen by the Darktrace system in
the last seven days.
```
```
devicecount.total numeric 204
Total number of active devices seen by the
Darktrace system in the last seven days.
```
###### Example Response

_Request:_ /summarystatistics_

```
{
"usercredentialcount": 82,
"subnets": 23,
"patterns": 3278640,
"bandwidth": [
{
"timems": 1699962000000,
"time": "2023-11-14 11:40:00",
"kb": 116493095
},
{
"timems": 1700048400000,
"time": "2023-11-15 11:40:00",
"kb": 455956196
},
{
"timems": 1700134800000,
"time": "2023-11-16 11:40:00",
"kb": 100218987
},
...
],
"antigenaDevices": 4,
"antigenaActions": 5,
"devicecount": {
"unknown": 7,
"laptop": 6,
"mobile": 1,
...
"saas": {
"Amazon": 3,
"AzureActiveDirectory": 39,
"Box": 2,
...
"total": 135
},
"licenseIPCount": 249,
"licenseCloudIPCount": 1,
"totalClient": 285,
"totalServer": 87,
"totalOther": 12,
"total": 519
}
}
```
_Response is abbreviated._


#### Response Schema - eventtype=loginput

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
events boolean TRUE A system field.
```
```
data array
```
```
An array of numeric counts of events in the
specified event type in the form of time-series
data.
```
```
data.timems numeric 1617105600000
Timestamp for the interval of grouped event data
in epoch time.
```
```
data.time string 2021-03-30 12:00:00
Timestamp for the interval of grouped event data
in human readable time.
```
```
data.events numeric 2736675 The number of events in the interval.
```
###### Example Response

```
{
"events": true,
"data": [
{
"timems": 1617105600000,
"time": "2021-03-30 12:00:00",
"events": 2736675
},
{
"timems": 1617109200000,
"time": "2021-03-30 13:00:00",
"events": 2859475
},
...
]
}
```
_Response is abbreviated._

#### Response Schema - csensor=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
csensor boolean true
If true, indicates the bandwidth values are
for Darktrace/Endpoint cSensor agents.
```
```
bandwidth array
```
```
Bandwidth of traffic ingested by Darktrace/Endpoint
cSensor agents over the last seven days in the form of time-
series data.
```
```
bandwidth.timems numeric 1666265400000
```
```
Timestamp for the interval of grouped
bandwidth data in epoch time.
```
```
bandwidth.time string 2022-10-20 11:30:00
Timestamp for the interval of grouped
bandwidth data in human readable time.
```
```
bandwidth.kb numeric 136233222
The bandwidth volume ingested during
the time interval.
```

```
{
"csensor": true,
"bandwidth": [
{
"timems": 1666265400000,
"time": "2022-10-20 11:30:00",
"kb": 136233222
},
...
{
"timems": 1668598200000,
"time": "2022-11-16 11:30:00",
"kb": 1441805
}
]
}
```
_Response is abbreviated._

#### Response Schema - mitretactics=true

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
mitreTactics array
```
```
An array of MITRE ATT&CK Framework tactics and events and model
breaches relevant to those tactics over the time period.
```
```
mitreTactics.tactic string credential-access A system name for the MITRE ATT&CK Framework tactic.
```
```
mitreTactics.name string Credential Access A human readable name for the MITRE ATT&CK Framework tactic.
```
```
mitreTactics.totalCount numeric 96334873
```
```
For each tactic, the number of events that were relevant to the type of
activity the tactic encompasses - and therefore were evaluated by the
Darktrace model engine - over the time period.. Tactics are not mutually
exclusive; the same activity may be relevant to, and been evaluated for,
multiple tactics.
```
```
mitreTactics.scoreCount numeric 437859 A system field.
```
```
mitreTactics.modelEstimate numeric 441
```
```
The estimated number of model breaches that would be created for
models relevant to this MITRE ATT&CK tactic if Darktrace AI-powered
analysis was not taken into account by the modeling engine.
```
```
mitreTactics.modelCount numeric 2
```
```
Darktrace default models are mapped to relevant MITRE ATT&CK
Framework techniques and tactics. For each tactic, the number of model
breaches triggered for mapped models over the time period.
```
```
modelCount numeric 13225 The total count of model breach events over the time period.
```
```
startTime numeric 1666266000000
The starttime in epoch time for the time window statistics are calculated
over. This is approximately 28 days in the majority of cases.
```
```
totalCount numeric 1019722951
The total number of raw events that were passed to Darktrace modeling
for further investigation over the last 28 days.
```

```
{
"mitreTactics": [
{
"tactic": "credential-access",
"name": "Credential Access",
"totalCount": 20056347,
"scoreCount": 2139944,
"modelEstimate": 38,
"modelCount": 4
},
...
{
"tactic": "lateral-movement",
"name": "Lateral Movement",
"totalCount": 99761956,
"scoreCount": 71360,
"modelEstimate": 438975,
"modelCount": 314
}
],
"modelCount": 5104,
"startTime": 1666267200000,
"totalCount": 113931648
}
```
_Response is abbreviated._


## /TAGS

The /tags endpoint allows tags to be controlled programmatically - tags can be reviewed, created or deleted via the API.

Tags which are restricted or referenced by model components cannot be deleted.

Tags applied to a device can be controlled by the /tags/entities and /tags/[tid]/entities extensions.

```
POST requests to this endpoint must be made in JSON format. Parameters are not supported.
```
As of Darktrace Threat Visualizer 5.2, POST and DELETE requests now require the “Edit Tags” permission. This

permission is automatically granted to users with the “Visualizer” or “SaaS Console” permission on upgrade to 5.2.

Global tokens generated on the System Config page should possess this permission automatically.

###### Request Type(s)

```
[GET] [POST] [DELETE]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
tag string The name of an existing tag
```
```
name string A name for the created tag. POST requests in JSON format only.
```
```
color numeric
The hue value (in HSL) used to color the tag in the Threat Visualizer user interface. POST requests in JSON
format only.
```
```
description string An optional description for the tag. POST requests in JSON format only.
```
```
responsedata string When given the name of a top-level field or object, restricts the returned JSON to only that field or object.
```
###### Notes

- /tags returns the details for all current tags. An individual tag can be references either by using the tag
    parameter and its name, or using the tid as an extension.
- The minimum requirements for a POST to create a new tag are the name parameter and an empty data
    object. description and color are optional but highly recommended.
- Tags with :: in the name format are treated as _scoped_. Scoped tags take the format [a]::[b], where a is
    the value used to determine the scope and b can be any text.

```
Scoped tags are mutually exclusive; only one tag of a specific scope can be present on a device at once.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET all details for ‘Active Threat’ tag:

```
https://[instance]/tags/5
```
```
https://[instance]/tags?tag=active threat
```
```
If using cUrl, ensure the space is percent-encoded when making the final request
```

2. POST to create a new tag called “Suspicious Behavior”:

```
https://[instance]/tags with body {"name":"Suspicious Behavior","data":
{"description":"Device is behaving suspiciously","color":100}}
```
3. DELETE the tag “Temporary Tag” which has tid=89:

```
https://[instance]/tags/89
```
###### Example Response

_Request: /tags/24_

```
{
"tid": 24,
"expiry": 0,
"thid": 24,
"name": "DNS Server",
"restricted": false,
"data": {
"auto": false,
"color": 112,
"description": "Devices receiving and making DNS queries",
"visibility": "Public"
},
"isReferenced": true
}
```

## /TAGS RESPONSE SCHEMA

This article previously covered /tags and /tags/entities. /tags/entities can now be found in

_/tags/entities and /tags/[tid]/entities Response Schema_

#### Response Schema

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
tid numeric 5 The “tag id”. A unique value.
```
```
expiry numeric 0 The default expiry time for the tag when applied
to a device.
```
```
thid numeric 5
The “tag history” id. Increments if the tag is
edited.
```
```
name string Active Threat The tag label displayed in the user interface or in
objects that reference the tag.
```
```
restricted boolean FALSE
Indicates a read-only tag - these tags can only be
modified or applied by Darktrace.
```
```
data object An object containing information about the tag.
```
```
data.auto boolean FALSE Whether the tag was auto-generated.
```
```
data.color numeric 200
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.
```
```
data.description string
```
```
A tag indicating
the device is
behaving
anomalously and
potentially
compromised.
```
```
An optional description summarizing the
purpose of the tag.
```
```
data.visibility string Public A system field.
```
```
isReferenced boolean TRUE
Whether the tag is used by one or more model
components.
```
#### Example Response

_Request: /tags/24_

```
{
"tid": 24,
"expiry": 0,
"thid": 24,
"name": "DNS Server",
"restricted": false,
"data": {
"auto": false,
"color": 112,
"description": "Devices receiving and making DNS queries",
"visibility": "Public"
},
"isReferenced": true
},
```

## /TAGS/ENTITIES

The /tags/entities has two forms - /tags/entities and /tags/[tid]/entities, where tid is the ID of a

specific tag.

```
/tags/[tid]/entities/ can be used to list the devices for a specific tag or add that specific tag to one or more entities.
```
_This endpoint uses different parameters and only supports JSON-format data in POST requests. This endpoint is covered_

_separately in_ tags/[tid]/entities.

```
/tags/entities can be used to list the devices for a tag, list the tags for a device, add a tag to a device or remove a tag
```
from a device.

A valid GET request must include either a did or a tag parameter. POST requests to this endpoint must be made with

parameters. JSON is not supported.

As of Darktrace Threat Visualizer 5.2, POST and DELETE requests now require the “Edit Tags” permission. This

permission is automatically granted to users with the “Visualizer” or “SaaS Console” permission on upgrade to 5.2.

Global tokens generated on the System Config page should possess this permission automatically.

###### Request Type(s)

```
[GET] [POST] [DELETE]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
did numeric Identification number of a device modelled in the Darktrace system.
```
```
duration numeric How long the tag should be set for the device. The tag will be removed once this duration has expired.
```
```
tag string The name of an existing tag
```
```
responsedata string
When given the name of a top-level field or object, restricts the returned JSON to only that field or
object.
```
```
fulldevicedetails boolean
```
```
When true and a tag is queried, adds a devices object to the response with more detailed device
data.
```
###### Example Request

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

1. GET the current tags for the device with did=1:

```
https://[instance]/tags/entities?did=1
```
2. DELETE the ‘Guest’ tag from device with did=1:

```
https://[instance]/tags/entities?tag=Guest&did=1
```
3. POST the ‘Active Threat’ tag for one hour on a device with did=1:

```
https://[instance]/tags/entities with body "tag=Active Threat&did=1&duration=3600"
```

_If using cUrl, ensure the space is percent-encoded when making the final request_

###### Example Response

_Request: /tags/entities?did=1_

```
[
{
"tid": 22,
"expiry": 0,
"thid": 22,
"name": "Admin",
"restricted": false,
"data": {
"auto": false,
"color": 200,
"description": "",
"visibility": ""
},
"isReferenced": true
},
{
"tid": 131,
"expiry": 0,
"thid": 62,
"name": "Re-Activated Device",
"restricted": false,
"data": {
"auto": false,
"color": 142,
"description": "A device that has been inactive for at least 4 weeks has re-appeared
on the network in the past 48 hours.",
"visibility": "Public"
},
"isReferenced": true
}
]
```

## /TAGS/[TID]/ENTITIES

The /tags/entities has two forms - /tags/entities and /tags/[tid]/entities, where tid is the ID of a

specific tag.

```
/tags/entities can be used to list the devices for a tag, list the tags for a device, add a tag to a device or remove a tag
```
_from a device. This endpoint was covered in_ /tags/[tid]/entities_._

```
/tags/[tid]/entities/ can be used to list the devices for a specific tag or add that specific tag to one or more entities
```
( _device_ or _credential_ ).

For POST requests, this endpoint uses different parameters (entityType and entityValue) and only supports JSON-

format data. Tags can be applied to multiple entities using an array of device ids (did) or credential values.

###### DELETE Requests

Tags can also be deleted from this endpoint using the teid - tag entity ID value - that represents the tag-to-entity

relationship. This value appears in the data returned from a GET request to this endpoint, and in the response when a tag is

added using this endpoint.

This should be formatted as a DELETE request to the URL /tags/[tid]/entities/[teid]. For example, for the

following response from /tags/1/entities:

```
{
"teid": 12345,
"tehid": 12345,
"tid": 1,
"entityType": "Device",
"entityValue": "1000",
"valid": true
}
```
This tag can be removed by a DELETE request to /tags/1/entities/12345

###### Request Type(s)

```
[GET] [POST] [DELETE]
```
###### Parameters

```
PARAMETER TYPE DESCRIPTION
```
```
entityType string The type of entity to be tagged. Valid values are Device and Credential.
```
```
entityValue string
```
```
For devices, the numeric did (device id) value for the entities (as a string). For credentials, the
credential value. Also accepts an array. Valid for POST requests only.
```
```
expiryDuration numeric Optional duration the tag should be applied for in seconds. Valid for POST requests only.
```
```
responsedata string
```
```
When given the name of a top-level field or object, restricts the returned JSON to only that field or
object. Valid for GET requests only.
```
```
fulldevicedetails boolean
When true and a tag is queried, adds a devices object to the response with more detailed device
data. Valid for GET requests only.
```

###### Notes

- The tid value for a tag can be retrieved from the /tags endpoint.
- The teid - tag entity ID value - required for DELETE requests can be retrieved from this endpoint, or observed
    in the response when a tag is added.

###### Example Requests

```
[instance] in the following examples may be replaced with the instance IP or FQDN - for example, https://10.0.0.1
```
or https://euw1-1234-01.cloud.darktrace.com

“Value for Signature Generation” represents the combined endpoint and request values that must be used to generate

the DTAPI-Signature value.

1. GET the current devices tagged with tag tid 1:

```
https://[instance]/tags/1/entities
```
2. POST the ‘Guest’ tag (tid: 1) to the devices with did 1, 2 and 4:

```
https://[instance]/tags/1/entities with body {"entityType":"Device","entityValue":
["1","2","4"]}
```
3. POST the ‘Guest’ tag (tid: 1) to the credential benjamin.ash for 1 hour:

```
https://[instance]/tags/1/entities with body
{"entityType":"Credential","entityValue":"benjamin.ash","expiryDuration":3600}
```
4. DELETE the ‘Guest’ tag (tid: 1) from a device. The teid of the tag-to-device relationship is 325614 :

```
https://[instance]/tags/1/entities/325614
```
###### Example Response

_Request: /tags/123/entities_


[
{
"teid": 325684,
"tehid": 325684,
"tid": 123,
"entityType": "Credential",
"entityValue": "b.ash@holdingsinc.com",
"valid": true,
"expiry": 1702038492000
},
{
"teid": 325614,
"tehid": 325614,
"tid": 123,
"entityType": "Device",
"entityValue": "400",
"valid": true
},
{
"teid": 325615,
"tehid": 325615,
"tid": 123,
"entityType": "Device",
"entityValue": "500",
"valid": true
}
]


## /TAGS/ENTITIES AND /TAGS/[TID]/ENTITIES

## RESPONSE SCHEMA

This article covers both /tags/entities and /tags/[tid]/entities. For /tags, please see

_/tags Response Schema_.

#### /tags/entities

When did is used, the response mirrors /tags. When a tag value is used, the output mirrors tags/[tid]/entities.

###### Response Schema - tag=High%20Risk

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
teid numeric 325684
The tag entity ID value, an ID which represents the tag-to-entity relationship.
Used in DELETE requests to remove the tag from the device.
```
```
tehid numeric 325684 The tag entity history id. A system field.
```
```
tid numeric 12 The “tag id”. A unique value.
```
```
entityType string Credential
The type of entity the tag is applied to. Valid values include “device” and
“credential”.
```
```
entityValue string b.ash@holdingsinc.com
The entity identifier. For devices, the did value. For credentials, the
credential value.
```
```
valid boolean TRUE A system field.
```
```
expiry numeric 1702038492000
The expiry time for the tag applied to the device or credential currently.The
“tag history” id. Increments if the tag is edited.
```
###### Example Response

_Request: /tags/entities?tag=High%20Risk_

```
[
{
"teid": 325684,
"tehid": 325684,
"tid": 24,
"entityType": "Credential",
"entityValue": "b.ash@holdingsinc.com",
"valid": true,
"expiry": 1702038492000
},
{
"teid": 325615,
"tehid": 325615,
"tid": 24,
"entityType": "Device",
"entityValue": "123",
"valid": true
}
]
```

###### Response Schema - tag=High%20Risk&fulldevicedetails=true

```
KEY TYPE VALUE DESCRIPTION
```
```
entities array An array containing tagged device or credential objects.
```
```
entities.teid numeric 325684
The tag entity ID value, an ID which represents the tag-to-entity relationship.
Used in DELETE requests to remove the tag from the device.
```
```
entities.tehid numeric 325684 The tag entity history id. A system field.
```
```
entities.tid numeric 12 The “tag id”. A unique value.
```
```
entities.entityType string Credential
The type of entity the tag is applied to. Valid values include “device” and
“credential”.
```
```
entities.entityValue string b.ash@holdingsinc.com
The entity identifier. For devices, the did value. For credentials, the
credential value.
```
```
entities.valid boolean TRUE A system field.
```
```
entities.expiry numeric 1702038492000
The time at which the tag will expire and be removed from the device or
credential.
```
```
devices array
```
```
An array of device objects in the standard, expanded format. For more details,
see the /devices endpoint schema where includetags=true.
```
###### Example Response

_Request: /tags/entities?tag=High%20Risk&fulldevicedetails=true_


{
"entities": [
{
"teid": 325684,
"tehid": 325684,
"tid": 12,
"entityType": "Credential",
"entityValue": "b.ash@holdingsinc.com",
"valid": true,
"expiry": 1702038492000
},
...
{
"teid": 325615,
"tehid": 325615,
"tid": 12,
"entityType": "Device",
"entityValue": "4841",
"valid": true
}
],
"devices": [
{
"did": 4841,
"sid": -9,
"saasmodule": "Office365",
"hostname": "SaaS::Office365: benjamin.ash@holdingsinc.com",
"firstSeen": 1683885806000,
"lastSeen": 1702040409000,
"typename": "saasprovider",
"typelabel": "SaaS Provider",
"credentials": [
{
"lastSeen": 1702040409000,
"credential": "benjamin.ash@holdingsinc.com"
}
],
"tags": [
{
"tid": 12,
"expiry": 0,
"thid": 12,
"name": "High Risk",
"restricted": false,
"data": {
"auto": false,
"color": 112,
"description": "A tag indicating the device is behaving anomalously and
potentially compromised",
"visibility": "Public"
},
"isReferenced": true
}
],
"customFields": {
...}
}
}
...
]
}


###### Response Schema /tags/entities?did=4841

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
tid numeric 12 The “tag id”. A unique value.
```
```
thid numeric 5
The “tag history” id. Increments if the tag is
edited.
```
```
expiry numeric
The time at which the tag will expire and be
removed from the device.
```
```
name string Active Threat
The tag label displayed in the user interface or in
objects that reference the tag.
```
```
restricted boolean FALSE
Indicates a read-only tag - these tags can only be
modified or applied by Darktrace.
```
```
data object An object containing information about the tag.
```
```
data.auto boolean FALSE Whether the tag was auto-generated.
```
```
data.color numeric 200
The hue value (in HSL) used to color the tag in
the Threat Visualizer user interface.
```
```
data.description string
```
```
A tag indicating
the device is
behaving
anomalously and
potentially
compromised.
```
```
An optional description summarizing the
purpose of the tag.
```
```
isReferenced boolean TRUE
Whether the tag is used by one or more model
components.
```
###### Example Response

_Request: /tags/entities?did=4841_

```
[
{
"tid": 12,
"thid": 39,
"name": "High Risk",
"restricted": false,
"data": {
"auto": false,
"color": 112,
"description": "A tag indicating the device is behaving anomalously and potentially
compromised",
"visibility": "Public"
},
"isReferenced": true
},
{
"tid": 531,
"thid": 538,
"name": "Global Admin (CG)",
"restricted": false,
"data": {
"color": 100,
"description": "(SaaS) This device has global admin privileges. This tag is
automatically applied to and removed from devices."
},
"isReferenced": false
}
]
```

#### /tags/[tid]/entities

###### Response Schema

This response is the same as that returned by /tags/entities/tag=High%20Risk.

```
RESPONSE FIELD TYPE EXAMPLE VALUE DESCRIPTION
```
```
teid numeric 325684
The tag entity ID value, an ID which represents the tag-to-entity relationship.
Used in DELETE requests to remove the tag from the device.
```
```
tehid numeric 325684 The tag entity history id. A system field.
```
```
tid numeric 12 The “tag id”. A unique value.
```
```
entityType string Credential
The type of entity the tag is applied to. Valid values include “device” and
“credential”.
```
```
entityValue string b.ash@holdingsinc.com
```
```
The entity identifier. For devices, the did value. For credentials, the
credential value.
```
```
valid boolean TRUE A system field.
```
```
expiry numeric 1702038492000 The expiry time for the tag applied to the device or credential currently.
```
###### Example Response

_Request: /tags/24/entities_

```
[
{
"teid": 325684,
"tehid": 325684,
"tid": 12,
"entityType": "Credential",
"entityValue": "b.ash@holdingsinc.com",
"valid": true,
"expiry": 1702038492000
},
{
"teid": 325615,
"tehid": 325615,
"tid": 12,
"entityType": "Device",
"entityValue": "123",
"valid": true
}
]
```
###### fulldevicedetails=true

See /tags/entities/tag=High%20Risk?fulldevicedetails=true above.


## APPENDIX: DARKTRACE THREAT VISUALIZER API

## GUIDE CHANGELOG

###### Darktrace 6.1

The following changes have been made to Darktrace Threat Visualizer API documentation for 6.1:

- Endpoint permission requirements have been updated to reflect new endpoints and capabilities added in this
    release.
- API authentication examples have been updated to use more recent dates.
- It is now possible to POST to the /advancedsearch/api/search endpoint for queries of greater length.
- New endpoints have been added to the list of current Darktrace/Email API endpoints available. Please refer to
    the API documentation available from the Email Console for more details on how to access and query these
    endpoints.
- A note about the sender field and impact upon the triggerDid field have been added to the
    /aianalyst/groups and /aianalyst/incidentevents endpoint documentation.
- The new aianalyst/investigations endpoint has added. This endpoint allows users to trigger custom AI
    Analyst investigations and review the status of ongoing or concluded investigations.
- A section on the blockedconnections parameter has been added to the /details endpoint
    documentation.
- The /devicesearch endpoint can now be time restricted with the seensince parameter.
- The example provided for /devicesearch has been corrected to remove reference to the devices.id key,
    which does not return from this endpoint.
- The default count value for the /devicesearch endpoint has been raised to 100. The maximum value (300)
    has also been documented.
- Two new parameters have been added to the /devices endpoint - cloudsecurity and saasfilter. The
    former restricts devices to those relevant to Darktrace Cloud Security. The latter allows returned devices to be
    filtered by a wildcard match against any Darktrace/Apps, Cloud and Zero Trust module. Usage notes and
    examples have been added for clarity.
- The /devices endpoint type parameter description has been amended to reflect that /enums no longer
    supports /enums/[category].
- References to the use of category extensions on the /enums endpoint have been revised to suggest the use
    of the responsedata parameter.
- For /modelbreaches, the creationTime and saasfilter parameters have been documented. The
    saasfilter parameter allows returned model breaches to be filtered by a wildcard match against any
    Darktrace/Apps, Cloud and Zero Trust module. Usage notes and examples for both parameters have been
    added for clarity.
- A note on the usage of pid vs uuid has been added to the /modelbreaches and /models endpoints.
- The new /tags/[tid]/entities endpoint has been added. This endpoint allows tags to be added to
    multiple entities at once, and supports tagging of credential entities.
- The documentation for the /tags and /tags/entities endpoints now reference the recommended use of
    /tags/[tid]/entities.


- The AI Analyst summariser field, which appears across multiple endpoints, is now documented in greater

```
detail in the relevant response schemas.
```
- Schemas for the /aianalyst/groups and /aianalyst/incidentevents endpoints now include the

```
sender field, which is populated for incident events created from Darktrace/Email activity.
```
- Schema added for the new /aianalyst/investigations endpoint.
- /details endpoint schema now has examples and schemas for Darktrace RESPOND blockedConnections

```
notices.
```
- User device example for /devicesearch endpoint displaying new devices.saasmodule field, observable

```
on multiple endpoints.
```
- Clarification in /devices endpoint schema added to indicate which fields are unique to this endpoint vs when

```
device objects are retrieved from other endpoints.
```
- Additional information has been added to the /devices endpoint schema on the presence of

```
generatedLabel and new Darktrace/Endpoint fields aghpublicip, aghasn and aghcountry.
```
- The /models endpoint schema now includes the history.accepted and history.acceptedBy fields

```
which are added when automatic model updates are accepted. The description for history.defeatsOnly
has also been amended.
```
- For /modelbreaches, added new percentScore field to all schema examples and corrected descriptions

```
for time and creationTime fields.
```
- Documented icsDevices field for the /subnets endpoint schema which is observable in Darktrace

```
DETECT/OT environments.
```
- The new response field - licenseCloudIPCount - is now documented for responses from the

```
/summarystatistics and /status endpoints.
```
- The /status schema now includes previously undocumented fields label, uuid and

```
maximumOSSensors.
```
- Credential count and credential source data examples are now provided for /status.
- New /status schema logIngestionMatches and logIngestionTypes objects provide detailed log input

```
processing information.
```
- Example probe data for /status now includes metadata, which is populated for compatible vSensors.
- The experimental antigenaNetworkBlockedConnections object is now referenced in the /status

```
schema.
```
- The /tags and /tags/entities schemas have been split. /tags/entities is now defined separately in a

```
joint schema with the new tags/[tid]/entities endpoint.
```

US:+1 415 229 9100 UK:+44 (0) 1223 394 100 LATAM:+55 11 4949 7696 APAC:+65 6804 5010 info@darktrace.com darktrace.com