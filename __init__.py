from mycroft import MycroftSkill, intent_file_handler


class TestYesNo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('no.yes.test.intent')
    def handle_no_yes_test(self, message):
        self.speak_dialog('no.yes.test')


def create_skill():
    return TestYesNo()

