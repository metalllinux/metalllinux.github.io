---
title: "Configure Key Based Authentication For Ssh"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "configure", "key", "based", "authentication"]
---

* Multiple ways to authenticate via SSH.
	* The two most common are passwords and private-public key pairs.
* How to generate the private-public key pair:
	* Generate the key pair using the ssh-keygen command.
		* `ssh-keygen`
			* Select the defaults when prompted.
				* This then creates RSA private and public keys.
					* Can verify this by listing the hidden `.ssh` directory.
						* `ls -l ~/.ssh`
							* Here we see a file named `id_rsa`
								* This is the private key.
							* `id_rsa.pub`
								* This is the public key.
									* This then needs to be copied to any other machines you want to access the main machine from.
										* Can copy this key using its hostname.
											* `ssh-copy-id rhhost2`
												* Type in `user1`'s password on `rhhost2`
										* To make sure the key is added to the local ssh agent (this is the one that manages the keys), type in `ssh-add`.
											* When using `ssh-copy-id`, two things happen: A) The local public key is copied across the network to the remote end and stored in the user's authorised keys file. B) The fingerprint of the remote server, is stored in the local known host file.
												* This local known host file, is called `~/.ssh/known_hosts`
													* The file stores the IPs of the remote servers, as well as their matching fingerprints.
														* If the remote server ever changes its IP address, need to delete its line for this file, before connecting again.
															* The `id_rsa.pub` file from the main machine, will be the same as the `~/.ssh/authorized_keys` file on other machine that is connecting in.
																* We can also manually append any ssh public key to the `authorized_keys` file using a redirect.
																	* Best to let the `ssh-copy-id` command do this for us however.
																		* SSH is very picky about file permissions and syntax.
* 