from linked_list import LinkedList


def main():
    llist = LinkedList()

    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)
    print("Linked list:")
    llist.print_list()

    llist.sort()
    print("\nSorted list:")
    llist.print_list()

    llist.reverse()
    print("\nReverse:")
    llist.print_list()

    llist_2 = LinkedList()

    llist_2.insert_at_beginning(1)
    llist_2.insert_at_beginning(3)
    llist_2.insert_at_beginning(9)
    llist_2.insert_at_end(27)
    llist_2.insert_at_end(81)

    print("Sorted merge")
    llist.sort()
    llist_2.sort()
    print("\nList 1 before merge:")
    llist.print_list()
    print("\nList 2 before merge:")
    llist_2.print_list()
    result = LinkedList.merge_sorted(llist, llist_2)
    print("\nList 1 after merge:")
    llist.print_list()
    print("\nList 2 after merge:")
    llist_2.print_list()
    print("\nResult:")
    result.print_list()


if __name__ == "__main__":
    main()
