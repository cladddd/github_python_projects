import requests
from datetime import datetime

def fetch_python_projects():
    # GitHub API endpoint to search for Python projects created today
    url = "https://api.github.com/search/repositories"
    
    # Define today's date in ISO 8601 format (YYYY-MM-DD)
    today_date = datetime.now().strftime("%Y-%m-%d")
    
    # Define query parameters
    params = {
        "q": f"language:python created:{today_date}",
        "sort": "stars",
        "order": "desc"
    }

    # Send GET request to GitHub API
    response = requests.get(url, params=params)
    
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        return data.get('items', [])
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

def save_projects_to_file(projects, filename):
    with open(filename, 'w') as f:
        for project in projects:
            f.write(f"Name: {project['name']}\n")
            f.write(f"Description: {project['description']}\n")
            f.write(f"Stars: {project['stargazers_count']}\n")
            f.write(f"URL: {project['html_url']}\n")
            f.write("\n")

if __name__ == "__main__":
    python_projects = fetch_python_projects()
    if python_projects:
        save_projects_to_file(python_projects, "python_projects.txt")
        print("Python projects saved to python_projects.txt")
    else:
        print("No Python projects found today.")
