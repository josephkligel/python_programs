import json
import os
import sys, argparse
import simple_chalk as chalk
from lib import gitList

parser = argparse.ArgumentParser(description='Command line tool to apply git commands to all Zigjag git repositories listed on Github.')
parser.add_argument('-c', '--clone', action='store_true', help='python gitpy.py --clone')
parser.add_argument('-p', '--pull', action='store_true', help='python gitpy.py --pull')
parser.add_argument('-pu', '--push', action='store_true', help='python gitpy.py --push')
args = parser.parse_args()

with open(os.path.join(os.path.dirname(__file__), 'lib/remoteRepoList.json')) as fh:
    repoDict = json.load(fh)

def gitTask(command):
    if args.clone:
        for repo, url in repoDict.items():
            print(f'===================== {repo.capitalize()} ====================')
            print(f'Git clone process in progress...')
            os.system(f'git clone {url}')
    elif args.pull:
        print(f'=========== Pull All Git Repos in home-user directory============')
        os.system('find /home/$USER -mindepth 1 -maxdepth 2 -type d -print -exec git -C {} pull \;')
    elif args.push:
        print(f'================= Push All Git Repos =============')
        os.system("git config --global credential.helper 'cache --timeout 7200'")
        localRepoList = json.load(open(os.path.join(os.path.dirname(__file__), 'lib/localRepoList.json')))
        for item, value in localRepoList.items():
            print(f'\n>>>>>>> {item} <<<<<<<')
            os.system(f'git -C {value} add .; git -C {value} commit -m "gitpy to your rescue"; git -C {value} push')

if len(sys.argv) > 1:
    gitList.main()
    gitTask(sys.argv[1])
else:
    print(chalk.bgRed('Not enough arguments'))
