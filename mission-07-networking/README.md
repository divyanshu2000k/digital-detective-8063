# Mission 7 - How Computers Communicate

## 1. Task / objective
Define fundamental networking concepts, run privacy-safe connectivity and DNS lookup tests from Terminal, and trace what happens step-by-step when opening a website.

## 2. Work completed
* Completed the networking concepts table with definitions and real-world examples.
* Ran `ping` and `nslookup` against `example.com` and documented the observations without exposing personal IP or Wi-Fi data.
* Wrote a 6-step walkthrough of how a browser loads a web page using client, DNS, router, protocol, and server terminology.

## 3. Commands / tools used
* `ping -c 3 example.com` — Sent 3 ICMP echo requests to test reachability and round-trip latency.
* `nslookup example.com` — Queried DNS to resolve the domain name `example.com` into its public IP address.

## 4. My understanding
### Task 7.1 — Network Concepts
| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN** | A Local Area Network connecting devices within a single building, home, or lab. | Devices connected to a hostel or home Wi-Fi router. |
| **MAN** | A Metropolitan Area Network spanning a city or large university campus. | Interconnected department buildings across a university campus network. |
| **WAN** | A Wide Area Network linking networks across cities, countries, or continents. | The global Internet connecting regional ISPs together. |
| **DNS** | The Domain Name System that translates human-friendly domain names into numeric IP addresses. | Resolving `example.com` to `93.184.216.34`. |
| **Router** | A networking device that forwards data packets between different networks (such as a LAN and the Internet). | A home/campus gateway router directing traffic to an ISP. |
| **Protocol** | A standardized set of rules governing how data is formatted, transmitted, and acknowledged. | HTTPS, TCP/IP, and DNS. |
| **Packet switching** | Breaking data into small numbered packets that travel independently across network paths and reassemble at the destination. | Streaming a video or loading a web page over TCP/IP. |
| **Client-server** | A communication model where a client requests data or a service and a server processes and responds to it. | A web browser (client) requesting a repository page from GitHub's web server. |

### Task 7.2 — Network Observations
* **Connectivity test (`ping -c 3 example.com`):** Checks whether a remote host is reachable over the network, measures round-trip time (latency in milliseconds), and verifies zero packet loss.
* **DNS lookup (`nslookup example.com`):** Displays the DNS resolver used (redacted) and the public IPv4/IPv6 addresses mapped to `example.com` (`93.184.216.34`).
* **Role of DNS in a browser:** Because network routers route packets using IP addresses rather than English words, the browser relies on DNS first to look up the target server's IP address before opening a connection.

### Task 7.3 — What Happens When You Open a Website?
1. **User Request (Client):** You type a URL (such as `https://example.com`) into your web browser, which acts as the **client**.
2. **DNS Resolution:** The browser checks its cache and queries a **DNS** resolver to translate the domain name into the destination **server**'s IP address.
3. **Routing & Connection:** Your device sends packets through your local router across the ISP network to reach that IP address, establishing a reliable connection using the TCP **protocol** (and TLS encryption for HTTPS).
4. **HTTP Request:** Following the HTTPS **protocol**, the **client** sends an HTTP `GET` request asking the **server** for the web page resources.
5. **Server Processing & Response:** The web **server** processes the request and sends back an HTTP response (such as `200 OK`) containing HTML, CSS, and JavaScript split into packets.
6. **Rendering:** Your browser reassembles the incoming packets and renders the visual web page on your screen.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
* `mission-07-networking/README.md`

## 8. Commit details
* **Commit message:** `Explain networking concepts and website communication`
* **Status:** Committed and pushed to GitHub on `main`.
