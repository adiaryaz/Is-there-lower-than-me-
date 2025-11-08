# Is there lower than me?

Sebuah program untuk membuat fungsi yang menentukan apakah sebuah array (list) 1-dimensi dari integer memiliki *setidaknya satu* pasangan elemen bersebelahan yang nilainya meningkat.

## 📝 Description

Program ini mengimplementasikan sebuah fungsi untuk mengecek sebuah array (list) integer. Fungsi ini akan mencari untuk menemukan apakah ada *setidaknya satu* pasangan elemen yang bersebelahan (adjacent) di mana nilai elemen di depan (kiri) *lebih kecil* daripada nilai elemen di belakangnya (kanan).

-----

## 🎯 Problem Statement

### Input:

  * Sebuah array (list) 1-dimensi berisi integer.

### Output:

  * Sebuah nilai boolean (`True` atau `False`).
      * `True` jika ada *setidaknya satu* pasangan `(a, b)` di mana `a < b`.
      * `False` jika *tidak ada* pasangan yang memenuhi kondisi tersebut (artinya array tersebut *non-increasing*).

### Rules:

1.  Program harus membandingkan setiap pasangan elemen yang bersebelahan (misalnya, `arr[i]` dan `arr[i+1]`).
2.  Kondisi yang dicari adalah `arr[i] < arr[i+1]`.
3.  Jika kondisi ini ditemukan *meskipun hanya satu kali*, fungsi harus segera mengembalikan `True`.
4.  Jika seluruh array selesai diperiksa tanpa menemukan kondisi tersebut, fungsi akan mengembalikan `False`.
5.  Array kosong (`[]`) atau array dengan satu elemen (`[5]`) akan mengembalikan `False` karena tidak ada pasangan yang bisa dibandingkan.

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
[1, 2, 3, 4, 5]
```

**Output:**

```
True
```

**Explanation:** Kondisi `1 < 2` langsung terpenuhi pada pasangan pertama.

### Example 2 (Sample 2)

**Input:**

```
[3, 2, 2, 1, 1]
```

**Output:**

```
False
```

**Explanation:** Tidak ada elemen yang lebih kecil dari elemen berikutnya. (`3 > 2`, `2 == 2`, `2 > 1`, `1 == 1`).

### Example 3 (Sample 3)

**Input:**

```
[10, 10, 10, 10, 10]
```

**Output:**

```
False
```

**Explanation:** Tidak ada elemen yang *lebih kecil* dari elemen berikutnya; semuanya sama.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/check-increasing-pair.git
    cd check-increasing-pair
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Masukkan array dalam format list (misalnya, `[3, 2, 5]`) saat diminta untuk melihat hasilnya.
