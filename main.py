from human_behavior import HumanBehavior
humanbehavior = HumanBehavior()

for dbg in range(0, 10):
    dbg = dbg + 1
    humanbehavior.say_with_color_for_secs(str(dbg), "green", None, None, 1)
