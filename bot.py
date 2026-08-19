import time

LANES = {
    "LEFT": 0,
    "CENTER": 1,
    "RIGHT": 2
}


class SubwayBot:

    def __init__(self):
        self.player_lane = LANES["CENTER"]

    def choose_lane(self, blocked_lanes):
        """
        blocked_lanes:
        لیست سه‌تایی که مشخص می‌کند
        کدام لاین مانع دارد.

        مثال:
        [False, True, False]
        یعنی لاین وسط بسته است.
        """

        if not blocked_lanes[self.player_lane]:
            return self.player_lane

        # اولویت: نزدیک‌ترین لاین آزاد
        possible = []

        for lane in range(3):
            if not blocked_lanes[lane]:
                possible.append(lane)

        if not possible:
            return None

        possible.sort(
            key=lambda x: abs(x - self.player_lane)
        )

        return possible[0]

    def action(self, target_lane):

        if target_lane is None:
            return "JUMP"

        if target_lane < self.player_lane:
            self.player_lane = target_lane
            return "LEFT"

        if target_lane > self.player_lane:
            self.player_lane = target_lane
            return "RIGHT"

        return "NOTHING"


def test_bot():

    bot = SubwayBot()

    situations = [
        [False, False, False],
        [False, True, False],
        [True, False, False],
        [False, False, True],
        [True, True, False],
        [False, True, True]
    ]

    for blocked in situations:

        target = bot.choose_lane(blocked)

        action = bot.action(target)

        print(
            "موانع:",
            blocked,
            "| تصمیم:",
            action,
            "| لاین:",
            bot.player_lane
        )

        time.sleep(0.5)


if __name__ == "__main__":
    test_bot()
