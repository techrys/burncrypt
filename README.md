# 🔥 Encrypted Self-Destructing Chat Room 🔥

A secure, self-destructing chat application in Python, perfect for sending temporary messages that vanish after reading! This chat room encrypts all messages, ensuring privacy, and includes a unique visual "burn" effect that erases messages completely after they’re viewed, leaving no trace.

## 🌟 Key Features

- **End-to-End Encryption**: Messages are securely encrypted with symmetric encryption, safeguarding communications from unauthorized access.
- **Self-Destructing Messages**: Messages display for a limited time before "burning away" in an animated effect that fully deletes them from the chat.
- **Multi-Client Support**: Connect multiple clients to a single server, making it ideal for private group chats.

## 🚀 Getting Started

### Prerequisites
- **Python 3.6+**
- **`cryptography` library**: Install it via:
  ```bash
  pip install cryptography
Running the Server

    Start the server to listen for incoming connections:

    bash

    python server.py

Running the Client

    Open a new terminal and run the client to connect to the server:

    bash

    python client.py

    Repeat this step for each additional client.

🛠️ How It Works

    Encryption: Messages are encrypted on the client side before sending and decrypted upon receipt, ensuring end-to-end privacy.
    Message Handling: Each message is briefly displayed on the client, followed by a "burn" animation to mimic its permanent deletion.
    Temporary Messages: No messages are stored; each message exists only briefly on-screen, making this chat room ideal for ephemeral conversations.

📌 Things to Add

Planned and potential improvements:

    User Interface Enhancements: Add a GUI with a cleaner, more user-friendly interface.
    Advanced Encryption: Improve encryption with additional security layers or asymmetric encryption for added protection.
    Additional Self-Destruct Options: Allow users to set custom durations for messages or implement one-time-view functionality.
    Secure Key Exchange: Replace the pre-shared key with a secure key exchange mechanism, such as Diffie-Hellman, for increased security.
    Persistent Room Support: Create an option to allow a mix of persistent and self-destructing messages for more flexible chat options.
