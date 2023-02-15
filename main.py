import subprocess

file1 = open("forloop.cpp", "w")
L = ["for(int i=0; i<10; i++){ cout<<i<<endl"]
file1.writelines(L)
file1.close()
commit_message = "For loop cpp code"
process = subprocess.call('./pushToGh.sh', shell=True)
# process = subprocess.call(['chmod +x ./pushToGh.sh', commit_message], shell=True)

print(process)