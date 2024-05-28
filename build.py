import requests
import base64
import vars
import call_api


class FindBuildPipelines:
    def __init__(self):
        self.personal_access_token = vars.personal_access_token
        self.build_api_organization_url = vars.build_api_organization_url
        self.project_name = vars.project_name
        self.repo_id = vars.repo_id

    def find_pipelines_using_repo(self, repo_id, list_all, update, rollback):
        cnt = 0
        print("################################Build Pipelines################################")

        if list_all:
            pipelines = call_api.list_pipelines(vars.build_definitions_url)
            for pipeline in pipelines:
                href_url = pipeline['_links']["self"]["href"]
                web_url = pipeline['_links']["web"]["href"]
                data = call_api.http_call(href_url)

                if self._should_include_pipeline(data):
                    if data["repository"] and repo_id in data["repository"]["id"]:
                        cnt += 1
                        api_url = self._generate_pipeline_link(data['id'])
                        self._print_pipeline_info(cnt, data['name'], web_url, api_url)

                        if update:
                            call_api.update_build_artifact(api_url, rollback)

    def _should_include_pipeline(self, data):
        for folder in vars.services_build_folders:
            if folder in data["path"]:
                return False
        return True

    def _generate_pipeline_link(self, pipeline_id):
        return f"https://dev.azure.com/aerdata/d64a9c3c-cec3-42be-b8a8-8010281bd397/_apis/build/Definitions/{pipeline_id}?api-version=7.1-preview.7"

    def _print_pipeline_info(self, count, name, web_url, api_url):
        print(f"{count}. {name}:")
        print(f"    Api: {api_url}")
        print(f"    Web: {web_url}")
