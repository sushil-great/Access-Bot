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

        self.log_channel_id = -100
        self.control_group_id = -100
        self.group_neccessary = -100
        self.google_group_link = "https://groups.google.com/g/<GroupName>"
        self.invite_channel_link = "@ChannelUsername"
        self.help_group_link = "t.me/ChannelUsername"

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

config = Config()
