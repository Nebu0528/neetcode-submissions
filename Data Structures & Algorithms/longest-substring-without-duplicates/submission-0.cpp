class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> seen;
        int left = 0;
        int longest = 0;

        for (int right = 0; right < s.length(); right++){
            while (seen.find(s[right]) != seen.end()){
                seen.erase(s[left]);
                left++;
            }
            seen.insert(s[right]);
            int window = right-left+1;
            longest = max(longest, window);
        }
        return longest;
    }
};
