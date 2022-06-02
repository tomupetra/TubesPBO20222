# TubesPBO2022

## 🔖 Kontributor Pengembangan Aplikasi
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
Library python adalah kumpulan modul terkait berisi kumpulan kode yang dapat digunakan berulang kali dalam program yang berbeda. Adanya library membuat pemrograman python menjadi lebih sederhana dan nyaman bagi programmer karena tidak perlu menulis kode yang sama berulang kali untuk program yang berbeda. Pygame adalah modul cross-platform dari Python dirancang untuk membuat game. Modulnya dirancang untuk menjadi sederhana, mudah digunakan, dan menyenangkan. Modul sys adalah modul yang berfungsi untuk mengakses program itu sendiri dan menjalankan file kode python di lingkungan direktori atau sistem itu sendiri. Modul lainnya yang digunakan yaitu tkinter, os dan pygame. 

## 📖: Cara menjalankan aplikasi (cara bermain)
- Open File menu.py (pastikan telah menginstall pygame pada aplikasi untuk menjalankan program)
- Kemudian setelahnya run program untuk dapat memainkan permainan
- Terdapat beberapa shortcut dalam permainan. Tombol Shortcut 1 untuk langsung memenangkan permainan dan Tombol Shortcut 2 dan player akan langsung kalah.

## 📖: UML Diagram
![UML Class Diagram-Page-2](https://user-images.githubusercontent.com/103347734/171573095-126bb6b5-5b65-45dd-8ed4-a9e4f0c483da.jpg)

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
## 📖: Video Demo Kontainer  
[![Text](https://img.youtube.com/vi/u1NzZxhdQX8/0.jpg)](https://www.youtube.com/watch?v=u1NzZxhdQX8)
