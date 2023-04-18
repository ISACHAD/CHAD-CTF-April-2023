# Good Streams
**Forensics - Medium**

Wyatt Tauber

## Challenge

Aziraphale's book shop is always such a mess... he always seems to misplace something important right as he needs it. Today, of all days, it's his list of secret books that he only allows other principalities to read. Gabriel is coming for tea and he's sure he'll ask to see it. Worse yet, he doesn't hide this list in any old way, lest a human casually stumble upon it. It's somewhere in his inventory spreadsheet, though, he's sure of that.

**This challenge _must_ be extracted with WinRAR on a Windows system.**

### Hint 1
You did use WinRAR to extract this challenge on a Windows system, right? Good.

There are some *alternate* ways of hiding data on Windows systems specifically.

### Hint 2
[Alternate Data Streams](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/e2b19412-a925-4360-b009-86e3b8a020c8) are a neat way to hide data on a Windows system. They can be viewed easily using PowerShell.

### Flag
```CHAD{7h3_n1c3_4nd_4ccur473_pr0ph3c135}```

## Technique Overview

The CSV data itself isn't actually relevant to this challenge, as the secret books list is hidden in an [alternate data stream (ADS)](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/e2b19412-a925-4360-b009-86e3b8a020c8) of the file.

Alternate data streams can be added to a file by executing the following in a command prompt:

```
echo text > "AZ Fell and Co Inventory.csv":ads_file_name.extension
```

They can be read by running the following command in PowerShell:

```
Get-Content -Path '.\AZ Fell and Co Inventory.csv:ads_file_name.extension'
```

### Solve challenge:

The name of the challenge indicates that the flag is hidden in an ADS. List all the ADSs in the file:

```
PS C:\Users\Wyatt\Documents\streams> Get-item -Path '.\AZ Fell and Co Inventory.csv' -stream * | Select-Object PSChildName

PSChildName
-----------
AZ Fell and Co Inventory.csv::$DATA
AZ Fell and Co Inventory.csv:armageddon_prep.csv
AZ Fell and Co Inventory.csv:best_friends.csv
AZ Fell and Co Inventory.csv:best_teas.csv
AZ Fell and Co Inventory.csv:book_shop_properties.csv
AZ Fell and Co Inventory.csv:crowleys_houseplant_watering_log.csv
AZ Fell and Co Inventory.csv:date_spots_in_london.csv
AZ Fell and Co Inventory.csv:excellent_cheese_shops.csv
AZ Fell and Co Inventory.csv:false_prophets_and_conspiracy_theorists.csv
AZ Fell and Co Inventory.csv:heaven_and_hell_office_locations.csv
AZ Fell and Co Inventory.csv:hellhound_walking_schedule.csv
AZ Fell and Co Inventory.csv:magical_armaments.csv
AZ Fell and Co Inventory.csv:magic_tricks.csv
AZ Fell and Co Inventory.csv:motzart_pieces.csv
AZ Fell and Co Inventory.csv:parts_for_vintage_bently.csv
AZ Fell and Co Inventory.csv:prime_ministers_who_were_actually_lizards.csv
AZ Fell and Co Inventory.csv:principality_tasks.csv
AZ Fell and Co Inventory.csv:secret_books.csv
AZ Fell and Co Inventory.csv:supplies_from_god.csv
AZ Fell and Co Inventory.csv:tailors_from_1200s.csv
AZ Fell and Co Inventory.csv:tailors_from_1300s.csv
AZ Fell and Co Inventory.csv:tailors_from_1400s.csv
AZ Fell and Co Inventory.csv:tailors_from_1400s_new.csv
AZ Fell and Co Inventory.csv:tailors_from_1500s.csv
AZ Fell and Co Inventory.csv:wine_list.csv
AZ Fell and Co Inventory.csv:witchfinder_generals.csv
```

The flag is in ```secret_books.csv```.

```
PS C:\Users\Wyatt\Documents\streams> Get-Content -Path '.\AZ Fell and Co Inventory.csv:secret_books.csv'

CHAD{7h3_n1c3_4nd_4ccur473_pr0ph3c135}
```
