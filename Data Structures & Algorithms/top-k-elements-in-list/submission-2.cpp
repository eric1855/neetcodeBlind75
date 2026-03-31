class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> res;
        vector<int> ret;
        for(int num : nums){
            res[num]++;
        }
        
        for(int i=0; i<k; i++){
            int max = 0;
            int maxint;
            for(auto& j : res){
                if(j.second >max){
                    max = j.second;
                    maxint = j.first;
                }
            }
            res.erase(maxint);
            ret.push_back(maxint);
        }

        return ret;
    }
};
