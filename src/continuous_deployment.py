import subprocess
import logging

def deploy_to_git(remote_name='origin', branch_name='master'):
    try:
        subprocess.run(['git', 'push', remote_name, branch_name], check=True)
        logging.info("Successfully pushed to Git repository.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Git push failed: {e}")

def deploy_to_heroku(app_name):
    try:
        subprocess.run(['heroku', 'git:remote', '-a', app_name], check=True)
        subprocess.run(['git', 'push', 'heroku', 'master'], check=True)
        logging.info(f"Successfully deployed to Heroku app: {app_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Heroku deployment failed: {e}")

# Example usage
deploy_to_git()
deploy_to_heroku('your_heroku_app_name')
