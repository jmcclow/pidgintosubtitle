This file strips pidgin logs with timestamps minus the AM/AP on them
File format should look like the following 
(07:32:31) Name: Text
There is an offset, I'll make it a variable and you can offset it there to tell it where to start 00:00:00 
to make it in sync

There's a lot to do, but this is the beginning


Adjust epoch_to_adjust to move the epoch time in reverse from where you are, unless you start exactly at midnight. 
The Year, Month, and Day don't matter. As long as it's in the same day. ;) That's something else to tackle at another time. 
