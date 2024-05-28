# Release notes:

 - Listing all build definitions which using a spesific repo url.
 - Listing all release definitions which using a spesific repo url.
 - Update single build definition from source to destination repository.
 - Update single release definition  from source to destination repository.
 - Rollback for single or bulk update.

## How to use test_purpose.py?

   release_definition_url = 'https://vsrm.dev.azure.com/xxxx/d64a9c3c-cec3-xxxx-xxxx-xxxx/_apis/Release/definitions/463?api-version=7.1-preview.4'
   build_definition_url =` `https://dev.azure.com/xxxx/d64a9c3c-xxx-xxxx-b8a8-xxxx/_apis/build/Definitions/3065?api-version=7.1-preview.7`

 1. **single update for build definition, rollback is true is false means it will rollback definition update**

        `call_api.update_build_artifact( build_definition_url, rollback=False )`
   

 2. **single update for releae definition, rollback is true is false means it will rollback**

       `call_api.update_release_artifact(release_definition_url, rollback=False)`

 3. **bulk update all release artifacts through all release pipelines which depend on Deployments repository, rollback is true is false means it will rollback definition update**

        findReposForReleases = release.FindReleasePipelines()
        findReposForReleases.find_releases_using_repo(vars.repo_id, list_all=True, update=False,rollback=False)

 4. **bulk update all build artifacts through all build pipelines depend on Deployments repository, 1. rollback is true is false means it will rollback definition update**

     `findForBuildPipelines = build.FindBuildPipelines()
findForBuildPipelines.find_pipelines_using_repo(vars.repo_id, list_all=True, update=False, rollback=False)`

  ## Environment variables
 
#Azure devops access token
personal_access_token = ''  

build_api_organization_url = 'https://dev.azure.com/xxx/'

release_api_organization_url = 'https://vsrm.dev.azure.com/xxx/'

project_name = ""
#Source repo ID

repo_id = 'd6e97c93-4023-xxxx-xx-xxxx

#Source repo Name

repo_name = 'Deployments'

#Source repo URL

repo_url = 'https://xxxx@dev.azure.com/xxxx/xxxx/_git/Core-Infrastructure'

#Whitelisted release folders not to apply
services_release_folders = ["Development-Azure", "Dev-Featurebranch", "Performance Testing-Azure", "Production-Azure", "Test-Azure", "Validation"]

#Whitelisted build folders not to apply
services_build_folders = ["Development", "LoadTesting", "Production", "Test"]

#destination repo name
infraRepoName = 'Core-Infrastructure'

#destination repo ID
infraRepoId = '53159690-6f60-xx-xxx-xxxx'

#destination repo URL

infraRepoUrl = 'https://xxx@dev.azure.com/xxx/xxx/_git/xxxxx'

release_definitions_url = release_api_organization_url + call_api.get_project_id() + '/_apis/release/definitions?api-version=7.1-preview.4'

build_definitions_url = build_api_organization_url + call_api.get_project_id() + '/_apis/build/definitions?api-version=7.1-preview.7'
