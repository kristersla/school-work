Can_we_count_it = [{'s': False}, "sassafrass", 18, ['a', 'c', 's', 'd']]

for element in Can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + "does not have .count attribute: ")
    else:
        print("ir")