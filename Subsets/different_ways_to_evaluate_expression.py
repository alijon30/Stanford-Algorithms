def diff_ways_to_evaluate_expression(input):
    result = []

    if "+" not in input and "-" not in input and "*" not in input:
        result.append(int(input))

    else:
        for i in range(0, len(input)):
            char = input[i]
            if not char.isdigit():
                Leftparts = diff_ways_to_evaluate_expression(input[:i])
                Rightparts = diff_ways_to_evaluate_expression(input[i+1:])
                for part1 in Leftparts:
                    for part2 in Rightparts:
                        if char == "+":
                            result.append(part1 + part2)

                        elif char == "-":
                            result.append(part1-part2)

                        elif char == "*":
                            result.append(part1 * part2)

    return result
def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
