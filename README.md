Loading Text Generator V0.1
=======

## Python script that cycles through custom loading texts in OBS

This was a simple exercise for me to add something interesting into my
twitch stream whilst getting to grips with python. Please feel free to use,
modify and update it with any new features you'd like! Would love to have more
done with it.

The folder contains 3 text files:

## allmessages.txt

This contains all the potential messages you would like to use for loading text.
Each line is a new message with the message and author separated by a semi-colon
(';'). For example:

`Boiling kettle;somedude
Eating hotpot;anotherguy`

## author.txt

This is where the authors of the current message will be. To add them to OBS, add
a text source that will read from this file.

## titlecard

This is where the current message will be. To add them to OBS, add a text source
that will read from this file.

If you would like to change the timings on the messages and the full stops, open
_textchange.py_ with any text editor and change the variables `timeToRefresh` and
`timeForBullet`. These variables are in seconds.

---

_Current bugs to fix and features to add_
* Author and message do not change at the same time, potentially OBS' refresh rate.
* Easier addition of messages to list.
* UI for easier use.