# Third Project in Data Security 
This project was completed by sophomore students from the Faculty of Electrical and Computer Engineering at the University of "Hasan Prishtina", under the expert guidance of Prof. Dr. Blerim Rexha and Ass. Mërgim Hoti, as part of our coursework in Data Security.

### Authors 

- [Aulona Livoreka](https://github.com/aulonalivoreka)
- [Artina Qorrolli](https://github.com/ArtinaQorrolli)
- [Aulona Ramosaj](https://github.com/aulonaramosaj)
- [Artin Dulahi](https://github.com/ArtinDulahi)


## Triple DES 2-Key CBC Mode Encryption and Decryption

Triple DES (3DES) is a symmetric-key block cipher that applies the DES (Data Encryption Standard) algorithm three times to each data block, enhancing its security compared to single DES. By using two unique keys, Triple DES provides increased protection against brute-force attacks and cryptographic vulnerabilities.


## Structure of the Triple DES 2-Key CBC Mode

Triple DES employs three stages of DES encryption:
- **Encryption: E(k1, D(k2, E(k1, P))):**
  - **First Stage (E(k1, ...)):** Encrypt the plaintext (P) using the first key (k1).
  - **Second Stage (D(k2, ...)):** Decrypt the output of the first stage using the second key (k2).
  - **Third Stage (E(k1, ...)):** Encrypt the output of the second stage using the first key (k1).
 
- **Decryption: D(k1, E(k2, D(k1, C))):**
  - **First Stage (D(k1, ...)):** Decrypt the ciphertext (C) using the first key (k1).
  - **Second Stage (E(k2, ...)):** Encrypt the output of the first stage using the second key (k2).
  - **Third Stage (D(k1, ...)):** Decrypt the output of the second stage using the first key (k1).
