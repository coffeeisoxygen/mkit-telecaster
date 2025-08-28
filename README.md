# MKIT TELECASTER

project ini adalah telegram bot untuk otomatisasi iklan / boradcast ke channel telegram untuk promosi produk, dan beberapa integrasi ke otomax.

## Fitur

- Mengirim pesan ke channel telegram
- Menjadwalkan pengiriman pesan
- Mengirim Pesan ke group

- dan lain lain.

## license

produk ini open source , silahkan di gunakan, developer tidak bertanggung atas hal hal yg terjadi akibat penggunaan produk ini.

## tech stack di gunakan

- python 3.13
- UV
- PTB [python-telegram-bot]

## cara penggunaan

- jalan run.bat

## todo

1- Buat Bot Telegram
2- Jadikan Bot sebagai Admin di Channel Telegram
Kalau channel public → cukup @nama_channel.

Kalau channel private → harus numeric chat_id.

Cara dapetnya:

Tambahin bot jadi admin channel.

Kirim 1 pesan di channel.

Panggil API getUpdates atau cek log update bot → nanti keliatan chat.id (biasanya minus, contoh: -1001234567890).
