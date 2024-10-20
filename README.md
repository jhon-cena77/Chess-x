# Chess-x

Supports Leela and Stockfish.

- **Multithreading**: Adjust the number of threads on line 10.
- **RAM Usage**: Depending on your memory, choose the amount of RAM to use (hash size) on line 11 in MB.

By default, I have a very large network. See the system requirements and download a [fitting one for your system](https://lczero.org/dev/wiki/best-nets-for-lc0/).

I only have Leela for CUDA devices, so to get it to run on some systems, you might need new binaries for Leela.

- **Network Adjustment**: Adjust your network for Leela on line 20.
- **Maximum Time**: Adjust the maximum time for Leela to run on line 31. It is recommended to set it to at least 3 seconds or higher.

If you want [my default binaries get them here](https://www.mediafire.com/file/8qbgmlgr5vzy1zu/dependencies.zip/file) note its .7 gb
