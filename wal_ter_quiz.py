# How well do you know Wal Ter?
from questions import Question

prompts = [
    "How old is Jimi Hendrix?\n (1) 420\n (2) 71\n (3) As old as the observable universe\n\n", 
    "Who organized the 52-53 Students Actions?\n (1) Maurizione\n (2) Uncle Gaetano\n (3) Wal Ter\n\n",
    "Which criminal organization does Clan Mulielo belong to?\n (1) Stidda\n (2) Cosa Nostra\n (3) Camorra\n\n", 
    "Are you Wal Ter or do you eat stones???\n (1) mlmlml stones\n (2) Of course I'm Wal Ter\n (3) I'm Maurizione\n\n", 
    "Wal Ter è proprio...\n (1) Contento\n (2) nu malantrinu!!!\n (3) pAZZO\n\n", 
    "Who's the only person who can challenge Wal Ter in a speed contest?\n (1) Zeb89\n (2) Mahmood Soldi\n (3) John Cena\n\n",
    "Which anime characters better represent Clan Mulielo's lifestyle?\n (1) Biker Mice\n (2) Ninja Turtles\n (3) Z fighters\n\n",
    "Does Wal Ter watch anime?\n (1) Yes, he's a fucking weeb\n (2) No\n (3) Only if it's hentai\n\n"
]

questions = [
    Question(prompts[0], "2"),
    Question(prompts[1], "2"),
    Question(prompts[2], "2"),
    Question(prompts[3], "1"),
    Question(prompts[4], "1"),
    Question(prompts[5], "3"),
    Question(prompts[6], "1"),
    Question(prompts[7], "1")
]

def score_normalizer(total_score, maximum_original_score, new_max):
    return (total_score/maximum_original_score) * new_max

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    new_score = score_normalizer(score, len(questions), 71)
    print("Your score is " + str(new_score) + " / 71. Just..wow!")

