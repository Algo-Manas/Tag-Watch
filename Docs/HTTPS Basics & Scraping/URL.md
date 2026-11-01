A **URL** (Uniform Resource Locator) works just like a magic delivery instruction telling a driver exactly how to travel, which building to visit, which room to walk into, and which toy to pick up.

![URL](<Docs/Assets/Images/Components%20of%20A%20URL.jpg>)

---

### The Toy Store Analogy

Imagine you want a specific blue teddy bear sitting on shelf #3 inside a giant toy building across town. Here is how your URL address, `[https://blog.example.com:443/path/to/page?search=query#section](https://blog.example.com:443/path/to/page?search=query#section)`, breaks down:

* **`https://` (The Armored Delivery Van):** This tells the driver *how* to travel. Regular `http://` is an open bicycle basket, but `https://` is a locked armored car so nobody can peek at your letter along the way.
* **`blog` (The Department Building):** The specific section of a big company—like going straight to the "Toy Zone" building before entering the main company.
* **`example` (The Big Store Name):** The main name written on the giant sign outside the store.
* **`.com` (The Town Neighborhood):** Shows what kind of place it is (`.com` means a shop town, `.edu` means a school town, `.gov` means a government town).
* **`:443` (The Door Number):** The exact door number on the side of the building the driver steps through to get inside.
* **`/path/to/page` (The Hallways & Room):** The signs guiding you step-by-step down hallway `path`, into room `to`, up to shelf `page`.
* **`?search=query` (The Sticky Note):** A tiny note attached to your request asking for a specific version (like asking for `?color=blue` or `?size=small`).
* **`#section` (The Bookmarked Spot):** A glowing sticky note that makes your eyes jump straight to one exact spot on that shelf without having to read from the top.

---

### Technical Breakdown

| Component              | URL Part          | Technical Term               | Function                                                                                                   |
| ---------------------- | ----------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Protocol**     | `https://`      | Scheme / Protocol            | Defines the rules and security methods for transferring data (`HTTPS` encrypts web traffic via SSL/TLS). |
| **Subdomain**    | `blog.`         | Subdomain                    | A child domain split off from the primary domain to host separate subsites or services.                    |
| **Domain Name**  | `example`       | Second-Level Domain (SLD)    | The registered, human-readable brand name or site identifier mapped to an IP address.                      |
| **TLD**          | `.com`          | Top-Level Domain             | The highest domain tier, categorizing sites by purpose (`.com`, `.org`) or region (`.uk`, `.in`).  |
| **Port**         | `:443`          | Port Number                  | A logical network gateway on the host server (`443` for HTTPS, `80` for unencrypted HTTP).             |
| **Path**         | `/path/to/page` | Resource Path                | The directory location of the target file, script, or endpoint on the web server.                          |
| **Query String** | `?search=query` | Query Parameters             | Key-value pairs following `?` used to send dynamic data, search inputs, or filters to the server.        |
| **Fragment**     | `#section`      | Anchor / Fragment Identifier | An internal page reference that causes the browser to scroll directly to an HTML element matching that ID. |

### Port Number

- Imagine a server is a giant apartment building with 65,535 front doors. An IP address gets you to the building's front gate, but the port number tells you which specific apartment door to knock on.
- **Why `443` by default?** Imagine every grocery store in town agrees to place their main customer entrance at Door `443`. Because almost every safe website on Earth uses Door 443, your web browser doesn't force you to type :`443` every time—it just walks straight to Door 443 automatically behind the scenes. You only have to type a port number (like `:8080`) if a server decides to put its entrance at a non-standard door.

### DNS

DNS is the contact list on a smartphone. You don't memorize your friend's 10-digit phone number; you just tap "Mom". Computers don't speak human words like `google.com`—they only understand number addresses. DNS looks up `google.com` and instantly tells your computer the exact number code to call.

### IP Address

Your home's unique physical street address. Every single phone, laptop, and web server connected to the internet gets its own unique numeric address so messages know exactly where on Earth to land.

### UDP (User Datagram Protocol)

- Imagine playing catch with water balloons as fast as you can. You keep throwing balloons without waiting to see if your friend caught the last one. If a balloon drops, you don't stop the game—you just throw the next one!
- **Why use it?** Online video games and live streams use UDP because speed matters more than perfection. If one frame of video drops, you don't want your live video to pause while waiting to fetch that missing frame; you just want the newest video instantly. (This is different from **TCP**, which acts like registered mail and double-checks that every single byte arrives safely).

| Concept                    | Technical Term | Technical Definition                                                                                                                                  |
| -------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Door Number**      | Port Number    | A 16-bit integer (0–65535) embedded in packet headers to direct traffic to a specific process or application.                                        |
| **Default Entrance** | HTTPS Port 443 | The standard network port reserved for encrypted HTTP traffic using TLS/SSL protocols.                                                                |
| **Web Contact Book** | DNS            | Domain Name System: a distributed hierarchical database that resolves human domain names to numeric IP addresses.                                     |
| **Street Address**   | IP Address     | Internet Protocol address: a numerical label assigned to every device participating in a computer network.                                            |
| **Fast Throwing**    | UDP            | User Datagram Protocol: a lightweight, connectionless Transport Layer protocol that sends data without connection setup or error-checking handshakes. |

---

Next: [[HTTP]]
