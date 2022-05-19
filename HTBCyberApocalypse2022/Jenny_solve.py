from hashlib import sha256

#decrypt plaintext using hash and ciphertext
def decrypt(enc_block, next_hash):
	pt_bytes = []
	for i,eb in enumerate(enc_block):
		if eb < next_hash[i]:
			pt_bytes.append(((eb+256) - next_hash[i]))
		else:
			pt_bytes.append(eb - next_hash[i])
	return bytes(pt_bytes)

#Find first hash using known plaintext and ciphertext
def org_hash(enc, pt):
	digest = []
	for i,eb in enumerate(enc):
		if eb < pt[i]:
			digest.append((eb+256) - pt[i])
		else:
			digest.append(eb-pt[i])
	return bytes(digest)

#combine previous hash with ciphertext to get the plaintext
if __name__ == "__main__":
	enc = bytes.fromhex('0a35079cec4ae6c937455a58c24ff5d43e5f21b5bd069111c9675d900375deb8965016cb7ae1ce601f0cdee83a2f07ef50d24312dfcb76eef7ccc7384869b632375b5db5aad5c37c1f99bcfe74c6f6aaad575bb7d98bfdf5ae4ae99199d5dd0fff2cb0aae6e5db54d04a941c2f9856d547047fca731be8a0bda8ad399a49b0491d58b2843363d232767e267b2d497396796f95f7ec85ddf428ae6aec81a8e59e1b40e10b4478b52a9cd5b2257fbb031d3a97a765c036f3c5350ede7e75317caf66da63397c85b5ef8edcb215729bb22944bd47b0f48095bfb52dfb98e571f194f09ff3d7293bf8b01e461d391a25e687f321d59bfb5e79ff6fae864942f7580a')
	pt_bytes = b'Command executed: cat secret.txt'
	first_hash = org_hash(enc[:32], pt_bytes)
	next_block = pt_bytes
	for i in range(0,len(enc),32):
		next_hash = sha256(enc[i:i+32] + next_block).digest()
		print(next_hash.hex())
		next_block = decrypt(enc[i+32:i+64], next_hash)
		print(f"Next block: {next_block}")
	
