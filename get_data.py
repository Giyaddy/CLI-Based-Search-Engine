f1=open("links.txt", "r")
barisLink = f1.readlines()
hasil=open("datadocs.txt", 'w+')
num=0

while num <1100:
    f2=open("texts/doc"+str(num+1)+".txt", 'r')
    baris = f2.readlines()

    judul = baris[0].replace("\n", "")
    isi = ""

    for i in range(1, len(baris)):
        isi = isi+baris[i]+" "
    
    isi = isi.replace("\n", " ")
    url = barisLink[num].replace("\n", "")
    hasil.write("doc"+str(num+1)+".txt :: "+str(url)+" :: "+str(judul)+" :: "+str(isi[:300])+"\n")
    
    f2.close()
    num+=1