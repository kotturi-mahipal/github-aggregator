# GitHub-AWS User Aggregator

This Python project synchronizes maintainers of a GitHub repository with users in AWS (e.g., IAM). It fetches the list of maintainers from a specified GitHub repository and updates AWS users accordingly, potentially adding new users or removing existing ones based on the maintainer list.

## Features

- Fetches maintainers from a GitHub repository using the GitHub API.
- Updates AWS users based on the fetched maintainer list.
- Configurable via a `config.ini` file for easy customization.
- Uses `boto3` for interacting with AWS services.
- Includes a `.gitignore` file to exclude sensitive information and unnecessary files from version control.

## Getting Started

### Prerequisites

- **Python 3.x:** Make sure you have Python 3 installed on your system.
- **Virtual Environment (Recommended):** Create a virtual environment to isolate project dependencies.
- **AWS Account:** You'll need an AWS account with the necessary permissions to manage IAM users.
- **GitHub Personal Access Token:** Generate a personal access token with `repo` (for public repos) or `repo:status` (for private repos) permissions.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/github-aws-user-sync.git
   cd github-aws-user-sync
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Create a `config.ini` file:**
   ```ini
   [GITHUB]
   api_token = <your_github_api_token>
   repo_owner = <github_username_or_organization>
   repo_name = <repository_name>

   [AWS]
   aws_access_key_id = <your_aws_access_key_id> 
   aws_secret_access_key = <your_aws_secret_access_key>
   aws_region = <your_aws_region> 
   ```

2. **Fill in the `config.ini` file:**
   - Replace the placeholders with your actual GitHub API token, repository details, and AWS credentials.

### Usage

1. **Run the script:**
   ```bash
   python main.py
   ```

## Security Considerations

- **Never hardcode API keys or secrets!** Use environment variables or a secure configuration management system for production environments.
- **Principle of Least Privilege:** Grant your AWS credentials and GitHub token the minimum necessary permissions.
- **Error Handling:** Implement robust error handling to catch API issues and prevent unexpected behavior.
- **Logging:** Log actions taken for auditing and debugging purposes.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
