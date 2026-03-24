---
title: "Securely Transfer Files Between Systems"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "securely", "transfer", "files", "between"]
---

scp [options] <source file> <destination file>
* scp = Secure Copy 
* Several ways to transfer files from one host to another using an encrypted tunnel.
* Source and Destination Files as shown above, may include the hostname or IP address. For example:
	* `scp /etc/hosts 192.168.1.247:/tmp`
		* Copies the host file to a remote server.
	* Can copy a remote file to the local location, by reversing the arguments:
	 `scp 192.168.1.247:/etc/hosts /tmp`
* By default, SCP uses a standard SSH port number of `22`.
	* If the remote server uses a non-standard port, have to specify this is a `-P`.
		* For example `scp -P 1022 192.168.1.247:/etc/hosts /tmp`
			* Slightly different than using `ssh`, which uses a lowercase `-p`.
				* With `scp`, the `-p` is used to preserve permissions.
					* For example `ssh -p 1022 192.168.1.247`
* We can also copy recursively using the `-r` option.
	* Example: `scp -r 192.168.1.247:/etc /tmp`
		* Since speed may be of interest, we may want to change the cipher.
			* We can do this by passing `-c`.
				* In the above example with `-r`, we were using the RC4 cipher, instead of the default `AES` cipher.
					* The RC4 cipher is an insecure cipher, but much faster than AES.
						* Only use this cipher when copying non-sensitive data or if you're copying on a trusted network.
							* For very slow networks, we can turn on compression by using the `-z` option.
								* Only use this on very slow networks and only if the data is compressable/not already compressed.
									* An example of this is `scp -p -c arcfour -r 192.168.1.247:/etc /tmp`
* The `-p` option preserves file ownership, timestamps and permissions. It does NOT preserve file ACLs or SELinux security context.
* A more powerful tool that still uses an SSH tunnel is `rsync`.
	* rsync syntax is a little more complicated, but worth it.
* Rsync will get a list of the files needed to copy and only copy the missing files.
	* Even if a file is in a broken state, `rsync` is smart enough to re-copy it.
		* A good example: `rsync -av -HAX --progress /etc 192.168.1.247:/tmp`
			* The `-a` option copies recursive and preserves permissions, ownership and symbolic links. It does NOT copy hard links. It does NOT preserve ACLs, extended attributes or SELinux Security Context.
				* For the above not included items, we need to add `-H` for hard links, `-A` for ACLs and `-X` for extended attributes (including SELinux security context as well).
					* `--progress` is good and shows you excellent process information.
* With `scp`, paths with a `/` or a trailing `/` are the same.
	* `rsync /etc` --> Copies the `/etc` directory.
	* `rsync /etc/` --> Copies the contents of the `/etc` directory.
* rsync has a `--dry-run` option to test commands with before copying anything. 
	* Worth doing a `--dry-run` first, to make sure the files get copied where they are needed.
		* Since rsync uses `ssh`, we can pass options such as different port numbers of ciphers to it.
			* An example of this is `rsync -av -e "ssh -p 1022" /etc 192.168.1.247:/tmp`
				* Can also add other options inside the quotes, such as `-c arcfour` for the RC4 cipher.
					* Rsync also has the option to mirror directories and delete files if they don't exist on the source and vice versa. 
					* Check the `man` page for this one.
						* We can also send files, by piping them through an ssh tunnel
						* An example is `cat ~/.ssh/id_rsa.pub | ssh 192.168.1.247 "cat - >> ~/.ssh/authorized_keys"`
							* The above outputs the pubic key, pipes it into the remote host and then executes the command between double quotes.
								* The above command is reading standardin and appending information to the file.
* Duplicating a disk through ssh:
	* dd if=/dev/sdb | ssh 192.168.1.247 "dd of=/dev/sdb"
* Can also copy files from one host to another using SFTP.
	* This is like FTP and uses an encrypted ssh tunnel.

			



 