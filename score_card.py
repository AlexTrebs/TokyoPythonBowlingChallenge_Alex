def pins_knocked_over(score_card: str) -> int:
    """
    Count the number of pins knocked over from a bowling score-card.

    Args:
        score-card: str
        A space-separated string of 10 frames.

    Returns: int
        Representing the number of pins knocked over during the game.

    Possible frame scores:
        "X": strike
        "i/": spare
        "ij": open frame
        "-": gutter ball(s)

        * where i,j are between 1 and 9 and i+j < 10

    Example input:
        "X 7/ 9- X -8 8/ - 72 X X81"

    Note:
        You may assume all score-cards are valid.
        A single frame scoring "-" means two gutter balls were rolled.
        A strike or spare in the 10th frame unlocks a bonus roll.
    """
    total_knocked_over = -1  # TO-DO

    return total_knocked_over
