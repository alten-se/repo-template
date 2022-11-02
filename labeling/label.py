import shutil
import os
import subprocess as sub
import sys

def bash_cmd(cmd):
    proc = sub.Popen(['bash', "-i", "-c", cmd])
    proc.communicate()
    exit_code = proc.wait()
    print(exit_code)
    if exit_code != 0:
        sys.exit("Derp!")



def install_labelerjs():
    bash_cmd("nvm use 18")
    bash_cmd("npm install labeler")


def get_labels_path() -> str:
    out = sub.check_output(["labeler", "-p"]).splitlines()
    path = str(out[2]).split(sep=" ")[1]
    return path[:-1]
    

def configure_label_maker():
    os.system("labeler -c")

def add_labels(path: str):
    repo_name = input("repo name: ")
    label_conf_path = get_labels_path()
    shutil.copyfile(path, label_conf_path)
    os.system(f"labeler -r {repo_name} -du")



if __name__ == "__main__":


    ans = input("install label maker? y/(n) ")
    if ans.lower() == "y":
        install_labelerjs()


    ans = input("config label maker y/(n) ")    
    if ans.lower() == "y":
        configure_label_maker()
    
    add_labels("labeler_labels.json")
