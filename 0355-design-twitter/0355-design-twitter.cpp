class Twitter {
private:
    long long int tweet_order;
    unordered_map<int, vector<pair<int, int>>> tweets;
    unordered_map<int, unordered_set<int>> followees;
    int most_recent_tweet_num;

public:
    Twitter() {
        tweets = {};
        followees = {};
        tweet_order = 0;
        most_recent_tweet_num = 10;
    }
    
    void postTweet(int userId, int tweetId) {
        if (tweets.find(userId) == tweets.end()) {
            tweets[userId] = {};
        }
        tweets[userId].push_back(make_pair(tweet_order, tweetId));
        tweet_order += 1;
    }
    
    vector<int> getNewsFeed(int userId) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        vector<int> newsWriter = {userId};

        if (followees.find(userId) != followees.end()) {
           for (int followee: followees[userId]) {
                newsWriter.push_back(followee);
            } 
        } 

        for (int &writer: newsWriter) {
            int num_tweet = 0;

            if (tweets.find(writer) != tweets.end()) {
                for (auto iter = tweets[writer].rbegin(); iter != tweets[writer].rend() && num_tweet < most_recent_tweet_num; iter++, num_tweet++) {
                    if (minHeap.size() < most_recent_tweet_num) {
                        minHeap.push(*iter);
                    } else if (minHeap.top().first < iter->first) {
                        minHeap.pop();
                        minHeap.push(*iter);
                    }
                }
            }
        }
        
        vector<int> result;

        while (!minHeap.empty()) {
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }
        reverse(result.begin(), result.end());

        return result;
    }
    
    void follow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return;
        }

        if (followees.find(followerId) == followees.end()) {
            followees[followerId] = {};
        }
        followees[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followees.find(followerId) != followees.end()) {
            followees[followerId].erase(followeeId);
        }
    }
};
