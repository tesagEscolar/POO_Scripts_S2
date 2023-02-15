import subprocess

commitMessage = 'For_loop'

file1 = open(f'{commitMessage}.cpp', "w")
L = ["for(int i=0; i<10; i++){ cout<<i<<endl"]
file1.writelines(L)
file1.close()

process = subprocess.call(['bash','./pushToGh.sh', commitMessage])
# process = subprocess.call(['chmod +x ./pushToGh.sh', commit_message], shell=True)

print(process)