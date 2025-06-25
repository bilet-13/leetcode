class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> inDeg(numCourses, 0);
        vector<vector<int>> graph(numCourses);
        queue<int> zeroInDegree;

        for (auto& preReq: prerequisites) {
            int course = preReq[0];
            int preCourse = preReq[1];

            inDeg[course]++;
            graph[preCourse].push_back(course);
        }

        for (int i = 0; i < numCourses; ++i) {
            if (inDeg[i] == 0) {
                zeroInDegree.push(i);
            }
        }
        
        int courseCount = 0;
        while (!zeroInDegree.empty()) {
            auto curCourse = zeroInDegree.front();
            zeroInDegree.pop();

            courseCount++;

            for (auto nextCourse: graph[curCourse]) {
                inDeg[nextCourse]--;
                if (inDeg[nextCourse] == 0) {
                    zeroInDegree.push(nextCourse);
                }
            }
        }

        return courseCount == numCourses;
    }
};
