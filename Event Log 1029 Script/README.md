The EID1029 Script is meant to help find the username associated with the RDP Event Log ID 1029.

In the Event Log, the username is encoded in UTF-16le and then hashed with SHA-256 then base64 encoded.

We can't reverse a hash, but we can enumerate all the users from the device and compile them into a list.
Ensure each username is on its own line and appended to a text file.

The script will run each username through the same calculation that the Event Log does and compare the results.

With a match, it will return the username associated with the Event Log ID.
