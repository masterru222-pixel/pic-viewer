# Deads

# 💀 Discord Logger
The Deads project is a Discord logging tool designed for educational purposes to demonstrate how image-based tracking works on Discord. It shows how clicking "Open Original" on an image can leak IP information and browser details.

The primary objective of Deads is to educate students about online privacy and security risks when sharing media on platforms like Discord.

---

# 📚 Table of Contents
* [Introduction](#-discord-logger)
* [Features](#-features)
* [Configuration](#-configuration)
* [Setup](#%EF%B8%8F-setup)

---

# 💎 Features
* Fast, Free, and Easy!
* Educational demonstration tool
* Shows how IP logging works through Discord's Open Original feature
* Demonstrates metadata collection including IP, location, browser info

---

# 🔧 Configuration

Before setting it up, let's modify the **config.**
Open up `main.py` and edit the values, refer to the key below.

**WEBHOOK:** `Your Discord webhook!`
**IMAGE:** `A LINK to your desired Image.`
**IMAGEARGUMENT:** `Enable image reading from the argument. (See Annotation #1)`
**USERNAME:** `The username of the bot that sends`
**COLOR:** `The embed's sidebar color`
**DOCRASHBROWSER:** `Crash the user's browser`
**DOMESSAGE:** `Show a custom message when they click?`
**MESSAGE:** `The message to show.`
**RICHMESSAGE:** `Enable a rich message, which allows inserting variables. (See Annotation #2)`
**VPNCHECK:** `Prevent VPNs from spamming your webhook!`
**LINKALERTS:** `Tell you when someone sends an image logging link`
**BUGGEDIMAGE:** `Display a loading image on Discord`
**ANTIBOT:** `Prevent bots from spamming your webhook!`
**REDIRECT:** `Redirect user?`
**PAGE:** `Page to redirect to, if so`

**ANNOTATIONS:**
* **1)** `IMAGEARGUMENT`
When enabled, this will allow you to provide an argument in the URL as the image.
You can do this by URL-safe Base64 encoding a link, and supplying it as the `URL` or `ID` argument.
EXAMPLE: `https://your.site/api/main?url=aHR0cHM6Ly8...`
The above Base64 is cut off short, but it would lead to a URL of an image.
If it's enabled and no `URL` or `ID` argument is supplied, the default configured one will be used.

* **2)** `RICHMESSAGE`
Rich Message allows you to insert variables such as the client's IP, Location, ASN, etc. for the Crashbrowser message.
Simply insert anything in the following table and it will replace it respectively.

| Values |
|--------|
| `{ip}` Their IP Address. |
| `{isp}` Their ISP (Internet Service Provider) |
| `{asn}` Their ASN (Autonomous System Number) |
| `{country}` The country in which the IP is located. |
| `{region}` The region in which the IP is located. |
| `{city}` The city in which the IP is located. |
| `{lat}` The IPs latitude. |
| `{long}` The IPs longitude. |
| `{timezone}` The timezone of the IP. |
| `{mobile}` If it's a mobile connection. |
| `{vpn}` If the IP belongs to a VPN/Proxy. |
| `{bot}` If the IP is a robot. |
| `{browser}` The Browser of the client. |
| `{os}` The OS of the client. |

---

# ⚒️ Setup

Now that you've got all that set up, let's install this thing!

- **1:** Create a GitHub repository. I recommend it be private.
- **2:** Make a folder named `Logger`, and place `requirements.txt` and `main.py` in it.
- **3:** (Optional) make a file in the main root (NOT IN Logger) named `index.html`, and put the code below in:
```html
<meta http-equiv="refresh" content="0;url=./Logger/main.py">
```
- **4:** Visit https://vercel.com and log in with GitHub.
- **5:** Click *add new* to make a new project. Select the GitHub repository you made.
- **6:** Copy the domain and add `/Logger/main` to it.

---

---

## About
Educational tool for demonstrating Discord image logging concepts.
