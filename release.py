import requests
import base64
import vars
import call_api


class FindReleasePipelines:
    def __init__(self):
        self.personal_access_token = vars.personal_access_token
        self.release_api_organization_url = vars.release_api_organization_url
        self.project_name = vars.project_name
        self.repo_id = vars.repo_id

    def find_releases_using_repo(self, repo_id, list_all, update, rollback):
        if not list_all:
            return

        print("################################Release Pipelines################################")
        definitions = call_api.list_pipelines(vars.release_definitions_url)
        cnt = 0

        for definition in definitions:
            href_url = self._generate_href_url(definition['id'])
            data = call_api.http_call(href_url)

            if self._should_include_release(data):
                if self._is_repo_used_in_artifacts(data['artifacts'], repo_id):
                    cnt += 1
                    self._print_release_info(cnt, data)
                    if update:
                        call_api.update_release_artifact(href_url, rollback)

    def _generate_href_url(self, definition_id):
        return f"https://vsrm.dev.azure.com/xxxx/xxxxx/_apis/Release/definitions/{definition_id}?api-version=7.1-preview.4"

    def _should_include_release(self, data):
        for folder in vars.services_release_folders:
            if folder in data["path"]:
                return False
        return True

    def _is_repo_used_in_artifacts(self, artifacts, repo_id):
        for artifact in artifacts:
            if repo_id in artifact["definitionReference"]["definition"]["id"]:
                return True
        return False

    def _print_release_info(self, count, data):
        definition_url = self._generate_href_url(data['id'])
        print(f"{count}. {data['name']}:")
        print(f"    Api: {definition_url}")
        print(f"    Web: {data['_links']['web']['href']}")

