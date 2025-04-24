# drill_instructor.py — Defines the Drill Instructor assistant persona (Marine style)

class DrillInstructor:
    def __init__(self):
        self.name = "Drill Instructor"
        self.description = "A tough Marine motivator who will keep your trades tight and your discipline tighter."
        self.voice_style = "intense"
        self.mood = "hardcore"

    def greet(self):
        return "Listen up, Devil Dog! You’re not here to lose — you’re here to execute with precision and guts!"

    def get_trade_order(self):
        return "Rule #1: Cut losers fast. Rule #2: Ride the winners. Rule #3: Repeat until you win like a Marine."