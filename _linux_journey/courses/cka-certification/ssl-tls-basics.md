---
title: "Ssl Tls Basics"
category: "cka-certification"
tags: ["cka-certification", "ssl", "tls", "basics"]
---

* A certificate is used to guarantee trust between two parties during a transaction.
* When a user attempts to access a server, teh TLS certificates ensure the connection is encrypted and the server says exactly whom it is.
	* Via HTTP, hackers can easily retrieve encryption.
* Must encrypt using a key - a set of random letters and numbers.
	* The user information such as a username and password is then merged with this key.
	* Then it is sent to the server and the hacker can't do anything with it.
	* The server cannot decrypt the sent data without the key.
	* A copy of the key must also be sent to the server.
		* Known as symmetric encryption - using the same key to encrypt and decrypt the data - risk of hacker getting the key in-flight and obtaining the data ¥.
* Asymmetric Encryption
	* Uses a pair of keys - a Private Key and a Public Key.
		* Can also think of it as a Private Key and a Public Lock.
		* If you encrypt data with the Public Lock, you can only decrypt it using a Private Key.
		* No matter what data is locked using the Public Lock, it can only be unencrypted using the Private Key of the user.
* Asymmetric Encryption - `ssh`
	* `ssh-keygen` - creating private and public keys.
	* Secure server by adding your public key (public lock) as an entryway into the server.
	* Can see the list of `public lock`s under the `~/.ssh/authorized_keys` file.
	* Shows `ssh-rsa <string_of_numbers_and_letters> <user>`
	* As long as no one gets access to the `Private Key`, no one else can get access to the server.
	* `ssh -i <path_to_private_key> user@server`
* How do you secure more than 1 server with your key-pair.
	* Can create copies of the public lock and place that on as many servers as required.
* What if other users need access to X servers - they generate their own private-public keypairs.
	* Add the user to the `authorized_keys` file.
* How to setup a private and public keypair on the server?
* Generate the Private Key:
```
openssl genrsa -out <keyname>.key 1024
```
* Generate the Public Key:
```
openssl rsa -in <key-name>.key -pubout > <keyname (different from public key name) > keyname.pem
```
* The server sends the user the public lock.
* The user's browser then encrypts the public key with their private key.
* The symmetric key is now secure and the private and public keys are both sent to the server.
	* This is sent to the server and the hacker receives the key along the way.
		* The hacker does not have the private key to decrypt the symmetric key. Only the public key that they have.
		* The Symmetric Key is only available for the user and the server.
		* The hacker is left with the encrypted messages and public keys.
* In order for the hacker to grab your credentials, they create an identitical website.
	* They generate their own private-public keypairs.
	* They route your DNS request to the hacker's servers.
	* The problem is, the server has to send its public key and the certificate as well to the user.
	* The certificate shows whom it issued to, the public key of the server, the location of the server.
		* Each certificate also has the person it has been issued to.
		* If the bank or organisation wants to have its users access other the same website but under different names, they should add a column under the `Alternative Name` row.
	* Anyone can generate a certificate like this.
		* How do you verify a certificate is from the legitimate website?
			* Who signed and issued the certificate?
			* For self-signed certificates, these are self-generated and are therefore not trustworthy.
			* If you check closely, the certificate will be flagged as un-trustworthy.
* How do you stop your website being flagged with a `Your connection is not private` message or similar?
	* Certificate Authorities - they can sign and validate certificates for you.
		* Popular ones are Symantec, GlobalSign, digitCert etc.
	* The Certificate Authority receives a Certificate Signing Request (CSR) with the key that was generated earlier.
	* Can do this via the following `openssl` command:
```
openssl req -new -key my-bank.key -out my-bank -subh "/C=US/ST=CA/O=MyOrg, Inc./CN=my-bank.com"
```
* Next they Validate Information.
* Finally they sign the certificate and send it back to the user.
	* A hacker would fail at the Validation Phase.
	* The Certificate Authority check to make sure you are the actual owner of the domain.
* What if it is signed by a fake CA ? Someone whom isn't Symmantec for example?
	* Each CA has their own public and private key pair.
		* The CAs use their private key to sign the certificates. The public key of all of the CAs is built into the browsers.
* You can host your own private CAs.
	* Then install the public key of the self-hosted CA into all of the browsers.
* The end user only generates a single symmetric key.
* The server can also request a certificate from a client.
	* This is similarly done with a client reaching out to a CA.
* The whole process above with the certificate requests, sending of certificates between the user and server, is known as PKI or Public Key Infrastructure.
* With Public and Private keys, you can encrypt data with either one of them actually.
	* Then only the data that has been encrypted with one key and be decrypted with another.
	* Be careful, if you encrypt something with your private key, literally anyone whom has access to your public key can decrypt it.
* For certificate (public key) naming, you have the following:
	* `server.crt` and `server.pem` for server certificates.
	* For clients you have `client.crt` and `client.pem`.
* For private key naming, you have these naming schemes:
	* `*.key` and `*-key.pem`
	* `server.key` and `server-key.pem`
	* `client.key` and `client-key.pem`
	* 