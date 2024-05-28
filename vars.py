import call_api
personal_access_token = ''
build_api_organization_url = 'https://dev.azure.com//'
release_api_organization_url = 'https://vsrm.dev.azure.com//'
project_name = ""
repo_id = ''
repo_name = 'Deployments'
repo_url = ''
services_release_folders = ["Development-Azure", "Dev-Featurebranch", "Performance Testing-Azure", "Production-Azure", "Test-Azure", "Validation"]
services_build_folders = ["Development", "LoadTesting", "Production", "Test"]
infraRepoName = ''
infraRepoId = ''
infraRepoUrl = ''
release_definitions_url = release_api_organization_url + call_api.get_project_id() + '/_apis/release/definitions?api-version=7.1-preview.4'
build_definitions_url = build_api_organization_url + call_api.get_project_id() + '/_apis/build/definitions?api-version=7.1-preview.7'

