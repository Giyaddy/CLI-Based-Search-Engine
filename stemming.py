from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

num = 0
while num < 1100:

    filein = open("free_stopwords/doc"+str(num+1)+".txt", 'r')
    fileout = open("stemmed/doc"+str(num+1)+".txt", 'w+')

    baris = filein.readlines()

    for i in range(0, len(baris)):
        katadasar = stemmer.stem(baris[i])
        katadasar = katadasar.replace("riah", "meriah")
        fileout.write(katadasar+"\n")
    
    print("doc"+str(num+1)+".txt telah diproses\n")
    
    num+=1
    
    filein.close()

fileout.close()
