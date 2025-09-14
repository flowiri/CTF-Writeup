OH no tung tung tung have given up some tralalalela:
Analyze the PCAP: You must inspect the TLS handshake in Wireshark and extract three key pieces of information:

Client's Public Key (Q_c): From the Client Key Exchange message. This is the client's ephemeral public key point.

Client Random & Server Random: From the Client Hello and Server Hello messages.

Curve Name: From the Server Hello message's extensions (e.g., supported_groups, which would show secp256r1).

Calculate the Pre-Master Secret (PMS): The contestant must write a script (e.g., Python with the cryptography library) to perform the Elliptic Curve multiplication: S = d_s * Q_c. The x-coordinate of the resulting point S is the Pre-Master Secret.

Derive the Master Secret: The PMS is not enough for Wireshark. You must derive the Master Secret using the TLS 1.2 PRF (Pseudo-Random Function):
MasterSecret = PRF(PMS, "master secret", ClientRandom + ServerRandom)
This also requires scripting and knowledge of the TLS specification.

Create Key Log File: You format their result into the key log format:
CLIENT_RANDOM <client_random_hex> <master_secret_hex>

Decrypt: You load this self-created key log file into Wireshark, which will then successfully decrypt the traffic and reveal the flag.

The ransom encryption scheme is it chacha20? have it been modified with some magic number (RFC? Standard?)?

Is it encrypt the whole file or just somebitibyte? Why it look so chaotic?