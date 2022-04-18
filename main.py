from priority_queue import MaxPriorityQueue


if __name__ == "__main__":
    # Define initial priority queue for five jobs A, B, C, D, E where priority of A > B > C > D > E
    mpq = MaxPriorityQueue()

    mpq.insert(10, "D")
    mpq.insert(15, "C")
    mpq.insert(25, "A")
    mpq.insert(5, "E")
    mpq.insert(20, "B")

    # List after insertion: [25, 20, 15, 5, 10] or processes [A, B, C, E, D]
    print(mpq.priority_queue)

    # Print out the jobs according to their priority
    print(mpq.extract_max()[1])
    print(mpq.priority_queue)
    # List after extraction: [20, 10, 15, 5] or processes [B, D, C, E]

    # Inserting a new job with higher priority than all the jobs in the queue
    mpq.insert(40, "A*")
    print("After insertion of A* :", mpq.priority_queue)
    # List after insertion: [40, 20, 15, 5, 10] or [A*, B, C, E, D]

    print(mpq.extract_max()[1])
    print(mpq.priority_queue)
    # List after extraction: [20, 10, 15, 5] or processes [B, D, C, E]

    print(mpq.extract_max()[1])
    print(mpq.priority_queue)
    # List after extraction: [15, 10, 5] or processes [C, D, E]

    # Increasing the priority of Job E (priority from 5 to 12) such that its priority is greater than that of D (priority 10)
    mpq.increase_key(2, 12)
    print("After increment of priority of E :", mpq.priority_queue)
    # List after increment: [15, 10, 12] or processes [C, D, E]

    print(mpq.extract_max()[1])
    print(mpq.priority_queue)
    # List after extraction: [12, 10] or processes [E, D]

    print(mpq.extract_max()[1])
    print(mpq.priority_queue)
    # List after extraction: [10] or processes [D]

    print(mpq.extract_max()[1])
    print(mpq.priority_queue)
    # List after extraction: [] or processes []
