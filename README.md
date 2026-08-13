# in-case-of-emergency

_Shell commands are for nu-shell._

## Decrypt

```shell
(gpg
    --decrypt
    --output ./decrypted/ice.tar
    ./encrypted/ice.tar.gpg)
```


-----

## Every year or so

### Archive

```shell
(tar
    --create
    --strip-components 1
    --file ./archived/ice.tar
    ./raw/*)
```

### Encrypt

```shell
(gpg
    --symmetric
    --output ./encrypted/ice.tar.gpg
    --compress-level 6
    ./archived/ice.tar)
```


