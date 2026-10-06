class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        allAnagrams = defaultdict(list)
        
        for word in strs: 
            count_arr = [0] * 26
            for letter in word:
                count_arr[(ord(letter) - ord('a'))] += 1
            allAnagrams[tuple(count_arr)].append(word)
            # allAnagrams[count_arr] =  allAnagrams[count_arr].append(word) # list cant be dict keys    
        return list(allAnagrams.values())