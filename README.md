# TubesPBO2022

## 🔖 Anggota Kelompok
1. Dwi Ananda Rizky (120140027)
2. Shah Raja Abdullah Al Turtusi (120140064)
3. Michelle Ayu Nastiti (120140072)
4. Tomu Petra M Nahulae (120140209)
5. Ahmad Nadhif Mu'afa (120140218)
6. Azlin Nafisa (120140223)

## ⭐ Judul Proyek
B'Pong

## 📖: Deskripsi Proyek
Game Pong adalah game arcade multiplayer dengan tampilan 2D. Game ini sejenis Air Hocky yang ada di tempat bermain pada mall-mall yang sering dijumpai. Tujuan dari game ini yaitu mendapatkan point sampai target untuk memenangkan permainan ini.
Aturan Permainan:
1. Mendapatkan point 10 untuk memenangkan pertandingan
2. Mengunakan keyboard sebagai pengendali permainan, player 1 menggunakan keyboard W dan S untuk gerak naik turun dan untuk player 2 menggunakan panah atas dan panah bawah.

## 📚: Dependensi paket (library) yang dibutuhkan untuk menjalankan aplikasi


## 📖: Cara menjalankan aplikasi (cara bermain)



## 📖: Cara menjalankan kontainer
1. Buat Docker file terlebih dahulu dengan nama Dockerfile. Dockerfile merupakan sebuah file yang mana pada file tersebut berisikan berbagai macam instruksi yang akan dieksekusi untuk membangun sebuah image.
2. Membuat Docker Image, dengan menjalankan perintah docker build. Kita bisa memberikan tag dengan parameter --tag 
```bash
docker build --tag nama-image .
  ```
3. Setelah berhasil membuat imagenya, kemudian jalankan command seperti ini di root terminal.
```bash
XAUTH=$HOME/.Xauthority
touch $XAUTH
xhost +
  ```
4. Kemudian run docker melalui command berikut ini.
```bash
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --device /dev/snd nama-image
  ```
