# first test
import requests

# Authentication credentials
data = {
    'username': 'your_username',
    'password': 'your_password'
}

# URL to obtain the JWT token
auth_url = 'http://localhost:8000/api/token/'

# Make a POST request to get the JWT token
response = requests.post(auth_url, data=data)

# Check if the authentication was successful
if response.status_code == 200:
    # Extract the JWT token
    token = response.json().get('access')

    # Print the obtained token
    print('JWT Token:', token)
else:
    print('Authentication failed:', response.status_code)




# SUCCESSSSS







#second test jwt

# Authentication details
username = 'your_username'
password = 'your_password'

# API endpoints
token_url = 'http://localhost:8000/api/token/'  # Replace with your token endpoint
post_endpoint = 'http://localhost:8000/cashier/products/'  # Replace with your POST endpoint

# Payload for obtaining token
auth_payload = {
    'username': username,
    'password': password,
}

# Obtain JWT token and post
response = requests.post(token_url, data=auth_payload)
if response.status_code == 200:
    token = response.json().get('access')
    print(f"JWT Token: {token}")

    # Using the obtained token in the header for the POST request
    headers = {'Authorization': f'Bearer {token}'}

    # Payload for the POST request
    product_payload = {
        'name': 'Sample Product',
        'price': 10.99,
        'stock': 100,
    }

    # Make the POST request
    post_response = requests.post(post_endpoint, json=product_payload, headers=headers)
    print(post_response.json())  # Prints the response from the POST request
else:
    print("Failed to obtain JWT token")




# SUCCESSSSS





#third test get

# JWT Token obtained from the previous authentication
jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwOTk4MTU2LCJpYXQiOjE3MDA5OTQ1NTYsImp0aSI6IjExMWM4YzQ4OGVkYjRmOTg5M2QxMzRkMDNhNzEzZDc1IiwidXNlcl9pZCI6Mn0.OQe4OWK4uIy02YS_uynPEqO7rqcpBwY9cLWLCx1ZSJc'

# API endpoint for fetching products
get_endpoint = 'http://localhost:8000/cashier/products/'  # Replace with your GET endpoint

# Headers with JWT token
headers = {'Authorization': f'Bearer {jwt_token}'}

# Perform a GET request
response = requests.get(get_endpoint, headers=headers)

if response.status_code == 200:
    products = response.json()
    print("Products:")
    print(products)
else:
    print("Failed to fetch products")
