import sys

counter = [0]

with open(sys.argv[1], "r") as f:
    for line in f:

        # identify a heading line
        if line and line[0:2] == "##":
            heading_md, heading_title = line.split(" ", 1)

            # surtitle
            for _ in range(len(counter) - (len(heading_md) - 1)):
                counter.pop()

            # subtitle
            for _ in range((len(heading_md) - 1) - len(counter)):
                counter.append(0)

            counter[-1] += 1

            new_h = (
                ".".join(str(x) for x in counter)
                + ". "
                + heading_title.replace("\n", "")
            )

            new_h_link = "#" + new_h.replace(".", "").replace(" ", "-").lower()

            print(f"{'  ' * (len(heading_md) - 2)}- [{new_h}]({new_h_link})")