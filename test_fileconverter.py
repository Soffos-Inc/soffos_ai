from soffos import Client, Services


api_key = "Token a1739a8f-c2cf-45e0-9bb1-0fd88beb717d"

ai_client = Client(api_key)

ai_client.user = "b5601df8-6af3-4c1a-9ded-b7df4c506eab"
ai_client.service = Services.FILE_CONVERTER
ai_client.src = 'Epidemiology.docx'
ai_client.normalize = 0
response = ai_client.get_response()
print(ai_client.response)
print(ai_client.raw_response)