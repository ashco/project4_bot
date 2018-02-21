from random import randint

score_wins = 0
score_losses = 0
score_draws = 0


user_scores = [
  {
    'user': 'U9D7A90VD', 
    'score_wins': 20, 
    'score_losses': 10,
    'score_draws': 0
  },{
    'user': 'ASHMAN', 
    'score_wins': 6, 
    'score_losses': 6,
    'score_draws': 5
  },{
    'user': 'DOBOCHO', 
    'score_wins': 12320, 
    'score_losses': 1233330,
    'score_draws': 4410
  }
]


class Command(object):
    def __init__(self):
        self.commands = {
            "rock" : self.rock_response,
            "paper" : self.paper_response,
            "scissors" : self.scissors_response,
            "score" : self.score_response,
        }

    def handle_command(self, user, command):
        response = "<@" + user + ">: "
     
        if command in self.commands:
            response += self.commands[command](user)
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()
         
        return response
     

    def help(self):
        response = "I am a contraption created to kick your ass at Rock, Paper, Scissors. \nPlease enter one of the following commands:\r\n"
         
        for command in self.commands:
            response += command + "\r\n"
             
        return response


    def rock_response(self, user):
        randnum, choice = self.bot_choice()

        if randnum == 0:
            verdict = 'DRAW'
        elif randnum == 1:
            verdict = 'LOSE'
        else:
            verdict = 'WIN'
        
        return self.verdict_analyzer(choice, verdict, user)


    def paper_response(self, user):
        randnum, choice = self.bot_choice()

        if randnum == 0:
            verdict = 'WIN'
        elif randnum == 1:
            verdict = 'DRAW'
        else:
            verdict = 'LOSE'
        
        return self.verdict_analyzer(choice, verdict, user)


    def scissors_response(self, user):
        randnum, choice = self.bot_choice()

        if randnum == 0:
            verdict = 'LOSE'
        elif randnum == 1:
            verdict = 'WIN'
        else:
            verdict = 'DRAW'
        
        return self.verdict_analyzer(choice, verdict, user)


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

    def verdict_analyzer(self, choice, verdict, user):
        if verdict == 'WIN':
            end_string = 'You win.'
            # global score_wins
            # score_wins += 1
        elif verdict == 'LOSE':
            end_string = 'You lose!'
            # global score_losses
            # score_losses += 1
        else:
            end_string = 'It\'s a draw'
            # global score_draws
            # score_draws += 1

        self.score_logic(verdict, user)

        response_text = 'I choose {}. {}'.format(choice, end_string)

        return response_text


   # SCORE LOGIC
    def score_logic(self, verdict, user):
        global user_scores
        user_index = None

        for i in range(len(user_scores)):
            if(user == user_scores[i]['user']):
                user_index = i

        if verdict == 'WIN':
            # user_score_dict[]
            user_scores[user_index]['score_wins'] += 1
            # print('current wins: ', user_scores[user_index]['score_wins'])
            # score_wins += 1
        elif verdict == 'LOSE':
            # score_losses += 1
            user_scores[user_index]['score_losses'] += 1
            # print('current losses: ', user_scores[user_index]['score_losses'])
        else:
            # score_draws += 1
            user_scores[user_index]['score_draws'] += 1
            # print('current draws: ', user_scores[user_index]['score_draws'])

        # print('Score logic triggered, user is: ', user)


    def score_response(self, user):
        user_index = None

        for i in range(len(user_scores)):
            if(user == user_scores[i]['user']):
                user_index = i

        response = "Here is your record..\nWins: {}\nLosses: {}\nDraws: {}".format(user_scores[user_index]['score_wins'], user_scores[user_index]['score_losses'], user_scores[user_index]['score_draws'])

        return response


# # Returns index of user's score object
# def find_user(user_name):
#   for i in range(len(user_scores)):
#     if(user_name == user_scores[i]['user']):
#       return i

# user_index = find_user('ASHMAN')

# print(user_scores[user_index]['score_wins'])







    # SET UP NEW CONSOLIDATE ROCK PAPER SCISSORS FUNCTION


 