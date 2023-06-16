# Concealed-Cloud-File-System
Concealed-Cloud File System is an encrypted file system designed to securely store data on an untrusted remote server. It ensures data confidentiality and integrity by encrypting files before sending them to the server and using cryptographic protocols and signatures to detect any tampering attempts.

Here's a summary of the key points and features of Concealed-Cloud File System:

Encryption and Confidentiality: Concealed-Cloud encrypts files using the EKAES-CBC algorithm. The encrypted file format is referred to as a secure file, which includes both the encrypted content and a cryptographic signature to detect any changes.

Key Management: Each file in  has a set of keys for AES-CBC encryption and RSA validation. These keys are randomly generated on the client-side and stored in a secure keychain file on the untrusted server. The keychain file is encrypted and signed using the user's password and salt.

Sharing and Access Control: Concealed-Cloud File-system allows file sharing with other users while maintaining access control. By sharing the appropriate keys from the keychain file, users can grant read or write permissions to other users. Mandatory Access Control (MAC) policies are enforced by selectively sharing the necessary keys.

Directory Support: Concealed-Cloud File-system supports directories and tracks their contents. It maintains a directory content file, which acts as a reference for verifying the server's directory contents. Encryption is applied to directory names, and any changes to the directory contents are detected through cryptographic verification.

Renaming and Deleting Files: When renaming or deleting files, Concealed-Cloud File-system updates the directory content file accordingly to ensure consistency between the server and the client. Any discrepancies in the directory contents indicate unauthorized changes.

Security Measures: Concealed-Cloud File-system  protects against unauthorized behavior by the untrusted server or user. The server cannot access the plaintext keys or modify encrypted files without triggering cryptographic verification failures. Users with limited privileges have restricted access to prevent malicious actions.

Detection of Unauthorized Actions: Concealed-Cloud File-system  employs cryptographic signatures and verification steps to detect unauthorized changes to files and directories. If the server or user attempts to modify encrypted files or tamper with signatures, the changes will be detected.

Handling Incorrect Files: Concealed-Cloud File-system  can identify situations where the server supplies the wrong secure file. By requesting the corresponding keychain file along with the file itself, Dark Cloud compares the received keys with the expected ones. Inconsistencies indicate incorrect files.

Overall, Concealed-Cloud File system provides a secure and encrypted file storage solution, ensuring data confidentiality, integrity, and controlled access in an untrusted server environment.
