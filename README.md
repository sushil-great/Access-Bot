# Access Bot

Join [@AccessBotHelp](https://t.me/AccessBotHelp) for help.

## Deploy

1. Import the Repo As you are filling Private Creedentials in config
2. Copy `sample_config.py` to `config.py`
3. Fill out the variables in `config.py`
4. Make the bot admin in log channel, control group and main group
5. Send `/start` in the control group to start the bot
6. You know the rest

### Repl.it

There is a separate branch for [repl.it](https://replit.com) support: [Click Here](https://github.com/akshettrj/Access-Bot/tree/replit)

## Features:

* Detects if the mail is gmail or edu
* Gives you search links and members link based on the email
* Easy keyboard interface, very less commands
* Reply to forwarded messages to reply to original sender
* Ban the spammers using `/ban` command on the forwarded messages
* Keeps a log of the members approved
* Checks if the person is a member of the main group or not
* Turn on/off Bot Invites Using Commands.

## Commands

All these commands work in the **Control Group** (specified in config.py)

* `ban/unban:` Pass in user id (not username) or reply to a forwarded message
* `findmember:` Pass in email id or reply to a message containing email id to get google grp membership search results
* `findreq:` Pass in email id or reply to a message containing email id to get google grp request search results
* `pin:` pin messages
* `purge:` purge messages
* `status:` Check Status of Bot Invites
* `inviteson:` Turn on Bot Invites
* `invitesoff:` Turn off Bot Invites

## Warning

* Any member of the control group can use the bot so make it private and add only trusted members.

- Copyright (©) by Akshett Rai Jindal

TODO:

* [ ] Add help command
