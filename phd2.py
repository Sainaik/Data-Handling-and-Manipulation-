import pandas as pd
import os
import glob

path1="C:\\Users\\sai kumar naik\\Desktop\\phd\\LABELS"
path2="C:\\Users\\sai kumar naik\\Desktop\\phd\\LABELS\\"

wrong=pd.read_csv('C:\\Users\\sai kumar naik\\Desktop\\phd\\WrongID.csv',header=None)
# listing the  wrong_ids
wrong_list=wrong[0].tolist()
ids=[] #ids are stored
i=0
for file in glob.glob(path1+"/*.desc"):
     ids.insert(i,file)

print("total no.of ids are : ",len(ids))

 #removing the prefix and suffix
j=0
indexes=[]
for x in ids:
      k=os.path.relpath(x,"C:\\Users\\sai kumar naik\\Desktop\\phd\\LABELS\\")
      l = os.path.splitext(k)[0]  # removing .desc    split(.)
      l = os.path.splitext(l)[0]  #remvoing .jpg
      indexes.insert(j,l)
      j=j+1


#ids elements are copied in indexes then

#set of indexex as index
index = set(indexes)

print("the size of the wrong id list ",len(wrong_list))

#i'm converting  wrong_list elememts to string
wrong_list=list(map(str, wrong_list))
 # creating a set of wrong list
wrong_last=set(wrong_list)

#print(wrong_last)
#print(indexes)

# final ids = (index -wrong ids) 
final_ids=index-wrong_last
final_ids=list(final_ids)
print("the final list size : ",len(final_ids))

print("finally the required ids are stored in final_ids list")

final=[]
m=0
#final_ids1=[path2+x+'.jpg.desc' for x in final_ids]
for x in final_ids:
      final.insert(m,(path2+x+".jpg.desc"))
      m=m+1
#print(final)


files=[]
col=[]
i=0
j=0
for name in final:
    fopen=open(name)
    files.insert(i,name)
    i=i+1

    for line in fopen:
        print(line)
        col.insert(j,line)
        j=j+1

print("Number of Rows :",i,"   NUmber of Columns: ",j)

index=pd.Series(files)
print(index)

columns=set(col)
columns=list(columns)


print(len(columns))
#print (columns)

Dataframe=pd.DataFrame(index=index,columns=columns)
Dataframe.fillna(0,inplace=True)
#print(Dataframe)
for file in index:
    fopen=open(file)
    for word in fopen:
        Dataframe.at[file,word]=1

    fopen.close()
print(Dataframe)
Dataframe.to_csv('C:\\Users\\sai kumar naik\\Desktop\\ML NIT\\labels2.csv',sep='\t')

