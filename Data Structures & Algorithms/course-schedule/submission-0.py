class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incomings = [0]*numCourses
        for a, b in prerequisites:
            incomings[a]+=1
        done = []
        q = deque()
        for i in range(len(incomings)):
            if incomings[i] == 0:
                q.append(i)
        while q:
            course = q.popleft()
            for a, b in prerequisites:
                if b == course:
                    incomings[a]-=1
                    if incomings[a] == 0:
                        q.append(a)
            done.append(course)
        return len(done) == numCourses

