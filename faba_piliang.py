import os,sys
def faban(branch):
    xt = ["conf","pay","trade","manager","www","api"]
    for i in xt:
        shell = "sh "+ i + ".sh "+ branch
        os.system(shell)

    #os.system  ("cd /opt/batch")
    os.system("source /etc/profile && cd /opt/batch && /bin/sh tongbu.sh "+branch )

if __name__ == '__main__':
    branch_ls = sys.argv
    if len(branch_ls) !=2:
        branch = "develop"
    else:
        branch = branch_ls[1]
    faban(branch)