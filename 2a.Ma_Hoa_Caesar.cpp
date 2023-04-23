#include <iostream>
#include <string>
using namespace std;

string caesarCipher(string plaintext, int shift) {
    string ciphertext = "";
    for (int i = 0; i < plaintext.length(); i++) {
        // Lấy ký tự thứ i trong plaintext
        char c = plaintext[i];

        // Nếu ký tự là một chữ cái
        if (isalpha(c)) {
            // Tính toán độ dịch chuyển cho ký tự này
            char base = isupper(c) ? 'A' : 'a';
            c = (c - base + shift) % 26 + base;
        }

        // Thêm ký tự đã được mã hóa vào chuỗi ciphertext
        ciphertext += c;
    }
    return ciphertext;
}

int main() {
    string plaintext;
    int shift;
    cout << "Enter plaintext: ";
    getline(cin, plaintext);
    cout << "Enter shift pattern: ";
    cin >> shift;
    string ciphertext = caesarCipher(plaintext, shift);
    cout << "Ciphertext: " << ciphertext << endl;
    return 0;
}