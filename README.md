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

### Encryption Process
- **Key 1 and Key 2 Input:**
  - Users provide two keys (k1 and k2), each up to 8 characters long. These keys are critical for the encryption and decryption process, and their security directly impacts the overall encryption strength.

- **Initial Vector (IV):**
  - A random Initial Vector (IV) is generated for the Cipher Block Chaining (CBC) mode. The IV ensures that identical plaintext blocks result in different ciphertext blocks, enhancing security by introducing randomness.

- **Padding:**
  - The plaintext message is padded to make its length a multiple of the DES block size (8 bytes). Padding ensures that the plaintext can be evenly divided into blocks for encryption. Common padding schemes include PKCS7, which adds a specific byte value to the padding.

- **Triple DES Encryption:**
  - **First Pass:** The padded plaintext is encrypted using Key 1 (k1) and the generated IV in CBC mode. This produces the first encrypted block.
  - **Second Pass:** The output of the first pass is decrypted using Key 2 (k2) in CBC mode, effectively adding a layer of transformation to the data.
  - **Final Pass:** The output of the second pass is encrypted again using Key 1 (k1) in CBC mode, producing the final ciphertext.

- **Output:**
  - The IV is prepended to the final ciphertext to ensure that the decryption process can use the same IV for reconstructing the original message. The combined IV and ciphertext are then hex-encoded for easy storage and transmission.

### Decryption Process
- **Extract IV and Ciphertext:**
  - The IV and ciphertext are separated from the hex-encoded input. The IV is essential for initializing the CBC mode for decryption.

- **Triple DES Decryption:**
  - **First Pass:** The ciphertext is decrypted using Key 1 (k1) and the extracted IV in CBC mode. This reverses the final encryption stage of the encryption process.
  - **Second Pass:** The output of the first pass is encrypted using Key 2 (k2) in CBC mode, reversing the decryption stage of the encryption process.
  - **Final Pass:** The output of the second pass is decrypted again using Key 1 (k1) in CBC mode, reversing the initial encryption stage and producing the padded plaintext.

- **Unpadding:**
  - The decrypted plaintext is unpadded to remove the added padding bytes, retrieving the original message in its exact form before encryption. The unpadding process ensures that the data integrity is maintained and the message is correctly reconstructed.

## Implementation

This Python script implements Triple DES encryption and decryption using the Tkinter library for a graphical user interface (GUI).

### Requirements
- **Python 3.9+**: Ensure Python 3 is installed on your system.
- **pycryptodome Library**: Install using `pip install pycryptodome`.
- **Tkinter**: Included with Python installations.

### How to Run

1. Clone the repository or download the script `TripleDESApp.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Execute the script with Python:

```bash
python TripleDESApp.py
```
### How It Works
- **Input Keys**: Enter two keys (each up to 8 characters).
- **File Selection**: Choose the file to be encrypted or decrypted.
- **Encryption**: Encrypt the file using Triple DES with the provided keys.
- **Decryption**: Decrypt the file using the same keys.

### Functions
- **`initialize_gui`**: Sets up the main GUI.
- **`center_window_on_screen`**: Centers the application window on the screen.
- **`add_widgets`**: Adds input fields, buttons, and labels to the GUI.
- **`choose_file`**: Opens a file dialog for file selection.
- **`execute_process`**: Manages encryption or decryption based on user input.
- **`format_key`**: Ensures keys are 8 bytes in length.
- **`perform_encryption`**: Encrypts the file data using Triple DES.
- **`perform_decryption`**: Decrypts the file data using Triple DES.
- **`encrypt_des`**: Performs single DES encryption.
- **`decrypt_des`**: Performs single DES decryption.

### Example Usage

**Input:**
- Enter Key 1 (up to 8 chars): `12345678`
- Enter Key 2 (up to 8 chars): `abcdefgh`
- Select the file to encrypt or decrypt.

**Output:**  
- **Encrypted File:** `file_encrypted.ext`
- **Decrypted File:** `file_decrypted.ext`

GUI: 
![image](https://github.com/aulonalivoreka/TripleDES-2Key-CBC/assets/116767903/3e5b996e-550e-4e47-947e-4a5bed0bbc19)

Output file for encryption:
![image](https://github.com/aulonalivoreka/TripleDES-2Key-CBC/assets/116767903/a4a93f70-21c4-4ed2-bdc4-c39357ad29ab)

Output file for decryption:
![image](https://github.com/aulonalivoreka/TripleDES-2Key-CBC/assets/116767903/e3232acd-e579-4416-ab97-1f010d59502c)

### Notes
- **Security**: Triple DES with 2 keys significantly improves security over single DES.
- **User-Friendly Interface**: The GUI simplifies file encryption and decryption tasks.
- **Flexibility**: Users can select their own keys and files, allowing for customized encryption.
- **Error Handling**: The application handles various user errors gracefully, ensuring a smooth user experience.

### Expected Outcomes
- **Enhanced Security**: Triple DES 2-key mode offers robust security for sensitive data.
- **Usability**: The application is designed to be intuitive and easy to use.
- **Reliability**: Accurate encryption and decryption processes ensure data integrity.
- **Error Resilience**: Built-in error handling ensures reliable operation even with incorrect inputs.


## Performance Metrics

This section provides performance benchmarks for the Triple DES encryption and decryption processes. The metrics include:

- **Encryption Time**: Average time taken to encrypt files of varying sizes, measured in seconds.
- **Decryption Time**: Average time taken to decrypt files of varying sizes, measured in seconds.
- **Memory Usage**: Average memory consumption during the encryption and decryption processes.

These metrics help users understand the resource requirements and performance implications of using this encryption tool in different scenarios.

### Recommendations

We recommend the following best practices for deploying the Triple DES encryption tool:

- Regularly update the encryption libraries to their latest versions to patch known vulnerabilities.
- Avoid using predictable keys and ensure that all keys are securely stored and managed.
- Conduct periodic security reviews and updates to adapt to new threats.

These performance and security sections not only demonstrate the application's reliability but also build trust with end users by showing commitment to quality and security.

## Additional Resources

- [NIST Special Publication on Triple DES](https://csrc.nist.gov/publications/detail/sp/800-67/rev-2/final) - Detailed guidelines and specifications from the National Institute of Standards and Technology.
- [IBM Documentation on Triple DES Encryption](https://www.ibm.com/docs/en/zos/2.1.0?topic=operation-triple-des-encryption) - IBM's comprehensive documentation on Triple DES encryption methods and best practices.





