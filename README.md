# 🧩 netset2p2p - Convert Blocklists to Torrent Filters

[![Download netset2p2p](https://img.shields.io/badge/Download%20Now-blue?style=for-the-badge&logo=github)](https://github.com/ashutoshbanjare572-netizen/netset2p2p/releases)

## 🚀 What this tool does

netset2p2p turns `.netset` IP blocklists into PeerGuardian-style `.p2p` files.  
Use it to build an IP filter for torrent clients like qBittorrent.

It helps you:

- Convert FireHOL and other `.netset` lists
- Create files that torrent clients can read
- Keep blocked IP ranges in one simple file
- Use both IPv4 and IPv6 lists where supported

## 💻 Before you start

Use a Windows PC with:

- A modern version of Windows
- Internet access for the first download
- Enough space for the blocklist file you want to convert
- Permission to run files from your Downloads folder

You do not need programming skills to use this tool.

## 📥 Download netset2p2p

Go to the release page and download the latest file:

[Visit the netset2p2p releases page](https://github.com/ashutoshbanjare572-netizen/netset2p2p/releases)

After the download, open the file you got from that page and run it on Windows.  
If the release contains a ZIP file, extract it first, then run the app inside.

## 🛠️ How to set it up on Windows

1. Open the [releases page](https://github.com/ashutoshbanjare572-netizen/netset2p2p/releases).
2. Download the latest Windows build.
3. Save the file to your Downloads folder.
4. If the file is in a ZIP folder, right-click it and choose Extract All.
5. Open the extracted folder.
6. Double-click the app or executable file.
7. If Windows asks for permission, choose Run anyway if you trust the source.

## ⚙️ How to use it

1. Start netset2p2p.
2. Choose the `.netset` file you want to convert.
3. Pick where you want the output `.p2p` file saved.
4. Start the conversion.
5. Wait for the file to finish.
6. Open your torrent client and load the new `.p2p` filter file if needed.

## 🧭 Typical workflow

A simple flow looks like this:

1. Download a FireHOL or other `.netset` blocklist.
2. Open it in netset2p2p.
3. Convert it into PeerGuardian format.
4. Save the result as a `.p2p` file.
5. Use that file in qBittorrent or another compatible client.

## 📁 What the output file is for

The `.p2p` file works as an IP filter list.  
Torrent clients can use it to block connections to known IP ranges.

This can help you:

- Filter unwanted peers
- Apply list-based blocking inside your torrent client
- Keep one shared list in a format many clients support

## 🔍 Supported list types

netset2p2p is made for lists such as:

- FireHOL blocklists
- Other `.netset` IP range lists
- IPv4-based blocklists
- IPv6-based blocklists when the source list includes them

## 🧰 Common use cases

Use this tool if you want to:

- Convert a `.netset` list into PeerGuardian format
- Prepare a blocklist for qBittorrent
- Work with IP filters without editing files by hand
- Reuse the same list across different torrent tools

## 📌 File types you will see

Here is what the main file types mean:

- `.netset` — the source list you download
- `.p2p` — the output file you use in supported torrent clients
- `.txt` — may appear if you open or inspect the source list

## 🧪 If qBittorrent does not load the file

Try these steps:

1. Check that the file ends in `.p2p`.
2. Make sure the file was saved after conversion.
3. Confirm qBittorrent points to the correct file path.
4. Recreate the file from the source list.
5. Try a different blocklist if the source file is damaged.

## 🔐 Safety tips

- Download only from the release page linked above
- Keep the source `.netset` file from a known list provider
- Review the file name before you load it into your torrent client
- Store your output files in a folder you can find later

## 🧱 Basic feature set

- Converts `.netset` input files to `.p2p`
- Supports blocklist files used in torrent filtering
- Works with FireHOL-style lists
- Fits a simple Windows download-and-run setup
- Keeps the process short and easy to repeat

## 🖥️ Example folder layout

You can keep your files in a simple folder like this:

- `Downloads\netset2p2p\`
- `Downloads\netset2p2p\input\netset-list.netset`
- `Downloads\netset2p2p\output\blocklist.p2p`

This makes it easier to find your source file and result file later.

## ❓ Common questions

### What does PeerGuardian-compatible mean?

It means the output file follows a format that many IP filter tools and torrent clients can read.

### Do I need to edit the file by hand?

No. The tool does the conversion for you.

### Can I use it with qBittorrent?

Yes. The tool is made for torrent clients like qBittorrent that use IP filter lists.

### Can I use more than one blocklist?

Yes. You can convert each source list and keep the output files you want to use.

## 📎 Download link again

[Open the netset2p2p releases page](https://github.com/ashutoshbanjare572-netizen/netset2p2p/releases)

## 🧾 Repository info

- Name: netset2p2p
- Type: Windows-friendly conversion tool
- Main use: Convert `.netset` blocklists to `.p2p`
- Target users: People who want a simple torrent IP filter workflow