# in-case-of-emergency

-----

# Archive

```shell
(tar
    --create
    --strip-components 1
    --file ./archived/ice.tar
    ./data/*)
```


# Encrypt

```shell
(gpg
    --symmetric
    --output ./encrypted/ice.tar.gpg
    --compress-level 6
    ./archived/ice.tar)
```


# Decrypt

```shell
(gpg
    --decrypt
    --output ./decrypted/ice.tar
    ./encrypted/ice.tar.gpg)
```

