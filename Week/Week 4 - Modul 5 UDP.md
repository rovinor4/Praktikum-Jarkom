# Modul 5 UDP
Nama : Rovino Ramadhani <br>
NIM : 103072400031 <br>
Kelas : IF-04-01

1. Pilih satu paket UDP yang terdapat pada trace Anda. Dari paket tersebut, berapa banyak
   “field” yang terdapat pada header UDP? Sebutkan nama-nama field yang Anda temukan!
   ![Modul 5](../Assets/week4/modul5/sc_soal_5.1.avif)
   **Jawaban:** <br/>
   Jumlah field pada header UDP = **4 field**, yaitu:
   * Source Port
   * Destination Port
   * Length
   * Checksum

2. Perhatikan informasi “content field” pada paket yang Anda pilih. Berapa
   panjang (dalam satuan byte) masing-masing “field” yang terdapat pada header UDP?
   ![Modul 5](../Assets/week4/modul5/sc_soal_5.2.1.avif)
    **Jawaban:** <br/> Panjang masing-masing field pada header UDP:
   * Source Port = **2 byte**
   * Destination Port = **2 byte**
   * Length = **2 byte**
   * Checksum = **2 byte**
   Total header UDP = **8 byte**

3. Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui paket UDP pada trace.
   ![Modul 5](../Assets/week4/modul5/sc_soal_5.3.avif)
   **Jawaban:** <br/>
   Nilai **Length = 51** menyatakan:

   * panjang **seluruh UDP segment (header + payload)**

   Verifikasi:

   * Header UDP = 8 byte
  * Payload = 43 byte
  * Total = **8 + 43 = 51 byte** ✅


4. Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP? (Petunjuk:
   jawaban untuk pertanyaan ini dapat ditentukan dari jawaban Anda untuk pertanyaan 2) <br/>
   ![Modul 5](../Assets/week4/modul5/sc_soal_5.2.1.avif)
    **Jawaban:** <br/>
   * Jumlah maksimum byte yang dapat disertakan dalam payload UDP adalah **65527 byte**.
   
   * Alasannya, field **Length** pada header UDP berukuran **2 byte**, sehingga nilai maksimum yang dapat direpresentasikan adalah **65535 byte**. Nilai ini menyatakan total panjang segmen UDP, yaitu **header + payload**. Karena panjang header UDP selalu **8 byte**, maka ukuran maksimum payload UDP adalah:
   
   * **65535 - 8 = 65527 byte**

5. Berapa nomor port terbesar yang dapat menjadi port sumber? (Petunjuk: lihat petunjuk
   pada pertanyaan 4)<br/>
   ![Modul 5](../Assets/week4/modul5/sc_soal_5.5.avif)
    **Jawaban:** <br/>
   * Nomor port sumber terbesar adalah **65535**.
   
   * Karena field **Source Port** berukuran **2 byte (16 bit)**, maka nilai maksimum yang dapat direpresentasikan adalah:
   **2¹⁶ − 1 = 65535**

6. Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan
   desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada
   datagram IP yang mengandung segmen UDP.
   ![Modul 5](../Assets/week4/modul5/sc_soal_5.6.avif)
   **Jawaban:** <br/>
   Nomor protokol untuk UDP adalah:

   * **Desimal: 17**
   * **Heksadesimal: 0x11**

7. Periksa pasangan paket UDP di mana host Anda mengirimkan paket UDP pertama dan paket
   UDP kedua merupakan balasan dari paket UDP yang pertama. (Petunjuk: agar paket kedua merupakan balasan dari paket pertama, pengirim paket pertama harus menjadi tujuan dari
   paket kedua). Jelaskan hubungan antara nomor port pada kedua paket tersebut!
   ![Modul 5](../Assets/week4/modul5/sc_soal_5.7.1.avif)
   ![Modul 5](../Assets/week4/modul5/sc_soal_5.7.2.avif)
   **Jawaban:** <br/>

   Hubungan nomor port pada kedua paket adalah:

   * Pada paket pertama:
     Source Port = **4372**, Destination Port = **53**
   * Pada paket balasan:
     Source Port = **53**, Destination Port = **4372**

   Kesimpulan:

   * **Source Port paket pertama = Destination Port paket balasan**
   * **Destination Port paket pertama = Source Port paket balasan**

