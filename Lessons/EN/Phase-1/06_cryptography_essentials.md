# Stage 6: Cryptography Essentials

## What Cryptography Does

Cryptography is the practice of using mathematics to protect information. In cybersecurity it primarily supports:

- **Confidentiality** — keeping data unreadable to unauthorized parties
- **Integrity** — detecting whether data has been altered
- **Authentication** — proving identity or origin
- **Non-repudiation** — making it difficult to deny an action

You do not need to understand the advanced mathematics. You only need to understand the main concepts and what problems each technique solves.

## Core Building Blocks

### Encryption and Decryption

- **Encryption** turns readable data (**plaintext**) into unreadable data (**ciphertext**).
- **Decryption** reverses the process, turning ciphertext back into plaintext.

Two main families exist:

#### Symmetric Encryption
The same secret key is used to encrypt and decrypt.  
Analogy: a single key that both locks and unlocks a box.  
Strength: fast.  
Challenge: securely sharing the key with the intended recipient.

#### Asymmetric Encryption (Public-Key Cryptography)
Uses a pair of keys:
- A **public key** that can be shared widely
- A **private key** that must be kept secret

What one key encrypts, only the matching key can decrypt.  
Analogy: a padlock that anyone can snap shut (public key), but only the owner of the matching key can open (private key).

Asymmetric cryptography is slower, so it is often used to protect a temporary symmetric key, which then encrypts the actual data.

### Hashing

A **hash function** takes input of any size and produces a fixed-size “fingerprint.”

Important properties (conceptual):
- Same input always produces the same output
- Tiny change in input produces a completely different output
- It is designed to be extremely difficult to reverse (you cannot get the original data back from the hash)

Hashes are used to:
- Verify file integrity
- Store passwords safely (you store the hash, not the password itself)
- Support digital signatures

### Digital Signatures

A digital signature combines hashing and asymmetric cryptography to provide:
- Integrity (the data has not changed)
- Authentication (it came from the claimed sender)
- Non-repudiation (the sender cannot easily deny it)

## Encryption in Transit vs. Encryption at Rest

- **In transit** — data is protected while moving across a network (e.g., HTTPS for websites).
- **At rest** — data is protected while stored on disk or in a database.

Both are important. Protecting data only while it moves still leaves it exposed when it is sitting still, and vice versa.

## Certificates and Trust

On the public internet, systems use **digital certificates** to prove identity. These certificates are issued by trusted organizations called Certificate Authorities. Your browser or operating system comes with a list of authorities it trusts. This system underpins the padlock icon you see on secure websites.

## Practical Takeaways for Beginners

- Encryption is powerful but only as strong as the protection of the keys.
- Hashing is one-way; encryption is two-way (with the right key).
- Modern systems almost always use a combination of techniques rather than a single algorithm in isolation.
- Cryptography can protect data, but it cannot protect against every threat (for example, if an attacker already has legitimate access, encrypted data may still be readable to them).

---

**Next stage:** High-level view of where systems are typically exposed.