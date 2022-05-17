# Enhashc

[![python-version](https://img.shields.io/badge/PYTHON-3.9-blue.svg)](https://www.python.org/) [![license](https://img.shields.io/badge/LICENSE-GNU-yellow.svg)](https://github.com/Sup3r-Us3r/HashCode/blob/master/LICENSE)

### About 
This is a python tool to perform various encoding and hashing operations.

### Installation

```
git clone https://github.com/asantoshka/enhashc.git
cd enhashc
pip install -r requirements.txt
python main.py 
```

### Usage

##### Help 

```
$python main.py --help

Commands:
  encode   Performs various types of encoding e.g. Base64, Base32, URL etc.
  hashing  Perfoms various types of hashings such as SHA, MD5 etc
```

##### Encode Help

```
Usage: python main.py encode [OPTIONS]

Options:
  -s, --string TEXT  Enter the string value. However it is optional to use.
  -t, --type TEXT    Type of Encoding. If you don't know what type of hash to
                     use. Simply don't use this option(--type)
  -l, --list         List the available encoding operations
  --help             Show this message and exit.
```

##### Hashing Help

```
Usage: python main.py hashing [OPTIONS]

Options:
  -s, --string TEXT  Enter the string value. However it is optional to use.
  -f, --file TEXT    Enter the file name
  -t, --type TEXT    Type of hash. If you don't know what type of hash to use.
                     Simply don't use this option(--type)
  -l, --list         List the available hashing operations
  --help             Show this message and exit.
```
##### If you don't want to use options

Hashing

```
python main.py hashing       
Enter the string: hello world
The plain text String: hello world
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Type                 ┃ Output                                                                                                                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ md4                  │ aa010fbc1d14c795d86ef98c95479d17                                                                                                 │
│ md5                  │ 5eb63bbbe01eeed093cb22bb8f5acdc3                                                                                                 │
│ sha1                 │ 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed                                                                                         │
│ sa224                │ 2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b                                                                         │
│ sha256               │ b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9                                                                 │
│ sha384               │ fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd                                 │
│ sha512               │ 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f │
│ sha3_224             │ dfb7f18c77e928bb56faeb2da27291bd790bc1045cde45f3210bb6c5                                                                         │
│ sha3_256             │ 644bcc7e564373040999aac89e7622f3ca71fba1d972fd94a31c3bfbf24e3938                                                                 │
│ sha3_384             │ 83bff28dde1b1bf5810071c6643c08e5b05bdb836effd70b403ea8ea0a634dc4997eb1053aa3593f590f9c63630dd90b                                 │
│ sha3_512             │ 840006653e9ac9e95117a15c915caab81662918e925de9e004f774ff82d7079a40d4d27b1b372657c61d46d470304c88c788b3a4527ad074d1dccbee5dbaa99a │
└──────────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Encode

```
python main.py encode  
Enter the string: Hello world
The plain text String: Hello world
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Type                 ┃ Output                       ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ base64               │ SGVsbG8gd29ybGQ=             │
│ base32               │ JBSWY3DPEB3W64TMMQ======     │
│ url                  │ Hello%20world                │
│ hex                  │ 622748656c6c6f20776f726c6427 │
│ reverse              │ dlrow olleH                  │
└──────────────────────┴──────────────────────────────┘
```