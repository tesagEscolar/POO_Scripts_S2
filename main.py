import subprocess

commitMessage = 'For_loop2'

file1 = open(f'Parcial1/{commitMessage}.cpp', "w")
L = ["for(int i=0; i<10; i++){ cout<<i<<endl"]
file1.writelines(L)
file1.close()

process = subprocess.call(['bash','./pushToGh.sh', commitMessage])
# process = subprocess.call(['chmod +x ./pushToGh.sh', commit_message], shell=True)

print(process)