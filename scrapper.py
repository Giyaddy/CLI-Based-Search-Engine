import time
import requests
from bs4 import BeautifulSoup

num = 0
start_time = time.time()
with open("links.txt", 'r') as file:

    for line in file:
        filename = "texts/doc"+str(num+1)+".txt"
        file_txt = open(filename, 'w+')
        response = requests.get(line)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find(id="dsharetitle").get_text()
        real_date = soup.find(class_="read__time").get_text()
        posts = soup.find(class_="read__content").find_all('p')
        date = real_date.split(' - ')
        date_abs=date[1].split(',')

        file_txt.write(title+"\n")

        for post in posts: #ambil text
            if post.find(class_= 'inner-link-baca-juga') or post.find('strong'): #jika ada class ini, maka jangan ambil teksnya
                continue

            word = post.get_text()
            file_txt.write(word+"\n")
                
        print(filename+" telah dibuat\n")
        num+=1
        file_txt.close()

print("Program Sukses mengekstrak data dari "+str(num)+" url")
print("Waktu pembuatan seluruh file teks :"+str((time.time()-start_time)/3600)+" jam")
