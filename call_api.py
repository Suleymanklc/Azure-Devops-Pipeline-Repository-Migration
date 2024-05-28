import requests
import base64
import vars
import json


def get_project_id():
    url = f"{vars.build_api_organization_url}/_apis/projects/"
    projects = http_call(url)
    for project in projects['value']:
        if project['name'] == vars.project_name:
            return project['id']
    return None


def has_attribute(data, attribute):
    keys = attribute.split('.')
    for key in keys:
        if key in data:
            data = data[key]
        else:
            return False
    return True


def get_headers():
    return {
        'Authorization': 'Basic ' + base64.b64encode(b':' + vars.personal_access_token.encode()).decode(),
        'Content-Type': 'application/json'
    }


def update_repository_data(data, rollback):
    if rollback:
        data["repository"]["url"] = vars.repo_url
        data["repository"]["name"] = vars.repo_name
        data["repository"]["id"] = vars.repo_id
        if has_attribute(data, 'repository.properties.cloneUrl'):
            data["repository"]["properties"]["cloneUrl"] = vars.repo_url
        if has_attribute(data, 'repository.properties.fullName'):
            data["repository"]["properties"]["fullName"] = vars.repo_name
        if has_attribute(data, 'repository.properties.safeRepository'):
            data["repository"]["properties"]["safeRepository"] = vars.repo_id
    else:
        data["repository"]["url"] = vars.infraRepoUrl
        data["repository"]["name"] = vars.infraRepoName
        data["repository"]["id"] = vars.infraRepoId
        if has_attribute(data, 'repository.properties.cloneUrl'):
            data["repository"]["properties"]["cloneUrl"] = vars.infraRepoUrl
        if has_attribute(data, 'repository.properties.fullName'):
            data["repository"]["properties"]["fullName"] = vars.infraRepoName
        if has_attribute(data, 'repository.properties.safeRepository'):
            data["repository"]["properties"]["safeRepository"] = vars.infraRepoId
    return data


def update_build_artifact(url, rollback):
    headers = get_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    data = update_repository_data(data, rollback)
    print(data["repository"])
    try:
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
    except Exception as e:
        e.with_traceback()


def update_release_artifact(definition_url, rollback):
    headers = get_headers()
    response = requests.get(definition_url, headers=headers)
    response.raise_for_status()
    data = response.json()
    data["source"] = 'restApi'

    for artifact in data["artifacts"]:
        if vars.repo_id in artifact["definitionReference"]["definition"]["id"]:
            if rollback:
                artifact["alias"] = vars.repo_name
                artifact["definitionReference"]["definition"]["id"] = vars.repo_id
                artifact["definitionReference"]["definition"]["name"] = vars.repo_name
            else:
                artifact["alias"] = vars.infraRepoName
                artifact["definitionReference"]["definition"]["id"] = vars.infraRepoId
                artifact["definitionReference"]["definition"]["name"] = vars.infraRepoName

    try:
        response = requests.put(vars.release_definitions_url, headers=headers, json=data)
        response.raise_for_status()
    except Exception as e:
        e.with_traceback()


def list_pipelines(url):
    return http_call(url)['value']


def http_call(url):
    headers = get_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
