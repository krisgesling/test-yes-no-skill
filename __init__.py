from mycroft import MycroftSkill, intent_file_handler


class TestYesNo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        # An arbitrary modification

    @intent_file_handler('no.yes.test.intent')
    def handle_no_yes_test(self, message):
        response = self.ask_yesno('no.yes.test')
        self.log.info('Response: {}'.format(response))
        if not response:
            self.speak_dialog('detected.nothing')
        elif response == 'yes':
            self.speak_dialog('detected.yes')
        elif response == 'no':
            self.speak_dialog('detected.no')
        else:
            self.speak_dialog('detected.other')


def create_skill():
    return TestYesNo()

