num = 0
kata = {}

while num <1100:
    nama_file = "stemmed/doc"+str(num+1)+".txt"
    f = open(nama_file, 'r')
    baris = f.readlines()

    for j in range(0, len(baris)):
	
        baris_kata = baris[j].split(" ")
        
        for k in range(0, len(baris_kata)):
            nilai_kata=baris_kata[k].lower()

            nilai_kata = nilai_kata.replace("\n", "")

            if nilai_kata == " ":
                continue

            elif nilai_kata not in kata.keys():
                kata[nilai_kata] = 1

            elif nilai_kata in kata.keys():
                continue
    
    print("doc"+str(num+1)+".txt telah diindeks")
    num+=1

    f.close()

file_hasil = open("kata.txt", 'w+')
for key in kata.keys():
    file_hasil.write(key+"\n")

file_hasil.close()
