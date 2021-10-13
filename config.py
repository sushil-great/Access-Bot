class Config:

    def __init__(self):

        # Bot Token : String
        self.bot_token = ""

        self.mongodb = {
            "uri": "",
            "username": "",
            "password": "",
            "db_name": ""
        }

        # The emails and the user ids will be forwarded here
        self.log_channel_id = -100

        # The group where the bot will forward the messages and can be controlled
        self.control_group_id = -100

        # The ID of the main group of which the person should be a member to be able to send messages through the bot
        self.group_neccessary = -100

        # The link to the google group
        self.google_group_link = "https://groups.google.com/g/<GroupName>"

        # You can point the members here to get invites to the group
        # NOTE: USE BACKSLASH TO ESCAPE ALL THE UNDERSCORES(_) AS SHOWN BELOW
        self.invite_channel_link = "@Channel\_Username"

        # Group for queries and help
        self.help_group_link = "t.me/Channel_Username"

        # GIFs : List[String]
        self.gifs_for_bans = [
            "https://media.giphy.com/media/xT9IgmYU3ZVaCjGafm/giphy.gif",
            "https://tenor.com/ba6QG.gif",
            "https://tenor.com/N22V.gif",
            "https://tenor.com/view/oh-fuck-off-go-away-just-go-leave-me-alone-spicy-wings-gif-14523970",
            "https://tenor.com/3noS.gif"
        ]
        self.gifs_for_unbans = [
            "https://tenor.com/bsU4Y.gif",
            "https://tenor.com/bwGMw.gif"
        ]
        self.gifs_for_approval = [
            "https://tenor.com/ytWA.gif",
            "https://tenor.com/bmLe6.gif",
            "https://tenor.com/ZYCh.gif",
            "https://tenor.com/Oehp.gif",
            "https://tenor.com/TQ4g.gif",
            "https://tenor.com/EPlH.gif",
            "https://tenor.com/6blS.gif",
            "https://tenor.com/6Qli.gif",
            "https://tenor.com/tY6n.gif"
        ]

        # This photo will be used for the start message in IBs
        self.private_chat_start_image = 'https://i.imgur.com/O0pyAJN.png'

        # Behaviour Configuration

        # Set to True if you want only messages containing email to be forwarded
        self.only_forward_with_email = False

config = Config()
