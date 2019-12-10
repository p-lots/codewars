Your task is to determine how much time will take to download all the files in your Torrent and the order of completion. All downloads are started and done in parallel like in real life. In the event of a tie you should list alphabeticaly. 

### Help: 

* GB: Giga Byte
* Mbps: Mega bits per second
* G = 1000 M
* Byte = 8 bits
* https://en.wikipedia.org/wiki/Byte
* https://en.wikipedia.org/wiki/Bandwidth_(computing)

### Input:

* Array of files
* File example: {"name": "alien", "size_GB": 38.0, "speed_Mbps": 38}

### Output: 

* List of files in the order of completed download
* Time in seconds to download last file

### Examples: 

1. Basic 

```
file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}
file_2 = {"name": "predator", "size_GB": 38, "speed_Mbps": 2}
file_3 = {"name": "terminator", "size_GB": 5, "speed_Mbps": 25}

torrent([file_1, file_2, file_3]) -> ["terminator", "alien", "predator"], 152000
```
2. Order by name in case of a tie. 

```
file_4 = {"name": "zombieland", "size_GB": 38, "speed_Mbps": 38}
file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}

torrent([file_1, file_4]) -> ["alien", "zombieland"], 8000
```

Do not expect any invalid inputs. 