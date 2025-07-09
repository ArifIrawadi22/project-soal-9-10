import cv2

def tampilkan_dua_gambar():
    img1 = cv2.imread("Douglas-fir.webp")
    img2 = cv2.imread("White Pine.jpeg")

    if img1 is None:
        print("Gambar douglas_fir.jpg tidak ditemukan.")
    else:
        cv2.imshow("Douglas Fir", img1)

    if img2 is None:
        print("Gambar white_pine.jpg tidak ditemukan.")
    else:
        cv2.imshow("White Pine", img2)

    # Tunggu tombol keyboard ditekan untuk menutup semua jendela
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Jalankan fungsi
if __name__ == "__main__":
    tampilkan_dua_gambar()
