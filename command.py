from random import randint

class Command(object):
    def __init__(self):
        self.commands = {
            "rock" : self.rock,
            "paper" : self.paper,
            "scissors" : self.scissors,
        }

    def handle_command(self, user, command):
        response = "<@" + user + ">: "
     
        if command in self.commands:
            response += self.commands[command]()
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()
         
        return response
     
    def help(self):
        response = "I am a contraption created to kick your ass at Rock, Paper, Scissors. \nPlease enter one of the following commands:\r\n"
         
        for command in self.commands:
            response += command + "\r\n"
             
        return response

    # LOGIC TO DETERMINE BOT CHOICE
    def bot_choice(self):
        randnum = randint(0, 2)

        if randnum == 0:
            choice = 'rock'
        elif randnum == 1:
            choice = 'paper'
        else:
            choice = 'scissors'

        return (randnum, choice)


    def rock(self):
        randnum, choice = self.bot_choice()

        if randnum == 0:
            verdict = 'It\'s a draw.'
        elif randnum == 1:
            verdict = 'I win!'
        else:
            verdict = 'I lose.'
        
        response = 'I choose {}. {}'.format(choice, verdict)
        return response


    def paper(self):
        randnum, choice = self.bot_choice()

        if randnum == 0:
            verdict = 'I lose.'
        elif randnum == 1:
            verdict = 'It\'s a draw.'
        else:
            verdict = 'I win!'
        
        response = 'I choose {}. {}'.format(choice, verdict)
        return response


    def scissors(self):
        randnum, choice = self.bot_choice()

        if randnum == 0:
            verdict = 'I win!'
        elif randnum == 1:
            verdict = 'I lose.'
        else:
            verdict = 'It\'s a draw.'
        
        response = 'I choose {}. {}'.format(choice, verdict)
        return response