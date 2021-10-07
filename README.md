# Access Bot

## Deploy

1. Fill out the variables in config.py
2. Make the bot admin in log channel, control group and main group
3. Send /start in the control group to start the bot
4. You know the rest

## Features:

* Detects if the mail is gmail or edu
* Gives you search links and members link based on the email
* Easy keyboard interface, very less commands
* Reply to forwarded messages to reply to original sender
* Ban the spammers using /ban command on the forwarded messages
* Keeps a log of the members approved
* Checks if the person is a member of the main group or not

## Commands

All these commands work in the **Control Group** (specified in config.py)

* ban/unban: Pass in user id (not username) or reply to a forwarded message
* findmember: Pass in email id or reply to a message containing email id to get google grp membership search results
* findreq: Pass in email id or reply to a message containing email id to get google grp request search results
* pin: pin messages
* purge: purge messages

## Warning

* Any member of the control group can use the bot so make it private and add only trusted members.

TODO:

* [ ] Add help command
