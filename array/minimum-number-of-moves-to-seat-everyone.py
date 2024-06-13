class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        move_count = 0
        for i in range(len(students)):
            if students[i] < seats[i]:
                while students[i] < seats[i]:
                    students[i] += 1
                    move_count += 1
            elif students[i] > seats[i]:
                while students[i] > seats[i]:
                    students[i] -= 1
                    move_count += 1
        return move_count



        