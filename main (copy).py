from replit import db
import random

# Cek dan inisialisasi leaderboard kalau belum ada
if "leaderboard" not in db:
    db["leaderboard"] = []


def tampilkan_leaderboard():
    print("\n🏆 LEADERBOARD:")
    papan = db["leaderboard"]
    papan_urut = sorted(papan, key=lambda x: x[1], reverse=True)
    for i, (nama, skor) in enumerate(papan_urut, start=1):
        print(f"{i}. {nama} — {skor} poin")


def main():
    while True:
        nama_pemain = input("Masukkan nama kamu: ")
        print(f"\nSelamat datang di KUIS KAIBARA, {nama_pemain}!")

        kata_list = [
            (["niki"], "artis favorit Kaibara"),
            ([
                "oceans & engines", "oceans and engines", "oceans n engines",
                "oceans engines"
            ], "lagu NIKI favorit Kaibara"),
            (["fixie"], "jenis sepeda Kaibara"),
            (["vaseline"], "lotion malam yang dipakai Kaibara"),
            (["rapriana"], "nama belakang Kaibara"),
            (["ibaa"], "nama panggilan spesial Kaibara"),
            (["shared goals"], "love language Kaibara"),
            (["businessman", "pengusaha", "pebisnis",
              "jualan"], "cita-cita Kaibara"),
            (["seru"], "kenapa Kaibara pengen belajar coding?"),
            ([
                "windah", "windah basudara", "luthfi", "luthfi halimawan",
                "sir v", "sebastian", "sebastian tedy"
            ], "nama streamer yang Ibaa tonton sebelum tidur"),
            (["selasa atau rabu", "tengah minggu", "rabu sore",
              "selasa sore"], "Kaibara biasanya nyuci baju hari apa?"),
            (["jawaban mudah", "clue instan",
              "skip soal"], "apa yang gak akan kamu temuin di kuis ini?")
        ]

        random.shuffle(kata_list)
        maks_salah = 3
        jumlah_salah = 0
        skor = 0

        for jawaban_list, kategori in kata_list:
            if jumlah_salah >= maks_salah:
                break

            jawaban_benar = jawaban_list[0]
            print(f"\n📚 Kategori: {kategori}")
            print(f"🔤 Jumlah huruf: {len(jawaban_benar)}")
            print(f"🅰️ Huruf pertama: '{jawaban_benar[0]}'")
            print(f"🅾️ Huruf terakhir: '{jawaban_benar[-1]}'")

            tebakan = input("Masukkan jawabanmu: ").lower()

            if tebakan in [j.lower() for j in jawaban_list]:
                print("✅ BENAR!\n")
                skor += 1
            else:
                jumlah_salah += 1
                print(f"❌ SALAH! Jawaban kamu: {tebakan}")
                print(f"✅ Jawaban yang benar: {jawaban_benar}")
                print(f"💥 Salah ke-{jumlah_salah} dari {maks_salah}\n")

        print("\n📊 Permainan selesai.")
        print(f"🧑 Pemain: {nama_pemain}")
        print(f"🏅 Skor kamu: {skor} dari {len(kata_list)}")

        # Simpan ke database
        papan = db["leaderboard"]
        papan.append((nama_pemain, skor))
        db["leaderboard"] = papan

        tampilkan_leaderboard()

        ulang = input("\nMau main lagi? (y/n): ").lower()
        if ulang != "y":
            print("👋 Terima kasih sudah main!")
            break


main()
