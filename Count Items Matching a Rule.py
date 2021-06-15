class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        matched_items = 0
        for item in items:
            if ruleKey == 'type':
                if ruleValue == item[0]:
                    matched_items += 1
            elif ruleKey == 'color':
                if ruleValue == item[1]:
                    matched_items += 1
            else:
                if ruleValue == item[2]:
                    matched_items += 1

        return matched_items
