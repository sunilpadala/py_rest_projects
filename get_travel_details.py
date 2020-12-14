from Travelapp import Travel_assistant

def print_instructions(src,dst):
    t = Travel_assistant.travel_assistant(src,dst)
    t.comp_src_to_dest()


if __name__ == '__main__':
    print("Enter your source country:")
    s = input().strip().lower()
    print("Enter your Destination country:")
    d = input().strip().lower()
    print_instructions(s,d)