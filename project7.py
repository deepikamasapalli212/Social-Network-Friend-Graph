from collections import defaultdict, deque


class SocialNetwork:

    def __init__(self):
        self.graph = defaultdict(set)


    # Add user
    def add_user(self, user):

        if user in self.graph:
            print("User already exists")
        else:
            self.graph[user] = set()
            print("User added")


    # Add friendship (bidirectional)
    def add_friendship(self, user1, user2):

        if user1 not in self.graph or user2 not in self.graph:
            print("One or both users not found")
            return

        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

        print("Friendship added")


    # Show mutual friends
    def mutual_friends(self, user1, user2):

        if user1 not in self.graph or user2 not in self.graph:
            print("User not found")
            return

        mutual = self.graph[user1].intersection(self.graph[user2])

        if mutual:
            print("Mutual friends:", mutual)
        else:
            print("No mutual friends")


    # Shortest path between users (BFS)
    def shortest_path(self, start, end):

        if start not in self.graph or end not in self.graph:
            print("User not found")
            return

        queue = deque([(start, [start])])
        visited = set([start])

        while queue:

            current, path = queue.popleft()

            if current == end:
                print("Shortest path:", " -> ".join(path))
                return

            for neighbor in self.graph[current]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        print("No connection found")


    # Friend recommendations (friends of friends)
    def recommend_friends(self, user):

        if user not in self.graph:
            print("User not found")
            return

        recommendations = set()

        for friend in self.graph[user]:

            for fof in self.graph[friend]:

                if fof != user and fof not in self.graph[user]:
                    recommendations.add(fof)

        if recommendations:
            print("Recommended friends:", recommendations)
        else:
            print("No recommendations")


    # Show network
    def show_network(self):

        print("\nSocial Network:")
        for user in self.graph:
            print(user, "->", self.graph[user])


# Interactive program
network = SocialNetwork()

print("=== Social Network Friend Graph ===")

while True:

    print("\nOptions:")
    print("1. Add user")
    print("2. Add friendship")
    print("3. Mutual friends")
    print("4. Shortest path")
    print("5. Friend recommendations")
    print("6. Show network")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        user = input("Enter username: ")
        network.add_user(user)


    elif choice == "2":

        u1 = input("User 1: ")
        u2 = input("User 2: ")
        network.add_friendship(u1, u2)


    elif choice == "3":

        u1 = input("User 1: ")
        u2 = input("User 2: ")
        network.mutual_friends(u1, u2)


    elif choice == "4":

        start = input("Start user: ")
        end = input("End user: ")
        network.shortest_path(start, end)


    elif choice == "5":

        user = input("Enter user: ")
        network.recommend_friends(user)


    elif choice == "6":

        network.show_network()


    elif choice == "7":
        break


    else:
        print("Invalid choice")