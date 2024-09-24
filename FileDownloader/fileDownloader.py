import requests


def download_file(url, file_name):
    '''
    Download a file from the provided URL and save it locally.
    '''
    file_name = f"{file_name}.{url.split('.')[-1].lower()}"

    # Send a GET request to the provided URL
    response = requests.get(url) 
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file '{file_name}'.")
        print(f"Status code: {response.status_code}")


# to test and debug the code
if __name__ == "__main__":
    url = 'https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-1024.png'
    download_file(url, "python_logo")
     
    