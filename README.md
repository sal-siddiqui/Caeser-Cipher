# **Ceaser Cipher**

<p align="center">
  <img src="./imgs/caesar-cipher-illustration.gif" alt="CANNOT DISPLAY IMAGE"/>
</p>

## Overview

**What is the Caesar Cipher?**

The Caesar cipher is an encryption technique where each letter in the alphabet is replaced by another letter that is a fixed number of positions down the alphabet. This process wraps around from Z back to A when necessary.

For example, with a Caesar cipher that has a shift of three:

- A is replaced by D.
- B is replaced by E.
- C is replaced by F.
- and so on.

The shift parameter serves as the key for the Caesar cipher and is used for both encrypting and decrypting texts. By default, the Caesar cipher uses a key of 3.

This method is believed to have been used by Julius Caesar for his private correspondence. However, the Caesar cipher is no longer considered secure, as it can be easily decrypted using brute-force algorithms. Despite its simplicity, it remains an excellent introduction to the world of cryptography and serves as an enjoyable programming exercise.

**Purpose of Program**

* Encrypt files using a specified key.
* Decrypt files using a specified key.
* Decrypt files using brute force.

## Usage

...

## Timeline

- [X] Task 1:

  - [X] Implement internal functions.
  - [X] Implement external functions.
- [ ] Task 2:

  - [ ] Implement Command Line Arguments
    - [ ] Resource 1 ([Link](https://www.youtube.com/watch?v=aGy7U5ItLRk))
    - [ ] Resource 2 ([Link](https://www.cherryservers.com/blog/how-to-use-python-argparse#sub-parsers-in-argparse))
    - [ ] Resource 3 ([Link](https://realpython.com/command-line-interfaces-python-argparse/#defining-mutually-exclusive-argument-and-option-groups))
  - [ ] Implement Brute Force Algorithm
    - [ ] w/ Web Scraping (Find the file with the highest number of matches to a list of most common english words)
    - [ ] w/ Machine Learning Model (Feed decrypted file to a model to determine whether the text is human readable or not)
