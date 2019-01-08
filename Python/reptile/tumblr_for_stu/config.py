# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'o25lc4XecQpXpoEIhoUu8AD2MMmQu3xXJLm9J6n2z6XH3wqwUK',
  'uD4EVD7rHG2iGYkWrxY6diZLTkd3WhjuCGrc8zryL731whXBb5',
  '8coTZoxNQSNzwpB2h60w3A8iNnzt7PhrxtK59vQd57zWfpCNqi',
  'mKoZEtvRWhU8ahmBt5iX9Z1lCXeM5xQeu9CaumZHcUPUthU30e'
)

# Make the request
client.info()