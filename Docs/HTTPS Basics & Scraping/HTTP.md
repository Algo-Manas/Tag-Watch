Imagine sending a secret drawing to your friend across town.

**HTTP** is like writing your secret drawing on an open **postcard**. As the mail carrier transports it, anyone along the way—delivery drivers, neighbors, or strangers—can look at your drawing and read everything on it.

---

**HTTPS** is like placing your drawing inside a **magic locked box** before sending it:

1. **The Secret Handshake:** Before sending the box, your computer and the website whisper to each other to create a special secret key.
2. **Locking the Box:** Your computer locks the box using that key.
3. **Safe Journey:** As the box travels across the internet, sneaky snoopers can see the box moving, but they cannot open it or peek inside.
4. **Unlocking:** Only your friend's website has the matching secret key to open the box and read your drawing safely.
5. **The Shiny Badge:** The website also shows your browser a special stamped ID badge to prove it really is your friend, and not a trickster pretending to be them.

---

### Key Differences Between HTTP and HTTPS

| Feature | HTTP | HTTPS |
| --- | --- | --- |
| **Full Name** | Hypertext Transfer Protocol | Hypertext Transfer Protocol **Secure** |
| **Security** | Unencrypted (Sent in clear text) | Encrypted (Scrambled and locked) |
| **Browser Symbol** | "Not Secure" warning | Padlock icon next to the web address |
| **Network Port** | Uses **Port 80** | Uses **Port 443** |
| **Identity Check** | None | Uses a verified digital security certificate |
| **Snooping Risk** | High (Anyone on the network can read it) | Very low (Eavesdroppers see only scrambled code) |

---

### Technical Terms Glossary

Here is the exact technical vocabulary used behind the scenes to power HTTP and HTTPS:

* **HTTP (Hypertext Transfer Protocol):** An application-layer network protocol used to transfer data (web pages, text, images) across the web in plain text.
* **HTTPS (Hypertext Transfer Protocol Secure):** An extension of HTTP that uses encryption protocols to secure all communication between a client (browser) and a web server.
* **SSL / TLS (Secure Sockets Layer / Transport Layer Security):** Cryptographic security protocols that create an encrypted link between a web browser and a server. TLS is the modern, secure successor to the older SSL protocol.
* **Encryption:** The mathematical process of converting human-readable data into unreadable code to prevent unauthorized access.
* **Plaintext vs. Ciphertext:** **Plaintext** is raw, unencrypted data (e.g., `MyPassword123`). **Ciphertext** is the scrambled, encrypted output (e.g., `9x#2L!k09a`).
* **Asymmetric Cryptography:** Encryption using a mathematically linked key pair (**Public Key** and **Private Key**). Anyone can use the Public Key to encrypt data, but only the holder of the Private Key can decrypt it.
* **Symmetric Cryptography:** Encryption where the exact same key is used by both parties to lock and unlock data. HTTPS uses asymmetric encryption to set up the connection, then switches to symmetric encryption for faster data transfers.
* **TLS Handshake:** The initial negotiation process between client and server where they verify identities, choose encryption algorithms, and exchange session keys.
* **SSL/TLS Certificate & Certificate Authority (CA):** A digital data file issued by a trusted third party (**Certificate Authority**) that verifies a domain owner's identity and supplies their public key.
* **Data Packets:** Formatted units of data transmitted over a network.
* **Port 80 & Port 443:** Virtual network channels on a server: **Port 80** serves unencrypted HTTP traffic, while **Port 443** serves encrypted HTTPS traffic.

### HTTP Request

An **HTTP request** is a formatted message sent from a client (such as your browser or mobile app) to a web server asking to retrieve data or perform an action on a web resource.

![HTTP Request](Docs/Assets/Images/HTTP%20Request%20Components.jpg)

---

### Components of an HTTP Request

An HTTP request message is organized into three distinct parts:

1. **Request Line:** The initial line defining the action, the resource path, and the protocol version (e.g., `POST /api/data HTTP/1.1`).
2. **Request Headers:** Key-value pairs providing metadata about the client and the payload, such as the host domain, accepted response formats, and user credentials.
3. **Empty Line (CRLF):** A blank line required by the protocol to separate headers from the actual message payload.
4. **Message Body:** The data payload sent to the server (e.g., JSON objects, form field inputs, or file uploads).

---

### Core HTTP Request Methods

The method (or "verb") specifies the action the server should perform on the target resource:

| Method | Action | Common Use Case | Request Body? |
| --- | --- | --- | --- |
| **GET** | Fetches an existing resource | Loading a web page, fetching search results | No |
| **POST** | Creates a new resource or submits data | Submitting a registration form, uploading media | Yes |
| **PUT** | Replaces a resource entirely | Updating an entire user profile record | Yes |
| **PATCH** | Applies partial modifications to a resource | Updating just a user's phone number | Yes |
| **DELETE** | Removes a resource from the server | Deleting an image, deleting an account | Optional |

---

### Key Request Headers

* **`Host`**: Specifies the target server domain name (e.g., `Host: api.example.com`).
* **`User-Agent`**: Identifies the client's browser engine, operating system, and hardware platform.
* **`Authorization`**: Passes authentication credentials (such as Bearer tokens or API keys).
* **`Content-Type`**: Indicates the media format of the request body (e.g., `application/json`, `multipart/form-data`).
* **`Accept`**: Informs the server about the data formats the client can process in return (e.g., `text/html`, `application/json`).

### HTTP Response

An **HTTP response** is the formatted message a web server sends back to a client (such as a browser or mobile application) after receiving and processing an HTTP request.

![HTTP Response](Docs/Assets/Images/HTTP%20Response%20Components.webp)

---

### Components of an HTTP Response

An HTTP response message consists of four primary parts:

1. **Status Line:** The opening line containing the protocol version, a 3-digit numerical status code, and a text phrase describing the outcome (e.g., `HTTP/1.1 200 OK`).
2. **Response Headers:** Key-value pairs containing metadata about the server, connection, and payload (e.g., caching rules, content formatting, security policies).
3. **Empty Line (CRLF):** A required blank line separating the headers from the body payload.
4. **Response Body:** The actual requested data payload sent back to the client—such as HTML markup, CSS stylesheets, JavaScript files, JSON data, or media files.

---

### HTTP Status Code Categories

The **status code** is a 3-digit number indicating whether a specific request was successfully completed, redirected, or encountered an error.

| Category | Range | Description | Common Examples |
| --- | --- | --- | --- |
| **1xx Informational** | 100–199 | Request received; process is continuing | `100 Continue`, `101 Switching Protocols` |
| **2xx Success** | 200–299 | Action was successfully received, understood, and accepted | `200 OK`, `201 Created`, `204 No Content` |
| **3xx Redirection** | 300–399 | Further action must be taken to complete the request | `301 Moved Permanently`, `302 Found`, `304 Not Modified` |
| **4xx Client Error** | 400–499 | Request contains bad syntax or cannot be fulfilled | `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found` |
| **5xx Server Error** | 500–599 | Server failed to fulfill an apparently valid request | `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable` |

---

### Key Response Headers

* **`Content-Type`**: Tells the browser how to render the body payload (e.g., `text/html; charset=utf-8` or `application/json`).
* **`Set-Cookie`**: Sends session identifiers or tracking tokens to be stored in the browser.
* **`Cache-Control`**: Specifies how long browsers or proxy servers may cache the response before fetching a fresh copy.
* **`Access-Control-Allow-Origin`**: A CORS (Cross-Origin Resource Sharing) header that specifies which external domains are permitted to access the resource.
* **`Server`**: Displays information about the software running on the host web server (e.g., `nginx` or `Apache`).

---

Next: [[Scraping]]