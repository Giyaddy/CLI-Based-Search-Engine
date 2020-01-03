from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

num = 0
while num < 1100:

    filein = open("texts/doc"+str(num+1)+".txt", 'r')
    fileout = open("free_stopwords/doc"+str(num+1)+".txt", 'w+')

    baris = filein.readlines()

    for i in range(0, len(baris)):
        katadasar = stopword.remove(baris[i])
        fileout.write(katadasar)
    
    print("doc"+str(num+1)+".txt telah diproses\n")
    
    num+=1
    
    filein.close()

fileout.close()
