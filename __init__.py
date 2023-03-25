from mycroft import MycroftSkill, intent_file_handler


class FlagGame(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('game.flag.intent')
    def handle_game_flag(self, message):
        self.speak_dialog('game.flag')


def create_skill():
    return FlagGame()

