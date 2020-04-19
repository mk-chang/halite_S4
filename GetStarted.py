from kaggle_environments import evaluate, make

env = make("halite", debug=True)
env.render()

# Play against yourself without an ERROR or INVALID.
# Note: The first episode in the competition will run this to weed out erroneous agents.
env.run(["/kaggle/working/submission.py", "/kaggle/working/submission.py"])
print("EXCELLENT SUBMISSION!" if env.toJSON()["statuses"] == ["DONE", "DONE"] else "MAYBE BAD SUBMISSION?")

# Play as the first agent against default "shortest" agent.
env.run(["/kaggle/working/submission.py", )"random"]
env.render(mode="ipython", width=800, height=600)