import requests
pixella_endpoint="https://pixe.la/v1/users"
USERNAME="test4"
TOKEN="THISISSECRET4"
user_params={
    "token":"THISISSECRET4",
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
graph_endpoint=f"{pixella_endpoint}/{USERNAME}/graphs"
 
#response=requests.post(url=pixella_endpoint,json=user_params)

graph_config={
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}
header={
    "X-USER-TOKEN":TOKEN
}
response=requests.post(url=graph_endpoint,json=graph_config,headers=header)
print(response.text)