import subprocess
import sys
import cgi

class Poebot:


    def __init__(self, db_file):
        self.name = "Poe"
        self.db_file = db_file
        self.speech_command = ''
        self.users = {}
        self.user_colors = [
            '#EFBD8B',
            '#A3D572',
            '#09CBFE',
            '#6095c5',
            '#FFA7DA',
            '#D370A3',
            '#AC7BDE',
            '#00FF00',
            '#6D9E3F',
            '#FFFFFF'
            ]

    def talk(self, message, user_address, new_color='off'):
        color = ''
        spoken_message = ''
        full_command = ''
        try:
            if not new_color:
                color = self.users[user_address]
            else:
                del self.users[user_address]
                color = self.colorize_user(user_address)
        except KeyError:
            self.colorize_user(user_address)

        full_command = self.speech_command + ' ' + message

        subprocess.Popen( full_command.split() );

        spoken_message = '<span style="color:' + color + '">' + cgi.escape(message) + '</span>'
        self.save(spoken_message)
        print message
        return color

    def colorize_user(self, user_address):
        color = self.user_colors.pop()
        self.users[user_address] = color
        self.user_colors.insert(0, color)
        return color

    def save(self, data):
        f = open(self.db_file, 'a')
        f.write('%s <br>' % data)
        f.close()

    def set_command(self, command):
        self.speech_command = command
