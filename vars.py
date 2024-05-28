import call_api
personal_access_token = ''
build_api_organization_url = 'https://dev.azure.com/aerdata/'
release_api_organization_url = 'https://vsrm.dev.azure.com/aerdata/'
project_name = "Leasing"
repo_id = 'd6e97c93-4023-48bf-ad23-7e835a026ae4'
repo_name = 'Deployments'
repo_url = 'https://aerdata@dev.azure.com/aerdata/Leasing/_git/Core-Infrastructure'
services_release_folders = ["Development-Azure", "Dev-Featurebranch", "Performance Testing-Azure", "Production-Azure", "Test-Azure", "Validation"]
services_build_folders = ["Development", "LoadTesting", "Production", "Test"]
infraRepoName = 'Core-Infrastructure'
infraRepoId = '53159690-6f60-4e86-8e64-9857b198ad83'
infraRepoUrl = 'https://aerdata@dev.azure.com/aerdata/Leasing/_git/Core-Infrastructure'
release_definitions_url = release_api_organization_url + call_api.get_project_id() + '/_apis/release/definitions?api-version=7.1-preview.4'
build_definitions_url = build_api_organization_url + call_api.get_project_id() + '/_apis/build/definitions?api-version=7.1-preview.7'

