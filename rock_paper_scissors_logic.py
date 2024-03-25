# rock_paper_scissors_logic.py

WINNING_ORDER = {"Rock": "Scissors", "Paper": "Rock", "Scissors":"Paper"}
SIGNS = ("Rock", "Paper", "Scissors")
VALID_KEYS = [["A", "S", "D"], ["J", "K", "L"]]

PLAY_TO = 3

class Move:
    def __init__(self, sign, player):
        self.sign = sign
        self.player = player

class RockPapperScissorGame:
    def __init__(self, _signs=SIGNS, _valid_keys=VALID_KEYS, winning_order=WINNING_ORDER, play_to=PLAY_TO):
        self.player_score = [0,0]
        self._has_winner = False
        self.winning_order = winning_order
        self.round_winner = 0
        self.play_to = play_to
        self._signs = _signs
        self._valid_keys = _valid_keys

 
    def reset_game(self):
        self._reset_score()
        self.round_winner = 0
        self._has_winner = False

    def reset_round(self):
        self.p1_move = Move("",0)
        self.p2_move = Move("",1)

    # Process the current move and determines who wins the round, earning 1 point. Check if win
    def round_outcome(self, p1_move, p2_move):
        if p1_move.sign == p2_move.sign:
            self.round_winner = 0
        elif self.winning_order[p1_move.sign] == p2_move.sign:
            self.player_score[0] += 1
            self.round_winner= -1
        elif self.winning_order[p2_move.sign] == p1_move.sign:
            self.player_score[1] += 1
            self.round_winner = 1
          
        is_winner = self.player_score[0] == self.play_to or self.player_score[1] == self.play_to

        if is_winner:
            self._has_winner = True
            self.winner = self.get_winner()

    def get_round_winner(self):
        return self.round_winner
    
    def get_score(self):
        return self.player_score
    
    def _reset_score(self):
        self.player_score= [0,0]
    
    def get_winner(self):
        if self.player_score[0] == self.play_to:
            return 0
        else:
            return 1
    
    def has_winner(self):
        return self._has_winner

    def get_round_sign(self):
        return self.round_sign
    
    def get_play_to(self):
        return self.play_to
    
    def submit_move(self, move):
        if move.player == 0:
            self.p1_move = move
        else: 
            self.p2_move = move


            