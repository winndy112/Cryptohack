#include <iostream>
#include <string>

using namespace std;

string encoded_rot13(string message) {
    string encoded = "";

    for (int i = 0; i < message.length(); i++) {
        char c = message[i];

        if (c >= 'A' && c <= 'Z') {
            c = ((c - 'A') + 13) % 26 + 'A';
        }
        else if (c >= 'a' && c <= 'z') {
            c = ((c - 'a') + 13) % 26 + 'a';
        }

        encoded += c;
    }

    return encoded;
}

string decoded_rot13(string message) {
    string decoded = "";

    for (int i = 0; i < message.length(); i++) {
        char c = message[i];

        if (c >= 'A' && c <= 'Z') {
            c = ((c - 'A') + 13) % 26 + 'A';
        }
        else if (c >= 'a' && c <= 'z') {
            c = ((c - 'a') + 13) % 26 + 'a';
        }

        decoded += c;
    }

    return decoded;
}

int main() {
    string message_1 = "Hello, World!";
    string encoded = encoded_rot13(message_1);
    
    cout << "Original message_1: " << message_1 << endl;
    cout << "Encoded message_1: " << encoded << endl;

    string message_2 = "Ornhgvshyy";
    string decoded = decoded_rot13(message_2);

    cout << "Original message_2: " << message_2 << endl;
    cout << "Encoded message_2: " << decoded << endl;

    return 0;
}
