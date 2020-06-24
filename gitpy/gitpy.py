import json
import os
import sys, argparse
import simple_chalk as chalk

parser = argparse.ArgumentParser(description='Command line tool to apply git commands to all Zigjag git repositories listed on Github.')
parser.add_argument('-c', '--clone', action='store_true', help='python gitpy.py --clone')
parser.add_argument('-p', '--pull', action='store_true', help='python gitpy.py --pull')
args = parser.parse_args()

with open(os.path.join(os.path.dirname(__file__), 'lib/repoList.json')) as fh:
    repoDict = json.load(fh)

gitCommands = ['clone', 'pull']

def gitTask(command):
    if args.clone:
        for repo, url in repoDict.items():
            print(f'===================== {repo.capitalize()} ====================')
            print(f'Git clone process in progress...')
            os.system(f'git clone {url}')
    elif args.pull:
        print(f'=========== Pull All Git Repos in home-user directory============')
        os.system('sudo find /home/$USER -mindepth 1 -maxdepth 1 -type d -print -exec git -C {} pull \;')

if len(sys.argv) > 1:
    gitTask(sys.argv[1])
else:
    print(chalk.bgRed('Not enough arguments'))
