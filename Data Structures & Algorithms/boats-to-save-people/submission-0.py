class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = people.sort()
        min_count = 0

        i = 0
        j = len(people)-1

        while i <= j:
            min_count += 1
            if people[i] + people[j] <= limit:
                i +=1
            j -=1
        
        return min_count



        