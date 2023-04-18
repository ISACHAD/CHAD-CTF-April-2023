# Golden Files
**Forensics - Easy**

Wyatt Tauber

## Challenge

Census instructions are so confusing. How am I even supposed to read this???

### Hint 1
The `file` command is a built-in Linux command for identifying files that don't have Windows-like extensions. Most importantly, it reads the file's hex [signature](https://en.wikipedia.org/wiki/List_of_file_signatures) ("magic bytes") at the start of the file to determine what kind of file it is.

Try running `file C` to see what kind of file this is and what you can do with it.

### Flag
```CHAD{bl44rfl44g44r_sp3ll3d_L-3-3_S-M-1-T-H}```

## Technique Overview
This is a series of archive files with their extensions removed. The names of the files contain the flag.
* C.tar
  * H.rar
    * A.7zip
      * p44ssw44rd.txt (contains text "betty")
      * D{.zip (encrypted)
        * bl44rfl44g44r_.txt
          *  Contains text "sp3ll3d_L-3-3_S-M-1-T-H} and "https://youtu.be/vW_qm_z09mo"

The YouTube link is irrelevant, it's just for fun.

### Solve challenge:

First use the ```file``` command to identify the first file format (tar).

* Simple method: Use 7zip to browse into the archives and assemble the flag.

* Tedious method: Use the ```file``` command to identify and then extract each archive format individually using tar, unrar, 7zip, and unzip to assemble the flag.
