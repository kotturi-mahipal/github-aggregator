import github_api
import aws_manager
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == "__main__":
    owner = config['GITHUB']['repo_owner']
    repo = config['GITHUB']['repo_name']

    maintainers = github_api.get_maintainers(owner, repo)
    print("GitHub Maintainers:", maintainers)

    aws_manager.update_aws_users(maintainers)
