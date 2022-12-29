"""
Tampilkan Title dari alamat-alamat berikut secara berurutan. tiket.com, tokopedia.com, orangsiber.com, 
demoqa.com, automatetheboringstuff.com

Expected Output :
tiket.com - titlenya
tokopedia.com - titlenya
orangsiber.com - titlenya
demoqa.com - titlenya
automatetheboringstuff.com - titlenya

Syarat wajib:
- Gunakan satu jendela browser
- Gunakan Looping
- Browse minimize dari awal 
- Tutup browser setelah selesai

Pengumpulan Tugas:
- Simpan program di repository Github kalian.
- Beri nama repository "kelasotomesyen-mid-nama".
- ganti "nama" pada nama repo tersebut dengan nama masing-masing.
- format nama file tugas01.py
- Kirim link repo-nya ke DM Telegram
- Paling lambat jam 6 sore sebelum Session 2 dimulai.
- Silahkan berdiskusi di group kelas, tapi tidak saling share jawaban.
"""

from selenium import webdriver

namaDomain = ['tiket',  'tokopedia',  'orangsiber', 'demoqa', 'automatetheboringstuff']
listUrl = [('https://' + domain + '.com') for domain in namaDomain ]

driver = webdriver.Chrome()
driver.minimize_window()

for url in listUrl:
    driver.get(url)
    domain = url[8:]
    judul = driver.title 
    print('{} - {}'.format(domain,judul))
    
driver.close()