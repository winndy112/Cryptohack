#include <iostream>
#include <string>

using namespace std;

// Giải mã chuỗi với khoảng cách cho trước
string decrypt(string message, int key) {
    string result = "";

    for (int i = 0; i < message.length(); i++) {
        char c = message[i];
        if (isupper(c)) {
            c = (c - key + 26) % 26 + 'A';
        } else if (islower(c)) {
            c = (c - key + 26) % 26 + 'a';
        }
        result += c;
    }

    return result;
}

int main() {
    string message;
    cout << "Enter a message to decrypt: ";
    getline(cin, message);

    for (int key = 0; key < 26; key++) {
        string decrypted_message = decrypt(message, key);
        cout << "Key " << key << ": " << decrypted_message << endl;
    }

    return 0;
}