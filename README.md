# topN

Prints the top `N` numbers from an arbitrarily large file consisting of
individual numbers each line.

### Dependencies

```bash
$ pip3 install -r requirements.txt
```
May need `sudo -H` or `--user` if not in a
[virtualenv](https://virtualenv.pypa.io/en/stable/)

### Usage
```bash
$ mpirun [ options ] python3 topN.py file.txt N
```
