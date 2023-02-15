file1 = open("myfile.cpp", "w")
L = ["for(int i=0; i<10; i++){ cout<<i<<endl"]
file1.writelines(L)
file1.close()