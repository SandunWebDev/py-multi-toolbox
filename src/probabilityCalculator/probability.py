import copy
import random
from collections import Counter


class Hat:
    def __init__(self, **kwargs):
        # For each mentioned ball type adding specified amount of balls. (Ex. `{"red": 2, "blue": 1}` ---> `contents` will be `["red", "red", "blue"]`.)
        ball_list = []
        for ball_color, no_of_balls in kwargs.items():
            for _ in range(no_of_balls):
                ball_list.append(ball_color)

        self.contents = ball_list

    def draw(self, no_of_balls_to_draw):
        if no_of_balls_to_draw > len(self.contents):
            return self.contents

        random_ball_list = []
        for _ in range(no_of_balls_to_draw):
            random_index = random.randrange(  # noqa: DUO102, S311
                0, len(self.contents)
            )

            removed_ball = self.contents.pop(random_index)
            random_ball_list.append(removed_ball)

        return random_ball_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    no_of_success = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_counter = Counter(drawn_balls)

        # Checking expected no of balls with relevant type is drawn.
        is_expected = False
        for ball_color, no_of_balls in expected_balls.items():
            if drawn_balls_counter[ball_color] >= no_of_balls:
                is_expected = True
            else:
                is_expected = False
                break

        if is_expected:
            no_of_success += 1

    return no_of_success / num_experiments
