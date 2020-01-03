import time

class Kata:
    def __init__(self):
        self.dokumen = {}

class Dokumen:
    def __init__(self, tautan, judul, isi):
        self.url = tautan
        self.judul = judul
        self.isi = isi

kamus = {}
dokumen ={}
f=open("words_score.txt", "r")
baris = f.readlines()

for i in baris:
    kata= i.split(" ")
    key = kata[0]
    kamus[key] = Kata()

    for j in range(1, len(kata)-1):
        temp = kata[j].split(":")
        kamus[key].dokumen[temp[0]] = float(temp[1])
f.close()
f=open("datadocs.txt", 'r')
line_docs = f.readlines()

for l in line_docs:
    docList = l.split(" :: ")
    link = docList[1]
    title = docList[2]
    content = docList[3]

    dokumen[docList[0]] = Dokumen(link, title, content)

query= input("Masukkan kata kunci : ")
banyak = int(input("Jumlah dokumen teratas : "))
query=query.lower()

# if query in kamus.keys():
#     for k, v, in kamus[query].dokumen.items():
#         print(k+" "+str(v)+"\n")

start = time.time()
querylist = query.split(" ")
result={}

for i in querylist: #simpan semua query ke dalam dictionary sebagai vektor query
    if i in kamus.keys():
        dokumenList = kamus[i].dokumen

        for j in dokumenList.keys():
            if j not in result.keys():
                result[j] = float(dokumenList[j])
            
            else:
                result[j]+= float(dokumenList[j])
finish = time.time()

print("\n")

nomor=1
for k, v in sorted(result.items(), key=lambda x:x[1], reverse=True):
    print(str(dokumen[k].judul)+" (Skor : "+str(v)+")\n"+str(dokumen[k].url)+"\n"+str(dokumen[k].isi[:250])+"...\n\n")

    if nomor==banyak:
        break
    nomor+=1

print("Waktu pencarian : "+str(finish-start)+" detik\n")