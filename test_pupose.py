import release
import build
import call_api
import vars

release_definition_url = 'https://vsrm.dev.azure.com/xx/xx/_apis/Release/definitions/463?api-version=7.1-preview.4'
build_definition_url = 'https://dev.azure.com/xxx/_apis/build/Definitions/3065?api-version=7.1-preview.7'

### update build artifact in a single build pipeline

#call_api.update_build_artifact(build_definition_url, rollback=True)


### update a release artifact in a single release pipeline

#call_api.update_release_artifact(release_definition_url)

####bulk update all release artifacts through all release pipelines which depend on Deployments repository

#findReposForReleases = release.FindReleasePipelines()
#findReposForReleases.find_releases_using_repo(vars.repo_id, list_all=True, update=False,rollback=False)

#### bulk update all build artifacts through all build pipelines depend on Deployments repository

findForBuildPipelines = build.FindBuildPipelines()
findForBuildPipelines.find_pipelines_using_repo(vars.repo_id, list_all=True, update=False, rollback=False)
