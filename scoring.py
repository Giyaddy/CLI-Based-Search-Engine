sc = open("words_score.txt", 'w+')
f=open("kata.txt", 'r')

kamus=f.readlines()

for i in range(0, len(kamus)):
    num = 0

    kata=kamus[i].replace("\n", "")

    sc.write(str(kata)+" ")
    while num < 1100:
        nama_file = "stemmed/doc"+str(num+1)+".txt"
        f = open(nama_file, 'r')
        baris = f.readlines()

        word_score=0.0
        temp_score=0.0
        all_freq=0
        freq=0

        for j in range(0, len(baris)):
            baris_kata = baris[j].split()
                
            if j==0: #jika yang dibaca baris pertama, maka itu adalah judul artikel. Skornya adalah hasil kali frekuensi kata dengan 0.5
                freq = baris_kata.count(kata)
                temp_score=freq*0.5
                word_score+=temp_score
                freq=0
            
            elif j==1: #jika yang dibaca baris kedua, maka itu adalah kalimat utama. Skornya adalah hasil kali frekuensi kata dengan 0.3
                freq = baris_kata.count(kata)
                temp_score=freq*0.3
                word_score+=temp_score
                freq=0

            elif j>1:
                freq += baris_kata.count(kata)

        word_score+=freq*0.2

        if word_score > 0.0:
            sc.write("doc"+str(num+1)+".txt:"+str(word_score)+" ")
        
        num+=1
    print("Kata ["+kata+"] telah di-scoring\n")
    sc.write("\n")
