class Node {
    public:
        unordered_set<int> inNodes;
        unordered_set<int> outNodes;
};

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        if (prerequisites.size() == 0) {
            return true;
        }

        vector<Node> nodes(numCourses, Node());
        unordered_set<int> takenCourse;

        for (auto &prequisite: prerequisites) {
            int course = prequisite[0];
            int preCourse = prequisite[1];

            nodes[course].inNodes.insert(preCourse);
            nodes[preCourse].outNodes.insert(course);
        }
        
        while (takenCourse.size() < numCourses) {
            int preCourse = -1;

            for (int i = 0; i < numCourses; ++i) {
                if (nodes[i].inNodes.size() == 0 && takenCourse.find(i) == takenCourse.end()) {
                    preCourse = i;
                    takenCourse.insert(i);
                    break;
                }
            }

            if (preCourse == -1) {
                return false;
            }

            for (int course: nodes[preCourse].outNodes) {
                nodes[course].inNodes.erase(preCourse);
            }
        }
        
        return true;
    }
};
