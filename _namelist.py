import random


def RandomTitle(mode):
    TITLE_LIST = [
        f"{mode} Graph",
        f"My {mode} Graph",
        f"My Awesome {mode} Graph",
        f"A {mode} Graph",
        f"An {mode} Graph",
        f"A(n) {mode} Graph",
        f"A Random {mode} Graph",
        f"Untitled {mode} Graph",
        f"Titled {mode} Graph",
        f"Graph of {mode}",
        f"Generated {mode} Graph",
        f"Computer Generated {mode} Graph",
        f"Graph of {mode}-ness",
        f"The {mode} Graph",
        f"The Best {mode} Graph",
        f"Your {mode} Graph",
        f"Your Awesome {mode} Graph",
        f"Our {mode} Graph",
        f"{mode} {mode}",
        f"Graph ({mode})",
        f"{mode} Graph 1",
        f"{mode} Graph 2: Electric Boogaloo",
        f"{mode} Graph 3",
        f"{mode} Graph?",
        f"{mode} Graph (I think)",
        f"Not a {mode} Graph",
        f"Totally Not a {mode} Graph",
        f"Weird {mode} Graph",
        f"{mode} Graph, Courtesy of Ralphar",
        f"{mode}ity, the Graph",
        f"I Love {mode} Graphs",
        f"I Hate {mode} Graphs",
        f"I Despise {mode} Graphs",
        f"I'm struggling to come up with funny titles ({mode} Graph)",
        f"Kasdlfhsdljfl ({mode})",
        f"Look at this {mode} graph",
        f"Traceback (most {mode} call last):",
        f"There's a {mode} Graph on your lawn!",
        f"Unlock the Golden {mode} Graph with only $9.99!!",
        f"{mode} Graph: Into the Graphing Verse",
        f"Adopted. Fatty. Fatty Fatty. No {mode} Graph.",
        f"MANKIND IS DEAD. BLOOD IS FUEL. GRAPH IS {mode.upper()}",
        f"Welcome to your final test, I'm {mode} Graph",
        f"{mode} Graph, You fool!",
        f"[{mode}] GRAPH SO GOOD I'LL [$!$$] MYSELF",
        f"...and his {mode} graph was electric",
        f"...and his {mode} graph was electric",
        f"NERF {mode.upper()} GRAPH",
        f"Close your ({mode}) graphs, you'll be here soon",
        f"{mode} Sign - Kaleidoslope Iridescence"
    ]

    return random.choice(TITLE_LIST)

if __name__ == "__main__":
    input("""This Python file does nothing when executed by the user.
It contains a list of names randomly selected by GraphGen.pyw when creating a graph.
Please open GraphGen.pyw to access the graph generator.
(Any input will terminate this program)
""")
