This challenge starts off by giving you a PCAP to analyze.
By following the various TCP streams, you can see some various authentication attempts and eventually a successful one under "asmith".
You can see the attacker upload and execute a powershell script and have the compromised device download and execute netcat.
The attacker then proceeds to dump the system registry key and the AD database over port 4443.
You can follow the TCP stream to get the full database and registry key. Copy them and save them.
After all of this, you can see the attacker authenticate as "Administrator" and start using WinRM on the device over the network.
The traffic is encrypted however.
We can use the registry key and the AD DB along with a script called Decrypt-WinRM and pass it the original PCAP to decrypt this data.
I then used the script.py located in this repository to parse through the base64 responses and find the flag.
