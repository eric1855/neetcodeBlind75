class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> prevNums;

        for(int i = 0 ; i<nums.size() ; i++){
            if(prevNums.find(target - nums[i]) !=  prevNums.end()){
                return {prevNums[target-nums[i]],i};
            }

            prevNums.insert({nums[i],i});
        }

        return {};
    }
};
