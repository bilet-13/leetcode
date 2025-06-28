class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        //kahn's algo
        // find topological sort order
        vector<int> order;
        vector<vector<int>> graph(numCourses); // adjancy list
        vector<int> inDegree(numCourses, 0);
        queue<int> q;

        for (const auto & preReq: prerequisites) {
            int course = preReq[0];
            int preCourse = preReq[1];

            graph[preCourse].push_back(course);
            inDegree[course]++;
        }

        for (int i = 0; i < numCourses; ++i) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            auto course = q.front();
            q.pop();

            order.push_back(course);

            for (auto nextCourse: graph[course]) {
                inDegree[nextCourse]--;

                if (inDegree[nextCourse] == 0) {
                    q.push(nextCourse);
                }
            }
        }
        return order.size() == numCourses ? order : vector<int>();
    }
};
